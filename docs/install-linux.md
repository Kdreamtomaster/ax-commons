# 리눅스에서 쓰기

데비안 계열(우분투·민트·데비안)과 RHEL 계열(페도라·로키·알마·CentOS) 모두 다룬다.
GUI를 쓰는 경우와 터미널만 쓰는 경우를 나눠 적었다.

**위에서부터 순서대로. 1단계만 해도 다 쓸 수 있다.**

---

## 내 배포판 확인

```bash
cat /etc/os-release
```

`ID=` 줄을 본다.

| 나오는 값 | 계열 | 설치 명령 |
|---|---|---|
| `ubuntu` `debian` `linuxmint` `pop` | 데비안 | `apt` |
| `fedora` `rhel` `rocky` `almalinux` `centos` | RHEL | `dnf` |
| `arch` `manjaro` | 아치 | `pacman` |
| `opensuse*` | 수세 | `zypper` |

---

## 1단계 · 설치 없이 쓰기 ★ 대부분 여기서 끝난다

### GUI를 쓰는 경우

1. 저장소 웹페이지에서 초록색 **`Code`** → **`Download ZIP`**
2. 받은 파일에 오른쪽 클릭 → **여기에 풀기**
3. `prompts/system-prompt-full.md` 를 텍스트 편집기로 연다
   (그놈 텍스트 편집기 / Kate / gedit 아무거나)
4. `Ctrl` + `A` → `Ctrl` + `C` → AI 채팅창에 `Ctrl` + `V`

**끝이다.**

### 터미널만 쓰는 경우

```bash
git clone https://github.com/Kdreamtomaster/ax-commons.git
cd ax-commons
cat prompts/system-prompt-full.md
```

`git` 이 없으면:

```bash
sudo apt install -y git        # 데비안 계열
sudo dnf install -y git        # RHEL 계열
sudo pacman -S git             # 아치
sudo zypper install git        # 수세
```

**터미널에서 클립보드로 바로 복사하기**

```bash
# X11
sudo apt install -y xclip && xclip -selection clipboard < prompts/system-prompt-full.md

# 웨이랜드
sudo apt install -y wl-clipboard && wl-copy < prompts/system-prompt-full.md
```

지금 어느 쪽인지 모르겠으면:

```bash
echo $XDG_SESSION_TYPE
```

SSH로 접속한 서버라면 클립보드가 없다.
`cat` 으로 띄운 뒤 터미널에서 직접 긁어 복사한다.

---

## 2단계 · Claude 웹·앱에 스킬로 올리기

### zip 만들기

```bash
cd dist/claude-web
zip -r owner-lens.zip owner-lens
zip -r insight-commons.zip insight-commons
```

`zip` 이 없으면:

```bash
sudo apt install -y zip        # 데비안
sudo dnf install -y zip        # RHEL
```

> `dist/claude-web/`에 이미 만들어진 zip이 있으면 그걸 그냥 쓴다.

### 올리기

claude.ai → 왼쪽 아래 이름 → **설정** → **Capabilities** → **Skills** → 업로드

서버라 브라우저가 없으면, `scp` 로 내 PC에 내려받아 올린다.

```bash
# 내 PC에서 실행
scp 사용자@서버주소:~/ax-commons/dist/claude-web/*.zip .
```

---

## 3단계 · Claude Code에서 쓰기

```bash
mkdir -p ~/.claude/skills
cp -r dist/claude-code/* ~/.claude/skills/
ls ~/.claude/skills
```

`owner-lens` 와 `insight-commons` 가 보이면 된다.

---

## 4단계 · 직접 고쳐 쓰기

```bash
nano skills/owner-lens/references/tuning.md    # 또는 vim, code
python3 scripts/build.py
```

### 파이썬 설치

```bash
sudo apt install -y python3          # 데비안 계열
sudo dnf install -y python3          # RHEL 계열
sudo pacman -S python                # 아치
sudo zypper install python3          # 수세
```

빌드 스크립트는 **표준 라이브러리만** 쓴다. 추가 패키지가 필요 없다.

---

## 5단계 · 로컬 오픈소스 모델에 붙이기

30B 이하 모델로 돌리는 방법은 따로 정리했다.

→ [`dist/local-models/README.md`](../dist/local-models/README.md)

---

## 자주 막히는 곳

| 증상 | 해결 |
|---|---|
| `Permission denied` | 명령 앞에 `sudo` 를 붙인다. 홈 디렉터리 안이면 붙일 필요 없다 |
| `python: command not found` | 리눅스에서는 `python3` 로 친다 |
| SELinux가 막는다 (RHEL 계열) | 홈 디렉터리 안에서만 작업하면 안 걸린다 |
| 한글이 깨진다 | `locale` 확인 후 `sudo locale-gen ko_KR.UTF-8` |
| `~/.claude` 가 `ls` 에 안 보인다 | 숨김 폴더다. `ls -a` 로 본다 |
| 서버에 브라우저가 없다 | 1단계(붙여넣기)나 5단계(로컬 모델)를 쓴다 |

---

## 어느 단계까지 하면 되나

| 하고 싶은 것 | 필요한 단계 |
|---|---|
| 그냥 한번 써보고 싶다 | **1단계** |
| 자주 쓸 것 같다 | 2단계 |
| 개발 작업 중에 쓰고 싶다 | 3단계 |
| 고쳐서 쓰고 싶다 | 4단계 |
| 내 서버에서 완전히 자체 운영 | 5단계 |
