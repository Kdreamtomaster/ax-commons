---
title: ax-commons
description: 고객사 안에 들어가 보기 전에, 공개된 신호만으로 그 회사를 읽는 AI 도구 모음. CC0, 설치 불필요.
issue_feed: true
---

<div class="hero" markdown="0">
  <h1>한 자리에 서면,<br>나머지 두 자리는 보이지 않는다</h1>
  <p class="lede">
    AX에는 세 자리가 있다. 파는 쪽, 사는 쪽, 일하는 쪽.<br>
    이 도구는 <strong>공개 자료 — 인터뷰·공시·업계 동향 — 로 나머지 두 자리의 시각을 재구성해</strong>
    내 시각과 맞붙인다. 어긋난 지점이 진짜 상대에게 물을 질문이 된다.
  </p>
  <div class="badges">
    <span>CC0 · 퍼블릭 도메인</span>
    <span>설치 불필요</span>
    <span>한국어 원본</span>
    <span>어떤 AI 채팅창에서나</span>
  </div>
  <div class="cta">
    <a class="btn primary" href="https://github.com/Kdreamtomaster/ax-commons/blob/main/prompts/system-prompt-full.md">프롬프트 복사하러 가기</a>
    <a class="btn" href="{{ '/examples/' | relative_url }}">먼저 결과부터 보기</a>
    <a class="btn" href="https://github.com/Kdreamtomaster/ax-commons">GitHub</a>
  </div>
</div>

## 무엇이 나오나

같은 회사, 같은 안건을 세 자리가 다르게 본다. 이 도구는 그 어긋남을 드러낸다.

> **어긋난 지점 — 같은 데이터를 두고**
>
> 쟁점: 생산 실적 데이터는 정형인가

| 자리 | 주장 | 등급 |
|---|---|---|
| ① 파는 쪽 | "정형이다. 자동 집계가 된다" | `[추론]` |
| ③ 일하는 쪽 | "손으로 고쳐 넣는 값이 하루 아홉 번" | `[사실]` |

판정: **둘 다 맞다** — 결과는 정형, 과정은 비정형.
→ 어느 쪽도 처음엔 안 갖고 있던 답: 두 층 설계.

재구성한 상대와의 일치는 정보가 아니다.
**어긋남만 정보고, 그 어긋남이 진짜 상대에게 물을 질문이 된다.**

그리고 안건마다 마지막에 이걸 본다 — **의사결정진이 바뀌어도 이 안건이 성립하는가.**
보도자료·산업 트렌드·뉴스로 오너십 전환 시나리오를 여러 개 만들어 논거를 부딪친다.
사람은 채널이자 주체이지 논거가 아니다. 특정 인물의 임기나 성향 위에 안건을 세우면
그 사람과 함께 안건이 죽는다.

전체 산출은 [예시 5건]({{ '/examples/' | relative_url }})에 있다. 전부 가공 데이터다.

---

## 처음에 묻는 건 하나다

**어느 쪽에 서 계신가요?**

<div class="cards" markdown="0">
  <div class="card">
    <h3>① 파는 쪽 <small>(AX 회사)</small></h3>
    <p>고객사를 분석해 미팅 가설을 만든다. 사는 쪽·일하는 쪽에서 이 제안이 어떻게 보일지 먼저 부딪쳐 본다.</p>
  </div>
  <div class="card">
    <h3>② 사는 쪽 <small>(AX 추진 조직)</small></h3>
    <p>우리 회사를 보거나, 받은 제안서의 ROI 주장을 다시 계산한다. 회수 기간의 정의부터 맞춰 본다.</p>
  </div>
  <div class="card">
    <h3>③ 일하는 쪽 <small>(현업)</small></h3>
    <p>내 업무를 남이 알아들을 형태로 정리하고, 논의 자리에서 쓸 역질문을 만든다.</p>
  </div>
</div>

나머지는 도구가 알아서 고른다. 외울 것이 없다.

같은 회사를 세 자리에서 각각 본 예시가 있고, [그 셋을 맞붙인 예시]({{ '/examples/' | relative_url }})도 있다.

---

## 5분 안에 시작하기

컴퓨터를 잘 몰라도 된다. 가장 쉬운 길은 두 줄이다.

1. [`prompts/system-prompt-full.md`](https://github.com/Kdreamtomaster/ax-commons/blob/main/prompts/system-prompt-full.md) 를 연다
2. 전체를 복사해서 쓰던 AI 채팅창에 붙여 넣는다

끝이다. 설치도 계정도 필요 없다. ChatGPT · Claude · Gemini · 로컬 모델 어디서나 된다.

더 편하게 쓰고 싶으면 → [윈도우]({{ '/docs/install-windows.html' | relative_url }}) ·
[맥]({{ '/docs/install-macos.html' | relative_url }}) ·
[리눅스]({{ '/docs/install-linux.html' | relative_url }})

---

## 왜 이렇게 만들었나

**권위를 만들지 않는다.** 산출물이 권위를 갖는 순간 되묻기 어려워진다.

전문 자료가 설득력을 갖는 이유 중 하나는 출처를 일일이 보여주지 않는다는 점이다.
따져볼 수가 없으면 받아들이는 수밖에 없다. 이 도구는 반대로 간다.

그래서 산출물에 항상 넷을 붙인다.

- **출처 대장** — 모든 주장이 어디서 왔는지
- **검증 로그** — 어떤 검증을 통과했고 어디서 막혔는지
- **확인하지 못한 영역** — 끝내 닿지 못한 것
- **반박 안내** — 이 분석을 어디부터 따져보면 되는지

마지막이 핵심이다. **스스로 약한 곳을 먼저 알려준다.**

→ [설계 철학 전문]({{ '/PHILOSOPHY.html' | relative_url }})

---

## 지금 열려 있는 것

<div id="issues" markdown="0">
  <p class="state">이슈를 불러오는 중…</p>
</div>

[열린 이슈 전체](https://github.com/Kdreamtomaster/ax-commons/issues) ·
[디스커션](https://github.com/Kdreamtomaster/ax-commons/discussions) ·
[`첫걸음` 이슈만 보기](https://github.com/Kdreamtomaster/ax-commons/labels/%EC%B2%AB%EA%B1%B8%EC%9D%8C)

`첫걸음` 은 **돌려보고 결과만 알려주면 되거나, 고칠 곳이 명확한 것**이다.
프로그래밍을 안 해도 되는 것이 대부분이다.

---

## 한계를 먼저 밝힌다

<div class="notice" markdown="1">
**이 저장소는 실제 업무에서 쓰인 기록이 0건이다.**
한 사람의 경험칙이지 검증된 규칙이 아니다.
그리고 **테스트가 0개다.** 스킬이 규칙대로 동작하는지 보는 검사가 없다.
</div>

- 시나리오 게이트의 임계값 `0.6` 은 경험칙이다 ([#1](https://github.com/Kdreamtomaster/ax-commons/issues/1))
- 실사용 보고가 아직 없다 ([#24](https://github.com/Kdreamtomaster/ax-commons/issues/24))
- 동작 검사기가 없다 ([#25](https://github.com/Kdreamtomaster/ax-commons/issues/25))
- 로컬 모델 성능표는 추정이다 ([#2](https://github.com/Kdreamtomaster/ax-commons/issues/2))
- 밖에서 본 것은 밖에서 본 것이다. 회사는 안에 들어가야 보인다

**숨기지 않는 것이 이 프로젝트의 방식이다.**
산출물에 반박 안내를 붙이는 것과 같은 논리로, 저장소도 자기 약한 고리를 공개해 둔다.

→ [프로젝트 성숙도 자기평가]({{ '/MATURITY.html' | relative_url }})

---

## 어떻게 운영되나

혼자 시작한 프로젝트라 **누가 무엇을 정하는지 미리 적어 두었다.**
Apache 인큐베이터 방식에서 쓸 만한 것만 골라 왔다.

| 문서 | 무엇 |
|---|---|
| [지금 어디쯤 왔나]({{ '/MATURITY.html' | relative_url }}) | 항목별 자기평가와 알려진 위험 |
| [누가 정하나]({{ '/GOVERNANCE.html' | relative_url }}) | 게으른 합의, 72시간 규칙, 커밋 권한 얻는 법 |
| [왜 이렇게 됐나]({{ '/DECISIONS.html' | relative_url }}) | 지금까지의 결정과 그때 버린 것 |
| [행동 규칙]({{ '/CODE_OF_CONDUCT.html' | relative_url }}) | 반박과 공격을 어떻게 가르나 |

> **판단에는 최종 판정자가 없다.** 처음 온 사람이 반례를 대면 그게 이긴다.
> **병합에는 판정자가 있다.** 이 둘을 섞지 않는 것이 이 프로젝트의 운영 원칙이다.

---

## 누가 만들었나

프리세일즈 실무자가 **자기 문제를 풀려고** 만들었다. 회사 제품이 아니고 파는 것도 아니다.

대기업을 상대하면 결정권자를 만날 일이 없는데, 제안이 통하려면 그쪽의 목적을 알아야 한다.
그 재료는 유료이거나 계약 당사자만 볼 수 있다.

그래서 **자료를 달라고 하는 대신 밖에서 재는 방법을 공개**하기로 했다.
정확도는 떨어진다. 숨기지 않고 근거 등급으로 표기한다.
그래도 "없어서 아무것도 못 함"과 "거칠게라도 앎"의 차이는 크다.

[CC0 1.0](https://github.com/Kdreamtomaster/ax-commons/blob/main/LICENSE) — 퍼블릭 도메인.
저작자 표시 의무도 없다. 가져가서 마음대로 쓰고 고치고 팔아도 된다.
