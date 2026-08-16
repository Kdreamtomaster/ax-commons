#!/usr/bin/env python3
"""
공개 전 비식별화 검사기

저장소에 회사를 특정할 수 있는 내용이 남았는지 훑는다.
커밋 전, PR 병합 전, 배포 전에 돌린다.

    python3 scripts/scan-private.py            전체 검사
    python3 scripts/scan-private.py --strict   경고도 실패로 처리 (CI용)

## 내 고객사 이름을 넣어 검사하려면

저장소 루트에 `.private-terms.txt` 를 만들고 한 줄에 하나씩 적는다.
이 파일은 .gitignore 에 들어 있어서 **커밋되지 않는다.**

    우리회사이름
    고객사A
    프로젝트코드명

검사기는 그 단어들이 저장소 어딘가에 남았는지 확인한다.
파일 자체는 올라가지 않으므로 안심하고 실제 이름을 적어도 된다.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIVATE_TERMS = ROOT / ".private-terms.txt"

SCAN_EXT = {".md", ".yml", ".yaml", ".py", ".txt", ".json", ".sh", ".ps1"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules"}

# 이 파일 자신과 검사 대상에서 뺄 것 (규칙을 설명하는 문서라 예시어가 들어감)
SELF = {"scripts/scan-private.py"}


# ---------------------------------------------------------------- 규칙
# (이름, 정규식, 심각도, 설명)
RULES: list[tuple[str, str, str, str]] = [
    ("이메일", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "error",
     "이메일 주소는 공개 저장소에 두지 않는다"),

    ("전화번호", r"(?<!\d)01[016-9][-\s]?\d{3,4}[-\s]?\d{4}(?!\d)", "error",
     "전화번호"),

    ("주민·사업자번호꼴", r"(?<!\d)\d{6}[-]\d{7}(?!\d)|(?<!\d)\d{3}[-]\d{2}[-]\d{5}(?!\d)", "error",
     "주민등록번호 또는 사업자등록번호 형식"),

    # 앞에 영문/숫자가 붙은 건 식별자다 (예: "T1 조건"의 "1 조"). 제외한다.
    ("구체적 금액", r"(?<![A-Za-z0-9○△□×?])\d{1,4}(,\d{3})*\s*(억|조)(?!건|직|사|정|치|각|절|합|약|례)", "warn",
     "구체적 금액은 회사를 특정한다. 관계나 범위로 바꾼다 (예: '수천억대')"),

    ("산업+규모 조합", r"(국내|국산)\s*\S{2,10}(사|업체|기업|제조사|장비사)", "warn",
     "산업과 규모를 같이 적으면 특정된다. 조건만 남기고 산업을 지운다"),

    ("사내 지칭", r"(우리\s?회사는|당사는|폐사|자사의)\s", "warn",
     "1인칭 회사 지칭은 문서를 특정 조직에 묶는다"),

    # 자리표시자(사용자이름, username 등)는 안내 문서에 필요하므로 제외한다.
    ("절대경로 노출",
     r"[A-Z]:\\\\?Users\\\\?(?!사용자이름|사용자|username|USERNAME|<|\{|\$)[^\\\s\"']+", "warn",
     "사용자 폴더가 드러나는 절대경로. 자리표시자로 바꾼다"),

    ("한국 대기업명", r"삼성전자|삼성SDS|삼성물산|현대자동차|현대오토에버|LG전자|LG CNS|"
                    r"SK하이닉스|SK텔레콤|포스코|한화시스템|두산에너빌리티|효성ITX|KT DS|"
                    r"신세계아이앤씨|롯데이노베이트|CJ올리브네트웍스", "error",
     "실명 대기업이 예시로라도 들어가면 고객사 추정을 부른다"),
]


def load_private_terms() -> list[str]:
    if not PRIVATE_TERMS.exists():
        return []
    out = []
    for line in PRIVATE_TERMS.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s)
    return out


def iter_files():
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in SCAN_EXT:
            continue
        rel = p.relative_to(ROOT).as_posix()
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if rel in SELF or rel == ".private-terms.txt":
            continue
        yield p, rel


def main() -> int:
    ap = argparse.ArgumentParser(description="공개 전 비식별화 검사")
    ap.add_argument("--strict", action="store_true", help="warn 도 실패로 처리")
    args = ap.parse_args()

    terms = load_private_terms()
    compiled = [(n, re.compile(rx), sev, note) for n, rx, sev, note in RULES]

    errors: list[str] = []
    warns: list[str] = []

    for path, rel in iter_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lines = text.splitlines()

        for name, rx, sev, note in compiled:
            for i, line in enumerate(lines, 1):
                for m in rx.finditer(line):
                    hit = f"{rel}:{i}  [{name}] {m.group(0).strip()[:60]}\n      → {note}"
                    (errors if sev == "error" else warns).append(hit)

        for t in terms:
            for i, line in enumerate(lines, 1):
                if t in line:
                    errors.append(f"{rel}:{i}  [비공개 용어] '{t}' 가 남아 있다")

    print("공개 전 비식별화 검사")
    print(f"  대상 파일 {sum(1 for _ in iter_files())}개")
    print(f"  비공개 용어 목록 {len(terms)}개" +
          ("" if terms else "  (.private-terms.txt 를 만들면 내 고객사명도 검사한다)"))
    print()

    if errors:
        print(f"■ 반드시 고칠 것 ({len(errors)})")
        for e in errors:
            print("  " + e)
        print()
    if warns:
        print(f"□ 확인 필요 ({len(warns)})")
        for w in warns:
            print("  " + w)
        print()

    if not errors and not warns:
        print("깨끗합니다.")
        return 0

    if errors:
        print("→ error 항목을 고치기 전에는 공개하지 마세요.")
        return 1
    if args.strict:
        print("→ --strict 이므로 warn 도 실패로 처리합니다.")
        return 1

    print("→ warn 은 사람이 판단합니다. 예시로 쓴 것이면 그대로 두어도 됩니다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
