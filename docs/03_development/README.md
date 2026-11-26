# 개발 환경 — 실행과 테스트

## 폴더 구조

```text
src/                     실행 코드
  app.py                 Flask 시작점 (경계 계층: 화면 요청과 템플릿만)
  templates/             HTML 템플릿
  static/                CSS 등
data/
  academic_system.json   가상 학사정보시스템 데이터 (수정 금지 — 다른 조직이 운영하는 시스템이라는 가정)
tests/                   테스트 코드 (pytest)
  test_smoke.py          개발 환경 확인용
requirements.txt         필요한 패키지
pytest.ini               tests/에서 src/ 안의 모듈을 가져오도록 하는 설정
```

- 제어·엔티티 클래스는 팀 SAD의 이름대로 `src/` 아래에 파일을 나눠 만듭니다.
- 제어·엔티티 코드는 Flask를 import하지 않습니다. 그래야 Flask 없이 단위 테스트를 할 수 있습니다.
- 테스트 파일 이름은 `tests/test_대상.py`, 테스트 함수 이름은 `test_`로 시작합니다.

## 처음 한 번

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS·Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 테스트

```bash
python -m pytest
```

처음에는 `1 passed`가 나오면 정상입니다.

## 실행

```bash
python src/app.py
```

브라우저에서 http://127.0.0.1:5000 을 엽니다. 끝낼 때는 터미널에서 Ctrl+C.

## 가상 학사정보시스템 (data/academic_system.json)

|필드|형식|설명|
|---|---|---|
|`semester`|문자열|학기 (예: `2026-2`)|
|`students`|목록|학생 목록|
|`students[].student_id`|문자열 8자리|학번|
|`students[].name`|문자열|학생 이름|
|`students[].courses`|문자열 목록|이번 학기 수강 과목 이름. 빈 목록일 수 있음|

- 학번으로 학생을 찾아 이름과 수강 과목 목록을 가져옵니다.
- 목록에 없는 학번은 **없는 학번**입니다.
- 파일이 없거나 JSON 형식이 깨져서 읽지 못하면 **연결 실패**로 처리합니다.
- 학사정보시스템을 읽는 클래스는 **JSON 파일 경로를 인자로 받게** 만듭니다. 실제 실행에서는 `data/academic_system.json`을 넘깁니다.
- 테스트에서는 이 파일을 직접 쓰지 않고, `tests/data/`에 테스트용 JSON 파일을 만들어 그 경로를 넘깁니다.
  - 정상·없는 학번·수강 과목 0개: 테스트용 학생 2~3명이 든 `tests/data/students.json`
  - 파일을 읽지 못함: 없는 경로 (예: `tests/data/no_file.json`)
  - JSON이 깨짐: 일부러 형식을 깨뜨린 `tests/data/broken.json`
- 테스트는 저장소 맨 위 폴더에서 `python -m pytest`로 실행합니다. 그래야 `tests/data/…` 같은 상대 경로가 맞습니다.
