#!/usr/bin/env python3
"""
깃헙 저장소 초기 설정 — 라벨과 시드 이슈를 만든다.

    gh auth login              먼저 한 번만
    python3 scripts/setup-github.py --dry-run      무엇이 만들어질지 확인
    python3 scripts/setup-github.py                실제로 만든다

시드 이슈는 docs/open-questions.md 의 Q1~Q10 을 그대로 옮긴 것이다.
사람이 읽을 문서와 이슈가 어긋나지 않게, 본문에 그 문서 링크를 단다.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- 라벨
LABELS = [
    ("field-report",   "0E8A16", "실측 보고 — 실제로 써 보고 나온 결과"),
    ("verification",   "1D76DB", "검증 필요 — 아직 근거 없이 쓰고 있는 값"),
    ("counterexample", "B60205", "반례 — 확인보다 값지다"),
    ("tenure-gate",    "5319E7", "임기 게이트 관련"),
    ("insight-entry",  "FBCA04", "인사이트 원장 항목 제출"),
    ("models",         "006B75", "로컬 모델·실행 환경"),
    ("adapter",        "C2E0C6", "플랫폼 연동"),
    ("reference-data", "D4C5F9", "마진 스프레드·신호 해석 규칙"),
    ("docs",           "BFD4F2", "문서"),
    ("good first issue", "7057FF", "처음 기여하기 좋은 것"),
    ("help wanted",    "008672", "도움이 필요합니다"),
]

# ---------------------------------------------------------------- 시드 이슈
DOC = "docs/open-questions.md"

ISSUES = [
    dict(
        key="Q1",
        title="[검증] 임기 게이트 safe_ratio 0.6 이 맞는 값인가",
        labels=["verification", "tenure-gate", "help wanted"],
        body=f"""\
`owner-lens` 의 S7은 `회수 기간 < 잔여 임기 × 0.6` 이면 "팔린다"로 판정한다.
**0.6이라는 숫자에 근거가 없다.** 경험칙이고 실측이 없다.

이 프로젝트에서 제일 중요한 미검증 항목이다.

### 무엇이 관찰되면 결론이 나는가

- 서로 다른 조직 10건 이상에서 게이트 판정과 실제 결과를 대조
- **탈락시켰는데 상대가 오히려 원한 사례**가 나오면 임계값이 너무 보수적이다
- 통과시켰는데 관심이 없던 사례가 반복되면 임계값 말고 다른 변수가 있다는 뜻

### 이미 나온 의심

임기만이 아니라 **담당자 KPI와의 연결 여부**가 더 셀 수 있다.
회수가 짧아도 자기 평가지표와 무관하면 움직이지 않는다.

### 어떻게 기여하나

이슈 템플릿 **① 임기 게이트 실측 보고** 로 새 이슈를 연다.
회사가 특정되지 않게, 숫자 대신 관계로 적는다.

> **틀렸다는 보고가 맞았다는 보고보다 값지다.**

관련: [{DOC}]({DOC}) Q1
""",
    ),
    dict(
        key="Q2",
        title="[검증] 몇 B 모델부터 이 도구가 제대로 작동하는가",
        labels=["verification", "models", "help wanted"],
        body=f"""\
`dist/local-models/README.md` 의 크기별 성능표는 **추정이다.**
"7~9B는 등급 표기를 자주 빠뜨린다" 같은 문장도 근거 없이 썼다.

### 채점 기준 — 답변 품질이 아니라 규칙 준수를 본다

- [ ] 근거 등급(`[사실]`/`[추론]`/`[가설]`/`[모름]`)을 문장마다 붙였다
- [ ] `[가설]`에 반증 조건을 달았다
- [ ] 뻔한 답을 먼저 적고 버렸다
- [ ] 질문을 한 라운드에 4개 이하로 했다
- [ ] R1에서 초안을 먼저 냈다
- [ ] `[불가]` 판정을 하나 이상 남겼다
- [ ] "남은 모름"을 비우지 않았다
- [ ] 반박 안내를 썼다
- [ ] 임기 게이트를 계산했다
- [ ] 표 형식이 깨지지 않았다

### 특히 궁금한 것

- 대화가 길어지며 무너지는지, 처음부터 무시하는지 (원인이 다르다)
- 양자화를 어디까지 내려도 되는지. 등급 표기가 먼저 사라지는지
- 국산 모델(EXAONE, Kanana)의 한국어 품질이 실제로 나은지

이슈 템플릿 **③ 모델 실측 보고** 를 쓴다.

관련: [{DOC}]({DOC}) Q2
""",
    ),
    dict(
        key="Q3",
        title="[연동] Hermes Agent 연동 실증 — 특히 프로필 메모리 격리",
        labels=["adapter", "verification", "help wanted"],
        body=f"""\
`dist/hermes/README.md` 는 **공식 문서만 보고 썼다. 직접 돌려보지 않았다.**

### 확인 못 한 것

- [ ] 스킬 경로 `~/.hermes/skills/<범주>/<이름>/` 가 맞는지
- [ ] **자동 메모리를 끄거나 좁히는 정확한 설정 키**
- [ ] **프로필 분리가 메모리까지 완전히 격리하는지** ← 제일 중요
- [ ] `hermes skills install` 로 깃헙에서 바로 받을 때의 경로 형식

### 왜 중요한가

Hermes는 에이전트가 스스로 메모리를 큐레이션한다.
`insight-commons` 는 고객사명·가격·계약 조건이 **반드시 사라져야 한다**고 규정한다.

**프로필 격리가 불완전하면 한 고객사 정보가 다른 고객사 대화로 샌다.**
이건 편의 문제가 아니라 신뢰 문제다.

### 검증 방법 제안

1. `--profile a` 에서 가상의 고객사 정보를 넣고 대화
2. `--profile b` 로 바꿔 "아까 그 회사" 를 물어본다
3. 뭐라도 기억하면 격리가 안 되는 것이다

이슈 템플릿 **④ 플랫폼 연동 보고** 를 쓴다.

관련: [{DOC}]({DOC}) Q3
""",
    ),
    dict(
        key="Q4",
        title="[연동] OpenClaw 연동 실증",
        labels=["adapter", "verification", "good first issue"],
        body=f"""\
`dist/openclaw/README.md` 는 문서 기준으로만 작성했다. 미실행.

- [ ] `~/.openclaw/skills/<이름>/SKILL.md` 로 잡히는지
- [ ] `openclaw.json` 의 `skills.load.extraDirs` 로 저장소를 직접 걸었을 때 되는지
      (되면 `git pull` 만으로 갱신된다)
- [ ] `SOUL.md` 에 원칙을 넣었을 때 스킬과 충돌하지 않는지

OpenClaw는 Claude와 같은 `SKILL.md` 형식을 쓴다고 확인했으나,
**실제로 복사해서 인식되는지는 확인하지 않았다.**

이슈 템플릿 **④ 플랫폼 연동 보고** 를 쓴다.

관련: [{DOC}]({DOC}) Q4
""",
    ),
    dict(
        key="Q5",
        title="[연동] GPT Codex의 AGENTS.md 가 이 분량을 감당하는가",
        labels=["adapter", "verification", "good first issue"],
        body=f"""\
`dist/codex/AGENTS.md` 는 빌드로 생성만 했고 **실동작을 확인하지 않았다.**

두 스킬을 한 파일로 합쳐서 꽤 길다.
Codex가 이 길이를 다 읽는지, 앞부분만 반영하는지 모른다.

### 검증 방법

Codex에게 이렇게 물어본다.

> 임기 게이트를 계산해서 이 안건이 팔릴지 판정해줘

규칙을 알고 있으면 읽은 것이다. 모르면 분량을 줄이거나 스킬을 하나만 넣어야 한다.

「반박 안내」를 자발적으로 붙이는지도 같이 본다. 그게 뒤쪽에 있는 규칙이라
분량 문제를 판별하기 좋다.

관련: [{DOC}]({DOC}) Q5
""",
    ),
    dict(
        key="Q6",
        title="[자료] 산업별 마진 스프레드가 비어 있다",
        labels=["reference-data", "help wanted"],
        body=f"""\
`skills/owner-lens/references/tuning.md` 의 `margin_reference` 가 **빈 껍데기다.**

`owner-lens` 의 S5는 "이 산업 상위/중위/하위 영업이익률"에서 출발한다.
**산업 평균은 아무것도 설명하지 않는다.** 편차가 설명 대상이다.

값이 없으면 `[모름]`으로 진행하게 되고 분석의 날이 무뎌진다.

### 필요한 것

```yaml
- industry: ""
  year: ""
  source: ""          # 이게 없으면 못 쓴다
  operating_margin:
    top: ""
    median: ""
    bottom: ""
  swing_factors: ["", "", ""]   # 상·하위를 가르는 운영 변수
```

**숫자는 낡는다.** 출처와 연도 없는 값은 받지 않는다.

공개 출처: 한국은행 기업경영분석 · 통계청 · 업종별 협회 공시

이슈 템플릿 **⑤ 참조 자료 제출** 을 쓴다.

관련: [{DOC}]({DOC}) Q6
""",
    ),
    dict(
        key="Q7",
        title="[검증] 채용공고 해석 규칙이 실제로 맞는가",
        labels=["verification", "reference-data"],
        body=f"""\
`skills/owner-lens/references/pipeline.md` 의 S1 해석표는 **경험에서 나온 추측이다.**

예: "오래 열려 있는 자리 = 못 채우는 자리 = 병목이거나 처우가 낮다"

이게 맞는지 확인된 바 없다. 단순히 채용을 늦게 하는 조직일 수도 있다.

### 무엇이 관찰되면 결론이 나는가

공고를 보고 세운 가설을 미팅에서 확인한 사례.
**맞은 것보다 틀린 것이 값지다** — 어떻게 잘못 읽었는지가 규칙을 고쳐 준다.

관련: [{DOC}]({DOC}) Q7
""",
    ),
    dict(
        key="Q9",
        title="[검증] 탈식별화가 실제로 되는가 — 실패 사례를 모읍니다",
        labels=["verification", "insight-entry"],
        body=f"""\
`insight-commons` 는 "이 문장만 보고 어디인지 좁혀지는가?" 라는 자문 규칙만 갖고 있다.

### 문제

**쓰는 사람은 자기 글이 얼마나 특정 가능한지 잘 모른다.**
업계 사람이 보면 바로 아는데 본인은 충분히 뭉갰다고 여긴다.

### 필요한 것

실패 사례다. "이렇게 썼는데 사람들이 알아보더라"

그런 사례가 모이면 `references/deident.md` 의
「특정을 만드는 것들」 표를 실제 데이터로 고칠 수 있다.

### 주의

**사례를 올릴 때 그 회사를 다시 특정하지 않도록** 조심한다.
"어떤 유형의 서술이 위험했는지"만 적으면 된다.

관련: [{DOC}]({DOC}) Q9
""",
    ),
    dict(
        key="Q10",
        title="[문서] 영어판을 어디까지 만들 것인가",
        labels=["docs", "help wanted"],
        body=f"""\
지금은 README와 각 스킬에 **짧은 영문 요약만** 있다.

### 정할 것

전체 번역은 유지 비용이 크다.
한국어판과 영어판이 어긋나기 시작하면 어느 쪽이 원본인지 모르게 된다.

- 원본 언어를 한국어로 고정하고 영어는 요약만 유지할지
- 아니면 병행 관리할지 (그렇다면 빌드로 어긋남을 검사해야 한다)

### 지금 방침

**한국어가 원본이고 영어는 요약이다.** 바꾸려면 이 이슈에서 논의한다.

번역 기여를 하실 분은 어느 파일부터 필요한지 여기에 적어 주시면 좋겠다.

관련: [{DOC}]({DOC}) Q10
""",
    ),
]


# ---------------------------------------------------------------- 실행
def run(cmd: list[str], dry: bool) -> bool:
    if dry:
        print("  $ " + " ".join(cmd[:6]) + (" ..." if len(cmd) > 6 else ""))
        return True
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        msg = (r.stderr or "").strip().splitlines()
        if msg and "already exists" in msg[-1]:
            print(f"    (이미 있음, 건너뜀)")
            return True
        print(f"    실패: {msg[-1] if msg else r.returncode}", file=sys.stderr)
        return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="깃헙 라벨·시드 이슈 생성")
    ap.add_argument("--dry-run", action="store_true", help="실행하지 않고 보여만 준다")
    ap.add_argument("--repo", help="owner/repo. 생략하면 현재 폴더의 원격을 쓴다")
    ap.add_argument("--labels-only", action="store_true")
    ap.add_argument("--issues-only", action="store_true")
    args = ap.parse_args()

    if not shutil.which("gh"):
        print("gh CLI가 필요합니다: https://cli.github.com/", file=sys.stderr)
        print("설치 후 `gh auth login` 을 한 번 실행하세요.", file=sys.stderr)
        return 1

    repo_args = ["--repo", args.repo] if args.repo else []

    if not args.issues_only:
        print("라벨 만드는 중")
        for name, color, desc in LABELS:
            print(f"  {name}")
            run(["gh", "label", "create", name, "--color", color,
                 "--description", desc, *repo_args], args.dry_run)

    if not args.labels_only:
        print("\n시드 이슈 만드는 중")
        for it in ISSUES:
            print(f"  {it['key']}  {it['title']}")
            cmd = ["gh", "issue", "create",
                   "--title", it["title"],
                   "--body", it["body"]]
            for lb in it["labels"]:
                cmd += ["--label", lb]
            run(cmd + repo_args, args.dry_run)

    print("\n완료." if not args.dry_run else "\n(미리보기였습니다. --dry-run 을 빼면 실제로 만듭니다.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
