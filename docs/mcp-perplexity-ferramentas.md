# Ferramentas MCP Perplexity Search - Documentação

**MCP:** perplexity-search
**Provedor:** @arjunkmrm/perplexity-search via Smithery
**Execução:** npx + Smithery CLI

---

## Sobre o MCP Perplexity Search

O MCP Perplexity Search fornece acesso à API do Perplexity AI, um mecanismo de busca com IA que retorna respostas contextualizadas e citadas, ideal para pesquisa acadêmica e estudos para concursos.

**Vantagens:**
- Respostas com citações de fontes
- Busca contextualizada e resumida
- Informações atualizadas da web
- Ideal para legislação e jurisprudência

---

## Status da Instalação

✅ **Configurado em:** [.claude/.mcp.json](../.claude/.mcp.json)
✅ **Habilitado em:** [.claude/settings.local.json](../.claude/settings.local.json)
⚠️ **Requer:** Reiniciar Claude Code para ativar

---

## Ferramentas Disponíveis

### 1. `perplexity_search`

**Descrição:** Realiza busca inteligente usando o Perplexity AI com respostas contextualizadas e citadas.

**Parâmetros:**
- `query` (string, obrigatório): Pergunta ou termo de busca

**Características:**
- Retorna resposta resumida e contextualizada
- Inclui citações de fontes
- Busca em tempo real na web
- Ideal para pesquisa legislativa e jurídica

**Exemplo de uso:**
```
Query: "ECA Lei 8069/1990 medidas socioeducativas artigos principais"
```

**Saída esperada:**
```
Resposta contextualizada sobre medidas socioeducativas do ECA
com citações de:
- Texto da lei
- Doutrina jurídica
- Jurisprudência relevante
- Fontes governamentais
```

---

## Casos de Uso para o Concurso IASES

### 1. Pesquisa de Legislação

**Objetivo:** Buscar informações atualizadas sobre leis específicas

**Exemplos de queries:**

```
"Lei 12.594/2012 SINASE principais artigos sobre atendimento socioeducativo"

"ECA artigo 112 medidas socioeducativas explicação detalhada"

"Resolução CONANDA 119/2006 diretrizes SINASE"

"Lei 706/2013 Espírito Santo sistema socioeducativo"
```

**Benefício:** Obter resumos com citações diretas da legislação

---

### 2. Análise da Banca IDCAP

**Objetivo:** Entender o perfil e padrão de questões da banca

**Exemplos de queries:**

```
"Banca IDCAP concursos públicos perfil de questões características"

"IDCAP estilo de prova pegadinhas comuns"

"Concursos IDCAP Espírito Santo análise"
```

**Benefício:** Identificar padrões e focar nos pontos mais cobrados

---

### 3. Direitos Humanos e Normas Internacionais

**Objetivo:** Estudar normas da ONU e tratados internacionais

**Exemplos de queries:**

```
"Regras de Beijing ONU adolescentes em conflito com a lei principais pontos"

"Declaração Universal dos Direitos Humanos artigos sobre crianças"

"Convenção sobre os Direitos da Criança ONU principais dispositivos"

"Regras da ONU para proteção de jovens privados de liberdade"
```

**Benefício:** Compreender contexto internacional das normas brasileiras

---

### 4. Justiça Restaurativa

**Objetivo:** Estudar práticas de justiça restaurativa

**Exemplos de queries:**

```
"Justiça restaurativa Brasil práticas com adolescentes"

"Comunicação não violenta Marshall Rosenberg aplicação socioeducativa"

"Círculos restaurativos no sistema socioeducativo brasileiro"
```

**Benefício:** Material complementar para questões sobre práticas inovadoras

---

### 5. Atualização Legislativa

**Objetivo:** Verificar alterações e atualizações nas leis

**Exemplos de queries:**

```
"ECA alterações recentes 2024 2025"

"SINASE mudanças legislativas atualizações"

"Lei de abuso de autoridade 13869/2019 aplicação agentes socioeducativos"
```

**Benefício:** Garantir que está estudando a versão atualizada da legislação

---

### 6. Ética na Administração Pública

**Objetivo:** Estudar princípios éticos e condutas

**Exemplos de queries:**

```
"Ética no serviço público brasileiro princípios fundamentais"

"Código de Ética do Servidor Público Federal principais deveres"

"Improbidade administrativa Lei 8429/1992 agentes públicos"
```

**Benefício:** Fundamentação teórica para questões de ética

---

### 7. Contexto Socioeducativo

**Objetivo:** Compreender o contexto do trabalho do agente socioeducativo

**Exemplos de queries:**

```
"Atribuições do agente socioeducativo no Brasil"

"Desafios do sistema socioeducativo brasileiro atual"

"Boas práticas em unidades socioeducativas"
```

**Benefício:** Visão prática e contextualizada do cargo

---

## Fluxo de Trabalho Recomendado

### Preparação de Simulados

1. **Pesquisar tema específico**
   ```
   "Art. 121 ECA medida de internação requisitos e exceções"
   ```

2. **Criar questões baseadas na resposta**
   - Usar citações literais
   - Criar distradores plausíveis
   - Verificar correção jurídica

3. **Validar com legislação original**
   - Conferir no texto da lei
   - Garantir literalidade

### Revisão de Tópicos

1. **Identificar dúvida**
2. **Formular query específica**
3. **Ler resposta com citações**
4. **Anotar no Obsidian** (usando MCP Obsidian)
5. **Criar flashcard** se necessário

### Estudo Diário

**Manhã:**
- Buscar 1 tema novo do edital
- Ler resposta do Perplexity
- Criar notas no Obsidian

**Tarde:**
- Revisar temas estudados
- Buscar jurisprudência relevante
- Fazer questões de simulado

**Noite:**
- Buscar atualizações legislativas
- Revisar flashcards
- Anotar progresso

---

## Comparação: Perplexity vs Google

| Característica | Perplexity | Google |
|----------------|------------|--------|
| Resposta resumida | ✅ Sim | ❌ Apenas links |
| Citações diretas | ✅ Sim | ⚠️ Depende |
| Contexto jurídico | ✅ Excelente | ⚠️ Variável |
| Legislação atualizada | ✅ Sim | ⚠️ Variável |
| Resposta direta | ✅ Sim | ❌ Não |
| Fontes confiáveis | ✅ Priorizadas | ⚠️ Variável |

---

## Integração com Outros MCPs

### Perplexity + Obsidian

**Fluxo:**
1. Buscar com Perplexity
2. Resumir informação importante
3. Salvar no Obsidian via MCP

**Exemplo prático:**
```
1. Query Perplexity: "Art. 112 ECA medidas socioeducativas"
2. Receber resposta com citações
3. Criar nota no Obsidian: "IASES/ECA-Art112.md"
4. Adicionar conteúdo via obsidian_append_content
```

---

## Limitações e Considerações

**Limitações:**
- Requer conexão com internet
- Depende da qualidade das fontes online
- Pode ter latência maior que busca local
- Consome créditos da API Perplexity

**Recomendações:**
- Sempre validar com legislação original
- Usar para compreensão, não como fonte única
- Verificar data de atualização das informações
- Priorizar fontes governamentais nas citações

---

## Comandos para Testar (Após Reiniciar)

Após reiniciar o Claude Code, você poderá usar:

### Teste Básico
```
Query: "O que é o ECA?"
```

### Teste para IASES
```
Query: "Medidas socioeducativas previstas no ECA Lei 8069/1990 artigos completos"
```

### Teste Legislação Estadual
```
Query: "Lei 706/2013 Espírito Santo IASES atribuições"
```

### Teste Banca
```
Query: "Perfil de questões da banca IDCAP em concursos públicos"
```

---

## Configuração Atual

**API Key:** Configurada (crude-vicuna-kofgid)
**Profile:** crude-vicuna-kofgid
**Comando:** npx @smithery/cli via cmd
**Status:** Aguardando reinício do Claude Code

---

## Troubleshooting

### MCP não está disponível
**Solução:** Reiniciar Claude Code

### Erro de API Key
**Solução:** Verificar key em [.claude/.mcp.json](../.claude/.mcp.json)

### Timeout na busca
**Solução:** Simplificar query ou dividir em múltiplas buscas

### Resposta genérica demais
**Solução:** Ser mais específico na query, incluir:
- Número da lei
- Artigo específico
- Contexto brasileiro/jurídico

---

## Próximos Passos

1. ✅ Configuração instalada
2. ⏳ Reiniciar Claude Code
3. ⏳ Testar busca básica
4. ⏳ Integrar com workflow de estudos
5. ⏳ Criar notas no Obsidian com resultados

---

**Documentação criada:** 2025-11-05
**Última atualização:** 2025-11-05
