REM rst2pdf is Python2 only
REM "C:\Program Files\Python36\python.exe" -m venv --clear venv
c:\Python27\Scripts\virtualenv.exe --clear venv
venv\Scripts\pip install -U pip
venv\Scripts\pip install -U setuptools
venv\Scripts\pip install -r requirements.txt
