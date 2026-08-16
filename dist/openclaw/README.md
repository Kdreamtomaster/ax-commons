# OpenClaw

OpenClaw는 메신저(텔레그램·슬랙·시그널·왓츠앱 등)를 AI 에이전트에 붙이는 자체호스팅 게이트웨이다.

**좋은 소식: OpenClaw는 Claude와 같은 `SKILL.md` 형식을 쓴다.**
YAML 프론트매터 + 마크다운 본문. 그래서 스킬 폴더를 그대로 복사하면 된다.

---

## 1. 스킬 넣기 (제일 간단)

```bash
mkdir -p ~/.openclaw/skills
cp -r owner-lens insight-commons ~/.openclaw/skills/
```

윈도우(PowerShell):

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.openclaw\skills" | Out-Null
Copy-Item owner-lens,insight-commons "$env:USERPROFILE\.openclaw\skills\" -Recurse -Force
```

최종 모양:

```
~/.openclaw/skills/owner-lens/SKILL.md
~/.openclaw/skills/insight-commons/SKILL.md
```

게이트웨이를 다시 시작하면 잡힌다.

### 다른 폴더에 두고 싶으면

`~/.openclaw/openclaw.json` 에 경로를 추가한다.

```json
{
  "skills": {
    "load": {
      "extraDirs": ["/경로/ax-commons/skills"]
    }
  }
}
```

이렇게 하면 **저장소를 `git pull` 하는 것만으로 갱신**된다. 복사할 필요가 없다.

---

## 2. 에이전트 성격에 반영하기 (선택)

OpenClaw는 `SOUL.md` 로 에이전트의 정체성과 행동 규칙을 정한다.
이 도구의 원칙을 항상 지키게 하려면 워크스페이스의 `SOUL.md` 에 아래를 더한다.

워크스페이스 기본 위치는 `~/.openclaw/workspace` 다.

```markdown
## 분석할 때의 원칙

- 일반론을 말하지 않는다. 뻔한 답을 먼저 적고 버린 뒤에 답한다.
- 모든 주장에 근거 등급을 붙인다. [사실] / [추론] / [가설] / [모름]
- [가설]에는 반드시 반증 조건을 단다.
- 모른다고 말하는 것이 기본값이다. "남은 모름"을 항상 남긴다.
- 권위를 만들지 않는다. 분석 끝에 「반박 안내」를 붙여
  이 분석을 어떻게 깰 수 있는지 스스로 알려준다.
- 회사와 직무를 다루고, 특정 개인의 신상은 다루지 않는다.
```

`SOUL.md` 는 항상 적용되고 `SKILL.md` 는 필요할 때 불려 온다.
**둘 다 넣으면 평소 성격과 전문 절차가 같이 간다.**

---

## 3. 워크스페이스에 AGENTS.md 로 넣기 (대안)

스킬 대신 항상 켜두고 싶으면 `dist/codex/AGENTS.md` 를 워크스페이스에 넣어도 된다.

```bash
cp ../codex/AGENTS.md ~/.openclaw/workspace/AGENTS.md
```

이미 `AGENTS.md` 가 있으면 내용을 이어 붙인다.

> 스킬 방식과 AGENTS.md 방식 중 **스킬 쪽을 권한다.**
> 항상 켜두면 문맥을 계속 잡아먹고, 이 도구가 필요 없는 대화에서도 끼어든다.

---

## 4. 메신저로 쓸 때 주의

OpenClaw는 메신저에 붙는다. 그래서 이 도구를 쓸 때 조심할 것이 있다.

- **고객사 정보를 메신저 대화에 흘리지 않는다.** 그 대화는 서버에 남는다
- 「회사 카드」는 기밀을 포함한다. 단체방에서 만들지 않는다
- 「인사이트 원장」만 공유한다. 탈식별화 점검을 통과한 것만
- 게이트웨이가 어느 LLM을 쓰는지 확인한다. 외부 API면 그쪽으로 내용이 나간다
  자체 운영이 필요하면 [`../local-models/`](../local-models/) 를 본다

---

## 확인

메신저에서 이렇게 말해 본다.

```
초도 미팅 준비를 하려고 하는데, 고객사 분석을 도와줘
```

문답이 시작되면 된다. 안 뜨면 `/owner-lens` 로 직접 부른다.

---

※ 이 폴더는 자동 생성 대상이 아니다. 안내 문서만 있다.
   스킬 원본은 `skills/` 이고 `python3 scripts/build.py` 로 갱신한다.
