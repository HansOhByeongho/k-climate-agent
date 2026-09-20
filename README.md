# K-Climate Agent

지역 온실가스·에너지·기후위험·감축·적응 분석하는 대한민국 공공업무용 오픈소스 프로토타입입니다.

## 목표
- 단독 FastAPI 서비스로 실행
- 공식 공공데이터 우선, 출처와 검증상태 보존
- API 키·개인정보·내부문서 저장 금지
- National AI Orchestrator의 전문 도구로 연결

## 실행
```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
pytest -q
```

## 공식 연계 후보
- 공공데이터포털: https://www.data.go.kr/
- KOSIS OpenAPI: https://kosis.kr/openapi/
- 국가법령정보 공동활용: https://open.law.go.kr/

## 개발 상태
**v0.4 research prototype** — 실제 행정 의사결정 전 최신 공식 원문을 재확인해야 합니다.
