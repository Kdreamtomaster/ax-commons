# 아직 검증되지 않은 것들

이 프로젝트가 **모른다고 인정하는 목록**이다.
숨기지 않는 것이 이 도구의 방식이라, 문서에도 그대로 적는다.

각 항목에 **무엇이 관찰되면 결론이 나는지**를 함께 적었다.
그게 없으면 영원히 "검토 중"으로 남는다.

---

## 이슈 대응표

| | 항목 | 이슈 | 상태 |
|---|---|---|---|
| Q1 | 임기 게이트 `0.6` ★ | [#1](https://github.com/Kdreamtomaster/ax-commons/issues/1) | 열림 |
| Q2 | 몇 B부터 작동하는가 | [#2](https://github.com/Kdreamtomaster/ax-commons/issues/2) | 열림 |
| Q3 | Hermes Agent 연동 | [#3](https://github.com/Kdreamtomaster/ax-commons/issues/3) | 열림 |
| Q4 | OpenClaw 연동 | [#4](https://github.com/Kdreamtomaster/ax-commons/issues/4) | 열림 |
| Q5 | Codex `AGENTS.md` 분량 | [#5](https://github.com/Kdreamtomaster/ax-commons/issues/5) | 열림 |
| Q6 | 산업 마진 스프레드 | [#6](https://github.com/Kdreamtomaster/ax-commons/issues/6) | 열림 |
| Q7 | 채용공고 해석 규칙 | [#7](https://github.com/Kdreamtomaster/ax-commons/issues/7) | 열림 |
| Q8 | 검증 등급 기준 | — | **보류**. 원장 항목이 쌓인 뒤 재검토 |
| Q9 | 탈식별화가 실제로 되는가 | [#8](https://github.com/Kdreamtomaster/ax-commons/issues/8) | 열림 |
| Q10 | 영어판 범위 | [#9](https://github.com/Kdreamtomaster/ax-commons/issues/9) | 열림 |

> Q8만 이슈가 없다. 지금 논의해도 근거가 될 데이터가 없어서다.
> [#2 템플릿](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=02-insight-entry.yml)으로
> 원장 항목이 어느 정도 모이면 그때 연다.

새 항목을 추가하면 [`scripts/setup-github.py`](../scripts/setup-github.py)에도 넣고
`python3 scripts/setup-github.py` 를 돌린다. 이미 있는 이슈는 건너뛴다.

---

## Q1. 임기 게이트 `safe_ratio: 0.6` 이 맞는 값인가 ★

**지금 상태** 경험칙. 실측 없음. 이 프로젝트에서 제일 중요한 미검증 항목.

`owner-lens` 의 S7은 `회수 기간 < 잔여 임기 × 0.6` 이면 "팔린다"로 판정한다.
0.6이라는 숫자에 근거가 없다.

**무엇이 관찰되면 결론이 나는가**

- 서로 다른 조직 10건 이상에서 게이트 판정과 실제 결과를 대조
- 특히 **탈락시켰는데 상대가 오히려 원한 사례**가 나오면 임계값이 너무 보수적이다
- 통과시켰는데 관심이 없던 사례가 반복되면 임계값 말고 **다른 변수**가 있다는 뜻

**이미 나온 의심** 임기만이 아니라 **담당자 KPI와의 연결 여부**가 더 셀 수 있다.
회수가 짧아도 자기 평가지표와 무관하면 움직이지 않는다.

→ **[이슈 #1](https://github.com/Kdreamtomaster/ax-commons/issues/1)** ·
보고는 [템플릿 ①](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=01-tenure-gate-report.yml)

---

## Q2. 몇 B부터 이 도구가 제대로 작동하는가

**지금 상태** `dist/local-models/README.md` 의 크기별 표는 **추정이다.**
"7~9B는 등급 표기를 자주 놓친다"도 근거 없이 쓴 문장이다.

**무엇이 관찰되면 결론이 나는가**

같은 입력으로 여러 모델을 돌려 **규칙 준수 여부만** 채점한다. 답변 품질이 아니다.

체크 항목: 등급 표기 · 반증 조건 · 뻔한 답 게이트 · 질문 4개 제한 ·
R1 초안 우선 · `[불가]` 판정 · "남은 모름" · 반박 안내 · 임기 게이트 계산 · 표 형식

**특히 궁금한 것**

- 대화가 길어지며 무너지는지, 처음부터 무시하는지 (원인이 다르다)
- 양자화를 어디까지 내려도 되는지. 등급 표기가 먼저 사라지는지
- 국산 모델(EXAONE, Kanana)의 한국어 품질이 실제로 나은지

→ **[이슈 #2](https://github.com/Kdreamtomaster/ax-commons/issues/2)** ·
보고는 [템플릿 ③](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=03-model-report.yml)

---

## Q3. Hermes Agent 연동이 실제로 되는가

**지금 상태** 공식 문서만 보고 썼다. **직접 돌려보지 않았다.**

확인 못 한 것:

- 스킬 경로 `~/.hermes/skills/<범주>/<이름>/` 가 맞는지
- **자동 메모리를 끄거나 좁히는 정확한 설정 키**
- **프로필 분리가 메모리까지 완전히 격리하는지** ← 제일 중요
- `hermes skills install` 로 깃헙 저장소에서 바로 받을 때의 경로 형식

**왜 중요한가** Hermes는 에이전트가 스스로 메모리를 큐레이션한다.
`insight-commons` 는 고객사명·가격·계약 조건이 **반드시 사라져야 한다**고 규정한다.
프로필 격리가 불완전하면 **한 고객사 정보가 다른 고객사 대화로 샌다.**

→ **[이슈 #3](https://github.com/Kdreamtomaster/ax-commons/issues/3)** ·
보고는 [템플릿 ④](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=04-adapter-report.yml)

---

## Q4. OpenClaw 연동이 실제로 되는가

**지금 상태** 문서 기준으로만 작성. 미실행.

- `~/.openclaw/skills/<이름>/SKILL.md` 로 잡히는지
- `openclaw.json` 의 `skills.load.extraDirs` 로 저장소를 직접 걸었을 때 되는지
- `SOUL.md` 에 원칙을 넣었을 때 스킬과 충돌하지 않는지

→ **[이슈 #4](https://github.com/Kdreamtomaster/ax-commons/issues/4)** ·
보고는 [템플릿 ④](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=04-adapter-report.yml)

---

## Q5. GPT Codex의 `AGENTS.md` 가 이 분량을 감당하는가

**지금 상태** 빌드로 생성만 했고 실동작 미확인.

두 스킬을 한 파일로 합쳐서 꽤 길다.
Codex가 이 길이를 다 읽는지, 앞부분만 반영하는지 모른다.

**무엇이 관찰되면 결론이 나는가**
Codex에게 "임기 게이트를 계산해 달라"고 했을 때 규칙을 알고 있으면 읽은 것이다.
모르면 분량을 줄이거나 스킬을 하나만 넣어야 한다.

→ **[이슈 #5](https://github.com/Kdreamtomaster/ax-commons/issues/5)** ·
보고는 [템플릿 ④](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=04-adapter-report.yml)

---

## Q6. 산업별 마진 스프레드가 비어 있다

**지금 상태** `tuning.md` 의 `margin_reference` 가 **빈 껍데기다.**

`owner-lens` 의 S5는 "이 산업 상위/중위/하위 영업이익률"에서 출발한다.
그 값이 없으면 `[모름]`으로 진행하게 되고, 분석의 날이 무뎌진다.

**필요한 것** 산업별 스프레드 + **출처와 연도.**
숫자는 낡으므로 출처 없는 값은 받지 않는다.

한국은행 기업경영분석, 통계청, 업종별 협회 공시가 공개 출처다.

→ **[이슈 #6](https://github.com/Kdreamtomaster/ax-commons/issues/6)** ·
제출은 [템플릿 ⑤](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=05-reference-data.yml)

---

## Q7. 채용공고 해석 규칙이 실제로 맞는가

**지금 상태** `pipeline.md` 의 S1 해석표는 **경험에서 나온 추측이다.**

예: "오래 열려 있는 자리 = 못 채우는 자리 = 병목이거나 처우가 낮다"

이게 맞는지 확인된 바 없다. 단순히 채용을 늦게 하는 조직일 수도 있다.

**무엇이 관찰되면 결론이 나는가**
공고를 보고 세운 가설을 미팅에서 확인한 사례. 맞은 것보다 **틀린 것**이 값지다.

→ **[이슈 #7](https://github.com/Kdreamtomaster/ax-commons/issues/7)** ·
제출은 [템플릿 ⑤](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=05-reference-data.yml)

---

## Q8. 검증 등급 기준(2회 잠정 / 3회 확인)이 타당한가

**지금 상태** 임의로 정한 숫자다. 통계적 유의성과 무관하다.

3건이면 충분한가? 아니면 조건이 좁을 때는 2건으로 족하고 넓을 때는 더 필요한가?

**의심** 건수보다 **조건의 다양성**이 중요할 수 있다.
같은 산업 3건보다 다른 산업 2건이 전이 범위를 더 잘 말해 준다.

**이슈를 아직 열지 않았다.** 지금 논의해도 근거가 될 데이터가 없어서다.
[템플릿 ②](https://github.com/Kdreamtomaster/ax-commons/issues/new?template=02-insight-entry.yml)로
원장 항목이 20건쯤 모이면 그때 연다.

---

## Q9. 탈식별화가 실제로 되는가

**지금 상태** "이 문장만 보고 어디인지 좁혀지는가?" 라는 자문 규칙만 있다.

**문제** 쓰는 사람은 자기 글이 얼마나 특정 가능한지 잘 모른다.
업계 사람이 보면 바로 아는데 본인은 충분히 뭉갰다고 여긴다.

**필요한 것** 실패 사례. "이렇게 썼는데 사람들이 알아보더라"

→ **[이슈 #8](https://github.com/Kdreamtomaster/ax-commons/issues/8)**

---

## Q10. 영어판이 필요한가, 필요하면 어디까지

**지금 상태** README와 각 스킬에 짧은 영문 요약만 있다.

전체 번역은 유지 비용이 크다. 한국어판과 영어판이 어긋나기 시작하면
어느 쪽이 원본인지 모르게 된다.

**정할 것** 원본 언어를 하나로 고정할지, 아니면 병행할지.
지금은 **한국어가 원본**이고 영어는 요약이다.

→ **[이슈 #9](https://github.com/Kdreamtomaster/ax-commons/issues/9)**

---

## 이 목록을 쓰는 법

- 결론이 나면 해당 항목을 지우지 말고 **결론과 근거를 적어 남긴다**
- 반례가 나오면 조건을 좁혀 다시 쓴다
- 새로 모르는 것이 생기면 여기에 더한다
- 이슈가 닫히면 위 대응표의 상태를 갱신한다

**"남은 모름"이 비어 있으면 분석이 아니다.** 그 규칙은 이 문서에도 적용된다.
