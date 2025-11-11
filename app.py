from flask import Flask, jsonify, render_template

app = Flask(__name__)

# ✅ JSON 한글 깨짐 방지
app.config['JSON_AS_ASCII'] = False


# -----------------------
# ✅  HTML 페이지 라우팅
# -----------------------
@app.get("/")
def main_page():
    return render_template("main.html")

@app.get("/main")
def main_page():
    return render_template("main.html")

@app.get("/subject")
def subject_page():
    return render_template("subject.html")

@app.get("/rationale")
def rationale_page():
    return render_template("rationale.html")

@app.get("/features")
def features_page():
    return render_template("features.html")

@app.get("/environment")
def environment_page():
    return render_template("environment.html")

@app.get("/team")
def team_page():
    return render_template("team.html")


# -----------------------
# ✅  JSON API 엔드포인트
# -----------------------

@app.get("/api/subject")
def api_subject():
    return jsonify({
        "subject": "풋살 매칭 및 리뷰 기반 지역 소모임 플랫폼 '플랩풋볼'"
    })

@app.get("/api/rationale")
def api_rationale():
    return jsonify({
        "rationale": [
            "지역별 풋살 경기 매칭 수요 증가",
            "초보자 문제, 자리 부족 문제 해결 필요성",
            "참여 후기 부족으로 인한 예약 의사결정의 어려움"
        ]
    })

@app.get("/api/features")
def api_features():
    return jsonify({
        "features": [
            "실시간 풋살 경기 매칭 기능",
            "지도 기반 주변 풋살장 검색",
            "필드 리뷰 및 평점 기능",
            "유저 프로필 · 소모임 커뮤니티 기능",
            "경기 일정 관리"
        ]
    })

@app.get("/api/environment")
def api_environment():
    return jsonify({
        "environment": {
            "language": "Python, Java(JSP)",
            "framework": "Flask, Servlet",
            "database": "MySQL",
            "server": "Tomcat 10.1",
            "tools": "Git, Docker Compose, AWS EC2"
        }
    })

@app.get("/api/team")
def api_team():
    return jsonify({
        "team": [
            {"name": "장세현", "role": "백엔드 / DB 설계 / 메인 기능 개발"},
            {"name": "팀원B", "role": "프론트엔드 / UI/UX"},
            {"name": "팀원C", "role": "맵 API / 리뷰 시스템"},
        ]
    })


# -----------------------
# ✅ 서버 실행
# -----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
