# ax-commons

**폐쇄 자료 없이도 고객과 현업이 스스로 판단할 수 있게 하는 AI 도구 모음.**

AX(AI 전환)에는 세 당사자가 있다. **AX 회사 · AX TF · 현업.**
지금은 균형이 없다. 현업이 제일 약하다.
자기 일을 남이 알아들을 형태로 기술할 언어도, 내려온 제안을 평가할 기준도 없어서다.

그리고 폐쇄 자료를 쥔 쪽이 "당신 회사를 이해시켜 드리겠다"를 판다.
**정작 그쪽이 AI를 잘 아는 것도 아니다.** 지대만 남고 역량은 없다.

이 저장소는 그 균형을 되돌리려는 도구다.
자료를 달라고 하지 않는다. **밖에서 재는 방법을 공개한다.**

> 설계 철학은 [PHILOSOPHY.md](PHILOSOPHY.md)에 있다. 장식이 아니라 설계를 규정하는 규칙이다.

---

## 5분 안에 시작하기

컴퓨터를 잘 몰라도 된다. **가장 쉬운 길은 아래 두 줄이다.**

1. [`prompts/system-prompt-full.md`](prompts/system-prompt-full.md) 파일을 연다
2. 전체를 복사해서 쓰던 AI 채팅창에 붙여 넣는다

끝이다. 설치도 계정도 필요 없다. ChatGPT, Claude, Gemini, 로컬 모델 어디서나 된다.

더 편하게 쓰고 싶으면 → [설치 안내](#설치) 로 간다.

---

## 무엇이 들어 있나

### 도구 1 · owner-lens — 오너의 렌즈

공개 신호(채용공고·뉴스·공시)만으로 회사의 목적함수를 역설계한다.
그리고 **그 개입이 담당자 임기 안에 회수되는지** 판정한다.

여섯 모드가 있다. 서 있는 자리에 따라 고른다.

| | 모드 | 누구를 위한 것인가 |
|---|---|---|
| A | 제안 준비 | AX 회사 |
| B | 자사 진단 | AX TF |
| C | 제안 검증 | TF · 현업 — 받은 제안서의 ROI 주장을 재계산 |
| D | 자료 재구성 | 자료 없는 모든 쪽 — 공개 뉴스로 리포트를 다시 만든다 |
| **E** | **현업 방어** | **현업** — 제일 약한 당사자 |
| **F** | **대립 검토** | 셋이 부딪칠 때. 합의가 아니라 정반합 |

→ [`skills/owner-lens/`](skills/owner-lens/)

### 도구 2 · insight-commons — 지식을 공유재로

현장 경험을 남이 쓸 수 있는 지식으로 만들고, **남의 지식이 내 조건에서 통하는지** 판정한다.

관통하는 규칙 하나.

> **남의 `[확인됨]`은 내게 `[미검증]`이다.**

→ [`skills/insight-commons/`](skills/insight-commons/)

---

## 왜 이렇게 만들었나

**권위를 만들지 않는다.** 산출물에 권위가 붙으면 반박이 막힌다.
컨설팅 자료의 힘은 내용보다 **불투명성**에서 온다. 출처를 안 보여주니 권위가 생긴다.

그래서 이 도구의 산출물은 항상 다음을 달고 나온다.

- 출처 대장 — 모든 주장이 어디서 왔는지
- 검증 로그 — 어떤 검증을 통과했고 어디서 실패했는지
- 실패 영역 — 도달하지 못한 것
- **반박 안내 — 이걸 깨려면 무엇을 보면 되는지**

마지막이 핵심이다. **자기를 공격하는 법을 스스로 알려준다.**
받은 사람이 "그렇군요"보다 "이 부분 근거가 뭐죠"를 하기 쉬워야 한다.

---

## 설치

쓰는 환경에 맞는 문서를 연다. **컴퓨터를 잘 몰라도 따라 할 수 있게 썼다.**

| 운영체제 | 문서 |
|---|---|
| 윈도우 (네이티브 · WSL) | [docs/install-windows.md](docs/install-windows.md) |
| 맥 (인텔 · 애플 실리콘) | [docs/install-macos.md](docs/install-macos.md) |
| 리눅스 (데비안·우분투 / RHEL·페도라, GUI·CLI) | [docs/install-linux.md](docs/install-linux.md) |

어디에 쓸지 정했으면 아래로 간다.

| 쓰는 곳 | 폴더 | 난이도 |
|---|---|---|
| **아무 AI 채팅창** (설치 없음) | [`prompts/`](prompts/) | ★☆☆ 복사·붙여넣기 |
| Claude 웹·앱 | [`dist/claude-web/`](dist/claude-web/) | ★☆☆ zip 올리기 |
| Claude Code | [`dist/claude-code/`](dist/claude-code/) | ★★☆ 폴더 복사 |
| GPT Codex | [`dist/codex/`](dist/codex/) | ★★☆ 파일 하나 |
| OpenClaw (자체호스팅 에이전트) | [`dist/openclaw/`](dist/openclaw/) | ★★☆ Claude와 같은 스킬 형식 |
| Hermes Agent (Nous, 프레임워크) | [`dist/hermes/`](dist/hermes/) | ★★★ 메모리 충돌 주의 |
| 로컬 오픈소스 모델 (30B 이하) | [`dist/local-models/`](dist/local-models/) | ★★★ Ollama · vLLM · LM Studio |

---

## 저장소 구조

```
skills/           ★ 원본. 여기만 고친다
prompts/          어디서나 붙여넣는 시스템 프롬프트
dist/             각 플랫폼용 배포본 — scripts/build로 생성된다
docs/             설치와 사용 안내
scripts/          빌드 스크립트
```

> **`dist/`는 직접 고치지 않는다.** `skills/`를 고치고 빌드를 돌린다.
> 안 그러면 8벌이 서로 어긋난다.

```bash
python scripts/build.py        # dist 전체 재생성
```

---

## 고쳐도 되는 것 / 안 되는 것

| | |
|---|---|
| **고쳐도 됨** | 임기 게이트 임계값 · 출력 언어와 분량 · 산업 마진 참조 · 신호 해석 규칙 |
| **고치면 다른 도구가 됨** | 뻔한 답 게이트 · 근거 등급 표기 · `[불가]` 판정 필수 · "남은 모름" 필수 · 반박 안내 필수 · 탈식별화 점검 |

아래쪽까지 고치는 것도 자유다. 다만 **다른 이름을 붙이기 바란다.**

각 스킬의 `references/tuning.md`가 고치는 곳이다.

---

## 한계 — 먼저 밝힌다

- **임기 게이트 임계값 0.6은 경험칙이지 검증된 값이 아니다.** 실제 결과로 조정해야 한다.
- **검증 등급 기준(2회 잠정, 3회 확인)도 통계적 유의성이 아니다.**
- 밖에서 본 것은 밖에서 본 것이다. 회사는 안에 들어가야 보인다.
- 한 사람이 쓰는 원장은 그 사람의 위치에 편중된다.

이 한계들을 숨기지 않는 것이 이 프로젝트의 방식이다.

---

## 기여

되돌려 주는 흐름이 있어야 이 프로젝트가 성립한다.

- **임기 게이트 임계값이 실제로 맞았는지 / 틀렸는지** ← 제일 필요하다
- 산업별 마진 스프레드 참조값 (출처와 연도 포함)
- 채용공고 해석 규칙 추가
- 다른 언어 번역
- 새 플랫폼 어댑터

**반례가 확인보다 값지다.** 조건을 좁힐 수 있게 해 주기 때문이다.

→ [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 라이선스

[CC0 1.0](LICENSE) — 퍼블릭 도메인.
저작자 표시 의무도 없다. 가져가서 마음대로 쓰고 고치고 팔아도 된다.

재생산이 가장 쉬운 형태를 골랐다. 그게 이 프로젝트의 목적이다.

---

## English

**ax-commons** gives customers and frontline workers the tools to judge AI
transformation proposals for themselves — without the closed datasets that
consultancies gate access behind.

Two skills:

- **owner-lens** reverse-engineers a company's objectives from public signals
  (job postings, filings, news), then checks whether a proposed intervention
  pays back **within the decision maker's remaining tenure**.
- **insight-commons** turns individual field experience into knowledge others
  can verify and reuse. Core rule: *someone else's `[confirmed]` is your `[unverified]`.*

Design principle: **create no authority.** Every output ships with a source
ledger, a verification log, what it failed to determine, and — most importantly —
**a guide to refuting it.**

Works anywhere. Start by pasting [`prompts/system-prompt-full.md`](prompts/system-prompt-full.md)
into any AI chat. Platform-specific packages are in [`dist/`](dist/).

CC0. Take it, fork it, sell it. Reproducibility is the point.
