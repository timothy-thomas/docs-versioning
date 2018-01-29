if exist _build rd /s/q _build
if exist venv rd /s/q venv
C:\Python27\python -m virtualenv venv
venv\scripts\python -m pip install -r requirements.txt
