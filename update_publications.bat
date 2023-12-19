@echo off

REM Specify the full or relative path to your LaTeX CV document (including the .tex extension)
SET CV_DOCUMENT_PATH=assets\CV\CV_AntoniosG.tex

REM Extract the directory path from the CV document path
FOR %%I IN ("%CV_DOCUMENT_PATH%") DO SET CV_DOCUMENT_DIR=%%~dpI

REM Change the current working directory to the directory containing your CV document
CD /D "%CV_DOCUMENT_DIR%"

REM Define the name of your LaTeX CV document (without the .tex extension)
SET CV_DOCUMENT=CV_AntoniosG

REM Compile the LaTeX document
pdflatex %CV_DOCUMENT%.tex

REM Run BibTeX to process the references (if needed)
biber %CV_DOCUMENT%

REM Run pdflatex again to resolve references
pdflatex %CV_DOCUMENT%.tex
pdflatex %CV_DOCUMENT%.tex
REM Cleanup unnecessary files (optional)
del %CV_DOCUMENT%.aux %CV_DOCUMENT%.bbl %CV_DOCUMENT%.blg %CV_DOCUMENT%.log %CV_DOCUMENT%.out %CV_DOCUMENT%.run.xml %CV_DOCUMENT%.bcf

REM Open the PDF in your default PDF viewer (optional)
REM Uncomment the following line if you want to automatically open the PDF after compilation
REM start "" %CV_DOCUMENT%.pdf

echo Compilation completed.
