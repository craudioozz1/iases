# CLAUDE.md

Este arquivo fornece orientações ao Claude Code (claude.ai/code) ao trabalhar neste repositório.

## Propósito do Repositório

Este repositório contém materiais de estudo para o **concurso público IASES 2025** (Espírito Santo, Brasil) para o cargo de **Agente Socioeducativo**.

**Detalhes da Prova:**
- Data: 18 de janeiro de 2026
- Banca: IDCAP
- Nível: Médio
- Total: 70 questões de múltipla escolha (4 alternativas cada)
- Distribuição: Português (10), Raciocínio Lógico (5), Informática (5), Conhecimentos Específicos (50)
- Pesos: Disciplinas básicas peso 1, Conhecimentos Específicos peso 2
- Nota de Corte: 50% = 60/120 pontos (100 pontos de específicas + 20 de básicas = 120 total)

## Estrutura do Repositório

- `agente_socioeducativo_masculino.pdf` - Prova anterior IASES (material de referência)
- `agente_socioeducativo_masculino.txt` - Extração de texto do PDF da prova
- `conteudo.md` - Conteúdo programático completo de todas as disciplinas


## Fluxo de Trabalho Principal

### Conversão de Materiais PDF
```bash
pdftotext -layout arquivo.pdf saida.txt
```
O repositório está configurado para permitir comandos pdftotext sem solicitação.

### Criação de Questões de Simulados

Ao criar provas ou questões de prática:
1. **Seguir distribuição exata**: 10+5+5+50 questões correspondendo à estrutura real da prova
2. **Usar 4 alternativas** (A, B, C, D) - não 5 como alguns outros concursos brasileiros
3. **Aplicar pesos corretos** ao calcular pontuações (básicas=1, específicas=2)
4. **Incluir gabarito comentado** com referências legislativas (ex: "Art. 112 do ECA")
5. **Seguir estilo IDCAP**: questões literais da legislação, linguagem formal/jurídica

### Áreas Prioritárias de Conhecimentos Específicos

As questões devem enfatizar estes tópicos (de `conteudo.md`):
- **ECA** (Estatuto da Criança e Adolescente) - Lei 8.069/1990
- **SINASE** - Lei 12.594/2012 e Resolução CONANDA 119/2006
- **Direitos Humanos** (Declaração Universal da ONU, convenções sobre direitos da criança)
- **Normas da ONU**: Regras de Beijing, Regras para Proteção de Jovens Privados de Liberdade
- **Justiça Restaurativa e Comunicação Não Violenta**
- **Ética na Administração Pública**
- **Constituição Federal 1988**: Direitos Fundamentais, Direitos Sociais, Segurança Pública, Família/Criança/Adolescente
- **Leis Federais**: 9.455/1997 (tortura), 12.288/2010 (igualdade racial), 7.716/1989 (racismo), 13.869/2019 (abuso de autoridade)
- **Lei Estadual**: 706/2013 (Espírito Santo)

### Princípios de Elaboração de Questões (Padrão IDCAP)

**Fazer:**
- Citar artigos específicos (ex: "Segundo o art. 112 do ECA...")
- Usar linguagem formal/jurídica
- Incluir pegadinhas comuns: palavras absolutas (sempre, nunca, apenas, somente)
- Focar em: medidas socioeducativas, direitos do adolescente, princípios do SINASE
- Indicar nível de dificuldade (fácil/médio/difícil)

**Não fazer:**
- Criar questões genéricas ou superficiais
- Inventar dados não presentes na legislação
- Usar linguagem informal ou emojis excessivos

## Preferências de Formato de Resposta

- Ser objetivo e direto
- Usar tabelas/listas quando aplicável
- Incluir referências (Art. X da Lei Y)
- Destacar pontos-chave com ênfase (negrito/itálico)
- Sugerir tópicos de revisão baseados em erros

## Ordem de Prioridade dos Estudos

1. **Conhecimentos Específicos** (83% da nota final com peso 2)
2. Português (interpretação de texto)
3. Informática (foco em Microsoft Word 2019)
4. Raciocínio Lógico

## Trabalho com Legislação

Todas as questões devem ser validadas com a legislação vigente. Em caso de dúvida:
- Referenciar o texto legal atual dos materiais de estudo
- Preferir dispositivos literais/explícitos em vez de interpretações
- Observar atualizações ou alterações legislativas
