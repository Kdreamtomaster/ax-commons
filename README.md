# ax-commons

**고객사 안에 들어가 보기 전에, 공개된 신호만으로 그 회사를 읽는 AI 도구 모음.**

`CC0` · 설치 불필요 · 한국어 원본 · [English below](#english)

**📖 웹으로 읽기 → [kdreamtomaster.github.io/ax-commons](https://kdreamtomaster.github.io/ax-commons/)**

---

## 무엇이 나오나

같은 회사, 같은 안건을 **세 자리가 다르게 본다.** 이 도구는 그 어긋남을 드러낸다.


## 어긋난 지점 — 같은 데이터를 두고

쟁점: 생산 실적 데이터는 정형인가

| 자리 | 주장 | 등급 |
|---|---|---|
| ① 파는 쪽  | "정형이다. 자동 집계가 된다" | [추론] |
| ③ 일하는 쪽 | "손으로 고쳐 넣는 값이 하루 아홉 번" | [사실] |

판정: 둘 다 맞다 — 결과는 정형, 과정은 비정형.
→ 어느 쪽도 처음엔 안 갖고 있던 답: 두 층 설계


어느 자리에 서 있든, **나머지 두 자리의 시각을 인터뷰·공시·업계 동향으로 재구성해**
내 시각과 맞붙인다. 재구성한 상대와의 일치는 정보가 아니다.
**어긋남만 정보고, 그 어긋남이 진짜 상대에게 물을 질문이 된다.**

그리고 안건마다 마지막에 이걸 본다 — **의사결정진이 바뀌어도 이 안건이 성립하는가.**
보도자료·산업 트렌드·뉴스로 오너십 전환 시나리오를 여러 개 만들어 논거를 부딪친다.
사람은 채널이자 주체이지 논거가 아니다. 특정 인물의 임기나 성향 위에 안건을 세우면
그 사람과 함께 안건이 죽는다. 어느 시나리오에서도 성립하는 비즈니스 논리로 세운다.

전체 산출은 [예시](examples/)에 5건 있다. 전부 가공 데이터다.

---

## FDE라면 이 셋 중 하나는 겪었을 것이다

고객사에 들어가서 만드는 일을 하는 사람 — Forward Deployed Engineer, 솔루션 아키텍트,
프리세일즈, 컨설턴트 — 이 도구는 그 자리에서 겪는 세 가지를 다룬다.

| 겪는 일 | 이 저장소가 다루는 방식 |
|---|---|
| **들어가기 전에 도메인을 알아야 하는데 자료가 없다** | 채용공고·뉴스·공시만으로 회사의 목적함수를 역설계한다 |
| **잘 만들었는데 안 쓰인다** | 단절마다 묻는다 — *"여기 데이터를 안 넣으면 누가 곤란해지는가?"* 아무도 안 곤란하면 넣어도 안 쓰인다 |
| **배운 게 다음 고객사로 안 넘어간다** | 경험을 검증 등급이 붙은 항목으로 만들고, 남의 것이 내 조건에 통하는지 판정한다 |

FDE는 파는 쪽·사는 쪽·일하는 쪽을 **다 오간다.** 그래서 이 도구는 세 자리 모두를 지원한다.
같은 회사를 세 자리에서 각각 본 예시가 있고, 그 셋을 맞붙인 예시도 있다.

---

## 누가 왜 만들었나

프리세일즈 실무자가 **자기 문제를 풀려고** 만들었다. 회사 제품이 아니고 파는 것도 아니다.

막힌 지점은 이랬다. 대기업을 상대하면 결정권자를 만날 일이 없는데,
제안이 통하려면 그쪽의 사업 모델과 목적을 알아야 한다.
그 재료(실사 보고서·산업 벤치마크)는 유료이거나 계약 당사자만 볼 수 있다.

그래서 **자료를 달라고 하는 대신 밖에서 재는 방법을 공개**하기로 했다.
정확도는 떨어진다. 숨기지 않고 근거 등급으로 표기한다.
그래도 "없어서 아무것도 못 함"과 "거칠게라도 앎"의 차이는 크다.

> 설계 철학은 [PHILOSOPHY.md](PHILOSOPHY.md)에 있다. 장식이 아니라 설계를 규정하는 규칙이다.

---

## 5분 안에 시작하기

컴퓨터를 잘 몰라도 된다. **가장 쉬운 길은 아래 두 줄이다.**

1. [`prompts/system-prompt-full.md`](prompts/system-prompt-full.md) 파일을 연다
2. 전체를 복사해서 쓰던 AI 채팅창에 붙여 넣는다

끝이다. 설치도 계정도 필요 없다. ChatGPT, Claude, Gemini, 로컬 모델 어디서나 된다.

**무엇이 나오는지 먼저 보고 싶으면** → [예시](examples/) 로 간다.
가공 데이터로 한 회사를 처음부터 끝까지 분석한 결과가 그대로 있다.

더 편하게 쓰고 싶으면 → [설치 안내](#설치) 로 간다.

---

## 무엇이 들어 있나

### 도구 1 · owner-lens — 오너의 렌즈

공개 신호로 회사의 목적함수를 역설계하고, 시나리오 게이트로 판정한다.
**처음에 묻는 건 딱 하나다. 어느 쪽에 서 계신가요?**

> AX = AI Transformation. DX(디지털 전환)의 다음 단계로 쓰는 말이다.
> 이 저장소에서는 **AI를 실제 업무에 들이는 일 전반**을 가리킨다.

| 답 | 하는 일 |
|---|---|
| **① 파는 쪽** (AX 회사) | 고객사를 분석해 미팅 가설을 만든다 |
| **② 사는 쪽** (AX 추진 조직) | 우리 회사를 보거나, **받은 제안서의 ROI 주장을 다시 계산한다** |
| **③ 일하는 쪽** (현업) | 내 업무를 남이 알아들을 형태로 정리하고, 역질문을 만든다 |

나머지는 스킬이 알아서 고른다. 안쪽에는 여섯 모드가 있지만 외울 필요가 없다.
자료가 거의 없으면 **공개 뉴스로 리포트를 재구성**하는 단계가 앞에 붙고,
서로 다른 위치의 문서가 둘 모이면 **어긋난 지점을 정리**하는 단계를 안내한다.

→ [`skills/owner-lens/`](skills/owner-lens/)

### 도구 2 · insight-commons — 지식을 공유재로

현장 경험을 남이 쓸 수 있는 지식으로 만들고, **남의 지식이 내 조건에서 통하는지** 판정한다.

관통하는 규칙 하나.

> **남의 `[확인됨]`은 내게 `[미검증]`이다.**

→ [`skills/insight-commons/`](skills/insight-commons/)

---

## 왜 이렇게 만들었나

**권위를 만들지 않는다.** 산출물이 권위를 갖는 순간 되묻기 어려워진다.

전문 자료가 설득력을 갖는 이유 중 하나는 출처를 일일이 보여주지 않는다는 점이다.
따져볼 수가 없으면 받아들이는 수밖에 없다. 이 도구는 반대로 간다.

그래서 산출물에 항상 다음을 붙인다.

- 출처 대장 — 모든 주장이 어디서 왔는지
- 검증 로그 — 어떤 검증을 통과했고 어디서 막혔는지
- 확인하지 못한 영역 — 끝내 닿지 못한 것
- **반박 안내 — 이 분석을 어디부터 따져보면 되는지**

마지막이 핵심이다. **스스로 약한 곳을 먼저 알려준다.**
받은 사람이 "그렇군요"보다 "이 부분 근거가 뭔가요"를 하기 쉬워야 한다.

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
examples/         가공 데이터로 실제 돌려본 결과
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
| **고쳐도 됨** | 시나리오 게이트 임계값·시나리오 구성 · 출력 언어와 분량 · 산업 마진 참조 · 신호 해석 규칙 |
| **고치면 다른 도구가 됨** | 뻔한 답 게이트 · 근거 등급 표기 · `[불가]` 판정 필수 · "남은 모름" 필수 · 반박 안내 필수 · 탈식별화 점검 |

아래쪽까지 고치는 것도 자유다. 다만 **다른 이름을 붙이기 바란다.**

각 스킬의 `references/tuning.md`가 고치는 곳이다.

---

## 한계 — 먼저 밝힌다

- **시나리오 게이트의 임계값 0.6(필요 지평 계산)은 경험칙이지 검증된 값이 아니다.** ([#1](https://github.com/Kdreamtomaster/ax-commons/issues/1))
- **검증 등급 기준(2회 잠정, 3회 확인)도 통계적 유의성이 아니다.** (Q8 — 데이터가 모이면 연다)
- **로컬 모델 크기별 성능표는 추정이다.** 실측이 아니다. ([#2](https://github.com/Kdreamtomaster/ax-commons/issues/2))
- **Hermes·OpenClaw·Codex 연동은 공식 문서만 보고 썼다.** 직접 돌려보지 않았다.
  ([#3](https://github.com/Kdreamtomaster/ax-commons/issues/3) ·
   [#4](https://github.com/Kdreamtomaster/ax-commons/issues/4) ·
   [#5](https://github.com/Kdreamtomaster/ax-commons/issues/5))
- **실제 업무에서 쓰인 기록이 0건이다.** 한 사람의 경험칙이지 검증된 규칙이 아니다.
  ([#24](https://github.com/Kdreamtomaster/ax-commons/issues/24))
- **테스트가 0개다.** 스킬이 규칙대로 동작하는지 보는 검사가 없다.
  지금 검사기 둘은 글자만 본다. ([#25](https://github.com/Kdreamtomaster/ax-commons/issues/25))
- 밖에서 본 것은 밖에서 본 것이다. 회사는 안에 들어가야 보인다.
- 한 사람이 쓰는 원장은 그 사람의 위치에 편중된다.

**모르는 것을 이슈로 열어 두었다.** → [docs/open-questions.md](docs/open-questions.md) ·
[열린 이슈 전체](https://github.com/Kdreamtomaster/ax-commons/issues)

이 한계들을 숨기지 않는 것이 이 프로젝트의 방식이다.
산출물에 「반박 안내」를 붙이는 것과 같은 논리로, 저장소도 자기 약한 고리를 공개해 둔다.

**프로젝트 자체의 상태도 같은 방식으로 적어 두었다.** → [MATURITY.md](MATURITY.md)
지금 참여자는 1명이고, 실사용 보고는 0건이다.

---

## 기여

되돌려 주는 흐름이 있어야 이 프로젝트가 성립한다.
한 사람의 원장은 몇 건짜리 경험칙이지만, 여럿이 모이면 독점 벤치마크를 대신할 자료가 된다.

### 처음 오셨다면 → [`첫걸음`](https://github.com/Kdreamtomaster/ax-commons/labels/%EC%B2%AB%EA%B1%B8%EC%9D%8C) 이슈부터

**돌려보고 결과만 알려주면 되거나, 고칠 곳이 명확한 것**에 이 딱지를 붙여 뒀다.
프로그래밍을 안 해도 되는 것이 대부분이다.

```
#2   Ollama 로 모델 하나 돌려보고 규칙을 지켰는지 체크박스만 채우기
#3   Hermes Agent 를 쓰신다면 문서대로 되는지 확인
#4   OpenClaw 를 쓰신다면 스킬 경로가 맞는지 확인
#5   Codex 에 AGENTS.md 붙이고 "시나리오 게이트 돌려 줘" 물어보기
#19  대립 검토에 절 하나 추가 — 고칠 파일이 정해져 있다
```

### 세 가지 방법

| | 무엇 | 어디로 |
|---|---|---|
| **1** | **써 보고 결과 알려주기** ← 제일 필요하다 | [이슈 템플릿 ①③④](https://github.com/Kdreamtomaster/ax-commons/issues/new/choose) |
| **2** | 현장에서 얻은 배움을 원장 항목으로 내놓기 | [이슈 템플릿 ②](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=02-insight-entry.yml) |
| **3** | 문서·규칙·어댑터 고치기 | PR |

**1번이 가장 값지다.** 이 저장소에는 아직 검증되지 않은 값이 여럿 있다.
특히 [**시나리오 게이트의 임계값 0.6**](https://github.com/Kdreamtomaster/ax-commons/issues/1)은
경험칙이지 실측이 아니다.

> **틀렸다는 보고가 맞았다는 보고보다 값지다.** 조건을 좁힐 수 있게 해 주기 때문이다.

### 세 가지만 지켜 주시면 된다

- **가공 데이터를 쓴다.** 예시든 원장 항목이든 회사가 특정되면 안 된다.
  판단이 어려우면 `python3 scripts/scan-private.py` 가 잡아 준다
- **`skills/` 를 고치고 `python3 scripts/build.py` 를 돌린다.**
  `dist/` 를 직접 고치면 8벌이 서로 어긋난다
- **[용어집](docs/glossary.md)을 따른다.** 한 단어는 한 뜻으로만 쓴다.
  여기서 만드는 건 AI에게 주는 규칙이라, 용어가 모호하면 모델이 다르게 해석한다.
  **품질 문제가 아니라 동작 문제다**

### 답이 정해지지 않은 것은 [디스커션](https://github.com/Kdreamtomaster/ax-commons/discussions)

검증으로 닫을 수 없는 것들을 열어 두었다.
현업 모드가 대립을 만들지 않으려면, 원장을 어디에 모을지,
그리고 **이 도구가 파는 쪽에 더 유리한 것 아닌지** 같은 것들이다.

자세한 규칙은 → [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 어떻게 운영되나

혼자 시작한 프로젝트라 **누가 무엇을 정하는지 미리 적어 두었다.**
Apache 인큐베이터 방식에서 쓸 만한 것만 골라 왔다.

| 문서 | 무엇 |
|---|---|
| [MATURITY.md](MATURITY.md) | **지금 어디쯤 와 있나** — 항목별 자기평가와 알려진 위험 |
| [GOVERNANCE.md](GOVERNANCE.md) | **누가 정하나** — 게으른 합의, 72시간 규칙, 커밋 권한 얻는 법 |
| [DECISIONS.md](DECISIONS.md) | **왜 이렇게 되어 있나** — 지금까지의 결정과 그때 버린 것 |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | **반박과 공격을 어떻게 가르나** |

세 가지만 알면 된다.

- **되돌릴 수 있는 것은 그냥 고쳐서 PR을 보낸다.** 허락을 먼저 구하지 않는다
- **용어·기본값·구조를 바꾸는 것은 이슈를 열고 사흘 기다린다**
- **[도구의 성격을 바꾸는 것](#고쳐도-되는-것--안-되는-것)은 근거 있는 반대가 하나만 있어도 멈춘다**

> **판단에는 최종 판정자가 없다.** 처음 온 사람이 반례를 대면 그게 이긴다.
> **병합에는 판정자가 있다.** 이 둘을 섞지 않는 것이 이 프로젝트의 운영 원칙이다.

---

## 라이선스

[CC0 1.0](LICENSE) — 퍼블릭 도메인.
저작자 표시 의무도 없다. 가져가서 마음대로 쓰고 고치고 팔아도 된다.

재생산이 가장 쉬운 형태를 골랐다. 그게 이 프로젝트의 목적이다.

---

## English

**Read a company from the outside — before you ever get inside it.**

`CC0` · No install · Korean-first, English summary

### What it actually produces

The same company, the same issue — three seats see it differently. This tool
surfaces the disagreement:

```
## Where the views split — same data

At issue: is production data structured?

| Seat            | Claim                                      | Grade      |
|-----------------|--------------------------------------------|------------|
| ① Selling side  | "Structured. Auto-aggregation will work"   | [inference]|
| ③ Doing side    | "I hand-correct nine values a day"         | [fact]     |

Verdict: both are right — the *output* is structured, the *process* is not.
→ The answer neither side started with: a two-layer design.
```

Whichever seat you're in, it **reconstructs how the other two would see the
issue** — from published interviews, filings, and industry coverage — and puts
the views against each other. Agreement with a reconstructed counterpart means
little; the disagreements become the questions you ask the real one.

And every issue faces one final test: **does the case still stand when the
decision makers change?** The tool builds several ownership-transition
scenarios from press releases, industry trends, and news, then stress-tests
each argument against them. People are channels and agents, never the
argument — the moment a case rests on one person's tenure or disposition,
it dies with that person. Cases must rest on business logic that holds in
any scenario.

Five worked examples are in [`examples/`](examples/). All fabricated data.

### If you're an FDE, you've hit at least one of these

Forward deployed engineers, solutions architects, pre-sales, consultants — anyone
who has to build inside someone else's company:

| The problem | What this does about it |
|---|---|
| **You need domain context before you're inside** | Reverse-engineers what leadership is optimizing for, from public signals only |
| **You built the right thing and nobody uses it** | At every process break it asks: *"if this data doesn't get entered, who is inconvenienced?"* If nobody is, a tool there won't get used |
| **What you learned doesn't transfer to the next account** | Turns experience into entries with explicit verification status, and checks whether someone else's lesson applies to your conditions |

FDEs move between selling, buying, and doing. All three seats are supported, with
worked examples of the same company seen from each seat — and one where those views
are put against each other.

### Why it's built this way

Three groups shape an AI transformation: the vendor, the internal task force,
and the people who actually do the work. Each knows something the others don't,
and **the people doing the work know it best.** They know where time leaks,
which exceptions keep coming up, and what never makes it into the system at all.
Decisions improve when that knowledge reaches the table.

The evidence usually doesn't reach it. Due-diligence reports and industry
benchmarks sit behind a paywall or a contract, so understanding your own company
often means paying someone else to do it. This repo opens a second route:
**judge from public signals alone.**

### Two skills

**owner-lens** reconstructs a company's objectives from public signals — job
postings, filings, news — then asks whether a proposed change pays back
**within the decision maker's remaining tenure.** That question stops more good
proposals than any technical objection, and almost no analysis asks it.

**insight-commons** turns field experience into knowledge other people can check.
One rule runs through it:

> **Someone else's `[confirmed]` is your `[unverified]`.**

Three confirmations under their conditions don't carry over to yours.
Counterexamples are never deleted; they narrow the conditions instead.

### The guiding principle: don't manufacture authority

An output that carries authority is hard to question. Part of what makes expert
reports persuasive is that they don't show their sources — if you can't check the
work, you can only accept it. This goes the other way. Every output ships with a
source ledger, a verification log, a plain list of what it couldn't determine,
and **a guide to arguing against it.**

Point at your own weak spots first, or the tool becomes one more authority.

That applies to the repo itself. Everything unverified is
[filed as an open issue](https://github.com/Kdreamtomaster/ax-commons/issues) —
including the tenure-gate threshold, which is a rule of thumb, not a measured value
([#1](https://github.com/Kdreamtomaster/ax-commons/issues/1)). There's even an open
discussion asking whether this tool
[quietly favors the selling side](https://github.com/Kdreamtomaster/ax-commons/discussions/18).

### Getting started

Paste [`prompts/system-prompt-full.md`](prompts/system-prompt-full.md) into any
AI chat. No install, no account. Packages for Claude, Codex, OpenClaw, Hermes
Agent, and local models under 30B are in [`dist/`](dist/).

New here? Start with the
[`첫걸음`](https://github.com/Kdreamtomaster/ax-commons/labels/%EC%B2%AB%EA%B1%B8%EC%9D%8C)
label — issues where you just run something and report what happened.
Reports that the tool got it **wrong** are worth more than confirmations.

Built by a pre-sales practitioner to solve their own problem. Not a company product,
not for sale. Korean is the source language; this section is a summary, not a full
translation ([#9](https://github.com/Kdreamtomaster/ax-commons/issues/9)).

**CC0 — public domain.** Fork it, change it, sell it. Easy reuse is the point.
