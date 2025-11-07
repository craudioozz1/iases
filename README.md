# 📚 IASES 2025 - Agente Socioeducativo

Material completo de estudos para o concurso público IASES 2025 (Espírito Santo) - Cargo: Agente Socioeducativo.

## 📋 Sobre o Concurso

- **Data da Prova:** 18 de janeiro de 2026
- **Banca:** IDCAP
- **Nível:** Médio
- **Total de Questões:** 70 (múltipla escolha com 4 alternativas)

### Distribuição das Questões

| Disciplina | Questões | Peso |
|------------|----------|------|
| Português | 10 | 1 |
| Raciocínio Lógico | 5 | 1 |
| Informática | 5 | 1 |
| **Conhecimentos Específicos** | **50** | **2** |
| **Total** | **70** | - |

**Nota de Corte:** 50% = 60/120 pontos

## 📁 Estrutura do Repositório

```
iases/
├── 📂 simulados/              ← Simulados e provas práticas
│   ├── latex/                 ← Arquivos .tex (fonte LaTeX)
│   ├── pdf/                   ← PDFs compilados
│   ├── templates/             ← Templates para criar novos simulados
│   └── *.docx                 ← Simulados em Word (legado)
│
├── 📂 docs/                   ← Documentação
│   ├── latex/                 ← Documentação LaTeX
│   │   ├── COMPILACAO_LATEX.md
│   │   └── README_LATEX.md
│   ├── analise-banca-idcap.md
│   ├── conteudo.md
│   └── mcp-*.md
│
├── 📂 scripts/                ← Scripts de automação
│   ├── compilar.bat           ← Compilação LaTeX
│   └── criar_prova_*.py       ← Geração de provas
│
├── 📂 materiais-referencia/   ← Material de estudo
│   ├── legislacao/
│   └── provas-anteriores/
│
├── 📂 ferramentas-estudo/     ← Ferramentas auxiliares
│
├── 📄 CLAUDE.md               ← Instruções para Claude Code
├── 📄 index.md                ← Índice geral do projeto
├── 📄 *.md                    ← Simulados temáticos
└── 📄 README.md               ← Este arquivo
```

## 🚀 Início Rápido

### 1️⃣ Simulados em LaTeX (Formato Oficial)

Os simulados em LaTeX seguem o formato visual da prova IASES original:

```bash
# Compilar simulado completo (70 questões)
scripts\compilar.bat

# PDF gerado em:
simulados\pdf\simulados_completos.pdf
```

**📖 Documentação completa:** [docs/latex/README_LATEX.md](docs/latex/README_LATEX.md)

### 2️⃣ Simulados Temáticos (Markdown)

Simulados focados em tópicos específicos:

- [simulado-tematico-01-eca.md](simulado-tematico-01-eca.md) - ECA versão 1
- [simulado-tematico-02-sinase.md](simulado-tematico-02-sinase.md) - SINASE versão 1
- [simulado-tematico-03-eca-v2.md](simulado-tematico-03-eca-v2.md) - ECA versão 2
- [simulado-tematico-04-sinase-v2.md](simulado-tematico-04-sinase-v2.md) - SINASE versão 2

### 3️⃣ Conteúdo Programático

Consulte [docs/conteudo.md](docs/conteudo.md) para ver todos os tópicos do edital.

## 📚 Principais Recursos

### ✅ Simulados

- ✨ **Simulado completo em LaTeX** (70 questões) - formato oficial da prova
- 📝 **4 simulados temáticos** em Markdown (ECA e SINASE)
- 📄 **5 simulados em DOCX** (questões 1-70 divididas)
- 🎯 **Templates prontos** para criar novos simulados

### ✅ Documentação

- 📖 **Guia completo LaTeX** - formatação e compilação
- 📊 **Análise da banca IDCAP** - padrão de questões
- 📋 **Conteúdo programático** completo e organizado
- 🛠️ **Ferramentas MCP** - Obsidian e Perplexity

### ✅ Scripts

- ⚡ **Compilação automática** de simulados LaTeX
- 🤖 **Geração de provas** em Python
- 🔄 **Conversão de formatos**

## 🎯 Áreas de Conhecimentos Específicos

Os tópicos mais cobrados na prova:

### Legislação Principal

1. **ECA** - Estatuto da Criança e Adolescente (Lei 8.069/1990)
2. **SINASE** - Sistema Nacional de Atendimento Socioeducativo (Lei 12.594/2012)
3. **Constituição Federal 1988** - Direitos Fundamentais, Família/Criança/Adolescente
4. **Direitos Humanos** - Declaração Universal da ONU

### Normas da ONU

- Regras de Beijing
- Regras para Proteção de Jovens Privados de Liberdade
- Regras Mínimas das Nações Unidas para Tratamento de Reclusos

### Leis Complementares

- Lei 9.455/1997 (Tortura)
- Lei 12.288/2010 (Igualdade Racial)
- Lei 7.716/1989 (Racismo)
- Lei 13.869/2019 (Abuso de Autoridade)
- **Lei Estadual 706/2013 (Espírito Santo)**

## 🔧 Ferramentas Necessárias

### Para Compilar Simulados LaTeX

**Windows:**
1. Instale [MiKTeX](https://miktex.org/download) ou [TeX Live](https://www.tug.org/texlive/)
2. Verifique a instalação:
   ```bash
   pdflatex --version
   ```

**Editor Recomendado:**
- VS Code + extensão LaTeX Workshop
- TeXstudio
- Overleaf (online)

### Para Scripts Python

```bash
pip install -r requirements.txt
```

## 📖 Documentação Completa

| Documento | Descrição |
|-----------|-----------|
| [README_LATEX.md](docs/latex/README_LATEX.md) | Índice da documentação LaTeX |
| [COMPILACAO_LATEX.md](docs/latex/COMPILACAO_LATEX.md) | Guia técnico completo LaTeX |
| [analise-banca-idcap.md](docs/analise-banca-idcap.md) | Padrão de questões da banca |
| [conteudo.md](docs/conteudo.md) | Conteúdo programático completo |
| [CLAUDE.md](CLAUDE.md) | Instruções para Claude Code |

## 🎓 Como Estudar

### Ordem de Prioridade

1. **Conhecimentos Específicos** (83% da nota com peso 2)
   - Foco em ECA e SINASE
   - Direitos Humanos e normas da ONU
   - Lei Estadual 706/2013

2. **Português** (interpretação de texto)

3. **Informática** (Microsoft Word 2019)

4. **Raciocínio Lógico**

### Estratégia Recomendada

1. ✅ Leia o material legislativo nos [materiais de referência](materiais-referencia/)
2. ✅ Faça os simulados temáticos (ECA e SINASE)
3. ✅ Revise erros e anote pontos importantes
4. ✅ Faça o simulado completo em condições de prova
5. ✅ Analise questões da banca ([docs/analise-banca-idcap.md](docs/analise-banca-idcap.md))

## 📝 Criando Novos Simulados

### LaTeX (Recomendado)

```bash
# 1. Copiar template
copy simulados\templates\template_simulado.tex simulados\latex\meu_simulado.tex

# 2. Editar conteúdo
code simulados\latex\meu_simulado.tex

# 3. Compilar
cd simulados\latex
pdflatex meu_simulado.tex
```

### Python

```bash
# Usar scripts de geração
python scripts\criar_prova_01.py
```

## 🤝 Contribuindo

Melhorias bem-vindas:
- [ ] Mais simulados temáticos
- [ ] Questões comentadas
- [ ] Mapas mentais
- [ ] Flashcards Anki
- [ ] App mobile

## 📧 Suporte

**LaTeX:** Consulte [docs/latex/](docs/latex/) ou [TeX Stack Exchange](https://tex.stackexchange.com/)

**Conteúdo:** Verifique [CLAUDE.md](CLAUDE.md) para orientações ao Claude Code

## 📊 Status do Projeto

- ✅ Simulado completo em LaTeX (70 questões)
- ✅ 4 simulados temáticos (ECA e SINASE)
- ✅ Documentação completa
- ✅ Scripts de compilação
- ✅ Templates prontos
- ⏳ Gabaritos comentados (em andamento)
- ⏳ Material de revisão (em andamento)

## 📅 Timeline

- **Hoje:** Prática com simulados
- **Próximos meses:** Revisão contínua
- **18/01/2026:** Prova oficial IASES

---

**🎯 Meta:** Aprovação no concurso IASES 2025
**📚 Foco:** Conhecimentos Específicos (ECA + SINASE)
**💪 Estratégia:** Prática constante com simulados

**Boa sorte nos estudos! 🚀**

---

*Última atualização: 06/11/2025*
