@echo off
REM ============================================
REM Script de Compilação LaTeX - Simulados IASES
REM ============================================

echo.
echo ============================================
echo  Compilando Simulados IASES
echo ============================================
echo.

REM Verifica se pdflatex está disponível
where pdflatex >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] pdflatex não encontrado!
    echo.
    echo Por favor, instale MiKTeX ou TeX Live:
    echo - MiKTeX: https://miktex.org/download
    echo - TeX Live: https://www.tug.org/texlive/
    echo.
    pause
    exit /b 1
)

REM Salvar diretório atual e navegar para pasta LaTeX
set SCRIPT_DIR=%~dp0
set REPO_ROOT=%SCRIPT_DIR%..
cd /d "%REPO_ROOT%\simulados\latex"

REM Nome do arquivo (sem extensão)
set ARQUIVO=simulados_completos

echo [1/2] Primeira compilacao...
echo Diretorio: %CD%
pdflatex -interaction=nonstopmode %ARQUIVO%.tex

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Falha na compilacao!
    echo Verifique o arquivo %ARQUIVO%.log para detalhes.
    echo.
    pause
    exit /b 1
)

echo.
echo [2/2] Segunda compilacao (atualizando indices)...
pdflatex -interaction=nonstopmode %ARQUIVO%.tex

if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Falha na segunda compilacao!
    echo Verifique o arquivo %ARQUIVO%.log para detalhes.
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================
echo  Compilacao concluida com sucesso!
echo ============================================
echo.

REM Mover PDF para pasta de saída
echo Movendo PDF para simulados/pdf/...
move /Y %ARQUIVO%.pdf ..\pdf\ 2>nul
if %errorlevel% equ 0 (
    echo PDF movido com sucesso: simulados/pdf/%ARQUIVO%.pdf
) else (
    echo Aviso: PDF nao foi movido. Verifique se esta aberto.
    echo Localizacao: simulados/latex/%ARQUIVO%.pdf
)

REM Limpar arquivos auxiliares
echo Limpando arquivos auxiliares...
del %ARQUIVO%.aux 2>nul
del %ARQUIVO%.log 2>nul
del %ARQUIVO%.toc 2>nul
del %ARQUIVO%.out 2>nul

echo.
echo ============================================
echo  Concluido!
echo ============================================
echo Arquivo TEX: simulados/latex/%ARQUIVO%.tex
echo Arquivo PDF: simulados/pdf/%ARQUIVO%.pdf
echo.

REM Abre o PDF automaticamente (descomente se desejar)
REM start ..\pdf\%ARQUIVO%.pdf

echo Pressione qualquer tecla para fechar...
pause >nul

REM Voltar ao diretório do script
cd /d "%SCRIPT_DIR%"
