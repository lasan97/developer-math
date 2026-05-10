# Developer Math

Python으로 수학 그래프 예제를 실행하는 프로젝트입니다.

## 가상환경 설정

프로젝트 루트에서 아래 명령을 실행합니다.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install sympy matplotlib
```

활성화가 끝나면 터미널 프롬프트 앞에 `(.venv)`가 표시됩니다.

## 실행

가상환경이 활성화된 상태에서 실행합니다.

```bash
python main.py
```

## PyCharm 설정

PyCharm에서 import가 인식되지 않으면 프로젝트 인터프리터가 `.venv`로 설정되어 있는지 확인합니다.

1. `PyCharm > Settings...`를 엽니다.
2. `Project: developer-math > Python Interpreter`로 이동합니다.
3. 인터프리터가 아래 경로인지 확인합니다.

```text
/Users/lasan/workspace/study/developer-math/.venv/bin/python
```

다른 Python이 선택되어 있다면 `Add Interpreter > Add Local Interpreter... > Existing`을 선택한 뒤 위 경로를 지정합니다.

## 종료

작업을 마치면 가상환경을 비활성화합니다.

```bash
deactivate
```

## 다음에 다시 작업할 때

이미 `.venv`를 만든 뒤라면 매번 새로 만들 필요 없이 활성화만 하면 됩니다.

```bash
source .venv/bin/activate
```
