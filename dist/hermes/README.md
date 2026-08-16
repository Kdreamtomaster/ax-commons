# Hermes Agent

[Hermes Agent](https://github.com/nousresearch/hermes-agent)는 Nous Research의
오픈소스 에이전트 프레임워크다(MIT). 터미널·데스크톱 앱·메신저·IDE에서 돌아간다.

**모델이 아니라 프레임워크다.** 모델은 갈아끼운다 —
Nous Portal, OpenRouter, OpenAI, 자체 엔드포인트 어디든 붙는다.
어떤 모델을 쓸지는 [`../local-models/README.md`](../local-models/README.md)를 본다.

---

## 1. 설치 확인

Hermes가 이미 깔려 있어야 한다. 없으면 [공식 저장소](https://github.com/nousresearch/hermes-agent)의
설치 명령 한 줄이면 된다. uv와 Python 3.11까지 알아서 깔고 sudo가 필요 없다.

```bash
hermes --help
```

주요 경로:

| | 위치 |
|---|---|
| 설정 | `~/.hermes/config.yaml` |
| 스킬 | `$HERMES_HOME/skills/` (기본 `~/.hermes/skills/`) |

---

## 2. 스킬 넣기

**Hermes의 스킬 경로는 두 단계다.** `skills/<범주>/<이름>/`
Claude나 OpenClaw의 한 단계 구조와 다르니 주의한다.

```bash
mkdir -p ~/.hermes/skills/ax-commons
cp -r owner-lens insight-commons ~/.hermes/skills/ax-commons/
```

윈도우(PowerShell):

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.hermes\skills\ax-commons" | Out-Null
Copy-Item owner-lens,insight-commons "$env:USERPROFILE\.hermes\skills\ax-commons\" -Recurse -Force
```

최종 모양:

```
~/.hermes/skills/ax-commons/owner-lens/SKILL.md
~/.hermes/skills/ax-commons/insight-commons/SKILL.md
```

확인:

```bash
hermes skills list
hermes chat -q "초도 미팅 준비를 하려고 하는데 고객사 분석을 도와줘"
```

> `hermes skills install` 로 저장소에서 바로 받는 방식도 있다.
> 이 저장소를 깃헙에 올린 뒤에는 그 경로를 쓰면 복사가 필요 없다.

---

## 3. 메모리 충돌 주의 ★ — 이 문서에서 제일 중요하다

**Hermes는 에이전트가 스스로 메모리를 큐레이션한다.**
대화를 요약해 저장하고, 주기적으로 상기시키고, 복잡한 작업 뒤에는 스킬을 자동 생성하기도 한다.

이 기능은 대개 유용하다. 그런데 **이 도구의 규칙과 정면으로 부딪친다.**

`insight-commons`는 무엇이 남고 무엇이 사라져야 하는지를 엄격히 나눈다.

| | 남아야 함 | 사라져야 함 |
|---|---|---|
| 회사 카드 | 개인 보관 | 공유 금지 |
| 인사이트 원장 | 공유 가능 | — |
| 고객사명·담당자·가격·계약 조건 | — | **반드시 사라져야 함** |

자동 메모리는 이 구분을 하지 못한다. **고객사 정보가 그대로 저장될 수 있다.**
그리고 그 정보에서 파생된 요약이 나중에 다른 대화에 끌려 나올 수 있다.

### 대응 세 가지

**① 고객사별로 프로필을 분리한다** ← 권장

Hermes는 프로필마다 설정·세션·스킬·메모리를 격리한다.
이건 우리의 「회사 카드는 회사별로」 원칙과 정확히 맞아떨어진다.

```bash
hermes --profile client-a chat
hermes --profile client-b chat
```

한 고객사 정보가 다른 고객사 대화로 새지 않는다.

**② 인사이트 원장은 별도 프로필에서 만든다**

원장은 공유용이라 기밀이 섞이면 안 된다.
회사 분석과 원장 정리를 같은 프로필에서 하면 자동 메모리가 섞어 버린다.

```bash
hermes --profile commons chat -q "이번 건에서 배운 걸 원장 항목으로 정리해줘"
```

이때 회사 정보는 **사람이 직접 골라 붙여 넣는다.** 자동으로 끌어오게 두지 않는다.

**③ 자동 메모리를 끄거나 좁힌다**

민감한 고객사를 다룬다면 `~/.hermes/config.yaml` 에서 메모리 프로바이더를
끄거나 범위를 좁히는 것을 검토한다. 설정 키 이름은 버전마다 다르니
`hermes plugins` 와 공식 문서로 현재 값을 확인한다.

> **자동으로 기억하는 시스템 위에서 "잊어야 하는 규칙"을 지키려면 사람이 개입해야 한다.**
> 이건 Hermes의 결함이 아니다. 두 설계 목적이 다를 뿐이다.

---

## 4. 메신저로 쓸 때

Hermes는 텔레그램·디스코드·슬랙·왓츠앱·시그널을 게이트웨이 하나로 묶는다.
편하지만 이 도구를 쓸 때는 조심할 것이 있다.

- **고객사 정보를 메신저 대화에 흘리지 않는다.** 그 대화는 서버에 남는다
- 「회사 카드」는 단체방에서 만들지 않는다
- 공유하는 것은 탈식별화 점검을 통과한 「인사이트 원장」뿐이다
- 게이트웨이가 어느 모델을 쓰는지 확인한다. 외부 API면 그쪽으로 내용이 나간다
  자체 운영이 필요하면 [`../local-models/`](../local-models/)의 로컬 모델을 붙인다

---

## 5. 모델 고르기

Hermes는 모델을 갈아끼울 수 있다. 이 도구는 규칙이 많고 프롬프트가 길어서
**작은 모델은 규칙을 흘린다.** 크기별 안내는 [`../local-models/README.md`](../local-models/README.md)에 있다.

요약하면 **20~30B 이상**에서 제대로 작동하고, 문맥은 **32k 이상**이 필요하다.
temperature는 **0.3** 근처로 낮춘다. 창의성이 아니라 규칙 준수가 중요하다.

---

## 검증되지 않은 것

- **이 조합을 실제로 돌려보지 않았다.** 경로와 명령어는 공식 문서 기준이다
- Hermes 버전에 따라 설정 키와 스킬 경로 규칙이 달라질 수 있다
- 자동 메모리를 끄는 정확한 설정 키를 확인하지 못했다
- 프로필 분리가 메모리까지 완전히 격리하는지 실측하지 않았다

써 보고 틀린 곳을 알려주면 고친다. **반례가 확인보다 값지다.**

---

※ 이 폴더는 자동 생성 대상이 아니다. 안내 문서만 있다.
