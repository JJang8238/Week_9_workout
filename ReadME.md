# 캡스톤 프로젝트 소개 웹 (EC2 + Docker, 또는 로컬)

본 저장소는 캡스톤 프로젝트 단일 소개 페이지와 API를 제공합니다.

---

## 1. 작업주제 (Subject)
- 제목: 플랩풋볼 – 풋살 매칭 및 리뷰 기반 소모임 플랫폼
- 요약: 사용자 주변 풋살장을 조회하고 매칭/리뷰 기능을 제공하는 웹 서비스

---

## 2. 실용적 근거 (Rationale)
- 문제: 풋살장을 찾기 어렵고 매칭 정보가 분산되어 있음  
- 근거(수치/설문/사례): 실제 사용자 설문에서 72%가 “근처 풋살장 찾기 불편” 응답  
- 기대 가치: 단일 플랫폼에서 매칭, 커뮤니티, 리뷰 통합 제공

---

## 3. 핵심기능 (Features)
- 기능 1: 풋살장 지도 조회 / 사용자 위치 기반 검색
- 기능 2: 매칭 일정 조회 API
- 기능 3: 리뷰 확인 및 기본 소모임 정보 제공

---

## 4. 구현환경 (Environment)
### ● Front-End(프론트엔드)
- Flask Jinja2 템플릿 기반 HTML 렌더링

### ● Back-End(백엔드)
- Python 3.11  
- Flask Web Framework  

### ● Runtime(런타임)
- Docker 컨테이너 기반 실행

### ● Deploy(배포)
- 컨테이너 빌드 → AWS ECR 업로드 → AWS ECS 배포  
- ECR 이미지 URI:  
  `037151312664.dkr.ecr.ap-northeast-2.amazonaws.com/test-api:1.0`

---

## 5. 팀원 구성 및 역할 (Team)
- 장세현 – 개발 및 배포 총괄

---

## 6. 실행 방법 (Run)

### ✅ 로컬 실행
```
docker compose up --build -d
```

### ✅ AWS ECS 배포 결과
- 퍼블릭 IP 접속 주소:  
  **http://13.124.235.237:5000/main**

(→ 프로젝트에 맞는 포트 또는 배포된 public IP로 접속)

---

## 7. API 엔드포인트
- `/api/subject`
- `/api/rationale`
- `/api/features`
- `/api/environment`
- `/api/team`

---

## 8. GitHub 업로드 안내
- README.md 포함 필수  
- app.py, templates/, Dockerfile, docker-compose.yml 포함  
- 프로젝트 구조 예:
```
📦project
 ┣ 📁templates
 ┣ 📜app.py
 ┣ 📜Dockerfile
 ┣ 📜docker-compose.yml
 ┣ 📜README.md
```

---

## ✅ 비고
- ECS에 정상 배포됨  
- 퍼블릭 IP로 직접 요청 시 API 확인 가능  
```

---