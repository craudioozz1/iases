# 📚 Documentação LaTeX - Simulados IASES

Conjunto completo de arquivos e documentação para criação e compilação de simulados no formato IASES.

## 📁 Estrutura de Arquivos

```
iases/
├── simulados/
│   ├── latex/
│   │   └── simulados_completos.tex    ← Documento principal (70 questões)
│   ├── pdf/
│   │   └── simulados_completos.pdf    ← PDF compilado
│   └── templates/
│       └── template_simulado.tex      ← Template para novos simulados
├── docs/
│   └── latex/
│       ├── COMPILACAO_LATEX.md        ← Guia completo de formatação
│       └── README_LATEX.md            ← Este arquivo
└── scripts/
    └── compilar.bat                   ← Script de compilação
```

### 📄 Documentos LaTeX

| Arquivo | Localização | Descrição |
|---------|-------------|-----------|
| `simulados_completos.tex` | `simulados/latex/` | Documento principal com todos os simulados |
| `simulados_completos.pdf` | `simulados/pdf/` | PDF compilado pronto para impressão |
| `template_simulado.tex` | `simulados/templates/` | Template vazio para criar novos simulados |

### 📖 Documentação

| Arquivo | Localização | Descrição |
|---------|-------------|-----------|
| `COMPILACAO_LATEX.md` | `docs/latex/` | **Guia completo** de formatação e compilação |
| `README_LATEX.md` | `docs/latex/` | Este arquivo - índice da documentação |

### 🔧 Scripts

| Arquivo | Localização | Descrição |
|---------|-------------|-----------|
| `compilar.bat` | `scripts/` | Script Windows para compilação automática |

## 🚀 Início Rápido

### Opção 1: Compilar Documento Existente

```bash
# Windows - da raiz do repositório
scripts\compilar.bat

# Ou manualmente (dentro de simulados/latex/)
cd simulados\latex
pdflatex simulados_completos.tex
```

### Opção 2: Criar Novo Simulado

1. Copie o template:
   ```bash
   cd simulados\templates
   copy template_simulado.tex ..\latex\meu_simulado.tex
   ```
2. Edite o conteúdo em `simulados/latex/meu_simulado.tex`
3. Compile:
   ```bash
   cd simulados\latex
   pdflatex meu_simulado.tex
   ```

## 📋 Pré-requisitos

### Instalar LaTeX

**Windows:**
- [MiKTeX](https://miktex.org/download) (Recomendado)
- [TeX Live](https://www.tug.org/texlive/)

**Verificar instalação:**
```bash
pdflatex --version
```

### Editores Recomendados

- **VS Code** + LaTeX Workshop extension
- **TeXstudio** (standalone)
- **Overleaf** (online)

## 📐 Formato da Prova

### Estrutura das Questões

```
Total: 70 questões
├── Língua Portuguesa (10 questões) - Peso 1
├── Raciocínio Lógico (5 questões) - Peso 1
├── Informática (5 questões) - Peso 1
└── Conhecimentos Específicos (50 questões) - Peso 2
```

### Layout

- **Formato:** A4, duas colunas
- **Fonte:** 10pt (corpo), 9pt (questões)
- **Margens:** 2cm topo, 2.5cm base, 1.5cm laterais
- **Rodapé:** Nome do cargo + página | Site

## 🎯 Características Principais

### ✅ Implementado

- [x] Layout em duas colunas
- [x] Rodapé personalizado (cargo + site)
- [x] Cabeçalhos de disciplina sublinhados
- [x] Gabaritos removíveis (vermelho)
- [x] Marcação de questões anuladas
- [x] Formatação de textos-base
- [x] Suporte a questões V/F
- [x] Caracteres especiais (expoentes, símbolos)
- [x] Espaçamento otimizado

### 📊 Estatísticas do Documento

**simulados_completos.pdf:**
- Tamanho: ~183 KB
- Páginas: 16
- Questões: 70
- Formato: Prova IASES 2022

## 📚 Documentação Detalhada

### [COMPILACAO_LATEX.md](COMPILACAO_LATEX.md)

Guia completo contendo:
- ✅ Configuração do preâmbulo
- ✅ Pacotes necessários
- ✅ Comandos personalizados
- ✅ Estrutura do documento
- ✅ Exemplos práticos
- ✅ Resolução de problemas
- ✅ Checklist de formatação

**Tópicos principais:**
1. Estrutura do Documento
2. Comandos Personalizados
3. Formatação de Questões
4. Compilação
5. Boas Práticas
6. Problemas Comuns

## 🔨 Uso dos Comandos

### Disciplina

```latex
\disciplina{Língua Portuguesa}
```

### Questão Simples

```latex
\textbf{Questão 01}

Enunciado...

(A) Alternativa A.
(B) Alternativa B.
(C) Alternativa C.
(D) Alternativa D.
(E) Alternativa E.
```

### Questão V/F

```latex
\textbf{Questão 15}

Analise as assertivas com V(Verdadeiro) ou F(Falso).

(\_\_) Primeira afirmativa.
(\_\_) Segunda afirmativa.

Marque a alternativa CORRETA:

(A) V, F.
(B) F, V.
```

### Gabarito (Opcional)

```latex
% Para MOSTRAR gabarito:
\newcommand{\correto}[1]{{\color{red}\textbf{(Correta: #1)}}}

% Para OCULTAR gabarito:
% Comente ou remova a linha acima

% Uso:
\textbf{Questão 01}
\correto{B}  % Remove esta linha para ocultar
```

### Questão Anulada

```latex
\textbf{Questão 18}

\anulada

Enunciado...
```

## ⚙️ Script de Compilação

### compilar.bat (Windows)

**Recursos:**
- ✅ Verifica se pdflatex está instalado
- ✅ Compila duas vezes (para índices)
- ✅ Limpa arquivos auxiliares
- ✅ Mostra mensagens de progresso
- ✅ Tratamento de erros

**Uso:**
```cmd
# Duplo clique no arquivo
compilar.bat

# Ou via terminal
cd c:\caminho\para\pasta
compilar.bat
```

## 🐛 Solução de Problemas

### Erro: "pdflatex not found"

**Solução:** Instale MiKTeX ou TeX Live

### Erro: Caractere Unicode

**Problema:**
```latex
10⁻² ml  ❌
```

**Solução:**
```latex
10$^{-2}$ ml  ✅
```

### Erro: Texto saindo da coluna

**Problema:** URL muito longa

**Solução:**
```latex
\small https://url-longa...
```

### Mais problemas?

Consulte a seção **"Problemas Comuns"** em [COMPILACAO_LATEX.md](COMPILACAO_LATEX.md)

## 📝 Workflow Recomendado

### 1. Preparação

```bash
# Navegar para o repositório
cd c:\Users\Admin\Documents\GitHub\iases

# Verificar instalação do LaTeX
pdflatex --version
```

### 2. Edição

```bash
# Abrir arquivo no editor
code simulados\latex\simulados_completos.tex

# Ou criar novo a partir do template
code simulados\templates\template_simulado.tex
```

### 3. Compilação

```bash
# Opção 1: Usar o script (recomendado)
scripts\compilar.bat

# Opção 2: Manualmente
cd simulados\latex
pdflatex simulados_completos.tex
pdflatex simulados_completos.tex  # Segunda vez (para índices)
```

### 4. Revisão

```bash
# PDF estará em simulados/pdf/
start simulados\pdf\simulados_completos.pdf
```

## 🎓 Recursos Adicionais

### Links Úteis

- [MiKTeX Documentation](https://docs.miktex.org/)
- [LaTeX WikiBook](https://en.wikibooks.org/wiki/LaTeX)
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [CTAN Packages](https://ctan.org/)

### Pacotes Utilizados

| Pacote | Finalidade |
|--------|------------|
| `multicol` | Layout em duas colunas |
| `geometry` | Configuração de margens |
| `fancyhdr` | Cabeçalhos e rodapés |
| `xcolor` | Cores (gabaritos em vermelho) |
| `ulem` | Sublinhados |

## ✨ Próximos Passos

1. ✅ Leia o [guia completo](COMPILACAO_LATEX.md) de formatação
2. ✅ Teste a compilação:
   ```bash
   scripts\compilar.bat
   ```
3. ✅ Experimente criar um novo simulado:
   ```bash
   copy simulados\templates\template_simulado.tex simulados\latex\meu_teste.tex
   ```
4. ✅ Personalize conforme necessário

## 🤝 Contribuições

Melhorias sugeridas:
- [ ] Script de compilação para Linux/Mac
- [ ] Gabarito separado em arquivo
- [ ] Folha de respostas automática
- [ ] Validação de questões

## 📧 Contato

Para dúvidas sobre formatação LaTeX, consulte:
- [Stack Exchange - TeX](https://tex.stackexchange.com/)
- [LaTeX Community](https://latex.org/forum/)

---

**Versão:** 1.0
**Atualizado:** 06/11/2025
**Autor:** Documentação do projeto IASES
**Licença:** Uso educacional
