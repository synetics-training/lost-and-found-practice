"""과제 할 일 관리 — 웹 화면 시작점 (경계 계층).

실행: python src/app.py → 브라우저에서 http://127.0.0.1:5000

- 이 파일에는 Flask 라우트(화면 요청 받기, 템플릿 그리기)만 둡니다.
- 제어·엔티티 클래스는 SAD에 맞게 src/ 아래 별도 파일로 만들고, Flask 없이 순수 Python으로 작성합니다.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
