@echo off

echo Extracting and processing references from google scholar...
REM call python assets\python\export_google_scholar.py
REM call python assets\python\bib_process.py

echo Updating YAML file...
REM call python assets\python\bib_to_yml.py

REM Specify the full or relative path to your LaTeX CV document (including the .tex extension)
SET CV_DOCUMENT_PATH=assets\CV\CV_AntoniosG.tex

REM Extract the directory path from the CV document path
FOR %%I IN ("%CV_DOCUMENT_PATH%") DO SET CV_DOCUMENT_DIR=%%~dpI

REM Change the current working directory to the directory containing your CV document
CD /D "%CV_DOCUMENT_DIR%"

REM Define the name of your LaTeX CV document (without the .tex extension)
SET CV_DOCUMENT=CV_AntoniosG

echo Updating CV...
REM Compile the LaTeX document
pdflatex %CV_DOCUMENT%.tex >NUL

REM Run BibTeX to process the references (if needed)
biber %CV_DOCUMENT% >NUL

REM Run pdflatex again to resolve references
pdflatex %CV_DOCUMENT%.tex >NUL
pdflatex %CV_DOCUMENT%.tex >NUL
REM Cleanup unnecessary files (optional)
del %CV_DOCUMENT%.aux %CV_DOCUMENT%.bbl  %CV_DOCUMENT%.log %CV_DOCUMENT%.out %CV_DOCUMENT%.run.xml %CV_DOCUMENT%.bcf
REM %CV_DOCUMENT%.blg
REM Open the PDF in your default PDF viewer (optional)
REM Uncomment the following line if you want to automatically open the PDF after compilation
REM start "" %CV_DOCUMENT%.pdf

echo Compilation completed.
