# owner-lens

**공개 신호만으로 고객사 오너의 관점을 복원하는 Claude 스킬.**

고객사 안에 들어가 본 적 없는 상태에서, 채용공고·뉴스·공시 같은 공개 신호만으로
오너가 지금 무엇을 극대화하고 무엇을 방어하는지 역설계한다.
그리고 어느 자리에 서 있든 **나머지 두 자리의 시각을 재구성해 맞붙인다.**
어긋난 지점이 진짜 상대에게 물을 질문이 된다.

Claude 웹·앱 채팅에서 쓴다. 문답으로 정보를 받아가며 단계적으로 좁혀 간다.

---

## 왜 만들었나

컨설팅·SI·PE가 쥔 비공개 자료가 없으면 **자기 회사조차 분석할 수 없게** 되어 있다.
그 자료를 가진 쪽이 AI를 잘 아는 것도 아니다. **지대만 남고 역량은 없다.**

그래서 이 스킬은 자료를 달라고 하지 않는다. **밖에서 재는 방법을 공개한다.**

목표는 파는 쪽을 더 잘 팔게 하는 것이 아니다.
**고객과, 진짜로 AX를 하려는 쪽이 스스로 판단할 수 있게 하는 것**이다.
그래야 사회가 AX 흐름을 제대로 탄다.

정확도는 비공개 자료보다 떨어진다. 숨기지 않고 등급으로 표기한다.
그러나 "없어서 아무것도 못 함"과 "거칠게라도 앎"의 차이는 크다.

### 밑에 깔린 판단

- 애널리스트 리포트와 실사 자료는 마법이 아니라 **방법**이다. 막힌 것은 자료 접근이지 방법이 아니다.
- 그 자료의 힘은 내용보다 **불투명성**에서 온다. 출처를 안 보여주니 권위가 생긴다.
- 그래서 흉내 내지 않는다. **추적 가능한 버전**을 만든다.
  출처 대장·검증 로그·재구성 확인하지 못한 영역을 붙인다. 원본에는 없는 것들이다.
- 한 사람의 인사이트 원장(현장 배움을 모아 두는 장부)은 몇 건짜리 경험칙이지만,
  **여럿이 모으면 독점 벤치마크를 대신할 자료**가 된다. 그것이 이 프로젝트의 끝 그림이다.

---

## 다른 분석 프롬프트와 다른 점 세 가지

**1. 뻔한 답을 먼저 쓰고 버리게 한다**

"구체적으로 써라"는 안 통한다. 일반론을 밖으로 꺼내 명시적으로 버리지 않으면
계속 되살아난다. 각 단계는 `뻔한 답 → 버림 → 실제 답` 순서를 강제한다.

**2. 맞은편을 재구성해서 부딪친다**

어느 자리를 골랐든 나머지 두 자리의 시각을 인터뷰·공시·업계 동향으로 재구성해 맞붙인다.
재구성한 상대와의 **일치는 정보가 아니다.** 어긋남만 정보고,
그 어긋남이 진짜 상대에게 물을 질문이 된다.

그 검토의 끝에 **시나리오 게이트**가 있다 — *"의사결정진이 바뀌어도 이 안건이 성립하는가."*
보도자료·산업 트렌드·뉴스로 오너십 전환 시나리오를 만들어 논거를 부딪친다.
**사람은 채널이자 주체이지 논거가 아니다.** 특정 인물의 임기·성향 위에 안건을
세우면 그 사람과 함께 안건이 죽는다. 실질 임기는 비공개 정보고, 애초에 필요 없다.

**3. 모른다는 사실이 산출물이다**

"남은 모름"이 비어 있으면 분석이 아니라 창작으로 본다.
밖에서 본 것만으로 다 알 수는 없다. 모르는 걸 정확히 적는 게 정직한 결과다.

---

## 설치

1. 이 폴더를 통째로 받는다
2. `references/tuning.md`를 열어 **내 정보와 임계값을 채운다** ← 여기만 고치면 된다
3. 폴더를 압축해 Claude 설정의 스킬(Capabilities)에 올린다
4. 채팅에서 회사 얘기를 꺼내면 자동으로 뜬다. `/owner-lens`로 직접 불러도 된다

---

## 쓰는 법

```
1회차
  회사 이름과 내가 팔 수 있는 것만 알려준다
  → 스킬이 틀릴 각오로 거친 초안을 낸다
  → "여기가 틀렸다"고 고쳐 준다          ← 빈칸 채우기보다 이게 쉽다
  → 신호(채용공고 등) 보강
  → 최종 산출 + 회사 카드

  회사 카드를 복사해 보관한다

미팅

2회차
  회사 카드를 붙여 넣고 미팅 결과를 말한다
  → 틀린 가설부터 분석
  → 카드 갱신 + 인사이트 원장 추가
```

---

## 세 자리, 여섯 모드

처음 묻는 건 하나다. **어느 쪽에 서 계신가요?**

| 답 | 들어가는 모드 |
|---|---|
| **① 파는 쪽** (AX 회사) | A 제안 준비 |
| **② 사는 쪽** (AX 추진 조직) | B 자사 진단 / **C 제안 검증** |
| **③ 일하는 쪽** (현업) | E 현업 관점 |

D(자료 재구성)와 F(대립 검토)는 자리가 아니라 **시점**으로 정해진다.
자료가 거의 없으면 D가 앞에 붙고, 서로 다른 자리의 문서가 둘 모이면 F를 안내한다.

C와 D가 주권이 실제로 움직이는 자리다.
C는 벤더 주장을 검증하게 하고, D는 비공개 자료 없이 시작할 수 있게 한다.
그리고 어느 모드든 마지막에 **맞은편 재구성**이 붙는다 — 혼자여도 세 자리로 간다.

## 구조

```
SKILL.md                     진입점. 모드 · 문답 진행 · 규칙
references/
  pipeline.md                S1~S9 상세
  synthesis.md               ★ 공개 뉴스로 비공개 자료 재구성 (검증 6단계)
  substitution.md            비공개 자료 → 공개 대체물 대응표
  tuning.md                  ★ 고칠 곳은 여기 하나
  memory.md                  회사 카드 / 인사이트 원장 / 삭제 규칙
  post-meeting.md            미팅 후 검증 모드
templates/
  company-card.md            회사별 기록 (기밀 포함, 비공유)
  insight-ledger.md          전이 가능한 배움 (공유 가능 — 이게 공유재다)
```

### 고쳐도 되는 것 / 안 되는 것

| | |
|---|---|
| **고쳐도 됨** | 시나리오 게이트 임계값·시나리오 구성 · 출력 언어와 분량 · 산업 마진 참조 · 신호 해석 규칙 추가 |
| **고치면 다른 도구가 됨** | 뻔한 답 게이트 · 근거 등급 표기 · `[불가]` 판정 필수 · "남은 모름" 필수 · 원장 특정 가능성 점검 |

---

## 다루지 않는 것

- 분석 대상은 **회사와 직무**다. 특정 개인의 신상·평판·사생활은 다루지 않는다.
- 직위는 "이 자리의 권한과 임기 구조"로만 다룬다.
- 비공개로 들은 내용은 회사 카드에만 두고 공유 가능한 원장에는 올리지 않는다.
  삭제는 파생물까지 따라가야 한다 — 회사명을 지웠는데 문장이 그 회사를 특정하면 지운 게 아니다.

---

## 한계

- 밖에서 본 것은 밖에서 본 것이다. 회사는 안에 들어가야 보인다.
- 시나리오 게이트의 임계값(0.6, 필요 지평 계산)은 **경험칙이지 검증된 값이 아니다.**
  실제 결과로 조정해 나가야 한다. `post-meeting.md`가 그 조정을 돕는다.
- 인사이트 원장의 `[확인됨]`은 3건 기준이다. 통계적 유의미성과는 무관하다.

---

## 기여

실전에서 쓰고 나온 것을 환영한다. 특히:

- 시나리오 게이트 판정이 실제로 맞았는지 / 틀렸는지
- 산업별 마진 스프레드 참조값 (출처와 연도 포함)
- 채용공고 해석 규칙 추가
- 다른 언어 번역

**라이선스: [CC0 1.0](../../LICENSE).** 퍼블릭 도메인. 저작자 표시 의무도 없다.

---

## English

**owner-lens** reconstructs what a company's leadership is actually optimizing
for, using nothing but public signals — job postings, filings, news. Then,
whichever seat you're in — vendor, internal task force, or the people doing the
work — it **reconstructs how the other two seats would see the same issue**,
from published interviews, filings, and industry coverage, and puts the views
against each other. Agreement with a reconstructed counterpart means little;
the disagreements become the questions you ask the real one.

One of those questions most analysis skips: *will the decision maker still be
around when this pays back?* When tenure is unknown — it usually is — the tool
doesn't guess a number; it hands you the question to ask. Even a registered
term is a ceiling, not a prediction.

It works by conversation. It asks for very little, drafts something rough on
purpose, and lets you correct it — most people find fixing a wrong draft far
easier than filling in a blank form.

Set your own numbers in `references/tuning.md`. Everything else is method.
