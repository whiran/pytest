@echo off

REM Install packages
pip install --upgrade pip && pip install -r requirements.txt

REM Run tests
python -m pytest --vv test_hello.py

REM Format code
black *.py

REM Lint code
pylint --disable=R,C *.py