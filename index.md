# Índice - Materiais de Estudo IASES 2025

**Concurso:** IASES 2025 - Agente Socioeducativo
**Banca:** IDCAP
**Data da Prova:** 18 de janeiro de 2026
**Nível:** Médio

---

## 📋 Sobre o Concurso

- **Total de questões:** 70 (múltipla escolha com 4 alternativas)
- **Distribuição:**
  - Português: 10 questões (peso 1)
  - Raciocínio Lógico: 5 questões (peso 1)
  - Informática: 5 questões (peso 1)
  - Conhecimentos Específicos: 50 questões (peso 2)
- **Nota de Corte:** 50% = 60/120 pontos
- **Pontuação máxima:** 120 pontos (100 de específicas + 20 de básicas)

---

## 📁 Estrutura do Repositório

### 📄 Arquivos na Raiz

- **[CLAUDE.md](CLAUDE.md)** - Instruções para o Claude Code trabalhar neste repositório
- **index.md** (este arquivo) - Índice e navegação do repositório

### 📚 `/docs` - Documentação e Análises

Contém documentos de referência sobre o concurso e conteúdo programático:

- **[conteudo.md](docs/conteudo.md)** - Conteúdo programático completo de todas as disciplinas
- **[analise-banca-idcap.md](docs/analise-banca-idcap.md)** - Análise do perfil e padrões da banca IDCAP
- **[mcp-obsidian-ferramentas.md](docs/mcp-obsidian-ferramentas.md)** - Documentação completa das ferramentas MCP Obsidian
- **[mcp-perplexity-ferramentas.md](docs/mcp-perplexity-ferramentas.md)** - Documentação completa das ferramentas MCP Perplexity Search

### 📖 `/materiais-referencia` - Materiais de Referência

#### `/materiais-referencia/provas-anteriores`

Provas anteriores do IASES para estudo e análise de padrões:

- **[agente_socioeducativo_masculino.pdf](materiais-referencia/provas-anteriores/agente_socioeducativo_masculino.pdf)** - Prova anterior em PDF
- **[agente_socioeducativo_masculino.txt](materiais-referencia/provas-anteriores/agente_socioeducativo_masculino.txt)** - Texto extraído da prova

#### `/materiais-referencia/legislacao`

Pasta destinada a armazenar legislações em PDF (ECA, SINASE, etc.) - **atualmente vazia**

### 📝 `/simulados` - Provas Simuladas

Simulados em formato DOCX organizados em 5 blocos de 14 questões cada:

1. **[Simulado 01 - Questões 01-14](simulados/Prova_Simulado_Questoes_01-14.docx)**
2. **[Simulado 02 - Questões 15-28](simulados/Prova_Simulado_Questoes_15-28.docx)**
3. **[Simulado 03 - Questões 29-42](simulados/Prova_Simulado_Questoes_29-42.docx)**
4. **[Simulado 04 - Questões 43-56](simulados/Prova_Simulado_Questoes_43-56.docx)**
5. **[Simulado 05 - Questões 57-70](simulados/Prova_Simulado_Questoes_57-70.docx)**

**Observação:** Cada simulado segue a estrutura da prova real com questões de Português, Raciocínio Lógico, Informática e Conhecimentos Específicos.

### 🛠️ `/scripts` - Scripts Python

Scripts para geração de provas e questões:

- **[criar_prova_01.py](scripts/criar_prova_01.py)** - Script gerador do Simulado 01
- **[criar_prova_02.py](scripts/criar_prova_02.py)** - Script gerador do Simulado 02
- **[criar_prova_03.py](scripts/criar_prova_03.py)** - Script gerador do Simulado 03
- **[criar_prova_04.py](scripts/criar_prova_04.py)** - Script gerador do Simulado 04
- **[criar_prova_05.py](scripts/criar_prova_05.py)** - Script gerador do Simulado 05

**Uso:**
```bash
python scripts/criar_prova_01.py
```

### 🎯 `/ferramentas-estudo` - Ferramentas de Estudo

Materiais auxiliares para revisão e memorização:

- **[flashcards-eca-sinase.md](ferramentas-estudo/flashcards-eca-sinase.md)** - Flashcards sobre ECA e SINASE

---

## 🎓 Áreas de Conhecimento Prioritárias

### Conhecimentos Específicos (83% da nota final)

1. **ECA** - Estatuto da Criança e Adolescente (Lei 8.069/1990)
2. **SINASE** - Sistema Nacional de Atendimento Socioeducativo (Lei 12.594/2012)
3. **Direitos Humanos** - Declaração Universal, Convenções da ONU
4. **Normas da ONU** - Regras de Beijing, Proteção de Jovens Privados de Liberdade
5. **Justiça Restaurativa e Comunicação Não Violenta**
6. **Ética na Administração Pública**
7. **Constituição Federal 1988** - Direitos Fundamentais, Segurança Pública
8. **Legislação Federal Específica:**
   - Lei 9.455/1997 (Tortura)
   - Lei 12.288/2010 (Igualdade Racial)
   - Lei 7.716/1989 (Racismo)
   - Lei 13.869/2019 (Abuso de Autoridade)
9. **Legislação Estadual** - Lei 706/2013 (ES)

### Conhecimentos Básicos (17% da nota final)

- **Português** - Interpretação de texto, gramática
- **Raciocínio Lógico** - Sequências, proposições lógicas
- **Informática** - Microsoft Word 2019, conceitos básicos

---

## 📊 Ordem de Prioridade nos Estudos

1. **Conhecimentos Específicos** (prioridade máxima - 83% da nota)
2. **Português** (interpretação de textos)
3. **Informática** (foco em Word 2019)
4. **Raciocínio Lógico**

---

## 🔧 Comandos Úteis

### Converter PDF para Texto
```bash
pdftotext -layout arquivo.pdf saida.txt
```

### Executar Scripts Python
```bash
python scripts/criar_prova_01.py
```

### Integração via MCP (Model Context Protocol)

O repositório possui 2 integrações MCP configuradas:

**MCP Obsidian:**
- Gerenciamento de notas no vault Obsidian
- Veja [documentação completa](docs/mcp-obsidian-ferramentas.md)

**MCP Perplexity Search:**
- Busca inteligente com IA e citações
- Ideal para pesquisa legislativa
- Veja [documentação completa](docs/mcp-perplexity-ferramentas.md)
- ⚠️ **Requer reiniciar Claude Code para ativar**

---

## 📅 Timeline

- **Data da Prova:** 18 de janeiro de 2026
- **Dias restantes:** Verificar calendário
- **Meta diária:** Revisar pelo menos 1 tema de conhecimentos específicos + 1 simulado parcial

---

## 💡 Dicas de Estudo

1. **Foco em legislação literal** - A banca IDCAP cobra conhecimento literal das leis
2. **Atenção às pegadinhas** - Palavras como "sempre", "nunca", "apenas", "somente"
3. **Revisar artigos específicos** - Decorar números de artigos importantes (especialmente ECA e SINASE)
4. **Praticar com simulados** - Fazer os 5 simulados disponíveis múltiplas vezes
5. **Usar flashcards** - Revisar diariamente os flashcards de ECA/SINASE

---

## 🔗 Links Úteis

- **Banca:** IDCAP
- **Órgão:** IASES - Instituto de Atendimento Socioeducativo do Espírito Santo
- **Cargo:** Agente Socioeducativo

---

**Última atualização:** Novembro 2025
