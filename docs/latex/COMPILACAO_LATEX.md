# Guia de Compilação LaTeX - Simulados IASES

Este documento descreve a formatação e compilação dos simulados no formato da prova IASES.

## 📋 Estrutura do Documento

### Preâmbulo e Pacotes Necessários

```latex
\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{xcolor}
\usepackage{multicol}  % Para layout em duas colunas
\usepackage{ulem}      % Para sublinhados
```

### Configuração de Página

```latex
\geometry{top=2cm, bottom=2.5cm, left=1.5cm, right=1.5cm}
```

**Margens otimizadas:**
- Superior: 2cm
- Inferior: 2.5cm (para rodapé)
- Laterais: 1.5cm

### Rodapé Personalizado

```latex
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[L]{\small AGENTE SOCIOEDUCATIVO - MASCULINO - \thepage}
\fancyfoot[R]{\small www.ioconcursos.com.br}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
```

**Elementos do rodapé:**
- Esquerda: Nome do cargo + número da página
- Direita: Site de referência
- Sem linhas de separação

### Configuração de Colunas

```latex
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5em}
\setlength{\columnsep}{1cm}
```

**Espaçamento:**
- Sem indentação de parágrafo
- 0.5em entre parágrafos
- 1cm entre colunas

## 🎨 Comandos Personalizados

### Cabeçalho de Disciplina

```latex
\newcommand{\disciplina}[1]{%
  \vspace{1em}
  {\large\textbf{\uline{#1}}}
  \vspace{0.5em}
}
```

**Uso:**
```latex
\disciplina{Língua Portuguesa}
\disciplina{Matemática}
\disciplina{Conhecimentos Específicos}
```

**Resultado:** Texto em negrito, tamanho large, com sublinhado

### Gabaritos (opcional)

```latex
% Comando para gabarito correto
\newcommand{\correto}[1]{{\color{red}\textbf{(Correta: #1)}}}

% Comando para questão anulada
\newcommand{\anulada}{{\color{red}\textbf{(Gabarito anulada)}}}
```

**Uso:**
```latex
\textbf{Questão 01}\\
\correto{B}  % Remove esta linha para não mostrar gabarito

Enunciado da questão...
```

## 📝 Estrutura do Conteúdo

### Início do Documento

```latex
\begin{document}

% Página de título (opcional)
\begin{titlepage}
    \centering
    \vspace*{2cm}
    {\Huge\bfseries Simulados IASES 2025\par}
    \vspace{1cm}
    {\Large Agente Socioeducativo\par}
    % ... mais conteúdo
\end{titlepage}

\tableofcontents
\newpage

% INÍCIO DO LAYOUT EM DUAS COLUNAS
\begin{multicols}{2}
```

### Formatação de Questões

```latex
% Cabeçalho do concurso
\section*{Concurso Público IASES 2022}
\textsc{AGENTE SOCIOEDUCATIVO - MASCULINO}

\rule{\columnwidth}{0.5pt}  % Linha separadora

% Cabeçalho da disciplina
\disciplina{Língua Portuguesa}

\small  % Tamanho de fonte reduzido

% Texto-base (se houver)
\textbf{Texto Base - Questões 1 a 5}

\textbf{Título do Texto}

\textit{Informações sobre o texto...}

Conteúdo do texto aqui...

\textit{\small Fonte: https://exemplo.com}

% Questões
\textbf{Questão 01}

Enunciado da questão aqui...

(A) Alternativa A.

(B) Alternativa B.

(C) Alternativa C.

(D) Alternativa D.

(E) Alternativa E.
```

### Quebra de Coluna

```latex
\columnbreak  % Força quebra para a próxima coluna
```

### Quebra de Seção

```latex
\disciplina{Nova Disciplina}
```

### Formatação de Textos Especiais

```latex
% Texto em negrito
\textbf{Texto importante}

% Texto em itálico (para citações)
\textit{Fonte ou citação}

% Parágrafos numerados
\textbf{(1º)} Primeiro parágrafo...

\textbf{(2º)} Segundo parágrafo...
```

### Caracteres Especiais

```latex
% Expoentes matemáticos
5 x 10$^{-2}$

% Porcentagens
60\% dos participantes

% Símbolos matemáticos
\leq  % menor ou igual
\geq  % maior ou igual
```

## 🔧 Compilação

### Comando Básico

```bash
pdflatex simulados_completos.tex
```

### Compilação Completa (com índice)

```bash
# Primeira compilação
pdflatex simulados_completos.tex

# Segunda compilação (para índice)
pdflatex simulados_completos.tex
```

### Compilação no Windows

```cmd
cd c:\Users\Admin\Documents\GitHub\iases
pdflatex -interaction=nonstopmode simulados_completos.tex
```

### Usando pdftotext (para extrair PDF)

```bash
pdftotext -layout arquivo.pdf saida.txt
```

## ✅ Checklist de Formatação

Antes de compilar, verifique:

- [ ] Todos os caracteres especiais estão escapados corretamente
- [ ] Expoentes usam notação matemática `$^{x}$`
- [ ] Porcentagens usam `\%`
- [ ] Comandos `\textbf{}` estão fechados corretamente
- [ ] Não há quebras de linha dentro de `\textbf{}`
- [ ] `\begin{multicols}{2}` foi aberto no início
- [ ] `\end{multicols}` foi fechado antes de `\end{document}`
- [ ] Gabaritos foram removidos (se aplicável)

## 🎯 Boas Práticas

### 1. Organização de Questões

```latex
% BOM
\textbf{Questão 01}

Enunciado claro e direto...

% EVITE
\textbf{Questão 01 -
Enunciado quebrado}  % Não funciona!
```

### 2. Textos-base

```latex
% Formato recomendado
\textbf{Texto Base - Questões 1 a 5}

\textbf{Título do Texto}

\textit{Informações em itálico}

Corpo do texto normal...

\textit{\small Fonte: referência}
```

### 3. Disciplinas

```latex
% Use o comando personalizado
\disciplina{Nome da Disciplina}

% NÃO use
\section{Nome da Disciplina}  % Muito grande
```

### 4. Espaçamento

```latex
% Deixe linhas em branco entre questões
\textbf{Questão 01}

Enunciado...

(E) Última alternativa.

\textbf{Questão 02}  % Nova questão
```

## 🐛 Problemas Comuns

### Erro: "Paragraph ended before \text@command"

**Causa:** Quebra de linha dentro de `\textbf{...}`

**Solução:**
```latex
% ERRADO
\textbf{Texto com
quebra de linha}

% CORRETO
\textbf{Texto sem quebra}
```

### Erro: "Unicode character not set up"

**Causa:** Caractere Unicode não suportado (ex: ⁻, ², ³)

**Solução:**
```latex
% ERRADO
10⁻² ml

% CORRETO
10$^{-2}$ ml
```

### Erro: "Extra }, or forgotten \endgroup"

**Causa:** Chaves desbalanceadas em `\textbf{}` ou `\textit{}`

**Solução:** Conte as chaves `{` e `}` - devem estar em pares

### Texto Saindo das Colunas

**Causa:** URLs ou palavras muito longas

**Solução:**
```latex
% Para URLs longas
\small https://exemplo.com/caminho-muito-longo

% Ou use quebra manual
\url{https://exemplo.com}  % Requer \usepackage{url}
```

## 📊 Exemplo Completo de Questão

```latex
\textbf{Questão 15}

Analise as assertivas com V(Verdadeiro) ou F(Falso).

(\_\_) Primeira afirmativa aqui.

(\_\_) Segunda afirmativa aqui.

(\_\_) Terceira afirmativa aqui.

Marque a alternativa com a sequência CORRETA:

(A) V, V, F.

(B) F, V, V.

(C) V, F, V.

(D) F, F, F.

(E) V, V, V.
```

## 🔄 Finalizando o Documento

```latex
% Antes de fechar, termine as colunas
\end{multicols}

\end{document}
```

## 📞 Dicas Finais

1. **Sempre compile duas vezes** para atualizar índices e referências
2. **Verifique o PDF gerado** antes de imprimir
3. **Mantenha backup** do arquivo .tex
4. **Use editor com syntax highlighting** (VS Code, TeXstudio, Overleaf)
5. **Teste com questões de amostra** antes do documento completo

---

**Última atualização:** 06 de novembro de 2025
**Versão:** 1.0
**Formato:** IASES 2025 - Agente Socioeducativo
