# 🤖 생성형 AI 입문 — LangChain 으로 만드는 LLM · RAG · Agent 서비스

파이썬 기초만 아는 **초보자**가 이 교안만 보고도 따라 할 수 있게 만든 자기주도 학습 과정이에요. 생성형 AI 의 원리부터 LangChain 으로 AI 부르기, 프롬프트, 웹 챗봇, RAG(문서 기반 답변), LangGraph 에이전트, MCP 와 안전한 서비스, 최종 프로젝트까지 한 줄로 이어서 배워요. 모든 예제는 실제 AI(OpenRouter)로 실행한 결과를 교안에 실었어요.

- **강사**: 김대철
- 📕 **통합 교안 PDF**: [생성형AI_통합교안.pdf](%EC%83%9D%EC%84%B1%ED%98%95AI_%ED%86%B5%ED%95%A9%EA%B5%90%EC%95%88.pdf) (현재 Part 01 ~ 05, 125쪽 · 학습 안내 · 진도표 · 쉬운 용어 사전 · 막힐 때 점검표)
- **실습 환경**: Windows + Python 3.12 이상 + VS Code + OpenRouter API 키 (키가 없으면 "연습 모드"로 실행돼요)
- 먼저 들으면 좋은 과정: [ai-service-course](https://github.com/sinaboro/ai-service-course) 의 Python 기초 (05 웹 앱은 HTML · CSS · JavaScript · FastAPI 과정과 이어져요)

## 📚 과정 구성 (100시간)

| Part | 주제 | 주요 내용 | 시간 | 교안 |
|:---:|---|---|---:|:---:|
| 01 | [생성형 AI 첫걸음](01_%EC%83%9D%EC%84%B1%ED%98%95AI_%EC%B2%AB%EA%B1%B8%EC%9D%8C/) | AI 에게 말 걸기 · 다음 낱말 맞히기 · 토큰 · temperature · 환각 · 웹 도구 | 6h | [📘](01_%EC%83%9D%EC%84%B1%ED%98%95AI_%EC%B2%AB%EA%B1%B8%EC%9D%8C/01_%EC%83%9D%EC%84%B1%ED%98%95AI_%EC%B2%AB%EA%B1%B8%EC%9D%8C_%EA%B5%90%EC%95%88.docx) |
| 02 | [LangChain 으로 LLM 부르기](02_LangChain%EC%9C%BC%EB%A1%9C_LLM_%EB%B6%80%EB%A5%B4%EA%B8%B0/) | .env · ChatOpenAI · 메시지 세 종류 · 토큰과 요금 · 오류 처리 · 모델 비교 | 8h | [📘](02_LangChain%EC%9C%BC%EB%A1%9C_LLM_%EB%B6%80%EB%A5%B4%EA%B8%B0/02_LangChain%EC%9C%BC%EB%A1%9C_LLM_%EB%B6%80%EB%A5%B4%EA%B8%B0_%EA%B5%90%EC%95%88.docx) |
| 03 | [프롬프트 엔지니어링](03_%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8_%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81/) | 구체적으로 · 역할 · 템플릿 · 체인 · Few-shot · 답의 모양 · 단계별로 | 8h | [📘](03_%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8_%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81/03_%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8_%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81_%EA%B5%90%EC%95%88.docx) |
| 04 | [출력 다루기](04_%EC%B6%9C%EB%A0%A5_%EB%8B%A4%EB%A3%A8%EA%B8%B0/) | 구조화 출력 · 스트리밍 · 대화 기록 · 기록 줄이기 | 8h | [📘](04_%EC%B6%9C%EB%A0%A5_%EB%8B%A4%EB%A3%A8%EA%B8%B0/04_%EC%B6%9C%EB%A0%A5_%EB%8B%A4%EB%A3%A8%EA%B8%B0_%EA%B5%90%EC%95%88.docx) |
| 05 | [LLM 웹 앱](05_LLM_%EC%9B%B9%EC%95%B1/) | FastAPI · /docs · HTML · JS 채팅 화면 · 스트리밍 · 카페 주문 도우미 | 8h | [📘](05_LLM_%EC%9B%B9%EC%95%B1/05_LLM_%EC%9B%B9%EC%95%B1_%EA%B5%90%EC%95%88.docx) |
| 06 | RAG ① 임베딩과 검색 | 뜻이 비슷하면 숫자도 비슷하다 · 벡터 저장소 · 검색기 | 8h | 준비 중 |
| 07 | RAG ② 문서 챗봇 | PDF · 청킹 · 출처 표시 · 품질 점검 | 10h | 준비 중 |
| 08 | LangGraph | 노드 · 갈림길 · 도구를 쓰는 에이전트 | 10h | 준비 중 |
| 09 | MCP 와 안전한 AI 서비스 | MCP 서버 · 프롬프트 인젝션 · 개인정보 · 비용 한도 · 평가 | 10h | 준비 중 |
| 10 | 최종 프로젝트 | RAG · 에이전트 웹 서비스 (YOLO 연동 선택 주제) | 24h | 준비 중 |

## 🛠 시작하기

```bash
git clone https://github.com/sinaboro/generative-ai-course.git
cd generative-ai-course
pip install -r requirements.txt
copy .env.example .env        # macOS · Linux 는 cp .env.example .env
```

1. [openrouter.ai](https://openrouter.ai) 에 가입하고 **Keys** 에서 API 키를 만들어요. 만들 때 **사용 한도(Credit limit)** 를 꼭 정해 두세요.
2. `.env` 파일의 `LLM_API_KEY=` 뒤에 키를 붙여 넣어요. 기본 모델은 `openai/gpt-4o-mini` (질문 하나에 1원도 안 들어요).
3. Part 폴더로 들어가 예제를 실행해요: `cd 01_생성형AI_첫걸음` → `python ex01_hello_ai.py`

> ⚠️ **API 키는 비밀번호예요.** `.env` 는 `.gitignore` 에 있어서 GitHub 에 올라가지 않아요. 키를 코드에 직접 쓰거나 채팅 · 메일로 보내지 마세요. 새어 나갔다면 OpenRouter 에서 바로 지우고 새로 만들어요.

## 📂 Part 폴더 구성

```
01_생성형AI_첫걸음/
├── NN_..._교안.docx     ← 학생용 Word 교안 (실제 AI 실행 결과 포함)
├── common.py           ← .env 를 읽어 AI 를 만들어 주는 공통 파일 (Part 02 에서 원리를 배워요)
├── ex01_....py         ← 예제 (번호 순서대로 실행)
└── 정답_문제1.py        ← 연습문제 정답 (같은 폴더라 바로 실행돼요)
```

> AI 의 답은 실행할 때마다 조금씩 달라요. 교안의 결과는 "한 번 실행했을 때의 예" 예요.
