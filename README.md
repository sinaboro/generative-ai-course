# 🤖 생성형 AI 입문 — 프롬프트부터 RAG · Agent 서비스까지

LLM 을 처음 다루는 **초보자**를 위한 자기주도 학습 과정이에요. 생성형 AI 의 원리, 프롬프트 엔지니어링, Python 으로 LLM API 부르기부터 웹 챗봇, 임베딩 · RAG, AI Agent, 최종 프로젝트까지 단계별로 배워요. 모든 예제는 실제 LLM(OpenRouter)으로 실행한 결과를 교안에 실었어요.

- **강사**: 김대철
- 📕 **통합 교안 PDF**: [생성형AI_통합교안.pdf](%EC%83%9D%EC%84%B1%ED%98%95AI_%ED%86%B5%ED%95%A9%EA%B5%90%EC%95%88.pdf) (현재 기본 Part 01 ~ 03 + 심화 Part 08 · 10 · 11, 117쪽 · 학습 안내 · 용어 사전 · 막힐 때 점검표 포함)
- **실습 환경**: Windows + Python 3.12 이상 + VS Code + OpenRouter API 키 (키가 없으면 "연습 모드"로 실행돼요)
- 함께 보면 좋은 과정: [ai-service-course](https://github.com/sinaboro/ai-service-course) (Python · HTML/CSS · JavaScript · FastAPI · AI 딥러닝)

## 📚 과정 구성 (기본 90시간 + 심화 10시간)

| Part | 주제 | 주요 내용 | 시간 | 교안 |
|:---:|---|---|---:|:---:|
| 01 | [생성형 AI 첫걸음](01_%EC%83%9D%EC%84%B1%ED%98%95AI_%EC%B2%AB%EA%B1%B8%EC%9D%8C/) | LLM · 토큰 · temperature · 환각, ChatGPT · Claude · Gemini 써 보기 | 6h | [📘](01_%EC%83%9D%EC%84%B1%ED%98%95AI_%EC%B2%AB%EA%B1%B8%EC%9D%8C/01_%EC%83%9D%EC%84%B1%ED%98%95AI_%EC%B2%AB%EA%B1%B8%EC%9D%8C_%EA%B5%90%EC%95%88.docx) |
| 02 | [프롬프트 엔지니어링](02_%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8_%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81/) | 구체적으로 · System Prompt · Few-shot · 출력 형식 · 단계별로 · 템플릿 | 6h | [📘](02_%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8_%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81/02_%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8_%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81_%EA%B5%90%EC%95%88.docx) |
| 03 | [Python 으로 LLM 부르기](03_Python_LLM_API/) | .env · OpenRouter · messages · temperature · 토큰과 요금 · 오류 처리 | 8h | [📘](03_Python_LLM_API/03_Python_LLM_API_%EA%B5%90%EC%95%88.docx) |
| 04 | LLM 출력 다루기 | JSON 구조화 출력 · 스트리밍 · 대화 기록 관리 | 8h | 준비 중 |
| 05 | LLM 웹 앱 | FastAPI + HTML · JS 챗봇 | 8h | 준비 중 |
| 06 | 임베딩과 벡터 검색 | 임베딩 · 코사인 유사도 · FAISS | 8h | 준비 중 |
| 07 | RAG 직접 만들기 | PDF 검색 · 청킹 · 출처 표시 · 품질 점검 | 10h | 준비 중 |
| 09 | AI Agent 기초 | Tool Calling · 도구 실행 반복 | 8h | 준비 중 |
| 12 | 최종 프로젝트 | RAG · Agent 웹 서비스 (YOLO 연동 선택 주제) | 24h | 준비 중 |

**심화 과정 (선택 · 스스로 학습, 10시간)**

| Part | 주제 | 주요 내용 | 시간 | 교안 |
|:---:|---|---|---:|:---:|
| 08 | [LangChain](08_LangChain_%EC%8B%AC%ED%99%94/) | 모델 · 프롬프트 체인(파이프) · 구조화 출력 · 작은 RAG | 3h | [📘](08_LangChain_%EC%8B%AC%ED%99%94/08_LangChain_%EC%8B%AC%ED%99%94_%EA%B5%90%EC%95%88.docx) |
| 10 | [LangGraph](10_LangGraph_%EC%8B%AC%ED%99%94/) | State · Node · Edge · 조건 갈림길 · 도구를 쓰는 에이전트 | 4h | [📘](10_LangGraph_%EC%8B%AC%ED%99%94/10_LangGraph_%EC%8B%AC%ED%99%94_%EA%B5%90%EC%95%88.docx) |
| 11 | [MCP 와 안전한 AI 서비스](11_MCP%EC%99%80_%EC%95%88%EC%A0%84%ED%95%9C_AI_%EC%8B%AC%ED%99%94/) | 프롬프트 인젝션 · 개인정보 가리기 · 비용 한도 · 자동 평가 · MCP 서버 · AGENTS.md | 3h | [📘](11_MCP%EC%99%80_%EC%95%88%EC%A0%84%ED%95%9C_AI_%EC%8B%AC%ED%99%94/11_MCP%EC%99%80_%EC%95%88%EC%A0%84%ED%95%9C_AI_%EC%8B%AC%ED%99%94_%EA%B5%90%EC%95%88.docx) |

## 🛠 시작하기

```bash
git clone https://github.com/sinaboro/generative-ai-course.git
cd generative-ai-course
pip install -r requirements.txt
copy .env.example .env        # macOS · Linux 는 cp .env.example .env
```

1. [openrouter.ai](https://openrouter.ai) 에 가입하고 **Keys** 에서 API 키를 만들어요. 만들 때 **사용 한도(Credit limit)** 를 꼭 정해 두세요.
2. `.env` 파일의 `LLM_API_KEY=` 뒤에 키를 붙여 넣어요. 기본 모델은 `openai/gpt-4o-mini` (질문 하나에 1원도 안 들어요).
3. 각 Part 폴더로 이동해 예제를 실행해요: `cd 01_생성형AI_첫걸음` → `python ex01_next_word.py`

> ⚠️ **API 키는 비밀번호예요.** `.env` 는 `.gitignore` 에 있어서 GitHub 에 올라가지 않아요. 키를 코드에 직접 쓰거나 채팅 · 메일로 보내지 마세요. 새어 나갔다면 OpenRouter 에서 바로 지우고 새로 만들어요.

> OpenAI 키로 바꾸려면 `.env` 의 `LLM_BASE_URL` 을 `https://api.openai.com/v1`, `LLM_MODEL` 을 `gpt-4o-mini` 로 바꾸면 돼요. 코드는 그대로예요.

## 📂 Part 폴더 구성

```
01_생성형AI_첫걸음/
├── NN_..._교안.docx     ← 학생용 Word 교안 (실제 LLM 실행 결과 포함)
├── ex01_....py         ← 예제 (번호 순서대로 실행)
├── llm.py              ← LLM 을 쉽게 부르는 도우미 (Part 03 에서 원리를 배워요)
└── 연습문제_정답/
```

> LLM 의 답은 실행할 때마다 조금씩 달라요. 교안의 결과는 "한 번 실행했을 때의 예" 예요.
