#!/usr/bin/env python3
"""
ax-commons 빌드 스크립트

skills/ 를 원본으로 삼아 dist/ 아래 각 플랫폼 배포본을 생성한다.
표준 라이브러리만 쓴다. 추가 설치가 필요 없다.

    python3 scripts/build.py            전체 생성
    python3 scripts/build.py --check    생성물이 최신인지만 확인 (CI용)

dist/ 는 직접 고치지 않는다. skills/ 를 고치고 이걸 돌린다.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
PROMPTS = ROOT / "prompts"
PHILOSOPHY = ROOT / "PHILOSOPHY.md"

SKILL_NAMES = ["owner-lens", "insight-commons"]

BANNER = "<!-- 자동 생성됨. 고치지 마세요. skills/ 를 고치고 `python3 scripts/build.py` 를 돌리세요. -->\n\n"


# ---------------------------------------------------------------- helpers
def log(msg: str) -> None:
    print(f"  {msg}")


def copy_skill(name: str, dest: Path, with_philosophy: bool = True) -> None:
    """스킬 원본을 dest/name 으로 복사한다."""
    src = SKILLS / name
    out = dest / name
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(src, out)
    if with_philosophy and PHILOSOPHY.exists():
        shutil.copy2(PHILOSOPHY, out / "PHILOSOPHY.md")


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(path.rglob("*")):
        if f.is_file():
            h.update(f.relative_to(path).as_posix().encode())
            h.update(f.read_bytes())
    return h.hexdigest()[:12]


# ---------------------------------------------------------------- targets
def build_claude_web() -> None:
    """폴더 + 바로 올릴 수 있는 zip."""
    dest = DIST / "claude-web"
    dest.mkdir(parents=True, exist_ok=True)
    for name in SKILL_NAMES:
        copy_skill(name, dest)
        zpath = dest / f"{name}.zip"
        if zpath.exists():
            zpath.unlink()
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            base = dest / name
            for f in sorted(base.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(base).as_posix())
        log(f"claude-web: {name}/ + {name}.zip")


def build_claude_code() -> None:
    """~/.claude/skills/ 에 그대로 복사하는 형태."""
    dest = DIST / "claude-code"
    dest.mkdir(parents=True, exist_ok=True)
    for name in SKILL_NAMES:
        copy_skill(name, dest)
        log(f"claude-code: {name}/")


def build_codex() -> None:
    """GPT Codex: AGENTS.md 한 장으로 합친다."""
    dest = DIST / "codex"
    parts = [BANNER, "# AGENTS.md — ax-commons\n\n"]
    parts.append(read(PHILOSOPHY).split("---", 1)[0].strip() + "\n\n---\n\n")
    for name in SKILL_NAMES:
        skill_md = read(SKILLS / name / "SKILL.md")
        body = skill_md.split("---", 2)[-1].strip()  # 프론트매터 제거
        parts.append(f"# {name}\n\n{body}\n\n---\n\n")
    write(dest / "AGENTS.md", "".join(parts))
    log("codex: AGENTS.md")


def build_prompt_variants() -> None:
    """전체판에서 컴팩트판을 만든다 (표와 예시 일부를 덜어낸다)."""
    full = PROMPTS / "system-prompt-full.md"
    if not full.exists():
        log("prompts: system-prompt-full.md 없음 — 건너뜀")
        return
    text = read(full)
    # 주석 헤더와 '6. 모드별 추가 규칙' 이후 상세는 컴팩트판에서 뺀다
    marker = "# 6. 모드별 추가 규칙"
    compact = text.split(marker)[0]
    compact += (
        "# 6. 모드별 상세\n\n"
        "전체판을 참고한다. 컨텍스트가 허락하면 system-prompt-full.md 를 쓴다.\n\n"
        + text.split("# 8. 출력 직전 점검")[-1].join(["# 7. 출력 직전 점검", ""])
    )
    write(PROMPTS / "system-prompt-compact.md", compact)
    log("prompts: system-prompt-compact.md")


def build_local_models() -> None:
    """로컬 모델용: 시스템 프롬프트를 그대로 두고 참조만 만든다."""
    dest = DIST / "local-models"
    dest.mkdir(parents=True, exist_ok=True)
    full = PROMPTS / "system-prompt-full.md"
    if full.exists():
        shutil.copy2(full, dest / "system-prompt.md")
        log("local-models: system-prompt.md")


# ---------------------------------------------------------------- main
TARGETS = {
    "claude-web": build_claude_web,
    "claude-code": build_claude_code,
    "codex": build_codex,
    "prompts": build_prompt_variants,
    "local-models": build_local_models,
}


def main() -> int:
    ap = argparse.ArgumentParser(description="ax-commons 빌드")
    ap.add_argument("--check", action="store_true", help="생성물이 최신인지 확인만 한다")
    ap.add_argument("--only", nargs="*", choices=list(TARGETS), help="특정 대상만")
    args = ap.parse_args()

    if not SKILLS.is_dir():
        print(f"오류: {SKILLS} 를 찾을 수 없습니다. 저장소 루트에서 실행하세요.", file=sys.stderr)
        return 1

    if args.check:
        before = {n: digest(DIST / "claude-web" / n) for n in SKILL_NAMES if (DIST / "claude-web" / n).is_dir()}

    names = args.only or list(TARGETS)
    print("ax-commons 빌드")
    for n in names:
        TARGETS[n]()

    if args.check:
        after = {n: digest(DIST / "claude-web" / n) for n in SKILL_NAMES}
        stale = [n for n in after if before.get(n) != after[n]]
        if stale:
            print(f"\n최신이 아님: {', '.join(stale)}", file=sys.stderr)
            print("`python3 scripts/build.py` 를 돌리고 결과를 커밋하세요.", file=sys.stderr)
            return 1
        print("\n최신입니다.")

    print("\n완료.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
