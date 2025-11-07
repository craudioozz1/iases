#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para converter todos os simulados DOCX em um único arquivo LaTeX
"""

import os
from pathlib import Path
from docx import Document
import re

def escape_latex(text):
    """Escapa caracteres especiais do LaTeX"""
    if not text:
        return ""

    # Dicionário de substituições
    replacements = {
        '\\': r'\textbackslash{}',
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }

    result = text
    for old, new in replacements.items():
        result = result.replace(old, new)

    return result

def extract_docx_content(docx_path):
    """Extrai o conteúdo de um arquivo DOCX"""
    doc = Document(docx_path)
    content = []

    for para in doc.paragraphs:
        if para.text.strip():
            content.append({
                'text': para.text,
                'style': para.style.name,
                'bold': any(run.bold for run in para.runs),
                'font_size': para.runs[0].font.size if para.runs and para.runs[0].font.size else None
            })

    return content

def convert_to_latex(contents, output_file):
    """Converte o conteúdo extraído para LaTeX"""

    latex_header = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{xcolor}

\geometry{top=2cm, bottom=2cm, left=2cm, right=2cm}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{IASES 2025 - Agente Socioeducativo}
\fancyhead[R]{Simulados Completos}
\fancyfoot[C]{\thepage}

\titleformat{\section}{\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\large\bfseries}{\thesubsection}{1em}{}

\setlength{\parindent}{0pt}
\setlength{\parskip}{1em}

\begin{document}

\begin{titlepage}
    \centering
    \vspace*{2cm}
    {\Huge\bfseries Simulados IASES 2025\par}
    \vspace{1cm}
    {\Large Agente Socioeducativo\par}
    \vspace{1.5cm}
    {\large Questões 01-70\par}
    \vspace{2cm}
    {\large Compilação Completa dos Simulados\par}
    \vfill
    {\large Espírito Santo - Brasil\par}
    {\large \today\par}
\end{titlepage}

\tableofcontents
\newpage

"""

    latex_footer = r"""
\end{document}
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_header)

        current_section = 0

        for file_idx, (filename, content) in enumerate(contents.items(), 1):
            # Extrai o range de questões do nome do arquivo
            match = re.search(r'Questoes_(\d+)-(\d+)', filename)
            if match:
                start_q, end_q = match.groups()
                f.write(f"\\section{{Simulado {file_idx}: Questões {start_q}-{end_q}}}\n\n")
            else:
                f.write(f"\\section{{Simulado {file_idx}}}\n\n")

            in_gabarito = False
            in_question = False
            question_number = None

            for item in content:
                text = item['text'].strip()

                if not text:
                    continue

                # Detecta título de gabarito comentado
                if 'gabarito' in text.lower() and 'comentado' in text.lower():
                    if not in_gabarito:
                        f.write("\\subsection{Gabarito Comentado}\n\n")
                        in_gabarito = True
                    continue

                # Detecta números de questão
                question_match = re.match(r'^(\d+)[\.\)]\s*(.*)', text)
                if question_match:
                    q_num = question_match.group(1)
                    q_text = question_match.group(2)

                    if in_gabarito:
                        f.write(f"\\textbf{{Questão {q_num}:}}\n\n")
                    else:
                        f.write(f"\\textbf{{{q_num}.}} {escape_latex(q_text)}\n\n")

                    in_question = True
                    question_number = q_num
                    continue

                # Detecta alternativas (A), B), C), D)
                alt_match = re.match(r'^([A-D])[\.\)]\s*(.*)', text)
                if alt_match and in_question and not in_gabarito:
                    alt_letter = alt_match.group(1)
                    alt_text = alt_match.group(2)
                    f.write(f"\\quad {alt_letter}) {escape_latex(alt_text)}\n\n")
                    continue

                # Detecta gabarito (ex: "Gabarito: A")
                gab_match = re.match(r'^Gabarito:\s*([A-D])', text, re.IGNORECASE)
                if gab_match:
                    gab_letter = gab_match.group(1)
                    f.write(f"\\textit{{Gabarito: {gab_letter}}}\n\n")
                    continue

                # Detecta comentário
                if text.startswith('Comentário:') or text.startswith('Justificativa:'):
                    f.write(f"\\textit{{{escape_latex(text)}}}\n\n")
                    continue

                # Texto normal
                if item['bold'] or (item['font_size'] and item['font_size'] > 220000):
                    f.write(f"\\textbf{{{escape_latex(text)}}}\n\n")
                else:
                    f.write(f"{escape_latex(text)}\n\n")

            f.write("\\newpage\n\n")

        f.write(latex_footer)

def main():
    # Diretório dos simulados
    simulados_dir = Path('simulados')

    # Lista todos os arquivos DOCX
    docx_files = sorted(simulados_dir.glob('*.docx'))

    if not docx_files:
        print("Nenhum arquivo DOCX encontrado na pasta simulados/")
        return

    print(f"Encontrados {len(docx_files)} arquivos DOCX:")
    for f in docx_files:
        print(f"  - {f.name}")

    # Extrai conteúdo de cada arquivo
    print("\nExtraindo conteúdo dos arquivos...")
    all_contents = {}

    for docx_file in docx_files:
        print(f"  Processando: {docx_file.name}")
        content = extract_docx_content(docx_file)
        all_contents[docx_file.name] = content

    # Gera arquivo LaTeX
    output_file = 'simulados_completos.tex'
    print(f"\nGerando arquivo LaTeX: {output_file}")
    convert_to_latex(all_contents, output_file)

    print(f"\n✓ Arquivo LaTeX gerado com sucesso: {output_file}")
    print("\nPara compilar, execute:")
    print(f"  pdflatex {output_file}")
    print(f"  pdflatex {output_file}  # Segunda vez para índice")

if __name__ == '__main__':
    main()
