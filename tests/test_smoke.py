"""개발 환경 확인용 테스트. pytest가 src/ 안의 모듈을 찾고 첫 화면이 열리면 통과합니다."""
from app import app


def test_첫_화면이_열린다():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
