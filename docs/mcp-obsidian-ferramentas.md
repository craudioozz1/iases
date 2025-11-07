# Ferramentas MCP Obsidian - Documentação

**MCP:** mcp-obsidian
**Versão:** Instalada via `uvx`
**Conexão:** Local REST API (porta 27124)

---

## Índice

1. [Listagem de Arquivos](#listagem-de-arquivos)
2. [Leitura de Conteúdo](#leitura-de-conteúdo)
3. [Busca e Pesquisa](#busca-e-pesquisa)
4. [Criação e Edição](#criação-e-edição)
5. [Exclusão](#exclusão)
6. [Notas Periódicas](#notas-periódicas)
7. [Mudanças Recentes](#mudanças-recentes)

---

## Listagem de Arquivos

### 1. `obsidian_list_files_in_vault`

**Descrição:** Lista todos os arquivos e diretórios na raiz do vault Obsidian.

**Parâmetros:** Nenhum

**Retorno:** Array de strings com nomes de arquivos e pastas

**Exemplo de uso:**
```
Lista todos os arquivos na raiz do vault
```

**Saída esperada:**
```json
[
  "IASES/",
  "Projetos/",
  "Daily Notes/"
]
```

---

### 2. `obsidian_list_files_in_dir`

**Descrição:** Lista todos os arquivos e diretórios dentro de um diretório específico.

**Parâmetros:**
- `dirpath` (string, obrigatório): Caminho relativo à raiz do vault

**Exemplo de uso:**
```
Listar arquivos em IASES/
```

**Saída esperada:**
```json
[
  "Index.md",
  "ECA.md",
  "SINASE.md"
]
```

**Observação:** Diretórios vazios não são retornados.

---

## Leitura de Conteúdo

### 3. `obsidian_get_file_contents`

**Descrição:** Retorna o conteúdo completo de um único arquivo do vault.

**Parâmetros:**
- `filepath` (string, obrigatório): Caminho do arquivo relativo à raiz do vault

**Exemplo de uso:**
```
Ler conteúdo de IASES/Index.md
```

**Saída esperada:**
```markdown
# Índice de Estudos - IASES 2025
...conteúdo do arquivo...
```

---

### 4. `obsidian_batch_get_file_contents`

**Descrição:** Retorna o conteúdo de múltiplos arquivos concatenados com cabeçalhos.

**Parâmetros:**
- `filepaths` (array, obrigatório): Lista de caminhos de arquivos

**Exemplo de uso:**
```
Ler múltiplos arquivos: ["IASES/ECA.md", "IASES/SINASE.md"]
```

**Vantagem:** Mais eficiente que fazer múltiplas chamadas individuais.

---

## Busca e Pesquisa

### 5. `obsidian_simple_search`

**Descrição:** Busca simples por texto em todos os arquivos do vault.

**Parâmetros:**
- `query` (string, obrigatório): Texto a buscar
- `context_length` (integer, opcional): Quantidade de contexto ao redor do match (padrão: 100)

**Exemplo de uso:**
```
Buscar "medidas socioeducativas" com contexto de 150 caracteres
```

**Saída esperada:**
```json
[
  {
    "file": "IASES/ECA.md",
    "match": "...contexto antes...medidas socioeducativas...contexto depois..."
  }
]
```

---

### 6. `obsidian_complex_search`

**Descrição:** Busca avançada usando queries JsonLogic com suporte a glob e regexp.

**Parâmetros:**
- `query` (object, obrigatório): Objeto JsonLogic

**Operadores suportados:**
- `glob`: Padrões de arquivo (ex: `*.md`)
- `regexp`: Expressões regulares
- Operadores JsonLogic padrão

**Exemplo de uso:**
```json
{
  "glob": ["*.md", {"var": "path"}]
}
```

**Casos de uso:**
- Buscar todos os arquivos markdown
- Filtrar por tags específicas
- Encontrar documentos com certas propriedades

---

## Criação e Edição

### 7. `obsidian_append_content`

**Descrição:** Adiciona conteúdo ao final de um arquivo (cria o arquivo se não existir).

**Parâmetros:**
- `filepath` (string, obrigatório): Caminho do arquivo
- `content` (string, obrigatório): Conteúdo a adicionar

**Exemplo de uso:**
```
Adicionar "## Nova seção" ao arquivo IASES/Index.md
```

**Comportamento:**
- Se o arquivo não existe, cria novo arquivo
- Se existe, adiciona ao final

---

### 8. `obsidian_patch_content`

**Descrição:** Insere conteúdo em local específico do arquivo (relativo a heading, bloco ou frontmatter).

**Parâmetros:**
- `filepath` (string, obrigatório): Caminho do arquivo
- `operation` (enum, obrigatório): `append`, `prepend` ou `replace`
- `target_type` (enum, obrigatório): `heading`, `block` ou `frontmatter`
- `target` (string, obrigatório): Identificador do alvo
- `content` (string, obrigatório): Conteúdo a inserir

**Exemplos de uso:**

#### Adicionar após um heading:
```
filepath: "IASES/ECA.md"
operation: "append"
target_type: "heading"
target: "Medidas Socioeducativas"
content: "### Advertência\n..."
```

#### Modificar frontmatter:
```
filepath: "IASES/Index.md"
operation: "replace"
target_type: "frontmatter"
target: "tags"
content: "['concurso', 'iases', '2025']"
```

#### Usar block reference:
```
filepath: "IASES/Notas.md"
operation: "append"
target_type: "block"
target: "^ref-123"
content: "Conteúdo adicional"
```

---

## Exclusão

### 9. `obsidian_delete_file`

**Descrição:** Deleta um arquivo ou diretório do vault.

**Parâmetros:**
- `filepath` (string, obrigatório): Caminho do arquivo/diretório
- `confirm` (boolean, obrigatório): Deve ser `true` para confirmar

**Exemplo de uso:**
```
Deletar IASES/rascunho.md com confirmação
```

**Atenção:** Ação irreversível! Sempre usar com cautela.

---

## Notas Periódicas

### 10. `obsidian_get_periodic_note`

**Descrição:** Obtém a nota periódica atual para o período especificado.

**Parâmetros:**
- `period` (enum, obrigatório): `daily`, `weekly`, `monthly`, `quarterly` ou `yearly`

**Exemplo de uso:**
```
Obter nota diária de hoje
```

**Retorno:** Conteúdo da nota periódica atual

**Casos de uso:**
- Acessar daily note de hoje
- Verificar nota semanal atual
- Revisar planejamento mensal

---

### 11. `obsidian_get_recent_periodic_notes`

**Descrição:** Obtém as notas periódicas mais recentes de um tipo.

**Parâmetros:**
- `period` (enum, obrigatório): Tipo de período
- `limit` (integer, opcional): Máximo de notas a retornar (padrão: 5, máx: 50)
- `include_content` (boolean, opcional): Incluir conteúdo completo (padrão: false)

**Exemplo de uso:**
```
Obter últimas 10 daily notes com conteúdo
```

**Casos de uso:**
- Revisar últimas 7 notas diárias
- Analisar progresso semanal
- Gerar resumo mensal

---

## Mudanças Recentes

### 12. `obsidian_get_recent_changes`

**Descrição:** Obtém arquivos modificados recentemente no vault.

**Parâmetros:**
- `limit` (integer, opcional): Máximo de arquivos (padrão: 10, máx: 100)
- `days` (integer, opcional): Incluir apenas modificados nos últimos N dias (padrão: 90)

**Exemplo de uso:**
```
Obter 20 arquivos modificados nos últimos 30 dias
```

**Saída esperada:**
```json
[
  {
    "file": "IASES/Index.md",
    "modified": "2025-11-05T10:30:00Z"
  }
]
```

**Casos de uso:**
- Revisar trabalho recente
- Encontrar arquivos esquecidos
- Acompanhar progresso de estudos

---

## Fluxos de Trabalho Recomendados

### Criação de Estrutura de Estudos

1. Usar `obsidian_list_files_in_vault` para verificar estrutura
2. Usar `obsidian_append_content` para criar índices
3. Usar `obsidian_patch_content` para organizar por seções

### Revisão de Conteúdo

1. Usar `obsidian_get_recent_changes` para ver modificações
2. Usar `obsidian_batch_get_file_contents` para ler múltiplos arquivos
3. Usar `obsidian_simple_search` para encontrar tópicos específicos

### Gerenciamento de Daily Notes

1. Usar `obsidian_get_periodic_note` para nota de hoje
2. Usar `obsidian_append_content` para adicionar anotações
3. Usar `obsidian_get_recent_periodic_notes` para revisar semana

---

## Limitações e Considerações

- **Conexão:** Requer Obsidian Local REST API rodando
- **Permissões:** Depende das configurações do plugin no Obsidian
- **Caminhos:** Sempre relativos à raiz do vault
- **Encoding:** UTF-8 padrão para todos os arquivos
- **Diretórios vazios:** Não aparecem em listagens

---

## Integração com IASES

### Casos de Uso Específicos

**1. Sincronizar flashcards do GitHub para Obsidian:**
```
Ler flashcards-eca-sinase.md do repo
→ Criar/atualizar IASES/Flashcards.md no Obsidian
```

**2. Registrar progresso de simulados:**
```
Após fazer simulado
→ Usar obsidian_append_content em IASES/Progresso.md
→ Adicionar nota com data, pontuação e tópicos para revisar
```

**3. Criar notas de revisão diárias:**
```
Usar obsidian_get_periodic_note(daily)
→ Adicionar tópicos estudados hoje
→ Linkar para materiais relevantes
```

**4. Buscar legislação específica:**
```
Usar obsidian_simple_search("Art. 112 ECA")
→ Encontrar todas as referências
→ Consolidar em nota de revisão
```

---

## Configuração Atual

**Vault Conectado:** Identificado
**Pastas Principais:**
- `IASES/` - Materiais de estudo do concurso

**Arquivos Criados:**
- `IASES/Index.md` - Índice principal

---

**Documentação atualizada:** 2025-11-05
