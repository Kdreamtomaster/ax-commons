# 윈도우에서 쓰기

컴퓨터를 잘 몰라도 따라 할 수 있게 썼다. **위에서부터 순서대로 읽으면 된다.**
아래로 갈수록 어려워진다. **1단계만 해도 다 쓸 수 있다.**

---

## 1단계 · 설치 없이 쓰기 ★ 대부분 여기서 끝난다

프로그램을 깔 필요가 없다. 파일 하나를 복사해서 붙여 넣기만 하면 된다.

### 파일 받기

1. 저장소 웹페이지에서 초록색 **`Code`** 단추를 누른다
2. **`Download ZIP`** 을 누른다
3. 받은 파일이 보통 `다운로드` 폴더에 들어간다
4. 그 파일에 **마우스 오른쪽 → 압축 풀기** 를 누른다

### 붙여 넣기

1. 압축 푼 폴더에서 `prompts` 폴더로 들어간다
2. `system-prompt-full.md` 파일을 **메모장으로 연다**
   - 파일에 오른쪽 클릭 → **연결 프로그램** → **메모장**
3. `Ctrl` + `A` (전체 선택) → `Ctrl` + `C` (복사)
4. 쓰던 AI 채팅창(ChatGPT, Claude 등)에 `Ctrl` + `V` 로 붙여 넣고 보낸다

**끝이다.** AI가 문답을 시작한다.

> 매번 붙여 넣기 귀찮으면 → 2단계로 간다.

---

## 2단계 · Claude 웹·앱에 스킬로 올리기

한 번 올려두면 매번 붙여 넣지 않아도 된다.

### zip 만들기

1. 압축 푼 폴더에서 `dist` → `claude-web` 으로 들어간다
2. 안에 있는 `owner-lens` 폴더에 **오른쪽 클릭**
3. **보내기** → **압축(ZIP) 폴더**
4. `owner-lens.zip` 이 만들어진다. `insight-commons`도 똑같이 한다

> `dist/claude-web/`에 이미 만들어진 zip이 있으면 그걸 그냥 써도 된다.

### 올리기

1. Claude 웹(claude.ai)에 접속해 로그인
2. 왼쪽 아래 **내 이름** → **설정(Settings)**
3. **Capabilities**(기능) → **Skills**(스킬)
4. **업로드** 를 누르고 만든 zip을 고른다

이제 채팅에서 회사 얘기를 꺼내면 자동으로 뜬다.
직접 부르려면 `/owner-lens` 라고 치면 된다.

---

## 3단계 · Claude Code에서 쓰기

명령창을 쓸 줄 알아야 한다. 모르면 2단계까지만 해도 충분하다.

### 폴더 복사

1. `Win` + `R` 을 누르고 `%USERPROFILE%\.claude` 를 입력, 엔터
   - 폴더가 없다는 창이 뜨면, 먼저 Claude Code를 한 번 실행하면 생긴다
2. 그 안에 `skills` 폴더가 없으면 만든다
3. 받은 폴더의 `dist\claude-code\` 안에 있는 두 폴더를
   방금 연 `skills` 폴더로 **복사해 넣는다**

최종 모양:

```
C:\Users\사용자이름\.claude\skills\owner-lens\SKILL.md
C:\Users\사용자이름\.claude\skills\insight-commons\SKILL.md
```

### 확인

명령창(PowerShell)에서 `claude` 를 실행하고 아무 폴더에서나 `/owner-lens` 를 쳐 본다.

---

## 4단계 · WSL(우분투)에서 쓰기

윈도우 안에 리눅스를 돌리는 환경이다. 안 써봤으면 건너뛰어도 된다.

### WSL이 있는지 확인

PowerShell을 열고 아래를 친다.

```powershell
wsl --status
```

없다고 나오면 아래로 설치한다. **관리자 권한으로 PowerShell을 열어야 한다.**
(시작 단추에 오른쪽 클릭 → **터미널(관리자)**)

```powershell
wsl --install
```

설치 후 컴퓨터를 다시 켠다.

### 파일 가져오기

WSL 안에서:

```bash
git clone https://github.com/Kdreamtomaster/ax-commons.git
cd ax-commons
```

`git` 이 없다고 하면:

```bash
sudo apt update && sudo apt install -y git
```

### 윈도우 쪽 파일을 WSL에서 보기

WSL 안에서 윈도우 드라이브는 `/mnt/c/` 로 보인다.

```bash
cd /mnt/c/Users/사용자이름/Downloads/ax-commons-main
```

> 한글 폴더명이 섞이면 경로 입력이 까다롭다.
> **WSL에서 쓸 거면 `git clone`으로 새로 받는 편이 편하다.**

이후 사용법은 [리눅스 문서](install-linux.md)와 같다.

---

## 5단계 · 직접 고쳐 쓰기

시나리오 게이트 임계값이나 내 회사 정보를 넣고 싶으면:

1. `skills\owner-lens\references\tuning.md` 를 메모장으로 연다
2. 값을 채운다
3. 다시 zip으로 묶어 올린다 (2단계 반복)

**`dist` 폴더는 직접 고치지 않는다.** `skills` 를 고치고 다시 만든다.

파이썬이 깔려 있으면 아래 한 줄로 `dist` 전체를 다시 만들 수 있다.

```powershell
python scripts\build.py
```

파이썬이 없으면 [python.org](https://www.python.org/downloads/)에서 받는다.
설치할 때 **`Add Python to PATH` 를 반드시 체크**한다.

---

## 자주 막히는 곳

| 증상 | 해결 |
|---|---|
| 파일 확장자가 안 보인다 | 탐색기 → **보기** → **파일 확장명** 체크 |
| `.claude` 폴더가 안 보인다 | 탐색기 → **보기** → **숨긴 항목** 체크 |
| `python` 을 인식 못 한다 | 설치할 때 PATH 체크를 놓친 것. 다시 설치하며 체크 |
| zip 올리기가 실패한다 | 폴더 자체가 아니라 **폴더 안 내용**이 zip 최상위에 와야 한다 |
| 스킬이 자동으로 안 뜬다 | `/owner-lens` 로 직접 부른다 |
| 한글이 깨진다 | 메모장 대신 **VS Code** 나 **메모장++** 로 연다 |

---

## 어느 단계까지 하면 되나

| 하고 싶은 것 | 필요한 단계 |
|---|---|
| 그냥 한번 써보고 싶다 | **1단계** |
| 자주 쓸 것 같다 | 2단계 |
| 개발 작업 중에 쓰고 싶다 | 3단계 |
| 로컬 모델이나 자동화에 붙이고 싶다 | 4~5단계 |
