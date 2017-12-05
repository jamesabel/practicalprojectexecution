REM rst2pdf
REM venv\Scripts\sphinx-build.exe -b pdf . _build
REM
REM latex to pdf simple command
REM pdflatex.exe _build\practicalprojectexecution.tex
REM
REM latex to pdf from PyCharm plugin
pushd .
cd _build
pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=C:/Users/james/projects/practicalprojectexecution/out -aux-directory=C:/Users/james/projects/practicalprojectexecution/auxil practicalprojectexecution.tex
popd
