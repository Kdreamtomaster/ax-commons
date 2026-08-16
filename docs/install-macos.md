# 맥에서 쓰기

인텔 맥과 애플 실리콘(M1~M4) 모두 같은 방법이다. 다른 부분만 따로 표시했다.
**위에서부터 순서대로 읽으면 된다. 1단계만 해도 다 쓸 수 있다.**

---

## 내 맥이 어느 쪽인지 확인 (나중에 필요할 때만)

화면 왼쪽 위 **사과 메뉴** → **이 Mac에 관하여**

- **칩: Apple M1/M2/M3/M4** → 애플 실리콘
- **프로세서: Intel** → 인텔

1~2단계에서는 몰라도 된다.

---

## 1단계 · 설치 없이 쓰기 ★ 대부분 여기서 끝난다

### 파일 받기

1. 저장소 웹페이지에서 초록색 **`Code`** 단추 → **`Download ZIP`**
2. 받은 파일이 **다운로드** 폴더에 들어간다
3. 파일을 **두 번 클릭**하면 압축이 풀린다

### 붙여 넣기

1. 압축 푼 폴더에서 `prompts` 폴더로 들어간다
2. `system-prompt-full.md` 를 **텍스트 편집기로 연다**
   - 파일에 오른쪽 클릭(또는 `control` + 클릭) → **다음으로 열기** → **텍스트 편집기**
3. `⌘` + `A` (전체 선택) → `⌘` + `C` (복사)
4. 쓰던 AI 채팅창에 `⌘` + `V` 로 붙여 넣고 보낸다

**끝이다.**

---

## 2단계 · Claude 웹·앱에 스킬로 올리기

### zip 만들기

1. 압축 푼 폴더에서 `dist` → `claude-web` 으로 들어간다
2. `owner-lens` 폴더에 오른쪽 클릭 → **"owner-lens" 압축**
3. `owner-lens.zip` 이 만들어진다. `insight-commons`도 똑같이

> `dist/claude-web/`에 이미 만들어진 zip이 있으면 그걸 그냥 쓴다.

### 올리기

1. claude.ai 로그인 → 왼쪽 아래 **내 이름** → **설정**
2. **Capabilities** → **Skills** → **업로드**

채팅에서 `/owner-lens` 로 부를 수 있다.

---

## 3단계 · Claude Code에서 쓰기

터미널을 써야 한다. 처음이면 겁먹지 말고 그대로 따라 치면 된다.

### 터미널 여는 법

`⌘` + `스페이스` → `터미널` 입력 → 엔터

### 폴더 복사

```bash
mkdir -p ~/.claude/skills
cd ~/Downloads/ax-commons-main
cp -r dist/claude-code/* ~/.claude/skills/
```

> 폴더 이름이 다르면 `cd ` 까지 친 다음
> **파인더에서 폴더를 터미널 창으로 끌어다 놓으면** 경로가 자동으로 들어간다.

### 확인

```bash
ls ~/.claude/skills
```

`owner-lens` 와 `insight-commons` 가 보이면 된다.

---

## 4단계 · 직접 고쳐 쓰기

`skills/owner-lens/references/tuning.md` 를 열어 값을 채운다.
그다음 `dist` 를 다시 만든다.

```bash
python3 scripts/build.py
```

### 파이썬이 없다고 나오면

맥에는 보통 `python3` 가 이미 있다. 없으면 둘 중 하나로 설치한다.

**방법 A — Homebrew (권장)**

Homebrew가 없으면 먼저 설치한다.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

설치가 끝나면 **애플 실리콘**은 아래를 추가로 실행하라고 안내가 나온다.
안내에 나온 두 줄을 그대로 복사해 실행한다. 보통 이런 모양이다.

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

> 인텔 맥은 경로가 `/usr/local/bin/brew` 다. 안내문을 그대로 따르면 된다.

그다음:

```bash
brew install python git
```

**방법 B — 설치 파일**

[python.org](https://www.python.org/downloads/macos/)에서 받아 설치한다.

---

## 자주 막히는 곳

| 증상 | 해결 |
|---|---|
| `~/.claude` 폴더가 안 보인다 | 파인더에서 `⌘` + `shift` + `.` 를 누르면 숨김 파일이 보인다 |
| `zsh: command not found: brew` | 위 `eval` 두 줄을 실행하지 않은 것. 터미널을 껐다 켠다 |
| `Operation not permitted` | 시스템 설정 → 개인정보 보호 및 보안 → **전체 디스크 접근 권한**에 터미널 추가 |
| 파일이 "확인되지 않은 개발자" 라고 막힌다 | 이 저장소는 텍스트 파일뿐이라 이 경고가 뜰 일이 없다. 뜨면 받은 곳을 다시 확인한다 |
| zip 올리기가 실패한다 | 폴더 자체가 아니라 **폴더 안 내용**이 zip 최상위에 와야 한다 |
| 한글이 깨진다 | 텍스트 편집기 대신 **VS Code** 로 연다 |

---

## 어느 단계까지 하면 되나

| 하고 싶은 것 | 필요한 단계 |
|---|---|
| 그냥 한번 써보고 싶다 | **1단계** |
| 자주 쓸 것 같다 | 2단계 |
| 개발 작업 중에 쓰고 싶다 | 3단계 |
| 고쳐서 쓰고 싶다 | 4단계 |
