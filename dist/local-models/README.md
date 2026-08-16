# 로컬 오픈소스 모델에서 쓰기 (30B 이하)

내 컴퓨터나 내 서버에서 완전히 자체 운영한다. 회사 정보가 밖으로 안 나간다.
**고객사 자료를 다루는 일이라 이게 중요할 때가 많다.**

이 폴더의 `system-prompt.md` 가 그대로 시스템 프롬프트다.

---

## 먼저 — 솔직한 성능 안내

이 도구의 프롬프트는 길고 규칙이 많다. **작은 모델은 규칙을 흘린다.**
특히 "뻔한 답 게이트"와 "근거 등급 표기"를 자주 빼먹는다.

| 모델 크기 | 쓸 수 있나 | 권장 프롬프트 | 주의 |
|---|---|---|---|
| ~4B | 힘들다 | compact | 단계를 하나씩 나눠서 시켜야 한다 |
| 7~9B | 제한적 | compact | 등급 표기를 자주 빠뜨린다. 사람이 확인 |
| 12~15B | 쓸 만하다 | compact / full | 대체로 규칙을 지킨다 |
| **20~30B** | **권장** | **full** | 여기서부터 제대로 작동한다 |

**문맥 길이는 32k 이상**을 권한다. full 프롬프트가 6~8천 토큰쯤 된다.
문맥이 짧으면 대화가 길어질수록 앞의 규칙을 잊는다.

> 작은 모델을 써야 한다면 **모드를 하나씩만** 돌린다.
> A~F를 다 넣지 말고, 지금 쓸 모드의 규칙만 남겨 프롬프트를 줄인다.

---

## 모델 고르기

크기 30B 이하에서 이 작업에 맞는 것들이다. 한국어를 많이 쓴다면 국산 모델도 본다.

| 모델 | 크기 | 특징 |
|---|---|---|
| Qwen3 30B-A3B | 30B (활성 3B) | MoE라 30B급인데 빠르다. 긴 규칙을 잘 따른다 |
| Qwen3 14B | 14B | 중간 사양에서 무난 |
| Gemma 3 27B | 27B | 어휘가 커서 한국어 토큰 효율이 낫다 |
| Mistral Small 3.x | 24B | 지시 따르기가 안정적 |
| gpt-oss 20B | 20B | OpenAI 공개 가중치 |
| Hermes 4 14B | 14B | 시스템 프롬프트 준수를 설계 목표로 삼은 모델. 규칙이 많은 이 도구에 맞을 가능성 |
| EXAONE | 7.8B / 32B | 한국어 특화 |
| Kanana | 8B급 | 한국어 특화 |

> Hermes **모델**과 [Hermes **Agent** 프레임워크](../hermes/)는 다른 것이다.
> 프레임워크는 모델을 갈아끼우는 껍데기고, 여기 표는 그 안에 넣을 모델 얘기다.

> **어느 모델이 이 작업에 제일 맞는지는 아직 검증되지 않았다.**
> 써 보고 결과를 알려주면 이 표를 고친다. 그게 이 프로젝트의 방식이다.

---

## 방법 A · Ollama (제일 쉽다)

### 설치

```bash
# 맥 / 리눅스
curl -fsSL https://ollama.com/install.sh | sh
```

윈도우는 [ollama.com](https://ollama.com/download)에서 설치 파일을 받는다.

### 모델 받고 실행

```bash
ollama pull qwen3:30b-a3b
```

### 시스템 프롬프트를 박아 전용 모델 만들기

매번 붙여 넣지 않으려면 `Modelfile` 을 만든다.

```bash
cd dist/local-models

# Modelfile 생성
{
  echo 'FROM qwen3:30b-a3b'
  echo 'PARAMETER num_ctx 32768'
  echo 'PARAMETER temperature 0.3'
  echo 'SYSTEM """'
  cat system-prompt.md
  echo '"""'
} > Modelfile

ollama create ax-commons -f Modelfile
ollama run ax-commons
```

> `temperature 0.3` 으로 낮춘 이유: 이 도구는 창의성이 아니라 **규칙 준수**가 중요하다.
> 값이 높으면 등급 표기와 게이트를 흘린다.

윈도우 PowerShell이면:

```powershell
cd dist\local-models
"FROM qwen3:30b-a3b`nPARAMETER num_ctx 32768`nPARAMETER temperature 0.3`nSYSTEM `"`"`"" | Out-File Modelfile -Encoding utf8
Get-Content system-prompt.md | Add-Content Modelfile -Encoding utf8
"`"`"`"" | Add-Content Modelfile -Encoding utf8
ollama create ax-commons -f Modelfile
```

---

## 방법 B · OpenAI 호환 API (표준 패턴)

Ollama · vLLM · LM Studio · llama.cpp 서버는 **모두 OpenAI와 같은 API**를 제공한다.
그래서 코드 하나로 전부 붙는다. 주소와 모델 이름만 바꾸면 된다.

| 실행기 | 기본 주소 |
|---|---|
| Ollama | `http://localhost:11434/v1` |
| vLLM | `http://localhost:8000/v1` |
| LM Studio | `http://localhost:1234/v1` |
| llama.cpp server | `http://localhost:8080/v1` |

### 파이썬

```python
from openai import OpenAI
from pathlib import Path

client = OpenAI(
    base_url="http://localhost:11434/v1",   # 위 표에서 골라 바꾼다
    api_key="not-needed",                    # 로컬은 아무 값이나
)

system = Path("system-prompt.md").read_text(encoding="utf-8")

resp = client.chat.completions.create(
    model="qwen3:30b-a3b",
    temperature=0.3,
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": "제조업 중견기업 초도 미팅 준비를 하려고 합니다."},
    ],
)
print(resp.choices[0].message.content)
```

`pip install openai` 만 있으면 된다.

### curl

```bash
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "model": "qwen3:30b-a3b",
  "temperature": 0.3,
  "messages": [
    {"role": "system", "content": $(python3 -c "import json,sys;print(json.dumps(open('system-prompt.md',encoding='utf-8').read()))")},
    {"role": "user", "content": "제조업 중견기업 초도 미팅 준비를 하려고 합니다."}
  ]
}
EOF
```

---

## 방법 C · vLLM (서버 운영용)

여러 사람이 같이 쓰거나 처리량이 필요하면 vLLM이 낫다.

```bash
pip install vllm

vllm serve Qwen/Qwen3-30B-A3B \
  --max-model-len 32768 \
  --port 8000
```

이후 방법 B의 코드에서 주소만 `http://localhost:8000/v1` 로 바꾼다.

GPU 메모리가 모자라면 양자화한 가중치를 쓴다.
다만 **양자화하면 규칙 준수가 먼저 나빠진다.** 등급 표기가 빠지기 시작하면 그 신호다.

---

## 방법 D · LM Studio (GUI, 컴맹 친화)

터미널을 안 쓰고 싶으면 이쪽이다.

1. [lmstudio.ai](https://lmstudio.ai) 에서 받아 설치
2. 검색창에서 모델을 골라 다운로드
3. 채팅 화면 왼쪽 **System Prompt** 칸에 `system-prompt.md` 내용을 붙여 넣는다
4. `Temperature` 를 **0.3** 으로 내린다
5. `Context Length` 를 **32768** 이상으로 올린다

서버로 쓰려면 **Developer** 탭 → **Start Server** 를 누르면
`http://localhost:1234/v1` 로 방법 B가 그대로 된다.

---

## 잘 안 될 때

| 증상 | 원인과 해결 |
|---|---|
| 등급 표기(`[사실]` 등)를 빼먹는다 | 모델이 작거나 temperature가 높다. 0.2~0.3으로 내린다 |
| "뻔한 답"을 안 적고 건너뛴다 | 작은 모델의 전형적 증상. compact 프롬프트 + 모드 하나만 |
| 대화가 길어지면 규칙을 잊는다 | 문맥 길이 부족. `num_ctx` / `--max-model-len` 을 올린다 |
| 질문을 4개 넘게 한다 | 사용자가 "질문은 4개까지"라고 한 번 상기시킨다 |
| 한국어가 어색하다 | 국산 모델(EXAONE, Kanana)을 시도한다 |
| 메모리 부족으로 죽는다 | 더 작은 모델이나 양자화 가중치를 쓴다 |
| 답이 너무 짧다 | `max_tokens` 를 4096 이상으로 |

---

## 결과를 알려주세요

이 표들은 아직 검증되지 않았다.

- 어떤 모델이 규칙을 잘 지켰는지 / 못 지켰는지
- 몇 B부터 쓸 만해지는지
- 양자화를 어디까지 내려도 되는지

알려주면 표를 고친다. **반례가 확인보다 값지다.**
