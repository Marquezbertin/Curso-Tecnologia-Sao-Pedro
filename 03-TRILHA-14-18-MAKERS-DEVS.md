# 🚀 Trilha MAKERS/DEVS (14–18 anos) — "Tecnologia na Prática" · São Pedro/SP

**Carga horária:** 16 aulas × 90 min = **24 horas**
**Formato:** 1 encontro por semana, **ao vivo online**, **gratuito**
**Público:** jovens de 14 a 18 anos de São Pedro/SP e região (região de Piracicaba)
**Entregável final:** **Projeto de Impacto Local em Open Source** — público, no GitHub, com testes e deploy

---

## Sumário

| Aula | Módulo | Entregável principal |
|---|---|---|
| [1](#b1) | [B1 — Pensamento Computacional Avançado](#b1) | Fluxograma + pseudocódigo de um sistema real de São Pedro/SP |
| [2](#b2) | [B2 — Lógica e Algoritmos (Visualg → pseudocódigo)](#b2) | 8 algoritmos em pseudocódigo + 2 no Visualg |
| [3](#b3) | [B3 — Python do Zero](#b3) | 5 scripts rodando + ficha de estudante |
| [4](#b4) | [B4 — Python: Projetos Práticos](#b4) | 1 CLI interativo + 1 script de automação |
| [5](#b5) | [B5 — Web: HTML, CSS e JavaScript](#b5) | Site responsivo de 3 páginas |
| [6](#b6) | [B6 — Banco de Dados e SQL](#b6) | Schema + 10 consultas do projeto |
| [7](#b7) | [B7 — Git e GitHub (portfólio público)](#b7) | Repositório + 10 commits + README + Pages |
| [8](#b8) | [B8 — QA: Testes de Software](#b8) | Plano de testes + 1 bug corrigido + suíte automatizada |
| [9](#b9) | [B9 — IA para Iniciantes](#b9) | 1 chatbot ou gerador com prompt avaliado |
| [10](#b10) | [B10 — Metodologias Ágeis (Scrum/Kanban)](#b10) | Sprint real com quadro, backlog e retrospectiva |
| [11](#b11) | [B11 — Cibersegurança, Ética e Paradigmas](#b11) | Política de segurança do projeto + aula aberta |
| [12](#b12) | [B12 — Inglês Técnico para Programadores](#b12) | README bilíngue + commits em inglês |
| [13](#b13) | [B13 — Projeto Final parte 1 (escopo)](#b13) | Carta de escopo + backlog priorizado |
| [14](#b14) | [B14 — Projeto Final parte 2 (implementação)](#b14) | MVP funcional no repositório |
| [15](#b15) | [B15 — Projeto Final parte 3 (testes, deploy, docs)](#b15) | Plano de testes + checklist de aceite + deploy no Pages |
| [16](#b16) | [B16 — Showcase, Demo Day e Certificação](#b16) | Apresentação + publicação + certificado |

**Blocos do documento**

- [Sobre este material](#sobre-este-material) — gratuito, MIT, repositório de origem, como usar e o "kit do Maker"
- [Encerramento e Certificação](#encerramento) — critérios, rubrica de 4 níveis, pesos e modelo de certificado
- [Como se inscrever](#como-se-inscrever)

---

## Sobre este material

### É gratuito, de verdade

- **Custo zero para o aluno e para a família.** Nenhuma aula depende de plano pago,
  assinatura, licença ou licença de escola. Todas as ferramentas usadas são gratuitas:
  [Python](https://www.python.org/downloads/), [Google Colab](https://colab.research.google.com/),
  [GitHub](https://github.com/), [GitHub Pages](https://pages.github.com/),
  [SQLite Browser](https://sqlitebrowser.org/), [Visualg 3.0](https://visualg3.com.br/),
  [VS Code](https://code.visualstudio.com/) e o [Laboratório Tech Social](https://marquezbertin.github.io/laboratorio-tech-social/).
- **Material que roda no celular.** Isso não é detalhe: em São Pedro/SP, **29,9% da população
  tem rendimento per capita de até meio salário mínimo**. Um curso que exige notebook
 caro deixa gente de fora. Todo exercício tem versão `.txt` com **"Resposta Esperada"**
  e roda no celular; o computador é recomendado a partir do B3 e obrigatório do B7 em diante.
- **Acesso aberto.** Todo este material é público e reutilizável sob **licença MIT**.
- **Sem prova eliminatória.** A avaliação é **formativa**: entregas, commits, testes e
  apresentação. Ninguém é reprovado: quem não cumprir um critério recebe plano de recuperação e conclui na turma seguinte, sem custo.

### Repositório de origem

Este material foi construído a partir de um conjunto real de repositórios abertos mantidos
por [Marquez Bertin](https://github.com/Marquezbertin) e pelo
[Laboratório Tech Social](https://marquezbertin.github.io/laboratorio-tech-social/):

| Repositório | O que traz |
|---|---|
| `laboratorio-tech-social/` | Plano pedagógico, trilhas web, 41 exercícios jogáveis no navegador, slides e modelo de certificado |
| `python-do-zero/` | 15 módulos × 6 exercícios de Python, todos em `.txt` com **"Resposta Esperada"** |
| `logica_programacao/` | Fundamentos de lógica com algoritmos em pseudocódigo |
| `pensamento_computacional/` | 15 módulos × 6 exercícios sobre os quatro pilares do pensamento computacional |
| `html-css-js-pratica/` | 15 módulos × 6 exercícios de HTML, CSS e JavaScript |
| `banco-de-dados-sql/` | 15 módulos × 6 exercícios de SQL e modelagem |
| `git-github-iniciantes/` | 15 módulos de Git e GitHub, do primeiro `commit` ao GitHub Pages |
| `manual-qa-completo/` | Manual de QA com templates em PT (`docs/10/PT/`) — base dos modelos de escopo, plano de testes e aceite |
| `qa-exercicios-praticos/` | Casos de teste, simulados, sites para testar e modelos em Markdown |
| `ia-para-iniciantes/` | 15 módulos × 6 exercícios sobre IA, prompt, ética e projetos |
| `ingles-para-programadores/` | 15 módulos × 6 exercícios de inglês técnico |
| `formacaoScrumMaster/` | Estudos de caso de Scrum em QA, ING BANK, Spotify e projeto distribuído |
| `esporte-sao-pedro/` | App real do clube da cidade (Supabase + RLS + Edge Functions + IA) — referência do capstone |
| `Central-de-noticias/` | PWA real de notícias com seção **"São Pedro e região"** — referência do capstone |
| `QA_RUN/` | 71 jogos educativos de QA e HTML5 no navegador |

Os nomes de pasta e de arquivo citados neste material foram **verificados** nos repositórios
locais. Quando um exercício é citado, o caminho é exato.

### Como usar este material

1. **Como aluno:** leia o módulo da semana antes do encontro. Chegue com o `README.md`
   do seu repositório aberto. O encontro tem 90 minutos e **cinco fases** — você vai
   construir algo em 45 dos 90 minutos.
2. **Como professor:** o roteiro de cada módulo traz os minutos de cada fase, a
   **fala exata** do professor, o comportamento das salas de breakout e o **plano B**
   para quando a internet cair. Os critérios de "pronto" são listas de verificação
   (`- [ ]`) prontas para virar rubrica.
3. **Como equipe de apoio (voluntário/tutor):** entre em uma sala de breakout e fique
   com um grupo. O nível 4 da rubrica exige que o aluno **ajude um colega** — ajudar é
   parte da nota.
4. **Offline:** todos os exercícios de `python-do-zero`, `logica_programacao` e
   `pensamento_computacional` são arquivos `.txt` com **"Resposta Esperada"**. Baixe
   antes da aula e use o plano B.

### O "kit do Maker" — ambiente de trabalho padrão da turma

Todo aluno mantém **um único repositório** durante as 16 aulas. A estrutura é a mesma
para todos e é distribuída na aula 1:

```
meu-projeto/
├── README.md            # índice do projeto: o que é, como rodar, quem fez
├── docs/
│   ├── decisoes.md      # ADR simplificado: cada decisão técnica tem data e motivo
│   └── setup.md         # como rodar o projeto do zero, passo a passo
├── src/                 # código
├── tests/               # testes automatizados
├── data/                # dados (CSV/JSON) — SEM dados pessoais reais
└── notas/               # anotações das aulas (o caderno digital)
```

**Regras do kit (valem do módulo B1 ao B16):**

| Regra | Por quê |
|---|---|
| **Commit ou não existe** | Tudo que funciona vira `commit` no mesmo dia, com mensagem no formato Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`) |
| **Nada é segredo** | O `README.md` é a avaliação. Se não está documentado, não está pronto |
| **`data/` sem dados pessoais reais** | Nada de nome completo, RG, endereço, telefone ou foto de aluno. Use dados fictícios ou dados públicos |
| **`docs/decisoes.md` sempre atualizado** | "Por que SQLite e não JSON?" — responder isso é parte do trabalho |
| **Um `commit` por ideia** | Se o commit diz 5 coisas, o commit está errado |

**Plano de usernames:** o aluno pode usar o apelido escolhido na primeira aula
(ex.: `luna_dev`). Nada de e-mail real em repositório público.

### Como a aula funciona (online, ao vivo)

```
Fase 1 — Apresentação  (10 min)  professor fala, mostra, não entrega
Fase 2 — Exploração     (20 min)  conceito + código ao vivo, pergunta e resposta
Fase 3 — Mão na massa  (35 min)  SALAS DE BREAKOUT de 3–4 alunos
Fase 4 — Projeto       (15 min)  cada grupo constrói a entrega do módulo
Fase 5 — Mostra        (10 min)  2 grupos apresentam, turma dá feedback
```

- **Câmera:** obrigatória até a Fase 2. Depois, o BREAKOUT não grava.
- **Falar:** mão levantada ou reação 🇚 (emoji de reação) no chat. O professor chama
  pelo apelido — nunca pelo nome completo.
- **Presença:** lista simples por **apelido** na planilha da turma. Ninguém precisa
  entregar nome completo em lugar nenhum.
- **Tela:** o professor compartilha a tela do editor durante as Fases 1 e 2. Durante o
  breakout, cada aluno compartilha a tela do próprio editor com o grupo.

---

<a id="b1"></a>

## Módulo 1 — Pensamento Computacional Avançado (Aula 1)

**Duração:** 90 min · **Aula 1 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Aplicar os **quatro pilares** (decomposição, reconhecimento de padrões, abstração e
   algoritmos) a um **problema real de São Pedro/SP**, e não a um exemplo delivro.
2. Desenhar o **fluxograma** de um processo com 3 decisões e **escrever o pseudocódigo**
   correspondente, com condição de término explícita.
3. Reconhecer, no próprio texto, os **padrões de abstração** (o que foi descartado e por quê).

**Objetivo secundário:** saber explicar, em 1 minuto, por que "pensamento computacional"
não é só "programação".

**Entregável do módulo:** **1 fluxograma + 1 pseudocódigo** de um processo real escolhido
pelo aluno (fila da lanchonete, agendamento de jogo na quadra, plantão da biblioteca,
rotina de treino na piscina municipal), entregues como `docs/fluxograma.md` e
`docs/pseudocodigo.md` no repositório, com **1 commit**.

### 📚 Fontes no repositório

`pensamento_computacional/` — **15 módulos × 6 exercícios = 90 exercícios**, cada um
com seção **"RESULTADO ESPERADO"**:

| Módulo | Conteúdo | Exercícios |
|---|---|---|
| `01_pensamento_computacional` | Os quatro pilares, autoavaliação, mundo contrário | 6 |
| `02_decomposicao` | Quebrar o problema em partes | 6 |
| `03_reconhecimento_padroes` | Achar repetições e regularidades | 6 |
| `04_abstracao` | Generalizar, filtrar, simplificar, níveis de detalhe | 6 |
| `05_pensamento_algoritmico` | Sequências, laços, condições | 6 |
| `06_fluxogramas` | Símbolos, setas, laços, depuração de fluxo | 6 |
| `07_pseudocodigo` | Do texto ao pseudocódigo, do fluxograma ao código | 6 |
| `08_logica_proposicional` | E, OU, NÃO, se-então, paradoxos | 6 |
| `09_sistema_binario` | Bits, bytes, conversão | 6 |
| `10_hardware_software` | Hardware, software, sistema operacional | 6 |
| `11_sistemas_operacionais` | Windows, Linux, arquivos, processos | 6 |
| `12_redes_internet` | Internet, IP, DNS, servidores | 6 |
| `13_ciberseguranca` | Senhas, phishing, golpes, criptografia | 6 |
| `14_tecnologias_emergentes` | IA, IoT, computação em nuvem | 6 |
| `15_etica_sociedade` | Dilemas, privacidade, desigualdade, manifesto | 6 |

**Trilha web e slides:**
`laboratorio-tech-social/site/trilhas/adolescentes/01-python.html` ·
`laboratorio-tech-social/materiais/slides/aula-teens-01-python.html` ·
`laboratorio-tech-social/site/exercicios/pensamento-computacional.html` ·
`laboratorio-tech-social/site/exercicios/code-builder.html` ·
`laboratorio-tech-social/site/exercicios/desafio-logica.html` ·
`laboratorio-tech-social/site/exercicios/planilha.html`

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Decomposição** | "Problema grande é vários problemas pequenos empilhados." |
| **Padrão** | "Se você já resolveu um caso parecido, você não começou do zero." |
| **Abstração** | "Esconder o detalhe que não importa **para este** problema." |
| **Algoritmo** | "Passos que sempre chegam no mesmo resultado." |
| **Fluxograma** | "O desenho do caminho, incluindo os becos sem saída." |
| **Pseudocódigo** | "Português com disciplina de programa. Sem palavra-chave de ninguém." |
| **Condição de término** | "Toda repetição precisa de um 'quando parar'. Sem isso, é laço infinito." |
| **Depuração** | "Fluxograma errado não é Failure. É rascunho que ainda não terminou." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Presentação (10 min)

**Abertura da sala online (2 min).** Cole o link da sala na descrição do encontro e
diga exatamente: *"Bom dia! Vou deixar a sala aberta nos próximos 90 minutos. Duas
regras simples: câmera ligada até eu avisar, e para falar, mão levantada ou reação no
chat. Hoje a gente vai transformar um problema **real de São Pedro** em um fluxograma.
Isso é o que programadores fazem antes de escrever uma linha de código."*

**Quiz de recuperação (3 min).** Pergunta de boca, sem nota: *"O que um computador faz
quando ele lê um PDF? Me dá três passos."* Anote as respostas no quadro branco do
programa. Não corrija — anote. No fim da aula você volta.

**Demonstração ao vivo (5 min).** Compartilhe a tela. Abra o `Despertar Kids` — o app
de lista de tarefas do repositório `html-css-js-pratica/14_projeto_lista_tarefas/` — e
pergunte: *"Antes de alguém escrever o JavaScript desse botão 'remover', o que a pessoa
precisa decidir?"* Escreva no quadro, ao vivo, a decomposição:

```
PROBLEMA: "o botão remover precisa apagar a tarefa da lista"
├── 1. O item existe?        → se não, SAI
├── 2. O usuário tem certeza? → se não, PERGUNTA
├── 3. Qual item da lista?    → busca pelo identificador
├── 4. Remove da lista
├── 5. Atualiza o contador do rodapé
└── 6. Devolve a lista para a tela
```

Diga: *"Isso aqui é o seu fluxograma antes de virar código. Ninguém programa sem isso."*

#### Fase 2 — Exploração (20 min)

**Parte 1 — Os quatro pilares com caso local (8 min).** Escreva no quadro e use os
números reais de São Pedro/SP:

| Pilar | Aplicação em São Pedro/SP |
|---|---|
| Decomposição | A rede municipal tem **23 unidades de ensino** e ~**5.200 alunos**. "Controlar a escola" se quebra em: Presença, Matrícula, Merenda, Diário, Reparo |
| Padrão | **15 unidades funcionam em tempo integral**. O padrão é "almoço → aula → atividade" — dá para copiar a rotina |
| Abstração | Cada turma é uma **turma** (não 34 alunos com nome). Detalhe que não muda a regra: cor da parede |
| Algoritmo | Se a merenda não chegou até 10h → avisar a cozinha → pedir fornecedor |

**Parte 2 — Fluxograma: os símbolos e os becos sem saída (7 min).** Desenhe no quadro:

```
┌─────────────┐
│  Início     │  ← fluxograma começa aqui, sempre
└──────┬──────┘
       ▼
   ◇ <condição?> ──Não──▶ [caminho B]
       │ Sim
       ▼
  [processo]
       │
       ▼
   ◇ <outra?>
       │
       ▼
  ┌─────────────┐
  │    Fim      │
  └─────────────┘
```

Explique o ponto que os adolescentes mais erram: **o losango tem duas saídas**.
Escreva: *"Fluxograma sem o caminho 'não' é erro de raciocínio, não de desenho."*

**Parte 3 — Pseudocódigo: as 6 palavras que bastam (5 min).**

```
ALGORITMO ClassificarIdade
INICIO
    LEIA idade
    SE idade >= 60 ENTAO
        ESCREVA "Idoso — fila prioritária"
    SENAO SE idade >= 18 ENTAO
        ESCREVA "Adulto — fila normal"
    SENAO
        ESCREVA "Menor de 18 - precisa de responsavel"
    FIM SE
FIM
```

Diga: *"Pseudocódigo não é português solto. Tem estrutura: cabeçalho, INICIO, FIM,
INDENTAÇÃO. Indentação não é enfeite: é o que diz qual linha pertence a qual SE."*

**Pergunte à turma (2 min):** *"O pseudocódigo acima tem condição de término? É um laço?
Por quê?"* → Não é laço, logo não precisa de condição de término. Conecte com o B2.

#### Fase 3 — Mão na massa (35 min)

**Organização:** o professor abre **salas de breakout de 3 a 4 alunos**. Cada sala
cria o próprio repositório (ou clona o repositório-base da turma) e escolhe **1 processo
real** de São Pedro/SP.

Opções validadas (todas com dados públicos, sem dados pessoais):
- **Fila da lanchonete** — 3 turnos, merenda às 10h e 12h, 34 alunos por sala.
- **Plantão de reparos municipal** — relato → triagem → equipe → peça → execução.
- **Inscrição em oficina gratuita** — verificação de vaga, lista de espera, horário.
- **Biblioteca municipal** — empréstimo, devolução, multa, reserva.

**O que o professor faz enquanto circula:** ele entra em cada sala por ~2 minutos,
olha a tela do aluno e diz exatamente isto:

> *"Boa, o fluxograma está no caminho certo. Agora me mostra: onde está a decisão que
> pode dar errado? E onde está o 'não'? Se não tem 'não', o fluxograma está mentindo."*

Depois de circular, ele volta para a sala principal e faz **uma demonstração ao vivo**
de um pseudocódigo completo, escrevendo junto com a turma.

**Plano B (internet caiu):** o professor desliga o breakout e distribui o enunciado em
texto no chat; os alunos abrem o arquivo `.txt` do exercício correspondente já
baixado e escrevem o fluxograma à mão no caderno (`notas/`), transcrevendo depois.

**Exercícios do repositório (10 min dentro do breakout).** Cada aluno faz **2**:

| Origem | Arquivo | O que pratica |
|---|---|---|
| `pensamento_computacional/06_fluxogramas` | `exercicio_05_montar_fluxo.txt` | Montar o fluxo de um processo real |
| `pensamento_computacional/06_fluxogramas` | `exercicio_06_corrigir.txt` | Achar o erro de um fluxo dado |
| `pensamento_computacional/07_pseudocodigo` | `exercicio_05_lista_compras.txt` | Pseudocódigo com lista e laço |
| `pensamento_computacional/07_pseudocodigo` | `exercicio_06_programa_completo.txt` | Programa completo do enunciado ao pseudocódigo |
| `pensamento_computacional/04_abstracao` | `exercicio_06_niveis.txt` | Níveis de detalhe |

Regra da turma: **colar a "RESPOSTA ESPERADA" do repo no topo do arquivo** e comparar
com o que foi feito. Erro de interpretation? Anotar em `notas/erros-da-aula-01.md`.

**Atividade A — do processo ao papel (20 min).** Cada sala entrega **1 folha** com:
o fluxograma desenhado e o pseudocódigo escrito à mão, assinado pelo apelido de quem
desenhou.

**Atividade B — digitalizar (5 min).** Foto da folha (câmera do celular serve) →
`docs/fluxograma.md` e `docs/pseudocodigo.md` → **1 commit**: `docs: fluxograma e
pseudocódigo do <processo>`.

#### Fase 4 — Projeto (15 min)

**Desafio: "Seu fluxograma do projeto final".**

Cada aluno escolhe **1 processo do projeto que vai construir** (ainda pode ser uma ideia
solta — será fechado no B13) e escreve:

1. O **fluxograma** com pelo menos **3 decisões**, incluindo todos os caminhos "não".
2. O **pseudocódigo** correspondente, indentado, com `SE` / `SENAO` / `ENQUANTO`.
3. Uma seção `## Decisões de projeto` em `docs/decisoes.md` com **3 decisões** e o
   **motivo** de cada uma (formato: Data · Decisão · Motivo · Alternativa descartada).

**Critério de pronto:**
- [ ] O fluxograma tem **início e fim** desenhados
- [ ] **Toda decisão tem os dois caminhos** ("sim" e "não")
- [ ] O pseudocódigo está **indentado** e tem `INICIO`/`FIM`
- [ ] Tem **pelo menos 1 laço** (`ENQUANTO` ou `PARA`) com condição de término
- [ ] `docs/decisoes.md` com **3 decisões datadas e justificadas**
- [ ] **1 commit** com mensagem no formato Conventional Commits

#### Fase 5 — Mostra (10 min)

Duas salas abrem a tela e apresentam o fluxograma em **60 segundos** cada. A turma dá
**1 ponto forte** e **1 pergunta** (não sugestão — pergunta). O professor anota as
perguntas no quadro; as perguntas boas viram material do módulo B2.

Volte ao **quiz de recuperação** do começo: *"O que um computador faz quando lê um PDF?
Agora com três passos de verdade."*

### ⚠️ Erros comuns e como lê-los

| Erro | Como aparece | Como corrigir |
|---|---|---|
| **Fluxograma sem o caminho "não"** | Todos os losangos descem só para baixo | Regra do professor: "todo losango tem dois filhos". Desenhe o "não" ao lado |
| **Pseudocódigo sem indentação** | `SENAO` colado no `SE` | Indentação é semântica. Regra: `SE` abre um bloco, `FIM SE` fecha |
| **Decomposição vaga** | "Passo 1: resolver o problema" | Exigir que cada passo caiba em **1 tela**. Se não cabe, ainda não decompôs |
| **Abstração que generaliza demais** | "Cada aluno é uma entidade abstrata" | Abstração esconde o detalhe que **não muda a regra**, não o que é essencial |
| **Laço sem término** | `ENQUANTO VERDADEIRO` | Todo laço precisa de "quando parar". Se não há, é laço infinito |
| **Confundir padrão com cópia** | "Copiei o Visualg e pronto" | Padrão é reconhecer a **regularidade**, não o texto |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Fluxograma | 3 decisões com os dois caminhos, início e fim |
| Pseudocódigo | Indentado, com `INICIO`/`FIM`, 1 laço com término |
| `docs/decisoes.md` | 3 decisões datadas com motivo e alternativa descartada |
| 2 exercícios do repo | "RESPOSTA ESPERADA" conferida |
| Commits | 1 commit com mensagem no padrão |
| Participação | 1 apresentação na Fase 5 ou 1 pergunta feita |
| Pergunta de saída | "Por que o pseudocódigo precisa de indentação?" |

**Pergunta de escrita:**
> "Você vai escrever um programa que distribui senhas de almoço na lanchonete da
> escola, para 34 alunos e 3 turmas. Escreva, em pseudocódigo, o trecho que decide em
> qual fila cada aluno entra, tratando o caso do aluno sem senha cadastrada."
>
> **Resposta:** é preciso um `SE` que verifica se a senha existe **antes** de qualquer
> outra coisa, e cada `SE` precisa do caminho "não" escrito:
> ```
> SE aluno tem senha cadastrada ENTAO
>     SE matricula na turma A ENTAO
>         ESCREVA "senha liberada para turma A"
>     SENAO
>         ESCREVA "senha liberada para outra turma"
> FIM SE
> SENAO
>     ESCREVA "sem senha: encaminhar para a secretaria"
> FIM SE
> ```
> Repare que o caminho "não" do primeiro `SE` (aluno sem senha) é o que impede o
> programa de tentar ler uma senha inexistente. É o mesmo cuidado que um `if`/`else`
> bem escrito em Python.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `pensamento_computacional/02_decomposicao/` | Decomposição de problemas reais |
| `pensamento_computacional/03_reconhecimento_padroes/` | Regularidades e cálculo mental |
| `pensamento_computacional/05_pensamento_algoritmico/` | Sequências, laços e condições |
| `pensamento_computacional/08_logica_proposicional/` | E, OU, NÃO e se-então (base do B2) |
| `pensamento_computacional/09_sistema_binario/` | Bits, bytes e conversão (base do B9) |
| `laboratorio-tech-social/site/exercicios/pensamento-computacional.html` | Os pilares em formato interativo |
| `laboratorio-tech-social/site/exercicios/code-builder.html` | Montar lógica em blocos |
| `laboratorio-tech-social/site/exercicios/planilha.html` | Organizar passos em tabela |

### 🏠 Para casa

Escolher **2 processos reais** de São Pedro/SP e escrever o pseudocódigo de **um** deles.
Subir em `docs/pseudocodigo-alternativo.md`. Comentar no issue do repositório da turma
o processo escolhido e **por que** ele serve para o projeto final.

### 🔗 Próximo módulo

[B2 — Lógica e Algoritmos (Visualg → pseudocódigo)](#b2)

<a id="b2"></a>

## Módulo 2 — Lógica e Algoritmos (Visualg → pseudocódigo) (Aula 2)

**Duração:** 90 min · **Aula 2 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Escrever **8 algoritmos** em pseudocódigo no padrão do repositório `logica_programacao`,
   usando variáveis, condicionais, laços, vetores e funções.
2. **Traduzir** um pseudocódigo para o [Visualg 3.0](https://visualg3.com.br/) e executá-lo
   no interpretador, e depois **traduzir de volta** para pseudocódigo — as duas direções.
3. Reconhecer as **3 estruturas clássicas** (sequência, seleção, repetição) em qualquer código
   que encontrar pela frente.

**Objetivo secundário:** saber explicar a diferença entre **algoritmo** e **programa**.

**Entregável do módulo:** **8 pseudocódigos** (em `docs/algoritmos/`) + **2 programas
funcionando no Visualg**, mais **1 commit** por algoritmo e um `docs/algoritmos/INDICE.md`
que liste os 8 com uma linha de descrição cada.

### 📚 Fontes no repositório

`logica_programacao/` — **15 módulos × 80 exercícios** em `.txt`, com **"RESPOSTA ESPERADA"**:

| Módulo | Conteúdo | Nº de exercícios |
|---|---|---|
| `01_variaveis_e_tipos` | Declaração, tipos, hello world, média | 4 |
| `02_entrada_saida` | `LEIA`, `ESCREVA`, formatação | 4 |
| `03_operadores` | Aritméticos, comparação, lógicos | 5 |
| `04_condicionais` | `SE`, `SENAO`, `SE ... SENAO SE` | 6 |
| `05_lacos_repeticao` | `ENQUANTO`, `PARA`, fatorial, Fibonacci, primos | 7 |
| `06_vetores` | Vetor, índice, busca, ordenação manual | 6 |
| `07_matrizes` | Matriz, linhas e colunas | 5 |
| `08_strings` | Concatenação, comparação, manipulação | 6 |
| `09_procedimentos` | Procedimento vs função | 5 |
| `10_funcoes` | Parâmetros, retorno, escopo | 6 |
| `11_recursao` | Recursão, fatorial recursivo | 5 |
| `12_ordenacao` | Bolha, seleção, inserção | 5 |
| `13_busca` | Busca linear e binária | 5 |
| `14_introducao_a_dados` | Pilha, fila, lista de tarefas | 5 |
| `15_exercicios_desafio` | Jogo da velha, força, labirinto, sistema bancário | 6 |

**Complementos:**
`pensamento_computacional/07_pseudocodigo/` (6 exercícios) ·
`pensamento_computacional/08_logica_proposicional/` (6 exercícios) ·
`laboratorio-tech-social/site/exercicios/desafio-logica.html` ·
`laboratorio-tech-social/site/exercicios/code-builder.html` ·
`laboratorio-tech-social/site/exercicios/casa-inteligente.html` ·
`laboratorio-tech-social/site/exercicios/robo-labirinto.html` ·
`laboratorio-tech-social/site/trilhas/adolescentes/01-python.html`

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Algoritmo** | "Receita sem ingrediente: só o passo." |
| **Pseudocódigo** | "Português com disciplina de programa." |
| **Variável** | "Uma caixa com nome. O nome é o rótulo, o conteúdo muda." |
| **Condicional** | "SE é a única coisa que o computador faz que você não consegue." |
| **Laço** | "Repetir é caro de escrever e barato de executar." |
| **Vetor** | "Várias gavetas numeradas, do 0 ao fim." |
| **Função** | "Trecho com nome que devolve valor. Sem devolve, é procedimento." |
| **Depuração** | "Achar o primeiro pensamento errado, não o último sintoma." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Bom dia, Makers. Ontem você desenhou o caminho de um processo
real. Hoje você escreve esse caminho em uma linguagem que o computador entende quando
vira código. E vai ver o Visualg, que é o parquinho do Brasil para isso — roda no
Windows, é gratuito, e 90% dos algoritmos que vocês vão ver a vida inteira já existem
nesse formato."*

**Quiz de recuperação (3 min).** *"Me dá um algoritmo para escovar os dentes. Não vale
'escovar os dentes' — valem os passos."* Peça 5 passos. Anote no quadro. Compare com
o pseudocódigo do Módulo 1: o mesmo raciocínio, outra notação.

**Demonstração ao vivo (5 min).** Compartilhe a tela com o Visualg aberto. Escreva um
algoritmo de **média de notas com 3 notas e situação**:

```
Algoritmo "Média e Situação"
var
   n1, n2, n3, media : real
inicio
   leia(n1, n2, n3)
   media <- (n1 + n2 + n3) / 3
   se media >= 7 entao
      escreva("Aprovado")
   senao
      escreva("Reprovado")
   fimse
fimalgoritmo
```

Execute e mostre o resultado. Depois diga: *"Isso aqui, traduzido para Python, são 8
linhas. A estrutura é a mesma. Por isso a aula de hoje vale a pena."*

#### Fase 2 — Exploração (20 min)

**Parte 1 — As 3 estruturas clássicas (8 min).** Escreva no quadro:

| Estrutura | Pseudocódigo | Exemplo São Pedro/SP |
|---|---|---|
| **Sequência** | uma linha depois da outra | Pegar o cardápio → distribuir → devolver o cardápio |
| **Seleção** | `SE ... SENAO ... FIMSE` | Se a vaga do curso de робótica acabar → entrar na lista de espera |
| **Repetição** | `ENQUANTO ... FIMENQUANTO` / `PARA` | Enquanto não confirmarem a presença → mandar o lembrete |

Diga: *"Qualquer programa que existe no mundo é essas três, combinadas. Isso não é
poesia. É taxonomia — e taxonomia é o que permite reorganizar, classificar e
ensinar."*

**Parte 2 — Condicional com 3 caminhos (6 min).** Mostre o erro clássico e o acerto:

```text
SE media >= 9 ENTAO
   ESCREVA "A"
SENAO
   SE media >= 7 ENTAO
      ESCREVA "B"
   SENAO
      ESCREVA "C"
   FIMSE
FIMSE
```
```
SE media >= 9 ENTAO
   ESCREVA "A"
SENAO SE media >= 7 ENTAO
   ESCREVA "B"
SENAO
   ESCREVA "C"
FIMSE
```
Diga: *"Os dois funcionam. O segundo é mais curto e mais fácil de ler. Lê-se de cima para
baixo, como uma escada."*

**Parte 3 — Laço: `ENQUANTO` e `PARA` (6 min).** Escreva lado a lado o mesmo cálculo:

```
ENQUANTO i <= 10 faca
   ESCREVA(i)
   i <- i + 1
FIMENQUANTO
```
```
PARA i DE 1 ATE 10 PASSO 1 FACA
   ESCREVA(i)
FIMPARA
```

Diga: *"Se você sabe quantas vezes repete, use `PARA`. Se você não sabe, use `ENQUANTO`.
Usar `ENQUANTO` quando dá para usar `PARA` é o erro mais comum de iniciante."*

**Parte 4 — A regra de ouro (2 min).** *"Todo laço precisa de uma frase que diz quando
para. Se essa frase depende só do contador, o laço é finito. Se depende de uma entrada
humana, pode não parar nunca."*

#### Fase 3 — Mão na massa (35 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala escolhe
**8 exercícios** da lista abaixo e resolve **4 deles** na aula (os outros 4 são para casa).

| Origem | Exercício | Conceito |
|---|---|---|
| `logica_programacao/01_variaveis_e_tipos` | `exercicio_04_calculadora_media.txt` | Variáveis e média |
| `logica_programacao/03_operadores` | 1 exercício de operadores | Aritmética e comparação |
| `logica_programacao/04_condicionais` | 1 exercício de condicionais | `SE`/`SENAO` |
| `logica_programacao/05_lacos_repeticao` | `exercicio_03_soma_1_N.txt` | `ENQUANTO`/`PARA` |
| `logica_programacao/05_lacos_repeticao` | `exercicio_06_primos.txt` | Busca e condição composta |
| `logica_programacao/06_vetores` | 1 exercício de vetores | Vetor e índice |
| `logica_programacao/10_funcoes` | 1 exercício de funções | Função com retorno |
| `logica_programacao/15_exercicios_desafio` | `exercicio_04_forca.txt` | Jogo da forca em pseudocódigo |

**O que o professor diz enquanto circula:**

> *"Boa. Agora me mostra onde o seu laço para. Se você me mostrar a linha que diz 'quando
> parar', o seu laço está seguro. Se não tem essa linha, olha de novo — quase sempre
> faltou atualizar a variável de controle dentro do laço."*

**Visualg (10 min dentro do breakout).** Cada sala transcreve **2 dos pseudocódigos**
para o Visualg, roda e compara com a "RESPOSTA ESPERADA" do `.txt`.

> **Plano B (sem internet):** o Visualg é um programa **offline**. Se a internet caiu, o
> professor desliga o breakout, distribui o enunciado em texto no chat e os alunos
> escrevem o pseudocódigo à mão no `notas/`. O Visualg continua disponível, mas cada um
> faz no seu ritmo.

#### Fase 4 — Projeto (15 min)

**Desafio: "Algoritmos do bairro".**

Cada aluno escreve **4 algoritmos** que resolvam problemas **concretos de São Pedro/SP**,
usando estruturas diferentes:

1. **Sequência** — calcular o valor de uma compra no mercado do bairro (lista de 5
   itens, subtotal, desconto por PIX, total). Use valores fictícios.
2. **Seleção** — classificar o **IDHM 0,755** de São Pedro em faixas de "desenvolvimento"
   (baixo, médio, alto) e explicar a classificação.
3. **Repetição** — montar o **calendário de jogos do torneio** de 8 rodadas com a tabela
   de pontos (2 redes de 8 times, 15 pontos por vitória, 1 por empate).
4. **Função** — uma função `classifica_idade(idade)` que retorne `"criança"`,
   `"adolescente"`, `"adulto"` ou `"idoso"`, e que seja usada por **duas** partes do
   programa (isso é reuso de função, e é o que o professor verifica).

Salvar em `docs/algoritmos/01_...txt` … `04_...txt` e criar `docs/algoritmos/INDICE.md`
com a lista e uma linha de descrição de cada.

**Critério de pronto:**
- [ ] **8 pseudocódigos** no total (4 do breakout + 4 do projeto), cada um em arquivo próprio
- [ ] Cada arquivo começa com `ALGORITMO "nome"` e termina com `FIMALGITMO`
- [ ] **Indentação** correta (4 espaços ou tabulação, sempre a mesma)
- [ ] Todo laço tem **condição de término visível**
- [ ] Pelo menos **1 função** (procedimento com retorno) reutilizada **2 vezes**
- [ ] `docs/algoritmos/INDICE.md` com os 8 nomeados e descritos
- [ ] **8 commits** (1 por algoritmo) com mensagem no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Duas salas apresentam **2 algoritmos** cada, no quadro ou na tela. A turma responde:
*"Qual estrutura clássica esse algoritmo usa?"* Se alguém disser "sequência, seleção,
repetição" e acertar, ganha o ponto de participação.

### ⚠️ Erros comuns e como lê-los

| Erro | Como aparece | Como corrigir |
|---|---|---|
| **Laço infinito** | O Visualg roda e não para | Procure a **variável de controle** dentro do laço. Ela precisa ser atualizada |
| **`FIMSE` faltando** | O Visualg acusa erro na linha do `SENAO` | Conte os `SE` e os `FIMSE`. Estão desbalanceados |
| **Divisão que dá inteiro** | `(7 / 2)` resulta em `3` | Declare as variáveis como `real`, não `inteiro` |
| **`ENQUANTO` que deveria ser `PARA`** | Laço de 1000 voltas para contar até 10 | Se você sabe o número de repetições, use `PARA` |
| **Pseudocódigo sem `INICIO`/`FIM`** | O Visualg recusa colar | O Visualg exige o bloco completo. Pseudo-linguagem é só o miolo |
| **Vetor começando em 1 no Visualg e 0 no Python** | Resultado errado ao migrar | Anote: Visualg = 1..N, Python = 0..N-1. Isso **vai** derrubar o B3 |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| 8 pseudocódigos | 8 arquivos com a estrutura completa |
| Visualg | 2 programas rodando com saída igual à "RESPOSTA ESPERADA" |
| Função reutilizada | 1 função chamada 2 vezes |
| Índice | `INDICE.md` com 8 entradas |
| Commits | 8 commits, 1 por algoritmo |
| Participação | 1 apresentação ou 1 resposta na Fase 5 |
| Pergunta de saída | "Por que o Visualg numera o vetor de 1 e o Python de 0?" |

**Pergunta de escrita:**
> "No Visualg, você precisa somar 10 números lidos do usuário e mostrar o total.
> Escreva o pseudocódigo. Se o usuário digitar a letra 'a' em vez de número, o que o
> seu programa faz?"
>
> **Resposta:** o Visualg 3.0 **não** valida tipo automaticamente: o `leia` lê o que foi
> digitado e a soma pode gerar erro de conversão. A resposta esperada é reconhecer o
> limite da ferramenta e prever o tratamento:
> ```
> PARA i DE 1 ATE 10 FACA
>    LEIA(n)
>    SE n > 0 E n <= 100 ENTAO
>       soma <- soma + n
>    SENAO
>       ESCREVA("Valor inválido, ignorado")
>    FIMSE
> FIMPARA
> ```
> Em Python, a mesma proteção é `try/except ValueError` — assunto do módulo B3.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `logica_programacao/01_variaveis_e_tipos/` | 4 exercícios de base |
| `logica_programacao/05_lacos_repeticao/` | 7 exercícios, incluindo primos e Fibonacci |
| `logica_programacao/11_recursao/` | Recursão (a base do B3) |
| `logica_programacao/12_ordenacao/` | Ordenação manual (a base do B6) |
| `logica_programacao/13_busca/` | Busca linear e binária (a base do B6) |
| `logica_programacao/14_introducao_a_dados/` | Pilha, fila, lista de tarefas |
| `logica_programacao/15_exercicios_desafio/` | Desafios: forca, labirinto, sistema bancário |
| `laboratorio-tech-social/site/exercicios/robo-labirinto.html` | Labirinto com lógica de laço |
| `laboratorio-tech-social/site/exercicios/casa-inteligente.html` | Casa inteligente: sensores e decisões |

### 🏠 Para casa

Terminar os **8 algoritmos** (os 4 que faltam). Rodar **1** deles no Visualg e gravar
**1 print** da saída. Subir o print em `docs/algoritmos/print-visualg.png`.

### 🔗 Próximo módulo

[B3 — Python do Zero](#b3)

<a id="b3"></a>

## Módulo 3 — Python do Zero (Aula 3)

**Duração:** 90 min · **Aula 3 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Escrever e executar um programa Python com **entrada, saída, variável, condicional, laço,
   lista e função** — sem colar resposta pronta do Stack Overflow.
2. Ler um **trace** (execução passo a passo) de um programa de 15 linhas e prever a saída.
3. Ler a **"Resposta Esperada"** de um exercício do repositório e **autoavaliar** a própria solução.

**Objetivo secundário:** ler mensagens de erro do Python em inglês e sacar o que elas dizem.

**Entregável do módulo:** **5 scripts rodando** em `src/` (um de cada tema: variáveis,
entrada/saída, condicional, laço, função), a **Ficha de Estudante** completa, e
**5 commits**.

### 📚 Fontes no repositório

`python-do-zero/` — **15 módulos × 6 exercícios = 90 exercícios**, todos em `.txt` com
**"Resposta Esperada"**:

| Módulo | Conteúdo | Exemplos de arquivo verificados |
|---|---|---|
| `01_introducao` | Variáveis, tipos, nomes, primeiro programa | `exercicio_01_variaveis.txt`, `exercicio_04_primeiro_programa.txt` |
| `02_entrada_saida` | `input()`, `print()`, f-string | — |
| `03_operadores` | Aritméticos, comparação, lógicos, `**`, `+=` | — |
| `04_condicionais` | `if`, `elif`, `else`, ternário | — |
| `05_repeticoes` | `for`, `range`, `while`, `break`, `continue` | `exercicio_01_for_basico.txt`, `exercicio_02_while_basico.txt`, `exercicio_03_break_continue.txt` |
| `06_listas` | Criar, acessar, percorrer, `append`, fatiamento | `exercicio_04_comprehension.txt`, `exercicio_06_desafio_estoque.txt` |
| `07_tuplas_dicionarios` | Tupla, dicionário, `.get()`, chave/valor | — |
| `08_funcoes` | `def`, parâmetros, retorno, escopo, padrão | `exercicio_01_def_retorno.txt`, `exercicio_05_escopo.txt` |
| `09_strings` | Fatiamento, `upper`, `split`, `replace`, `join` | `exercicio_02_split_join.txt`, `exyncio_05_format.txt` |
| `10_arquivos` | Abrir, ler, escrever, `with`, CSV | `exercicio_04_with.txt`, `exercicio_05_csv.txt` |
| `11_tratamento_erros` | `try/except/finally`, `raise` | `exercicio_01_try_except.txt`, `exercicio_05_entrada_segura.txt` |
| `12_modulos` | `import`, `from`, biblioteca padrão | — |
| `13_programacao_orientada_objetos` | Classes, `__init__`, herança | `exercicio_01_classe_objeto.txt`, `exercicio_06_desafio_banco_poo.txt` |
| `14_projetos_praticos` | 6 projetos completos | `exercicio_03_jogo_da_velha.txt`, `exercicio_04_agenda.txt` |
| `15_api_e_json` | JSON, `requests`, consumo de API | `exercicio_04_api_consumo.txt` |

**Complementos:**
`laboratorio-tech-social/site/trilhas/adolescentes/01-python.html` ·
`laboratorio-tech-social/materiais/slides/aula-teens-01-python.html` ·
`laboratorio-tech-social/site/exercicios/desafios-python.html` ·
`laboratorio-tech-social/site/exercicios/flashcards.html` ·
`lista-de-exercicios-python-brasil/` — 112 exercícios com **doctests** ·
`python-do-zero/14_projetos_praticos/exercicio_06_sistema_notas.txt` (base da Ficha de Estudante)

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Variável** | "Uma caixa com nome dentro. O nome é o rótulo, o conteúdo muda." |
| **Tipo** | "Python descobre o tipo sozinho. Você não declara." |
| **Indentação** | "Em Python, espaço no começo da linha **é sintaxe**." |
| **`input()` sempre devolve texto** | "Sempre. Sempre. Sempre. Precisa converter." |
| **f-string** | "`f\"Olá {nome}\"` — o jeito moderno de juntar texto." |
| **Lista vs Dicionário** | "Lista = gavetas numeradas. Dicionário = gavetas com etiqueta." |
| **Função** | "Uma caixa que recebe, faz, devolve. Sem devolução, é procedimento." |
| **`with`** | "Abre, usa e fecha sozinho. Mesmo se der erro." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Bom dia, Makers. Ontem foi lógica no papel. Hoje é lógica
funcionando. Python é a linguagem mais usada no mundo por quem faz automação, dados e
IA — e é a que mais aparece no mercado de trabalho da região de Piracicaba. E ela roda
no navegador, sem instalar nada."*

**Quiz de recuperação (3 min).** *"Me dá 3 estruturas de controle."* — sequência,
seleção, repetição. *"Agora me dá um pseudocódigo que some de 1 a 10."* — use a resposta
do quadro do módulo anterior.

**Demonstração ao vivo (5 min).** Compartilhe a tela com o
[Google Colab](https://colab.research.google.com/) aberto. Digite **com erros de
propósito**:

```python
print("Olá" nome)
```

A turma vê o `SyntaxError`. Pergunte: *"O que ele está reclamando?"* Explique: em
Python, `(` precisa fechar. O erro de digitação **é** o erro de sintaxe.

Depois:

```python
idade = input("Idade: ")
print(idade + 1)
```

`TypeError: can only concatenate str (not "int") to str`.

Diga: *"Erro em Python não é um problema. É o Python te mostrando onde está o problema.
Traduzir a mensagem é 80% do trabalho de programador."*

#### Fase 2 — Exploração (15 min)

**Parte 1 — A anatomia de um programa (7 min).** Escreva no quadro e peça para a turma
identificar as 8 partes:

```python
# 1. comentário
nome = input("Como você se chama? ")            # 2. entrada
notas = []                                        # 3. lista
for i in range(3):                                # 4. laço
    notas.append(float(input(f"Nota {i + 1}: ")))  # 5. entrada dentro do laço
media = sum(notas) / len(notas)                    # 6. cálculo
if media >= 7:                                    # 7. condicional
    situacao = "aprovado"
else:
    situacao = "reprovado"
print(f"{nome}: média {media:.2f} - {situacao}")  # 8. saída com f-string
```

Pergunte: *"Qual linha precisa de indentação?"* / *"Onde está o `input`?"* /
*"O que o `:.2f` faz?"* (duas casas decimais).

**Parte 2 — Lista vs Dicionário (5 min).**

```python
# LISTA: índice numérico
alunos = ["Ana", "Bruno", "Carla"]
print(alunos[0])               # Ana

# DICIONÁRIO: chave -> valor
notas = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.5}
print(notas["Ana"])             # 8.5
print(notas.get("Dani", 0))     # 0  <- .get() não quebra se não existe
```

Pergunta: *"Qual você usaria para uma lista de presença? E para o cadastro de cada aluno?"*

**Parte 3 — Lendo erro (3 min).** Mostre 4 erros típicos:

| Erro | Significado | O que fazer |
|---|---|---|
| `SyntaxError` | Faltou `:` ou parêntese, ou indentação errada | Releia a linha do traceback |
| `NameError: name 'x' is not defined` | Você usou `x` antes de criar | Verifique a ordem das linhas |
| `TypeError` | Tipo errado (texto com número) | `int()`, `float()`, `str()` |
| `IndentationError` | Espaço faltando ou sobrando | Regra: 4 espaços |

> **Método do repo `ingles-para-programadores/08_comandos_ingles/`:** leia a mensagem como
> uma frase — "cannot convert str to float" quer dizer "não consegui converter texto em
> número". Esta é a aula que separa quem desiste da documentação da quem usa.

#### Fase 3 — Mão na massa (40 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Ideal: **1 computador
por 2 alunos** — um digita, o outro dita e confere. Se só houver 1 computador por 4,
use o papel: um escreve o pseudocódigo (do Módulo 2), o outro vira o "digitador".

**Atividade A — Do módulo 01 ao 05 (25 min dentro do breakout).** Cada aluno faz
**5 exercícios** de `python-do-zero`, 1 de cada módulo:

| Módulo | Exercício sugerido | Como achar |
|---|---|---|
| `01_introducao` | Primeiro programa | `01_introducao/exercicio_04_primeiro_programa.txt` |
| `02_entrada_saida` | Formatar saída com f-string | `02_entrada_saida/` |
| `03_operadores` | Calcular IMC | `03_operadores/exercicio_05_calculo_imc.txt` |
| `04_condicionais` | Classificar por faixa de idade | `04_condicionais/` |
| `05_repeticoes` | Somar de 1 a N com `for` e depois com `while` | `05_repeticoes/exercicio_01_for_basico.txt` e `exercicio_02_while_basico.txt` |

**Regra da turma:** para cada exercício, o aluno **cola a "Resposta Esperada" do repo**
no começo do arquivo e compara com a saída real.

**Atividade B — Funções (10 min).** Do módulo `08_funcoes`, implemente:

```python
def media(notas):
    return sum(notas) / len(notas)


def classificacao(m):
    if m >= 9:
        return "A"
    elif m >= 7:
        return "B"
    elif m >= 5:
        return "C"
    else:
        return "D"


alunos = {"Ana": [8, 9, 10], "Bruno": [5, 6, 4], "Carla": [10, 10, 9]}
for nome, notas in alunos.items():
    print(f"{nome}: {media(notas):.1f} - {classificacao(media(notas))}")
```

Pergunta: *"Por que `classificacao` recebe um número e não a lista?"* → **função pura**,
testável. Guarde essa resposta: ela vira teste no módulo B8.

**O que o professor diz enquanto circula:**

> *"Me mostra o resultado. Agora me mostra a Resposta Esperada que você colou no topo.
> Bateu? Se não bateu, antes de mudar o código, me diz: qual das duas está certa — a
> minha saída ou a esperada? Essa pergunta vale mais que o programa."*

**Plano B (internet caiu):** o professor desliga o breakout e distribui no chat o
**enunciado + a "Resposta Esperada"** de 5 exercícios. Os alunos escrevem o código à
mão no `notas/` (ou no bloco de notas do celular) e o professor corrige junto, por
comentário no chat. Ninguém fica parado esperando a internet voltar.

#### Fase 4 — Projeto (15 min)

**Desafio: "Sua ficha de estudante".**

Escreva um programa (`src/ficha_estudante.py`) que:
1. Peça nome, idade, 3 notas e 1 cidade.
2. Valide cada entrada (idade entre 0 e 120, nota entre 0 e 10) **usando uma função**
   que devolve `True`/`False`.
3. Calcule a média com **f-string** formatado.
4. Salve os dados em uma **lista de dicionários**.
5. No final, mostre todos os cadastros em **tabela** (com `f"{:<20}"` para alinhar).

**Critério de pronto:**
- [ ] Usa **função** para a validação (não repete o `if` 4 vezes)
- [ ] Usa **f-string** em toda saída
- [ ] Guarda em **lista de dicionários**
- [ ] **Nenhum** erro ao rodar com entradas inválidas
- [ ] Entrada inválida **não quebra** o programa (repete a pergunta)
- [ ] **5 commits** (1 por script do breakout + 1 da ficha), mensagens no padrão

#### Fase 5 — Mostra (10 min)

2 alunos rodam seu programa ao vivo. Um deles **digita uma entrada inválida de propósito**
para mostrar que o programa pede a entrada de novo. A turma vê a robustez — e o professor
explica: *"Isso é teste. Vocês acabaram de fazer QA sem perceber. No módulo B8 a gente
faz isso com um roteiro escrito."*

### ⚠️ Erros comuns e como lê-los

| Erro | Mensagem | Como ler / corrigir |
|---|---|---|
| **Falta de parêntese** | `SyntaxError: '(' was never closed` | A mensagem diz **qual** parêntese. Olhe a linha que ela aponta |
| **Texto com número** | `TypeError: can only concatenate str (not "int") to str` | "`input()` devolve texto". Converta com `int()` ou `float()` |
| **Variável não criada** | `NameError: name 'media' is not defined` | Usei antes de criar? Verifique a **ordem** das linhas |
| **Espaço errado** | `IndentationError: expected an indented block` | Regra do professor: **4 espaços**, nunca tabulação, nunca misturar |
| **Lista indexada errado** | `IndexError: list index out of range` | A lista vai de 0 até `len(lista) - 1`. `notas[3]` numa lista de 3 não existe |
| **Divisão por zero** | `ZeroDivisionError: division by zero` | Lista vazia. `sum(notas) / len(notas)` com `notas = []` → sempre proteja |
| **Chave que não existe** | `KeyError: 'Dani'` | Use `dic.get("Dani", 0)` quando a chave puder faltar |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| 5 exercícios do repo | "Resposta Esperada" coincide com a saída real |
| Funções | 2 funções implementadas e usadas |
| Ficha de estudante | 6 critérios do "pronto" |
| Leitura de erro | 3 erros explicados corretamente (quiz rápido) |
| Commits | 5 commits, 1 por script |
| Participação | Demonstração ao vivo ou pergunta na Fase 5 |
| Pergunta de saída | "O que `input()` devolve e por que `idade + 1` quebra?" |

**Quiz rápido (5 min, oral, dentro da Fase 5):**
1. `input()` devolve que tipo? → `str` (sempre)
2. Como descubro o tipo de uma variável? → `type(x)`
3. O que faz `//`? → Divisão inteira
4. O que é indentação? → Bloco de código; em Python é sintaxe (4 espaços)
5. `notas[0]` se `notas` está vazio? → `IndexError`

**Pergunta de escrita:**
> "O programa abaixo funciona em 3 das 4 primeiras linhas e quebra na quinta. Leia o
> traceback e escreva a causa e a correção:
> ```python
> idade = input('Idade: ')
> peso = input('Peso: ')
> imc = peso / (idade * idade)
> print(f'IMC: {imc:.1f}')
> ```
> Onde está o erro?"
>
> **Resposta:** a causa é o **tipo**. `input()` devolve texto (`str`), então
> `idade * idade` não é multiplicação — é repetição de string (`"15" * "15"`), que
> nem chega a ser válida em Python 3, e mesmo que fosse, o resultado seria um texto
> gigante, não 225. A correção é converter na entrada:
> ```python
> idade = int(input('Idade: '))
> peso = float(input('Peso: '))
> ```
> E, se quiser ser robusto (é o que a aula mostra na Fase 3):
> ```python
> try:
>     idade = int(input('Idade: '))
> except ValueError:
>     print('Digite um número inteiro.')
> ```
> Esse `ValueError` é literalmente o que o traceback diria.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `python-do-zero/06_listas/` | Fatiamento e comprehensions |
| `python-do-zero/07_tuplas_dicionarios/` | Dicionários aninhados |
| `python-do-zero/09_strings/` | Limpeza de texto (base do projeto de dados) |
| `python-do-zero/10_arquivos/` | Ler/escrever CSV (base do projeto final) |
| `python-do-zero/11_tratamento_erros/` | `try/except` (obrigatório no projeto final) |
| `python-do-zero/13_programacao_orientada_objetos/` | Classes e herança (base do B6 e do B14) |
| `python-do-zero/14_projetos_praticos/` | 6 projetos prontos para adaptar |
| `python-do-zero/15_api_e_json/` | Consumo de API (base do bot de notícias) |
| `lista-de-exercicios-python-brasil/` | 112 exercícios com doctest — banco de exercícios |
| `laboratorio-tech-social/site/exercicios/desafios-python.html` | Exercícios rodando no navegador |

### 🏠 Para casa

Refazer a Ficha de Estudante **em VS Code** (não no Colab), colocar em `src/`, com
`src/ficha_estudante.py` e um `README.md` na raiz do repositório explicando como rodar.
**Ainda não precisa subir para o GitHub** — isso vem no módulo B7. Faça 1 commit.

### 🔗 Próximo módulo

[B4 — Python: Projetos Práticos](#b4)

<a id="b4"></a>

## Módulo 4 — Python: Projetos Práticos (Aula 4)

**Duração:** 90 min · **Aula 4 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Entregar **1 programa de linha de comando (CLI) interativo**, com menu, laço principal e
   tratamento de entrada inválida.
2. Entregar **1 script de automação** que lê dados de um arquivo e gera um relatório.
3. Organizar o código em **funções**, com **docstring** em cada uma, e ler os dados de
   um **CSV** com o módulo `csv` da biblioteca padrão.

**Objetivo secundário:** entender por que "programar" é 30% escrever código e 70% ler
código existente com calma.

**Entregável do módulo:** **2 programas completos** em `src/` (`<nome>_cli.py` e
`<nome>_automacao.py`), com `README.md` da pasta `src/` explicando como rodar cada um,
mais **1 commit por programa** e **1 `data/` com CSV fictício**.

### 📚 Fontes no repositório

`python-do-zero/14_projetos_praticos/` — **6 projetos completos**, com enunciado e
**"Resposta Esperada"**:

| Arquivo | Projeto |
|---|---|
| `exercicio_01_calculadora.txt` | Calculadora |
| `exercicio_02_conversor.txt` | Conversor de unidades |
| `exercicio_03_jogo_da_velha.txt` | Jogo da velha |
| `exercicio_04_agenda.txt` | Agenda de contatos |
| `exercicio_05_quiz.txt` | Quiz de perguntas |
| `exercicio_06_sistema_notas.txt` | Sistema de notas |

**Banco de exercícios (112 com doctests):** `lista-de-exercicios-python-brasil/` —
6 seções: `secao_01_estrutura_sequencial` · `secao_02_estrutura_de_decisao` ·
`secao_03_estrutura_de_repeticao` · `secao_04_exercicios_lista` ·
`secao_05_exercicios_funcoes` · `secao_06_exercicios_strings`.

**Módulos de apoio:**
`python-do-zero/10_arquivos/` (CSV e `with`) ·
`python-do-zero/13_programacao_orientada_objetos/` (classes) ·
`python-do-zero/15_api_e_json/` (JSON e API) ·
`python-do-zero/11_tratamento_erros/` (robustez).

**Projetos reais do autor (referência de nível):**
`Calculadora/app.py` + `Calculadora/templates/calculator.html` + `Calculadora/templates/resultado.html` ·
`jogo_da_velha/jogo_da_velha.py` ·
`o_acolito/acolyte_adventure.py` (jogo de aventura narrativo) ·
`anyms/` (IndexedDB, 17 tabelas, custo médio ponderado) ·
`Central-de-noticias/scripts/gerar.py` (gerador de RSS com `pytest.ini` e `tests/test_gerar.py`).

**Trilha web e slides:**
`laboratorio-tech-social/site/exercicios/desafios-python.html` ·
`laboratorio-tech-social/site/exercicios/gerador-dados.html` ·
`laboratorio-tech-social/materiais/slides/aula-teens-04-dados.html` ·
`laboratorio-tech-social/site/trilhas/adolescentes/04-dados.html`

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **CLI** | "Programa que conversa pelo teclado. É o programa mais fácil de automatizar." |
| **Menu / laço principal** | "Enquanto o usuário não disser 'sair', o programa pergunta de novo." |
| **Função pura** | "Recebe dados, devolve resultado. Não mexe no mundo. Dá para testar." |
| **Docstring** | "A primeira linha depois de `def` explica o que a função faz. É o contrato." |
| **CSV** | "Tabela em arquivo de texto. Separador vírgula. É o formato mais universal que existe." |
| **`with open(...)`** | "Abre, lê, fecha. Mesmo se o código explodir no meio." |
| **Idempotência** | "Rodar duas vezes não muda nada. É o que diferencia script de gambiarra." |
| **`if __name__ == "__main__"`** | "O ponto de partida. Deixa o arquivo ser importado sem rodar nada." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (5 min)

**Abertura (1 min).** *"Mesa dois: vocês já sabem a sintaxe. Hoje vão construir
**programas**, não scripts soltos. A diferença é a mesma que existe entre um post e um
jornal: estrutura, seções e um ponto de partida claro."*

**Demonstração ao vivo (4 min).** Compartilhe a tela. Abra o `Calculadora/app.py` do
repositório do autor e rode. Depois mostre o `jogo_da_velha/jogo_da_velha.py`. Diga:

> *"Olha a diferença: o código do jogo tem funções com nome, tem docstring, tem um
> `if __name__ == '__main__'` no final. Isso não é enfeite. É o que faz o programa crescer
> sem virar bagunça. Hoje o تسليم é isso: código que dá para manter."*

**Quiz de recuperação (1 min).** *"Qual a diferença entre `input()` e uma função sua?"*
→ `input()` lê do mundo; sua função recebe e devolve.

#### Fase 2 — Exploração (10 min)

**Parte 1 — A anatomia de um CLI (5 min).** Escreva no quadro:

```python
"""Calculadora deprovas de São Pedro — exemplo da estrutura de um CLI."""


def somar(a: float, b: float) -> float:
    """Soma dois números e devolve o resultado."""
    return a + b


def main() -> None:
    """Laço principal: pergunta, executa, repete até o usuário sair."""
    while True:
        print("\n1) Somar  2) Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            try:
                x = float(input("Primeiro número: "))
                y = float(input("Segundo número: "))
            except ValueError:
                print("Entrada inválida. Tente de novo.")
                continue
            print(f"Resultado: {somar(x, y):.2f}")
        elif opcao == "2":
            print("Até mais!")
            break
        else:
            print("Opção desconhecida.")


if __name__ == "__main__":
    main()
```

Aponte as 4 peças: **docstring do módulo**, **funções com anotação de tipo**,
**laço principal com `break`**, **`if __name__ == "__main__"`**.

Diga: *"Repare no `continue` depois do `except`. Sem ele, o programa cairia no
`somar(x, y)` com `x` inexistente. Esse é o detalhe que separa programa de toy."*

**Parte 2 — CSV: ler dados de verdade (5 min).** Mostre `data/` da turma:

```csv
bairro,quantidade_rua,status
Centro,12,iluminada
Jardim Aurora,7,sem_iluminacao
Vila Industrial,19,parcial
```

```python
import csv
from pathlib import Path


def carregar_ruas(caminho: str) -> list[dict]:
    """Lê o CSV de ruas e devolve uma lista de dicionários."""
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def total_sem_iluminacao(ruas: list[dict]) -> int:
    """Conta quantas ruas estão sem iluminação."""
    return sum(1 for r in ruas if r["status"] == "sem_iluminacao")
```

Diga: *"Reparem que o nome da coluna tem acentos e sublinhado, e funciona. Use `utf-8`
sempre. E reparem que a função `total_sem_iluminacao` **não sabe de onde veio a lista**.
Ela é pura. Amanhã, no módulo de QA, isso vira teste unitário."*

#### Fase 3 — Mão na massa (40 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala escolhe
**um projeto entre as sugestões** (ou um dos 6 do repo):

| Sugestão da turma | Base |
|---|---|
| **Placar da Cidade** — placar de torneios de São Pedro | `python-do-zero/14_projetos_praticos/exercicio_06_sistema_notas.txt` adaptado |
| **Lista de Espera de Oficina Gratuita** — vagas, lista de espera, ordem | `python-do-zero/14_projetos_praticos/exercicio_04_agenda.txt` adaptado |
| **Quiz de Conhecimentos de São Pedro** — 10 perguntas, pontuação | `python-do-zero/14_projetos_praticos/exercicio_05_quiz.txt` |
| **Controle de Merenda** — cardápio, presença, mediação | `14_projetos_praticos/exercicio_06_sistema_notas.txt` |

**Atividade A — O CLI (25 min dentro do breakout).** Requisitos obrigatórios:

1. Menu com **pelo menos 3 opções** e uma opção de **sair**.
2. Laço principal (`while True`) com `break` na saída.
3. **Toda entrada numérica protegida** com `try/except ValueError`.
4. **Nenhuma função** maior que 20 linhas.
5. **Docstring** em todas as funções.
6. `if __name__ == "__main__":` no final.

**Atividade B — O script de automação (15 min dentro do breakout).** Lê um **CSV de
`data/`** e escreve um **relatório `.txt`** ou `.md`. Sugestões de CSV fictício:
- Ruas sem iluminação (exemplo acima).
- Pontuação dos times do torneio.
- Turmas da EJA e número de alunos.
- Aulas gratuitas do bairro (base do projeto "Aulas Abertas").

Requisito extra: o script **não pode escrever em cima do CSV de entrada**.

**O que o professor diz enquanto circula:**

> *"Me mostra a função mais comprida do seu arquivo. Mais de 20 linhas? Corta. Agora
> me mostra o que acontece se o usuário digitar uma letra onde o programa espera número.
> Se o programa morre, o problema é seu, não do usuário."*

**Plano B (internet caiu):** o professor desliga o breakout e entrega o enunciado em
texto no chat. Os alunos escrevem a **estrutura** do CLI (menu + laço + 3 funções) à
mão no `notas/`, e transcrevem depois. O CSV e o `data/` já estão no repositório
clonado, então a automação continua funcionando offline.

#### Fase 4 — Projeto (25 min)

**Desafio: "Ferramenta do projeto final".**

Cada aluno escolhe **1 das 5 sugestões de capstone** (Placar da Cidade, Despertar Kids,
Estação Clima, Aulas Abertas, Bot de Notícias do Bairro) e escreve:

1. **Um CLI** que resolva **um** fluxo real do seu projeto (ex.: registrar resultado
   de jogo; cadastrar criança em oficina; registrar leitura de sensor; publicar aula).
2. **Um script de automação** que leia um CSV de `data/` e gere um relatório.
3. Um **`data/dados_exemplo.csv`** com **8 a 12 linhas fictícias**.
4. **`src/README.md`** explicando como rodar os dois programas (comando exato).

**Critério de pronto:**
- [ ] CLI com **menu ≥ 3 opções** + opção de sair
- [ ] Laço principal com `break` e **entradas protegidas** com `try/except`
- [ ] **Toda função com docstring** e ≤ 20 linhas
- [ ] `if __name__ == "__main__":` presente
- [ ] Script de automação lê **CSV** de `data/` e escreve relatório
- [ ] `data/` **sem dados pessoais reais**
- [ ] `src/README.md` com o **comando exato** de execução de cada programa
- [ ] **2 commits** com mensagens no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

2 salas rodam seus CLIs ao vivo. **Uma sala erra de propósito** (digita letra onde
espera número) para mostrar o tratamento de erro. A turma dá 1 ponto forte e 1 sugestão
escrita no issue do repositório da turma.

### ⚠️ Erros comuns e como lê-los

| Erro | Mensagem / sinal | Como corrigir |
|---|---|---|
| **`NameError` ao usar `x` depois do `except`** | `NameError: name 'x' is not defined` | No `except`, use `continue` para voltar ao menu, ou `else` do `try` |
| **CSV com `\r\n` do Windows** | Coluna com nome `bairro\r` | Abra com `newline=""` **e** `encoding="utf-8"` |
| **Programa reescreve o CSV de entrada** | Arquivo zerado depois da 2ª execução | Leia para uma **lista** primeiro; escreva em **outro** arquivo |
| **Função de 60 linhas** | Não dá para testar | Quebre em 2 ou 3 funções com nome |
| **Loop infinito travando a aula** | O programa não volta ao menu | Todo caminho dentro do `while` precisa de `continue` ou `break` |
| **F-string com aspas erradas** | `SyntaxError: f-string: unmatched '['` | Dentro da f-string, use aspas simples por fora: `f"{d['chave']}"` |
| **CSV com vírgula no texto** | Coluna quebrada | Use `;` como separador ou coloque o texto entre aspas no CSV |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| CLI | 6 critérios do "pronto" |
| Script de automação | Lê CSV e gera relatório; não destrói a entrada |
| `data/` | 8–12 linhas fictícias, zero dados pessoais |
| `src/README.md` | Comando exato de execução dos 2 programas |
| Commits | 2 commits, mensagens no padrão |
| Participação | Apresentação ao vivo ou sugestão escrita no issue |
| Pergunta de saída | "Por que a função `total_sem_iluminacao` não recebe o caminho do arquivo?" |

**Pergunta de escrita:**
> "Seu CLI tem um menu. O usuário digita `9`, que não existe no menu. O que o programa
> deve fazer — e o que acontece se você simplesmente não tratar esse caso?"
>
> **Resposta:** o programa **deve** avisar ("Opção desconhecida") e voltar ao menu,
> porque entrada inválida é evento normal, não exceção. Se você não tratar, o
> `if/elif` cai no `else` e o programa **sai do laço** — ou, pior, se não houver
> `else`, ele simplesmente não faz nada e volta ao topo. Em ambos os casos o comportamento
> está errado ou indefinido. O padrão correto é:
> ```python
> else:
>     print("Opção desconhecida. Escolha 1, 2 ou 3.")
> ```
> O mesmo princípio vale no Python: **`else` é o caminho "não" que nunca pode faltar**
> — exatamente como no fluxograma do módulo B1.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `python-do-zero/14_projetos_praticos/` | Os 6 projetos-base do módulo |
| `python-do-zero/10_arquivos/exercicio_05_csv.txt` | CSV na prática |
| `python-do-zero/12_modulos/` | `import`, `from`, biblioteca padrão |
| `python-do-zero/13_programacao_orientada_objetos/exercicio_06_desafio_banco_poo.txt` | POO com classes (base do B6/B14) |
| `lista-de-exercicios-python-brasil/secao_05_exercicios_funcoes/` | 112 exercícios com doctests |
| `lista-de-exercicios-python-brasil/secao_06_exercicios_strings/` | Manipulação de texto |
| `Calculadora/app.py` | CLI + interface web do mesmo projeto |
| `jogo_da_velha/jogo_da_velha.py` | Projeto real completo em um arquivo |
| `o_acolito/acolyte_adventure.py` | Jogo narrativo com menu |
| `Central-de-noticias/scripts/gerar.py` | Script real de geração com testes (`tests/test_gerar.py`) |

### 🏠 Para casa

Refinar o CLI: **3 opções → 5 opções**, com validação de entrada em todas. Escrever o
`README.md` da raiz do repositório com: o que o programa faz, como rodar, um exemplo de
saída real (copiado do terminal) e o que **não** faz. **1 commit.**

### 🔗 Próximo módulo

[B5 — Web: HTML, CSS e JavaScript](#b5)

<a id="b5"></a>

## Módulo 5 — Web: HTML, CSS e JavaScript (Aula 5)

**Duração:** 90 min · **Aula 5 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Construir uma página **semântica** (`header`, `nav`, `main`, `section`, `footer`) com
   **CSS de layout** (`Flexbox` e `Grid`) e **JavaScript de DOM**.
2. Escrever um **formulário com validação** em HTML e validar também em JS.
3. Consumir uma **API** com `fetch` e renderizar o resultado na tela.

**Objetivo secundário:** explicar a diferença entre HTML, CSS e JS em uma frase cada.

**Entregável do módulo:** **1 site responsivo de 3 páginas** (`index.html`, `sobre.html`,
`contato.html`) com CSS externo, 1 interação em JS e **0 erros no console**, mais
**1 commit por página** e `docs/decisoes.md` com 2 decisões de layout.

### 📚 Fontes no repositório

`html-css-js-pratica/` — **15 módulos × 6 exercícios = 90 exercícios**, cada um com
**"RESULTADO ESPERADO"** e código de exemplo:

| Módulo | Conteúdo |
|---|---|
| `01_html_basico` | Estrutura, tags, atributos, texto, imagens, links |
| `02_listas_e_tabelas` | `<ul>`, `<ol>`, `<li>`, `<table>`, `<thead>`, `<tbody>` |
| `03_css_fundamentos` | Seletores, cores, tipografia, box-model, margins, padding |
| `04_css_layout` | Display, position, Flexbox, Grid, responsividade |
| `05_css_avancado` | Pseudo-classes, `:hover`, `:focus`, transições, animações, variáveis |
| `06_html_formularios` | `<form>`, input, label, select, textarea, `required`, `pattern` |
| `07_javascript_basico` | Variáveis, tipos, operadores, funções, arrow functions |
| `08_javascript_dom` | `getElementById`, `querySelector`, criar/remover elementos |
| `09_javascript_events` | `addEventListener`, `click`, `submit`, `keydown`, delegação |
| `10_javascript_assincrono` | `fetch`, Promises, `async/await`, JSON, tratamento de erro |
| `11_bootstrap` | Grid, componentes, responsividade |
| `12_projeto_landing_page` | **Projeto: landing page** |
| `13_projeto_portfolio` | **Projeto: portfólio** |
| `14_projeto_lista_tarefas` | **Projeto: lista de tarefas** |
| `15_projeto_jogo_simples` | **Projeto: jogo simples** |

**Projetos reais do autor (mostram o nível profissional):**
`esporte-sao-pedro/` (Supabase + RLS + Edge Functions + IA + SEO, com `CNAME`,
`sitemap.xml`, `robots.txt`, `manifest.json` e `sw.js`) ·
`Central-de-noticias/` (PWA com `app.js`, `sw.js`, `manifest.webmanifest` e seção
"São Pedro e região") ·
`meu-treino/` (PWA com Wake Lock, GPS, Web Share, localStorage) ·
`anyms/` (IndexedDB, 17 tabelas) ·
`hubias-estudos/` (SQLite via WASM no navegador + flashcards + Pomodoro) ·
`portfolio/` (Webpack + API do GitHub + localStorage).

**Trilha web e slides:**
`laboratorio-tech-social/site/trilhas/adolescentes/02-web.html` ·
`laboratorio-tech-social/materiais/slides/aula-teens-02-web.html` ·
`laboratorio-tech-social/site/exercicios/criador-site.html` ·
`laboratorio-tech-social/site/exercicios/simulador-api.html` ·
`laboratorio-tech-social/site/exercicios/validador-regex.html` ·
`laboratorio-tech-social/site/exercicios/gerador-dados.html`

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **HTML** | "A **esqueleto**. A estrutura. O que existe." |
| **CSS** | "A **aparência**. Como cada coisa se apresenta." |
| **JavaScript** | "O **comportamento**. O que acontece quando..." |
| **DOM** | "A árvore de objetos que o navegador fez do seu HTML." |
| **Seletor CSS** | "Uma regra de 'ache quem' para estilizar." |
| **Box-model** | "Conteúdo + padding + borda + margem = o espaço que o elemento ocupa." |
| **Flexbox** | "1-dimensional: linha **ou** coluna." |
| **Grid** | "2-dimensional: linhas **e** colunas ao mesmo tempo." |
| **async/await** | "Pausa o código até a resposta chegar, sem travar a página." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Vocês usam o Instagram duas horas por dia. Ele é feito de HTML,
CSS e JavaScript. E a mesma coisa vale para o site da escola, o do banco e o da
prefeitura. A web é a linguagem mais registrada que existe."*
Não diga "não é possível". Diga: **"É a mesma base. A diferença é o tamanho e a disciplina."**

**Demonstração ao vivo (5 min).** Compartilhe a tela, abra o DevTools (F12) em qualquer
site e mostre:
- Aba **Elements** → o HTML (a árvore)
- Aba **Styles** → o CSS aplicado
- Aba **Console** → o JavaScript

Diga: *"Três abas, três linguagens. Todos os sites do mundo são isso."*

**Quiz de recuperação (3 min).** *"Qual linguagem cuida da **aparência**?"* →
CSS. *"E qual cuida do que **acontece**?"* → JavaScript. *"E o esqueleto?"* → HTML.
Pergunta extra: *"Por que a gente usa `<header>` e não só `<div>`?"* → semântica e
acessibilidade (o leitor de tela sabe o que é cabeçalho).

#### Fase 2 — Exploração (20 min)

**Parte 1 — Anatomia de uma página (8 min).**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Minha Página</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header><h1>Título</h1></header>
  <nav><a href="#">Link</a></nav>
  <main>
    <section>
      <h2>Seção</h2>
      <p>Texto</p>
      <form id="form">
        <label for="nome">Nome:</label>
        <input id="nome" type="text" required>
        <button type="submit">Enviar</button>
      </form>
    </section>
  </main>
  <footer><p>&copy; 2026 São Pedro/SP</p></footer>
  <script src="script.js"></script>
</body>
</html>
```

Explique por que `viewport` está no `<head>`: sem isso, o site aparece minúsculo no celular.
Em São Pedro/SP, boa parte dos alunos usa **só o celular** — isso não é detalhe
estético, é usabilidade real.

**Parte 2 — Box-model e Flexbox (7 min).** Desenhe no quadro:

```
        margem (margin)
     ┌──────────────────────┐
     │  borda (border)       │
     │  ┌────────────────┐  │
     │  │ padding        │  │
     │  │  ┌──────────┐  │  │
     │  │  │ conteúdo │  │  │
     │  │  └──────────┘  │  │
     │  └────────────────┘  │
     └──────────────────────┘
```

Flexbox em 1 linha:
```css
.container { display: flex; gap: 1rem; }
.card { flex: 1; padding: 1rem; border-radius: 8px; }
```

Grid em 1 linha:
```css
.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
```

**Parte 3 — DOM e eventos (5 min).**

```javascript
const botao = document.querySelector('#botao');
const saida = document.querySelector('#saida');

botao.addEventListener('click', () => {
  saida.textContent = 'Cliquei!';
});
```

**Parte 4 — `fetch` (0 min, só mostrar).**

```javascript
async function carregar() {
  const r = await fetch('https://api.exemplo.com/dados');
  if (!r.ok) throw new Error('HTTP ' + r.status);
  const dados = await r.json();
  console.log(dados);
}
```

#### Fase 3 — Mão na massa (35 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala monta a
**landing page do projeto que a turma vai entregar**.

**Atividade A — Landing page (25 min dentro do breakout).** Base:
`html-css-js-pratica/12_projeto_landing_page/`. Construa uma página de **1 seção** com:
- `header` com título e subtítulo
- `nav` com 3 links
- 3 `cards` em **Flexbox** (depois em **Grid**)
- 1 `form` de contato com `required` e `type="email"`
- 1 botão que **mostra uma mensagem** sem recarregar a página
  (`addEventListener` + `preventDefault`)

**Atividade B — 3 exercícios do repo (10 min dentro do breakout).** Escolha 3 entre
(veja a tabela de arquivos abaixo):

| Pasta | Conceito |
|---|---|
| `03_css_fundamentos` | box-model |
| `04_css_layout` | Flexbox e Grid |
| `06_html_formularios` | validação de formulário |
| `08_javascript_dom` | criar elementos |
| `09_javascript_events` | evento de `submit` |
| `10_javascript_assincrono` | `fetch` |

Cada um tem um **"RESULTADO ESPERADO"** no repo. Cole-o como comentário no código e
confirme que a página faz o que diz.

**O que o professor diz enquanto circula:**

> *"Abre o F12, aba Console, e me mostra. Se tiver um erro vermelho ali, seu critério de
> pronto não está atendido — mesmo que a página 'funcione'. Console limpo é
>requisito, não detalhe."*

**Plano B (internet caiu):** o professor desliga o breakout e entrega o HTML e o CSS
**prontos no chat** (em bloco de texto) para o aluno salvar e abrir. Sem CSS externo
carregado da internet, a página ainda renderiza. A atividade de JS passa a ser a
**digitação à mão** da função de `addEventListener` no `notas/`.

#### Fase 4 — Projeto (15 min)

**Desafio: "As 3 páginas do seu projeto".**

Monte o site do seu projeto de capstone (a ser fechado no B13) com **3 páginas**:
`index.html`, `sobre.html` e `contato.html`, e **1 CSS externo** (`style.css`).

- `index.html`: `header` com nome do projeto e slogan, `nav` com os 3 links, `main` com
  **3 cards** (os "pilares" do projeto) em **Grid**, `footer` com o crédito e o ano.
- `sobre.html`: o **problema real** que o projeto resolve, com **dados públicos de
  São Pedro/SP** (ex.: IDHM 0,755; 23 unidades de ensino; ~5.200 alunos; 29,9% de
  rendimento per capita até meio salário mínimo). **Cite a fonte do dado.**
- `contato.html`: 1 `form` com `label` + `input` + `required`, **validação em JS** e
  mensagem de sucesso **sem recarregar a página**.

**Critério de pronto:**
- [ ] HTML **semântico** (`header`, `nav`, `main`, `section`, `footer`)
- [ ] `viewport` no `<head>` e `lang="pt-BR"`
- [ ] Layout com **Flexbox ou Grid**
- [ ] **1 interação** com JS (formulário, botão ou menu)
- [ ] **0 erros no console** (F12 → Console)
- [ ] CSS em **arquivo externo** (não `<style>` dentro do HTML)
- [ ] `docs/decisoes.md` com **2 decisões de layout** datadas e justificadas
- [ ] **3 commits** (1 por página) no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Duas salas abrem a landing page no projetor (ou compartilham a tela). Cada turma dá
**1 ponto forte** e **1 sugestão**. O professor registra as sugestões no issue do
repositório da turma, e as duas melhores viram tarefa da aula B7.

### ⚠️ Erros comuns e como lê-los

| Erro | Como aparece no console | Como corrigir |
|---|---|---|
| **Tag não fechada** | O HTML "engole" a página: tudo vira um bloco | Use o formatador do VS Code (`Shift` + `Alt` + `F`) ou o botão "Format Document" |
| **`id` escrito diferente no HTML e no JS** | `Cannot read properties of null (reading 'addEventListener')` | O `querySelector('#id')` devolveu `null`. Confira letra por letra |
| **Faltou `await`** | A tela fica vazia e o console mostra `Promise {<pending>}` | `const dados = await fetch(...)` |
| **`.json()` sem `await`** | `dados` é uma Promise, não um objeto | `const dados = await r.json()` |
| **CSS não aplicado** | A página fica "crua" | `link` com caminho errado, ou o CSS está **depois** do `</body>` |
| **Flexbox que não cresce** | Cards grudados à esquerda | Faltou `flex: 1` ou `gap` no container |
| **Imagem quebrada** | ícone de imagem quebrada no DevTools | Caminho relativo errado ( `./img/x.png` vs `img/x.png`) |
| **Formulário recarrega a página** | A URL ganha `?` e a página volta ao topo | Faltou `event.preventDefault()` |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Site de 3 páginas | 7 critérios do "pronto" |
| 3 exercícios do repo | "RESULTADO ESPERADO" conferido |
| Console limpo | 0 erros no DevTools |
| Semanticidade | Aluno sabe dizer o que é `main` e por que existe |
| `docs/decisoes.md` | 2 decisões de layout datadas e justificadas |
| Commits | 3 commits, 1 por página |
| Participação | 1 sugestão na Fase 5 |
| Pergunta de saída | "O que o `preventDefault()` faz?" |

**Pergunta de escrita:**
> "Você tem um `<form>` que envia para o servidor. Ao clicar em enviar, a página recarrega
> e o texto digitado se perde. Como resolver sem recarregar?"
>
> **Resposta:** `event.preventDefault()` no handler do `submit` + manipulação local ou
> `fetch`:
> ```javascript
> form.addEventListener('submit', async (event) => {
>   event.preventDefault();
>   const dados = Object.fromEntries(new FormData(form));
>   // aqui você decide: guardar localmente ou enviar com fetch
>   saida.textContent = `Recebido, ${dados.nome}!`;
> });
> ```
> E o plano B honesto: se o servidor não é necessário (formulário de inscrição local,
> lista de espera, contato sem backend), **não envie para lugar nenhum** — salve no
> `localStorage` e mostre a confirmação na tela. É a mesma decisão que o projeto
> "Aulas Abertas" vai precisar tomar no módulo B13.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `html-css-js-pratica/05_css_avancado/` | Pseudo-classes, transições, variáveis CSS |
| `html-css-js-pratica/11_bootstrap/` | Bootstrap (grid e componentes) |
| `html-css-js-pratica/13_projeto_portfolio/` | Portfólio — o mais próximo do "portfólio do aluno" |
| `html-css-js-pratica/14_projeto_lista_tarefas/` | App de tarefas com filtros (base do "Despertar Kids") |
| `html-css-js-pratica/15_projeto_jogo_simples/` | Jogo simples (canvas ou DOM) |
| `esporte-sao-pedro/index.html` + `app.js` + `style.css` | App real da cidade, com SEO (`sitemap.xml`, `robots.txt`, `CNAME`) |
| `Central-de-noticias/index.html` + `app.js` + `sw.js` | PWA real com service worker e manifest |
| `meu-treino/` | PWA: Wake Lock, GPS, Web Share, localStorage |
| `anyms/` | Banco no navegador (IndexedDB) com 17 tabelas |
| `laboratorio-tech-social/site/exercicios/criador-site.html` | Gerador de site (para quem travou) |
| `laboratorio-tech-social/site/exercicios/validador-regex.html` | Regex no navegador |
| `laboratorio-tech-social/site/exercicios/gerador-dados.html` | Gerar dados fictícios para popular o site |

### 🏠 Para casa

Transformar a landing page em **site de 3 páginas** com CSS externo em arquivo próprio.
Testar no celular (o professor pede isso: "me manda um print do celular"). Publicar
no GitHub Pages **depois** da aula B7. **3 commits.**

### 🔗 Próximo módulo

[B6 — Banco de Dados e SQL](#b6)

<a id="b6"></a>

## Módulo 6 — Banco de Dados e SQL (Aula 6)

**Duração:** 90 min · **Aula 6 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. **Modelar** um banco relacional do seu projeto (entidades, atributos, chaves,
   relacionamentos) e criar o **schema** no SQLite.
2. Escrever as **10 consultas SQL** do projeto (SELECT, WHERE, ORDER BY, GROUP BY,
   JOIN, agregação) e ler o resultado com lógica.
3. Conectar **Python + SQLite** (`sqlite3` da biblioteca padrão) e popular o banco a
   partir de um **CSV** de `data/`.

**Objetivo secundário:** explicar por que "guardar tudo em um JSON" **não** é a mesma
coisa que "guardar em um banco de dados".

**Entregável do módulo:** **1 arquivo `.db`** com o schema do projeto, **10 consultas
SQL** salvas em `docs/consultas.sql` (com comentário explicando o que cada uma faz),
**1 script** `src/popular_bd.py` que popula o banco a partir do CSV, e **1 commit** por
artefato.

### 📚 Fontes no repositório

`banco-de-dados-sql/` — **15 módulos × 6 exercícios = 90 exercícios** em `.txt`:

| Módulo | Conteúdo | Arquivos verificados |
|---|---|---|
| `01_o_que_e_banco_dados` | Conceitos, tipos, SGBDs, relacional vs NoSQL | `exercicio_01_conceitos.txt` |
| `02_instalando_sqlite` | Instalação, primeiro banco, DB Browser | — |
| `03_tabelas_e_tipos` | `CREATE TABLE`, tipos, restrições | — |
| `04_inserindo_dados` | `INSERT`, `UPDATE`, `DELETE` | — |
| `05_consultando_dados` | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, aliases | `exercicio_01_select_basico.txt`, `exercicio_04_limit.txt` |
| `06_operadores_logicos` | `AND`, `OR`, `NOT`, `BETWEEN`, `IN` | — |
| `07_funcoes_agregacao` | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP BY` | — |
| `08_joins` | `INNER`, `LEFT`, `RIGHT`, 3 tabelas | `exercicio_01_inner_join.txt`, `exercicio_02_left_join.txt`, `exercicio_05_join_3_tabelas.txt` |
| `09_subqueries` | Subconsultas, `IN`, `EXISTS` | — |
| `10_atualizando_deletando` | `UPDATE`, `DELETE`, transações | — |
| `11_indices_e_performance` | `CREATE INDEX`, `EXPLAIN`, custo | `exercicio_04_explain.txt` |
| `12_modelagem_er` | Entidades, atributos, relacionamentos, normalização | `exercicio_04_normalizacao.txt`, `exercicio_05_diagrama_er.txt` |
| `13_sqlite_com_python` | Conectar, `INSERT`, `SELECT`, CRUD | `exercicio_01_conectar.txt`, `exercicio_05_crud.txt` |
| `14_projeto_sistema_escolar` | **Projeto: sistema escolar** | — |
| `15_projeto_ecommerce` | **Projeto: e-commerce** | — |

**Dados de apoio:** `Analise-de-Dados/datasets/Gapminder.csv` (CSV grande, bom para
`GROUP BY`) e os demais `datasets/*.xlsx` (Aracaju, Fortaleza, Natal, Recife, Salvador,
AdventureWorks) · `esporte-sao-pedro/supabase/functions/send-push/index.ts` (Edge Function real com
consulta ao Supabase) · `esporte-sao-pedro/supabase-rls-admin.sql` (segurança de banco
real) · `Central-de-noticias/noticias.json` (dados em JSON — o oposto do banco relacional).

**Ferramenta:** [DB Browser for SQLite](https://sqlitebrowser.org/) — gratuito, desktop.

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Tabela** | "Planilha com regra. Toda linha é da mesma forma." |
| **Chave primária** | "O RG da tabela. Nunca se repete, nunca fica vazia." |
| **Chave estrangeira** | "O número de um RG de outra tabela. É o que junta as tabelas." |
| **Relacionamento** | "1 para N é comum. N para N precisa de tabela no meio." |
| **SELECT** | "Pergunta. `SELECT` puxa, `WHERE` filtra, `ORDER BY` arruma." |
| **JOIN** | "Junta duas tabelas por uma chave comum. `INNER` só traz quem tem par." |
| **Agregação** | "`GROUP BY` agrupa; `COUNT`/`SUM`/`AVG` contam." |
| **Normalização** | "Não repita o mesmo dado em duas linhas. Guarde uma vez e referencie." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Hoje a gente sai do texto e entra no **dado guardado**.
Um projeto de verdade tem dados que precisam sobreviver ao fechar o programa: os
jogos do torneio, os alunos da EJA, as ruas sem iluminação, as vagas das oficinas.
Guardar isso num arquivo de texto funciona até o primeiro `Ctrl+C` errado."*

**Demonstração ao vivo (5 min).** Compartilhe a tela com o
[DB Browser for SQLite](https://sqlitebrowser.org/) aberto. Mostre o `CREATE TABLE`:

```sql
CREATE TABLE times (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    nome     TEXT    NOT NULL,
    categoria TEXT   NOT NULL
);

CREATE TABLE jogos (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    data     TEXT    NOT NULL,
    local    TEXT    NOT NULL,
    id_time_casa INTEGER NOT NULL,
    id_time_fora INTEGER NOT NULL,
    gols_casa   INTEGER NOT NULL DEFAULT 0,
    gols_fora   INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (id_time_casa) REFERENCES times(id),
    FOREIGN KEY (id_time_fora) REFERENCES times(id)
);
```

Depois rode uma consulta:
```sql
SELECT t.nome AS time, COUNT(j.id) AS jogos, SUM(j.gols_casa + j.gols_fora) AS gols
FROM times t
JOIN jogos j ON j.id_time_casa = t.id OR j.id_time_fora = t.id
GROUP BY t.nome
ORDER BY gols DESC;
```

Diga: *"Isso é o placar do torneio de São Pedro em SQL. Duas tabelas, uma chave
estrangeira, uma agregação. Sem nenhuma biblioteca paga."*

**Quiz de recuperação (3 min).** *"O que o `WHERE` faz? E o `GROUP BY`?"* →
`WHERE` filtra linhas; `GROUP BY` agrupa linhas com o mesmo valor.

#### Fase 2 — Exploração (20 min)

**Parte 1 — Modelagem antes de tabela (8 min).** Ensine o caminho certo:

```
1. ENTIDADES      → "Time", "Jogo", "Jogador" (substantivos)
2. ATRIBUTOS      → "Time tem nome, categoria, cidade"
3. CHAVES         → "Time tem id (PK); Jogo tem id_time_casa (FK)"
4. RELACIONAMENTOS → "Time 1 —— N Jogos"
5. NORMALIZAÇÃO   → "cidade fica na tabela times, não repetida em cada jogo"
```

Exemplo do **Projeto Placar da Cidade** (São Pedro/SP):

| Entidade | Atributos | Chave |
|---|---|---|
| `times` | nome, categoria, cidade | `id` (PK) |
| `jogadores` | nome, id_time, numero_camisa | `id` (PK), `id_time` (FK) |
| `jogos` | data, local, gols_casa, gols_fora | `id` (PK), duas FKs |
| `competicoes` | nome, ano, modalidade | `id` (PK) |

Diga: *"Se você escreveu a tabela antes de pensar nas entidades, você vai ter que
reescrever. Todo mundo escreve. A diferença é que quem planeja reescreve 1 vez."*

**Parte 2 — As 5 consultas que resolvem 80% (8 min).** Escreva no quadro:

```sql
-- 1. TRAZER
SELECT nome, cidade FROM times;
-- 2. FILTRAR
SELECT nome FROM times WHERE categoria = 'Futsal';
-- 3. ORDENAR
SELECT nome FROM times ORDER BY nome DESC;
-- 4. LIMITAR
SELECT nome FROM times ORDER BY nome LIMIT 5;
-- 5. CONTAR
SELECT COUNT(*) AS total FROM times;
```

Explique a **ordem de execução** do SQL, que é sempre a mesma:

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

Diga: *"Você escreve `SELECT` primeiro e `WHERE` depois, mas o banco executa `FROM`
primeiro. Isso é por isso que não dá para usar o alias do SELECT dentro do WHERE."*

**Parte 3 — JOIN em 30 segundos (4 min).**

```sql
-- INNER: só quem tem par nos dois lados
SELECT t.nome, j.data FROM times t
INNER JOIN jogos j ON j.id_time_casa = t.id;

-- LEFT: preserva a tabela da esquerda mesmo sem par
SELECT t.nome, j.data FROM times t
LEFT JOIN jogos j ON j.id_time_casa = t.id;
```

Diga: *"Um time que ainda não jogou **some** no `INNER JOIN`. Isso é um bug clássico
de relatório. Se você quer todos os times, inclusive os que não jogaram, use `LEFT`."*

#### Fase 3 — Mão na massa (30 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala cria o schema
do **seu** projeto de capstone (pode ser rascunho — será fechado no B13).

**Atividade A — Schema (10 min).** Criar o arquivo `data/projeto.db` com o DB Browser
(ou por script Python) e **3 tabelas** com chave primária e pelo menos **1 chave
estrangeira**. Inserir **10 linhas** em cada tabela, com **dados fictícios** de São Pedro/SP
(nomes de times inventados, ruas reais ou inventadas, nenhum dado de aluno).

**Atividade B — 6 consultas (15 min).** Cada sala escreve **6 consultas** e salva em
`docs/consultas.sql`, cada uma com um comentário `--` explicando a pergunta que ela
responde:

1. Listar tudo de uma tabela.
2. Filtrar por condição (com `AND` e com `OR`).
3. Ordenar e limitar.
4. Contar / somar / média com `GROUP BY`.
5. `INNER JOIN` entre 2 tabelas.
6. `LEFT JOIN` mostrando quem **não** tem vínculo.

**Atividade C — Python + SQLite (5 min).** Do módulo `13_sqlite_com_python`:

```python
import sqlite3

con = sqlite3.connect("data/projeto.db")
cursor = con.cursor()
cursor.execute("SELECT nome, cidade FROM times ORDER BY nome")
for nome, cidade in cursor.fetchall():
    print(f"{nome} - {cidade}")
con.close()
```

**O que o professor diz enquanto circula:**

> *"Me mostra o schema. Se uma tabela tem o nome da cidade repetido em 10 linhas, você
> fez normalização errada. E me mostra a consulta que traz o time que ainda não jogou
> — se ela sumir, você precisa de LEFT JOIN."*

**Plano B (internet caiu):** o DB Browser é **offline** e o `sqlite3` é parte do Python
instalado. O professor desliga o breakout e entrega o `CREATE TABLE` e as 6 consultas
**em texto no chat**; os alunos colam no DB Browser e no `data/` local. Nada aqui
depende de internet depois do download.

#### Fase 4 — Projeto (20 min)

**Desafio: "O banco do seu projeto".**

Cada aluno entrega:

1. `data/projeto.db` — schema com **3 a 5 tabelas**, chaves e **10+ linhas** por tabela.
2. `docs/consultas.sql` — **10 consultas** comentadas, com pelo menos 1 `JOIN`,
   1 `GROUP BY` e 1 `LEFT JOIN`.
3. `src/popular_bd.py` — lê o **CSV de `data/`** e popula o banco com `sqlite3`,
   criando as tabelas se não existirem.
4. `docs/modelo_er.md` — o **diagrama ER em texto**, mostrando as entidades e os
   relacionamentos com cardinalidade (`1 — N`).
5. `docs/decisoes.md` — **+1 decisão**: *"Por que banco relacional e não um JSON?"*
   com o motivo.

**Critério de pronto:**
- [ ] `.db` com **3 a 5 tabelas**, **PK** em todas e **≥1 FK**
- [ ] **10+ linhas** por tabela, **sem dados pessoais reais**
- [ ] `docs/consultas.sql` com **10 consultas comentadas**
- [ ] Pelo menos **1 `JOIN`**, **1 `GROUP BY`** e **1 `LEFT JOIN`**
- [ ] `src/popular_bd.py` roda **2 vezes** sem duplicar registro (idempotente)
- [ ] `docs/modelo_er.md` com o diagrama em texto
- [ ] `docs/decisoes.md` com a justificativa relacional × JSON
- [ ] **3 commits** no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Cada sala abre o DB Browser e mostra **1 consulta** que responde a uma pergunta real
do bairro: *"Quantas ruas sem iluminação por bairro?"* / *"Qual o time com mais gols
na COMPETIÇÃO?"* / *"Quantos alunos por turno na EJA?"*. A turma vota na consulta mais
útil.

### ⚠️ Erros comuns e como lê-los

| Erro | Mensagem do SQLite | Como corrigir |
|---|---|---|
| **Tabela já existe** | `sqlite3.OperationalError: table times already exists` | Use `CREATE TABLE IF NOT EXISTS` ou apague o `.db` e rode de novo |
| **Coluna não existe** | `no such column: cidade` | Confira o nome exato com `.schema` no DB Browser |
| **Foreign key violada** | `FOREIGN KEY constraint failed` | Você inseriu a FK antes de existir o registro pai. Insira na ordem |
| **SQLite travado** | `database is locked` | Duas conexões abertas no mesmo `.db`. Feche com `con.close()` |
| **Filtro sem resultado** | Tabela vazia | Esqueceu do `COMMIT`? Use `con.commit()` depois do `executemany` |
| **JOIN que some com o time** | Resultado incompleto | Use `LEFT JOIN` |
| **Aspas simples** | `near "O": syntax error` | Em SQL, string usa `'texto'`, não aspas duplas. Para string com apóstrofo, dobre: `'d''Oeste'` |
| **Ordenação errada** | Ordem alfabética em vez de numérica | A coluna foi salva como TEXT. Use `ORDER BY CAST(coluna AS INTEGER)` |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Schema | 3–5 tabelas, PKs e FKs corretas |
| `docs/consultas.sql` | 10 consultas comentadas, com JOIN/GROUP BY/LEFT JOIN |
| `src/popular_bd.py` | Popula o banco e é idempotente |
| `docs/modelo_er.md` | Diagrama em texto com cardinalidade |
| Dados | 10+ linhas por tabela, zero dados pessoais |
| Commits | 3 commits |
| Participação | 1 consulta apresentada na Fase 5 |
| Pergunta de saída | "Por que o time que nunca jogou some no `INNER JOIN`?" |

**Pergunta de escrita:**
> "Você tem a tabela `alunos` (id, nome, id_turma) e a tabela `turmas` (id, turno).
> Escreva a consulta que lista **todos** os alunos, mostrando também o turno — inclusive
> os alunos cuja `id_turma` está vazia."
>
> **Resposta:** é preciso um `LEFT JOIN` a partir dos alunos, porque a exigência é
> preservar **todos os alunos**:
> ```sql
> SELECT a.nome, t.turno
> FROM alunos a
> LEFT JOIN turmas t ON t.id = a.id_turma;
> ```
> Se o `JOIN` fosse `INNER`, os alunos sem turma **desapareceriam** do resultado — e
> isso é exatamente o tipo de bug que um relatório precisa evitar. A alternativa
> equivalente é `FULL OUTER JOIN`, mas o SQLite só a partir da versão 3.39, então
> `LEFT JOIN` é a escolha segura.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `banco-de-dados-sql/07_funcoes_agregacao/` | COUNT, SUM, AVG, GROUP BY |
| `banco-de-dados-sql/09_subqueries/` | Subconsultas e `EXISTS` |
| `banco-de-dados-sql/11_indices_e_performance/` | Índices e `EXPLAIN` (dá para citar no README do projeto) |
| `banco-de-dados-sql/12_modelagem_er/` | Normalização e diagrama ER |
| `banco-de-dados-sql/14_projeto_sistema_escolar/` | Projeto real de sistema escolar |
| `banco-de-dados-sql/15_projeto_ecommerce/` | Projeto real de e-commerce |
| `qa-exercicios-praticos/sql-para-qa/exercicios-sql.md` | SQL do ponto de vista do QA |
| `Analise-de-Dados/datasets/Gapminder.csv` | CSV grande para `GROUP BY` e agregação |
| `esporte-sao-pedro/supabase-rls-admin.sql` | Segurança de banco em projeto real |
| `Central-de-noticias/noticias.json` | O contraste: dados em JSON |

### 🏠 Para casa

Adicionar **2 tabelas** ao seu banco e **3 consultas** novas a `docs/consultas.sql`.
Se seu projeto usa Python, escrever `src/consultar.py` que abre `data/projeto.db` e
mostra o resultado da consulta mais útil como **tabela formatada** (com `f"{:<25}"`).
**2 commits.**

### 🔗 Próximo módulo

[B7 — Git e GitHub (portfólio público)](#b7)

<a id="b7"></a>

## Módulo 7 — Git e GitHub (portfólio público) (Aula 7)

**Duração:** 90 min · **Aula 7 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Usar Git como **diário de bordo**: `status`, `add`, `commit`, `log`, `diff`, `restore`.
2. Publicar um **repositório público** no GitHub com **README**, licença MIT e `.gitignore`.
3. Trabalhar com **branches** e **Pull Requests** — inclusive **receber e revisar** PR de
   outra pessoa da turma.
4. **Publicar o site no GitHub Pages** e escrever um `README.md` que faça sentido para
   quem nunca te viu.

**Objetivo secundário:** explicar por que "commit ou não existe" é uma regra de
**segurança**, não de vaidade.

**Entregável do módulo:** **repositório público** no GitHub com **10 commits**,
**README.md** completo, **licença MIT**, `.gitignore`, **1 branch** e **1 Pull Request**,
e o site **no ar** no GitHub Pages. **"Commit ou não existe"** vale a partir de hoje.

### 📚 Fontes no repositório

`git-github-iniciantes/` — **15 módulos** com `README.md` próprio em cada pasta
(verificados):

| Módulo | Conteúdo | Arquivo verificado |
|---|---|---|
| `01_o_que_e_git` | O que é versionamento, repositório, working tree | `README.md` |
| `02_primeiro_repositorio` | `init`, `add`, `commit` | `README.md` |
| `03_trabalhando_com_mudancas` | `status`, `diff`, `restore` | `README.md` |
| `04_branches` | `branch`, `switch`, `merge` | `README.md` |
| `05_remotes_e_push` | `remote`, `push`, `pull`, `fetch` | `README.md` |
| `06_github` | Repositório, Issues, Projects | `README.md` |
| `07_pull_requests` | PR, revisão, comentário | `README.md` |
| `08_issues_e_projetos` | Issues, etiquetas, boards | `README.md` |
| `09_github_pages` | Publicar site estático | `README.md` |
| `10_git_avancado` | `rebase`, `stash`, `tag`, `amend` | `README.md` |
| `11_trabalho_em_equipe` | Conflitos, revisão de código, pairing | `README.md` |
| `12_ci_cd_basico` | GitHub Actions, pipeline | `README.md` |
| `13_open_source` | Licenças, contribuir, issue-first | `README.md` |
| `14_ferramentas` | GitHub Desktop, WSL, IDEs | `README.md` |
| `15_projeto_pratico` | Projeto final do curso de Git | `README.md` |

**Referências de projeto real:**
`esporte-sao-pedro/` (`CNAME`, `sitemap.xml`, `robots.txt`, `manifest.json`, `sw.js`,
`.github/workflows/`) ·
`Central-de-noticias/` (`.github/workflows/ci-tests.yml`, `update-news.yml`,
`monitoramento.yml`, `limpar-historico.yml`, `pytest.ini`) ·
`laboratorio-tech-social/site/certificado/` (`index.html`, `verificar.html`,
`historia.html` — a página de verificação de certificado) ·
`laboratorio-tech-social/materiais/templates/certificado/certificado.html` e
`modelo-certificado.md`.

**Links oficiais:**
[GitHub](https://github.com/) · [cadastro](https://github.com/signup) ·
[GitHub Pages](https://pages.github.com/) · [GitHub Desktop](https://desktop.github.com/) ·
[Pro Git em PT-BR](https://git-scm.com/book/pt-br/v2) ·
[WSL no Windows](https://learn.microsoft.com/pt-br/windows/wsl/install)

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Working tree** | "A pasta onde você mexe. Onde o erro acontece." |
| **Stage** | "A fila do que vai entrar no commit. Você escolhe, arquivo por arquivo." |
| **Commit** | "Uma foto do estado do projeto. Com uma frase que diz o que mudou." |
| **Histórico** | "O log de commits é o **diário de bordo** do projeto. Nunca mente." |
| **Branch** | "Uma linha do tempo paralela. Teste sem medo de quebrar a linha principal." |
| **Pull Request** | "Pedido para entrarem na linha principal. Com revisão, não com pressa." |
| **Merge** | "Juntou as duas linhas e resolveu o conflito **à mão**." |
| **`.gitignore`** | "Lista do que **não** entra no repositório: senhas, senhas de senha, arquivos pesados." |
| **Licença MIT** | "Permite usar, estudar, modificar e redistribuir. Só exige crédito." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"A partir de hoje, a regra da sala é: **commit ou não
existe**. Não é freshura. É o que vai te salvar quando você quebrar o código sem
querer — e vai acontecer, hoje mesmo, antes do fim da aula."*

**Demonstração ao vivo (5 min).** Compartilhe a tela com um repositório de exemplo.
Execute, na ordem, e narre:

```bash
git status
git diff
git add src/calculadora.py
git commit -m "feat: adiciona calculadora de IMC"
git log --oneline --graph
```

Depois mostre o **desastre** e o **resgate**:

```bash
# apagou o arquivo por engano
git restore src/calculadora.py
# fez uma bagunça e quer voltar atrás
git log --oneline
git revert <hash>
```

Diga: *"Três segundos de `git log` e você volta para qualquer ponto da história. Isso
não existe em nenhum editor de texto do mundo."*

**Quiz de recuperação (3 min).** *"O que a ordem `add` → `commit` faz? O que é
`restore`?"* → `add` escolhe o que entra; `commit` grava o instantâneo; `restore`
descarta a mudança local.

#### Fase 2 — Exploração (15 min)

**Parte 1 — Os 6 comandos que você usa 90% do tempo (8 min).** Escreva no quadro:

| Comando | O que faz | Analogia do dia a dia |
|---|---|---|
| `git status` | O que está acontecendo agora | "O que eu fiz na cozinha?" |
| `git diff` | O que mudou desde o último commit | "O que eu mudei na receita?" |
| `git add <arquivo>` | Escolhe o que entra no commit | "Coloco na sacola" |
| `git commit -m "..."` | Grava o instantâneo com frase | "Fecho o caderno e escrevo o que fiz" |
| `git log --oneline` | Lista o histórico | "Índice do caderno" |
| `git restore <arquivo>` | Desfaz a mudança local | "Desfaço a rabiscada" |

**Parte 2 — Mensagem de commit que serve (4 min).** Ensine o padrão
**Conventional Commits** e mostre a régua:

```
<tipo>(<escopo>): <descrição curta no imperativo>

feat: adiciona filtro por bairro no placar
fix: corrige contagem de gols quando o time da casa não jogou
docs: documenta como rodar o projeto
test: adiciona caso de teste para time sem jogos
refactor: extrai a função de cálculo da classificação
```

Tipos: `feat`, `fix`, `docs`, `test`, `refactor`, `test`, `chore`.
Diga: *"Regra de ouro: mensagem no **imperativo** e no **tempo presente**. 'Adiciona',
não 'Adicionei' ou 'Adicionado'. O primeiro que você lê o histórico vai saber o que
fazer sem abrir o arquivo."*

**Parte 3 — Branch, PR e merge (3 min).**

```bash
git switch -c feat/placar
# ... trabalha ...
git add . && git commit -m "feat: tabela de classificação"
git push -u origin feat/placar
```

E no GitHub: **Compare & pull request** → revisão → **Merge pull request**.
Diga: *"Você não vai mexer na `main` direto. Nem eu. Nem o professor. A `main` é o que
está no ar. Tudo passa por PR. Isso é o que separa projeto de bagunça."*

#### Fase 3 — Mão na massa (40 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala **não**
trabalha sozinha: ela faz **pull request entre si**. Um aluno da sala abre a branch e
o PR; **outro** revisa e comenta. Isso é o "lê o código do colega" que a rubrica exige.

**Atividade A — Repositório e commits (15 min dentro do breakout).**

1. Criar o repositório no GitHub (privado ou público, decisão do aluno — a recommendação
   é **público** no B16, quando o projeto estiver pronto).
2. `git init`, `git remote add origin ...`, `git push -u origin main`.
3. Subir o conteúdo dos módulos B3 a B6 com **10 commits** separados (não 1 commit
   gigante). Sugestão de divisão:
   ```
   chore: estrutura inicial do repositório
   feat: adiciona scripts da aula de Python
   feat: adiciona site de 3 páginas
   feat: adiciona schema e consultas SQL
   docs: documenta decisões de projeto
   ```
4. Criar `.gitignore` com, no mínimo:
   ```
   __pycache__/
   *.pyc
   .venv/
   node_modules/
   .env
   *.db-journal
   .DS_Store
   ```
5. Adicionar a **licença MIT** (o professor entrega o texto pronto no chat).

**Atividade B — Branch e Pull Request (15 min dentro do breakout).**

1. `git switch -c feat/melhoria-readme`
2. Melhorar o `README.md` (ou o CSS, ou uma query).
3. `git commit` + `git push -u origin feat/melhoria-readme`
4. Abrir o **Pull Request** no GitHub, com título e descrição.
5. **Outro aluno** da sala revisa, deixa **1 comentário** e aprova (ou pede ajuste).
6. `git switch main` + `git merge feat/melhoria-readme` + `git push`.

**Atividade C — GitHub Pages (10 min dentro do breakout).**

1. No repositório: **Settings** → **Pages** → Source: branch `main`, folder `/ (root)`.
2. Criar um `index.html` na raiz (o professor mostra como pegar o `index.html` da
   landing page e renomear para a raiz).
3. Publicar. Em ~1 minuto o site fica no ar em
   `https://<usuario>.github.io/<repositorio>/`.

> ⚠️ **Regra da sala:** Pages só publica **HTML, CSS e JS estáticos**. Nada de chave
> de API no navegador. Nada de dado pessoal. Se o projeto precisar de backend, ele vai
> rodar localmente ou via GitHub Actions — e isso é assunto do módulo B15.

**O que o professor diz enquanto circula:**

> *"Me mostra o `git log --oneline`. Se tem um commit chamado 'att', eu vou pedir para
> você reescrever a mensagem. Commit é documentação que ninguém vai ler se estiver
> escrito em 'att'."*

**Plano B (internet caiu):** Git é **offline**. O professor desliga o breakout e cada
aluno continua fazendo os 10 commits localmente. Só o `push` (Atividade B e C) fica para
depois — o professor organiza um **compartilhamento de tela** de 10 minutos no encontro
seguinte para publicar. Ninguém perde o conteúdo.

#### Fase 4 — Projeto (15 min)

**Desafio: "Seu portfólio público".**

Entregue, no seu repositório:

1. **`README.md` completo**, com esta estrutura:
   ```markdown
   # Nome do Projeto
   > Uma frase que explica o problema real que ele resolve.

   ## O problema
   (dados públicos de São Pedro/SP, com a fonte citada)

   ## Como rodar
   (comandos exatos, copiável)

   ## O que tem aqui
   (tabela: pasta → o que tem)

   ## Como foi feito
   (stack, decisões principais, link para docs/decisoes.md)

   ## Contribuição
   (como abrir issue e PR)

   ## Licença
   MIT
   ```
2. **`LICENSE`** com o texto MIT.
3. **`.gitignore`** testado (crie um arquivo `teste.pyc` e veja que ele **não** aparece
   no `git status`).
4. **1 branch** e **1 Pull Request** já **merged**.
5. **GitHub Pages no ar** com o `index.html` do módulo B5.
6. **`docs/decisoes.md`** com as decisões acumuladas dos módulos B1 a B6 (mínimo 5).

**Critério de pronto:**
- [ ] Repositório **público** no GitHub
- [ ] **10 commits** com mensagens no padrão Conventional Commits
- [ ] `README.md` com **as 7 seções** acima
- [ ] `LICENSE` MIT presente
- [ ] `.gitignore` funcionando (arquivo `.pyc` **não** versionado)
- [ ] **1 PR merged** na `main`
- [ ] **GitHub Pages no ar** com link no README
- [ ] `docs/decisoes.md` com **5+ decisões**

#### Fase 5 — Mostra (10 min)

Cada sala mostra o **repositório** de um colega (não o próprio — isso treina revisão).
A turma responde: *"Se essa pessoa abrir esse repositório agora, ela entende o que
faz em 30 segundos?"* O professor dá 1 nota de clareza por repositório.

Volte ao **quiz de recuperação**: *"O que o `git restore` faz?"*

### ⚠️ Erros comuns e como lê-los

| Erro | Mensagem | Como corrigir |
|---|---|---|
| **Commit sem mensagem útil** | `Aborting commit due to empty commit message` | Escreva o que mudou, no imperativo |
| **Esqueceu o `add`** | `nothing added to commit but untracked files present` | `git status` mostra o que está "untracked". `git add` |
| **Commit vazio** | `nothing to commit, working tree clean` | Não há mudança. Ou você já commitou, ou salvou o arquivo errado |
| **Push rejeitado** | `! [rejected] main -> main (non-fast-forward)` | Alguém pushou antes. `git pull` e depois `git push` |
| **Conflito de merge** | `CONFLICT (content): Merge conflict in <arquivo>` | Abra o arquivo, procure `<<<<<<<`, escolha o lado certo, apague os marcadores, `git add` e `git commit` |
| **Esqueceu o `.gitignore` e versionou `.env`** | `git ls-files` mostra o `.env` | `git rm --cached .env`, adicione ao `.gitignore`, faça commit. **Troque a chave** se era real |
| **Branch errada** | Suas mudanças não aparecem na `main` | `git status` mostra "On branch ...". `git switch main` e `git merge` |
| **Pages não atualiza** | Site mostra a versão antiga | 1) espere 1 min, 2) force refresh (`Ctrl`+`Shift`+`R`), 3) confirme que o branch e a pasta estão certos em Settings → Pages |
| **Escreveu tudo em `main`** | PR com 40 arquivos | Não é erro técnico, é de processo. Use branch sempre |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Repositório | Público, com 10 commits |
| `README.md` | 7 seções preenchidas |
| PR | 1 PR merged, com 1 comentário de revisão de colega |
| `.gitignore` | `.pyc` não versionado |
| `LICENSE` | MIT presente |
| GitHub Pages | No ar, link no README |
| `docs/decisoes.md` | 5+ decisões |
| Participação | Revisão ao vivo de repositório de colega |
| Pergunta de saída | "Por que `git restore` é mais seguro do que `Ctrl+Z`?" |

**Pergunta de escrita:**
> "Você passou a tarde inteira refatorando `src/calculadora.py` e terminou com um arquivo
> 3 vezes maior do que começou. O código funciona. Você commita tudo em um commit
> chamado 'ajustes'?"
>
> **Resposta:** **não**, e a razão não é estética, é técnica. Um commit grande demais
> significa que, quando algo quebrar daqui a duas semanas, você não consegue voltar
> atrás sem perder trabalho bom junto. O commit ideal é o que você consegue **desfazer
> inteiro** sem perder nada importante. Então: divida em commits pequenos
> (`refactor: extrai cálculo do IMC para função`, `refactor: separa validação de
> entrada`, `refactor: documenta a função`), rode os testes a cada commit, e só então
> faz o merge na `main`. **Commit ou não existe** — e commit grande demais é quase
> tão ruim quanto commit nenhum.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `git-github-iniciantes/10_git_avancado/README.md` | Rebase, stash, tag, amend |
| `git-github-iniciantes/11_trabalho_em_equipe/README.md` | Conflitos e revisão de código |
| `git-github-iniciantes/12_ci_cd_basico/README.md` | GitHub Actions (base do B15) |
| `git-github-iniciantes/13_open_source/README.md` | Licenças e como contribuir |
| `git-github-iniciantes/14_ferramentas/README.md` | GitHub Desktop e WSL |
| `git-github-iniciantes/15_projeto_pratico/README.md` | Projeto final do curso de Git |
| `Central-de-noticias/.github/workflows/ci-tests.yml` | Pipeline real de testes |
| `Central-de-noticias/.github/workflows/update-news.yml` | Atualização automática de conteúdo |
| `esporte-sao-pedro/CNAME` | Domínio próprio em Pages |
| `laboratorio-tech-social/site/certificado/index.html` | Página de certificado verificável (modelo para o B16) |

### 🏠 Para casa

Escrever o `README.md` final do projeto com todas as seções. Publicar o site no
GitHub Pages e **testar no celular**. Mandar o link no issue do repositório da turma
com o texto: *"Quero feedback no README. O que está confuso?"*. **3 commits.**

### 🔗 Próximo módulo

[B8 — QA: Testes de Software](#b8)

<a id="b8"></a>

## Módulo 8 — QA: Testes de Software (Aula 8)

**Duração:** 90 min · **Aula 8 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Diferenciar **teste manual** de **teste automatizado**, e **teste unitário** de
   **teste de sistema**, e saber **quando usar cada um**.
2. Escrever **3 casos de teste** no formato do repositório `manual-qa-completo`
   (ID, pré-condição, dados, passos, resultado esperado, status).
3. Reportar **1 bug** com severidade, prioridade, passos de reprodução e evidência.
4. Escrever e rodar **1 suíte automatizada** (`pytest` ou Node) que **falha de propósito**
   para provar que ela detecta erros.

**Objetivo secundário:** entender que **teste que não roda é bug** e que **qualidade
não é etapa final, é hábito**.

**Entregável do módulo:** **1 plano de testes** (`docs/plano-de-testes.md`) com **5 casos
de teste**, **1 bug reportado** (`docs/bugs/BUG-001.md`) e **1 suíte automatizada** em
`tests/` com **pelo menos 3 testes automatizados** (dos quais **1 deve falhar** quando
o bug existir). **"Commit ou não existe"** vale para testes também.

### 📚 Fontes no repositório

`manual-qa-completo/docs/10/PT/` — **templates oficiais em português** (verificados):

| Arquivo | O que é |
|---|---|
| `test_plan_template.md` | Modelo de plano de testes (9 seções: introdução, itens, fora de escopo, abordagem, ambiente, cronograma, riscos, critérios de entrada/saída, aprovações) |
| `test_case_template.md` | Modelo de caso de teste (ID, título, módulo, pré-condições, dados, passos, resultado esperado/obtido, status, executor, data) |
| `bug_report_template.md` | Modelo de bug report (ambiente, passos, esperado, obtido, severidade, prioridade, evidência, anexos) |
| `checklist_aceite.md` | Checklist de homologação (funcionalidade, validação de dados, UI/UX, segurança, performance, dados/ambiente) |
| `charter_template.md` | Charter de sessão de teste exploratório |
| `matriz_rastreabilidade.md` | Matriz requisito → caso de teste → resultado (com fórmula de cobertura) |
| `glossario.md` | Glossário QA PT/EN |
| `indice.md` | Índice do manual |
| `solucoes.md` | Soluções dos exercícios do manual |

**Bateria de exercícios:** `qa-exercicios-praticos/` —
`casos-de-teste/exercicios-escrever-casos.md` ·
`encontre-o-bug/codigo/exercicio-01-calculadora.py` (+ `exercicio-02-banco.py`,
`exercicio-03-carrinho.py`, `exercicio-04-formulario.html`, `exercicio-05-datas.py`,
`exercicio-06-cpf.py`) com gabaritos em `encontre-o-bug/gabarito/` ·
`modelos-templates/` (`test-plan.md`, `test-case.md`, `bug-report.md`,
`relatorio-teste.md`, `checklist-smoke-e-aceite.md`) ·
`tecnicas-de-teste/exercicios-tecnicas-de-teste.md` ·
`api-testing/exercicios-de-api.md` · `sql-para-qa/exercicios-sql.md` ·
`simulados/simulado-01-fundamentos.md` e `simulado-02-api-sql-seguranca.md` ·
`perguntas-respostas/perguntas-entrevista-QA.md` ·
`simulacoes/cenarios-role-play.md` ·
`sites-para-testar/` (9 sites: `agenda-medica`, `banco-abc`, `calc-impostos`,
`crm-connect`, `foodgo`, `hotel-reserva`, `momento-matador`, `portal-cliente`,
`techstore`).

**Conceitos e casos reais:** `QualityHub/Documentação (Docs)/` —
`Tipos de Testes de Software.md`, `Conceitos.md`, `Testes de Aceitação.md`,
`Testes de Integração.md`, `Testes de Regressão.md`, `Testes de Segurança.md`,
`Testes de Usabilidade.md` — e `QualityHub/Cases QA/` (falhas reais: controle de voo,
reservas da British Airways, NHS, Knight Capital, votação eletrônica).

**Automação real:** `boilerplate-mochachai/tests/1_unit-tests.js` e
`tests/2_functional-tests.js` (Mocha + Chai) ·
`listadetarefas_qualityAssurance/` (app com **bugs propositais** + `script_test.py`,
`script_test2.py`, `tests/example.spec.js`, `tests/Testes E2E/new_task_test.py`,
`Testes manuais.md`, `testes_automatizados.md`, `playwright.config.js`, `pytest.ini`) ·
`Central-de-noticias/tests/test_gerar.py` e `pytest.ini` ·
`qa-automation-framework/tests/api/test_crud.py`, `tests/api/test_status_codes.py`,
`tests/ui/test_saucedemo.py` · `QA_RUN/` (71 jogos de QA + `tests/smoke.js`).

**Lúdico e didático:** `o-despertar-qa/` (jogo "Despertar para Qualidade de Software",
com `src/pages/Bug Hunter A Aventura QA.hvp52.js`, `src/pages/QA Lab.q82r1.js`,
`src/pages/Ferramentas de Testes .soa7r.js`) ·
`laboratorio-tech-social/site/exercicios/caca-bugs.html` ·
`laboratorio-tech-social/site/exercicios/plano-testes.html` ·
`laboratorio-tech-social/site/exercicios/simulador-api.html` ·
`laboratorio-tech-social/site/exercicios/quiz-teens.html` ·
`laboratorio-tech-social/site/exercicios/verdadeiro-falso.html` ·
`laboratorio-tech-social/site/exercicios/validador-regex.html`

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **QA** | "Garantia da qualidade é o **processo**. Testar é uma parte dele." |
| **Bug** | "Comportamento diferente do esperado — e o esperado está escrito." |
| **Severidade** | "Quão grave é o estrago. Alto, crítico, médio, baixo." |
| **Prioridade** | "Quão rápido a gente precisa arrumar. Urgente, alta, média, baixa." |
| **Caso de teste** | "Um cenário com resultado esperado **escrito antes** de rodar." |
| **Teste unitário** | "Testa uma função sozinha. Rápido e barato." |
| **Teste de integração** | "Testa duas peças juntas. Onde nasce o bug." |
| **Teste de regressão** | "Rodar tudo de novo depois de mexer, para não quebrar o que já funcionava." |
| **Cobertura** | "Quanto do código os testes de fato tocam." |
| **Ciclo do bug** | "Encontrar → reportar → corrigir → retestar → fechar. Sem pular etapa." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Vocês já viveram com QA. Toda vez que um app do banco te
derruba depois de atualizar, você **reporta** o bug. Todo mundo faz isso sem pensar.
Hoje vocês vão fazer isso **de propósito**, com método, para o projeto de vocês."*

**Demonstração ao vivo (5 min).** Compartilhe a tela. Abra o
`qa-exercicios-praticos/encontre-o-bug/codigo/exercicio-01-calculadora.py`, que tem um
**bug proposital**. Rode. Mostre o resultado errado. Depois abra o
`encontre-o-bug/gabarito/exercicio-01-gabarito.md` e revele o bug.

Diga: *"Esse arquivo tem um bug plantado. Em 2 minutos a turma toda achou. Em código
real, o bug está escondido em 400 linhas, e ele custa R$ 200 mil do ensino público.
**Testar é economia**."*

**Quiz de recuperação (3 min).** *"Qual a diferença entre severidade e prioridade?"*
→ Severidade = gravidade do impacto; prioridade = urgência da correção. Um bug de
severidade **baixa** (texto errado) pode ter prioridade **alta** (é o texto do nome
da escola que aparece no relatório oficial).

#### Fase 2 — Exploração (20 min)

**Parte 1 — O modelo mental (6 min).** Desenhe no quadro a **pirâmide de testes**:

```
          ▲ poucos e caros, automatizado
         ╱  Teste de Sistema / E2E
        ╱   Teste de Integração
       ╱    Teste Unitário
      ╱     Teste Manual / Exploratório
     ╱_______________________________
   muitos e barato, feedback rápido
```

Diga: *"A pirâmide tradicional tem a base larga de teste manual. Em projeto real, a
base larga é teste **automatizado** unitário, e o topo fino é o teste manual exploratório.
pirâmide invertida — a que a maioria dos sites usa — é mais lenta e mais cara."*

**Parte 2 — Anatomia de um caso de teste (7 min).** Escreva, usando o
`manual-qa-completo/docs/10/PT/test_case_template.md`:

```
ID: TC-PLACAR-001
Título: Time sem jogos aparece na classificação
Módulo: Classificação

Pré-condições:
  - Banco populado com 3 times
  - "Esporte Clube Aurora" não tem nenhum jogo registrado

Dados de entrada:
  - Sem entrada manual (consulta disparada pela tela)

Passos:
  1. Abrir a página "Classificação"
  2. Rolar até o fim da tabela

Resultado esperado:
  - "Esporte Clube Aurora" aparece com 0 jogos e 0 pontos

Resultado obtido: [preenchido na execução]
Status: [Pass | Fail | Blocked | Not Run]
Executor: [apelido] | Data: [dd/mm/aaaa]
```

Diga: *"O **resultado esperado vem ANTES**. Se você escreve o esperado depois de ver
o que o programa fez, você não está testando — está descrevendo. E se o resultado
obtido for diferente, isso é um **bug**, não um erro seu."*

**Parte 3 — Severidade, prioridade e o ciclo do bug (7 min).** Escreva a tabela:

| Severidade | Exemplo no nosso contexto |
|---|---|
| **Crítico** | O site não abre. O banco de dados apaga dados. A página expõe chave de API |
| **Alto** | Placar mostra resultado errado. Formulário perde a inscrição |
| **Médio** | Layout quebrado no celular. Texto com acento errado |
| **Baixo** | Cor do botão. Espaço em branco |

```
ENCONTRAR → REPORTAR → CLASSIFICAR → CORRIGIR → RETESTAR → FECHAR
```

Aponte o `qa-exercicios-praticos/modelos-templates/bug-report.md` e mostre que ele
tem **passos para reproduzir** — *"um bug sem passos de reprodução não é bug, é
relato de humilhação"*.

#### Fase 3 — Mão na massa (35 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Formato sugerido:
**1 dupla por bug** — um acha, o outro reproduz e escreve o relatório.

**Atividade A — Caça-bugs em código real (12 min dentro do breakout).** Cada sala pega
**2 dos 6 arquivos com bug proposital** de `qa-exercicios-praticos/encontre-o-bug/codigo/`
(`exercicio-01-calculadora.py`, `exercicio-02-banco.py`, `exercicio-03-carrinho.py`,
`exercicio-04-formulario.html`, `exercicio-05-datas.py`, `exercicio-06-cpf.py`), roda,
acha o bug **antes** de abrir o gabarito, e escreve o relatório no formato do
`bug_report_template.md`.

> **Dica do professor:** *"Não abra o gabarito ainda. Vocês têm 8 minutos. Depois
> comparem com o gabarito e vejam quantos acharam."*

**Atividade B — Plano de testes do seu projeto (15 min dentro do breakout).** Cada aluno
escreve, em `docs/plano-de-testes.md`, o **plano de testes do seu projeto**, adaptando
o `manual-qa-completo/docs/10/PT/test_plan_template.md`:

```
1. INTRODUÇÃO
   Objetivo: [validar a release v0.1 do <projeto>]
   Escopo: [o que entra e o que fica de fora]
   Público: [quem vai usar — ex.: torcedores do torneio]
2. ITENS DE TESTE
   - [funcionalidade 1], [funcionalidade 2]
3. FORA DE ESCOPO
   - [ex.: login real com e-mail do aluno]
4. ABORDAGEM
   Níveis: [unit, integração, manual]
   Tipos: [regressão, smoke, exploratório]
5. AMBIENTE E DADOS
   Ambiente: [Chrome + Python 3.12 local]
   Dados: [CSV fictício de data/, 10 linhas]
6. CRONOGRAMA E RESPONSÁVEIS
   Início: [data] | Fim: [data]
   QA Lead: [apelido] | Testers: [apelidos]
7. RISCOS E MITIGAÇÕES
   Risco: [internet instável] → Mitigação: [exercícios .txt offline]
8. CRITÉRIOS DE ENTRADA/SAÍDA
   Entrada: [código commitado e rodando]
   Saída: [todos os casos críticos verdes, 0 bug crítico aberto]
9. APROVAÇÕES
   Aluno(a): [ ]   Professor: [ ]
```

E preenche **5 casos de teste** usando o `test_case_template.md`, no arquivo
`docs/casos-de-teste.md`.

**Atividade C — Suíte automatizada (8 min dentro do breakout).** Escreva **3 testes**
em `tests/` — escolha **Python + pytest** (mais simples de instalar) ou **Node + Mocha**
(veja o `boilerplate-mochachai/tests/1_unit-tests.js`).

Em Python:
```python
# tests/test_classificacao.py
from src.classificacao import calcular_pontos


def test_vitoria_vale_3_pontos():
    assert calcular_pontos(vitorias=2, empates=1, derrotas=0) == 7


def test_derrota_nao_da_ponto():
    assert calcular_pontos(vitorias=0, empates=0, derrotas=4) == 0


def test_time_sem_jogos_fica_com_zero():
    assert calcular_pontos(vitorias=0, empates=0, derrotas=0) == 0
```

Regra da turma: **rodar a suíte com `pytest` e colar a saída no README**. Depois,
**quebrar de propósito** uma função e rodar de novo: **pelo menos 1 teste deve
falhar**. Se todos passarem com o código quebrado, os testes **não estão testando
nada**.

**O que o professor diz enquanto circula:**

> *"Me mostra a suíte rodando. Agora quebra a função na sua frente e roda de novo. Se
> continua verde, seus testes são enfeite. Teste que nunca falha não é teste — é
> decoração."*

**Plano B (internet caiu):** os arquivos com bug proposital e os templates são **todos
locais**. O professor desliga o breakout e distribui no chat o código de 1 dos 6
exercícios para a turma caçar o bug **em dupla no chat** (um digita, o outro registra o
relatório). O `pytest` funciona offline se já estiver instalado.

#### Fase 4 — Projeto (15 min)

**Desafio: "Seu plano de testes e sua primeira suíte".**

Entregue:

1. `docs/plano-de-testes.md` — o plano completo com as **9 seções** do template.
2. `docs/casos-de-teste.md` — **5 casos de teste** no formato oficial.
3. `docs/bugs/BUG-001.md` — **1 bug reportado** no formato oficial, com severidade,
   prioridade e passos de reprodução. (Você pode achar um bug **no seu próprio
   projeto** — esse vale mais.)
4. `docs/matriz-rastreabilidade.md` — a **matriz requisito → caso de teste → status**,
   com a fórmula de cobertura embaixo:
   ```
   Cobertura = (Reqs com teste / total de Reqs) × 100
   ```
5. `tests/` — **3 testes automatizados** que rodam com um comando único
   (`pytest` ou `npm test`), com a **saída real** colada no `README.md`.
6. `docs/decisoes.md` — **+1 decisão**: *"Por que automação em Python e não em Java?"*

**Critério de pronto:**
- [ ] `docs/plano-de-testes.md` com as **9 seções** preenchidas
- [ ] `docs/casos-de-teste.md` com **5 casos** no formato oficial
- [ ] `docs/bugs/BUG-001.md` com **severidade**, **prioridade** e **passos de reprodução**
- [ ] `docs/matriz-rastreabilidade.md` com a fórmula de cobertura
- [ ] **3 testes automatizados** em `tests/` que rodam com **1 comando**
- [ ] **Prova** de que os testes falham: saída colada no README
- [ ] `README.md` com a seção **"Como rodar os testes"**
- [ ] **4 commits** no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Duas salas apresentam **1 bug encontrado** e **1 teste automatizado**. A turma vota:
*"Qual dos dois bugs relatados é o mais grave?"* O professor usa a votação para
reforçar a diferença entre severidade e prioridade.

Volte ao **quiz de recuperação**: *"Severidade e prioridade são a mesma coisa?"*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Teste sem resultado esperado escrito antes** | O resultado esperado foi preenchido depois | Escreva o esperado **antes** de executar |
| **Teste que passa com código quebrado** | A suíte continua verde após mutar o código | O teste não está exercising nada. Teste **uma coisa** por vez |
| **Bug sem passos de reprodução** | Relato: "não funciona" | Escreva os passos numerados, o ambiente e a URL/arquivo |
| **Confundir severidade com prioridade** | Tudo marcado como "Crítico" | Severidade = impacto; prioridade = urgência. São **duas** colunas |
| **Confundir "não testado" com "passou"** | Status sempre `Pass` | Use os 4 status: `Pass`, `Fail`, `Blocked`, `Not Run` |
| **`AssertionError` sem saber o esperado** | `assert 7 == 10` | Escreva a asserção do lado certo: `assert resultado == 7` |
| **Teste que depende de internet** | Falha no CI | Use dados locais de `data/` (regra do módulo: **sem internet**) |
| **"Teste manual que ninguém executa"** | Plano com 40 casos, 0 executados | Plano com **5 casos** que rodam de verdade > plano com 40 que não rodam |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Plano de testes | 9 seções preenchidas |
| Casos de teste | 5 casos no formato oficial |
| Bug report | Severidade, prioridade e passos de reprodução |
| Matriz de rastreabilidade | Requisito → caso → status + fórmula de cobertura |
| Suíte automatizada | 3 testes, 1 comando, **falha comprovada** |
| Commits | 4 commits |
| Participação | Bug ou teste apresentado na Fase 5 |
| Pergunta de saída | "Qual a diferença entre severidade e prioridade?" |

**Pergunta de escrita:**
> "Você escreveu um teste que verifica se a média das notas é 7. O código da média está
> errado (divide por 2 em vez de 3). O teste passa mesmo assim. Por quê — e como você
> conserta?"
>
> **Resposta:** o teste está errado, não o código. Um teste que passa com a
> implementação quebrada é um **teste fraco**: ele não fixa o comportamento esperado,
> só repete o que o código faz. As causas mais comuns são:
> 1. **Asserção invertida ou tautológica** — `assert resultado == resultado` sempre passa.
> 2. **Valor esperado copiado da saída atual** — em vez de calculado na mão.
> 3. **Teste do detalhe errado** — ele verifica se a função **retorna um número**, e não
>    se o número está **certo**.
> O conserto é escrever o valor esperado **na mão**, a partir do enunciado:
> ```python
> def test_media_de_tres_notas():
>     assert media([8.0, 6.0, 7.0]) == 7.0   # (8+6+7)/3 = 7
> ```
> Com `media` dividindo por 2, o resultado seria `10.5` e o teste **falha**. A regra é:
> **se o teste nunca falha, ele não está testando**.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `qa-exercicios-praticos/casos-de-teste/exercicios-escrever-casos.md` | Exercícios de escrita de casos |
| `qa-exercicios-praticos/tecnicas-de-teste/exercicios-tecnicas-de-teste.md` | Boundary, equívoco, tabela de decisão |
| `qa-exercicios-praticos/api-testing/exercicios-de-api.md` | Teste de API e status HTTP |
| `qa-exercicios-praticos/sites-para-testar/portal-cliente` | Site real para testar (9 sites disponíveis) |
| `qa-exercicios-praticos/simulados/simulado-01-fundamentos.md` | Simulado com gabarito comentado (formativo) |
| `QualityHub/Documentação (Docs)/Tipos de Testes de Software.md` | Todos os tipos, em PT |
| `QualityHub/Documentação (Docs)/Testes de Aceitação.md` | Teste de aceitação, com exemplos reais |
| `QualityHub/Cases QA/` | Falhas reais: British Airways, NHS, Knight Capital, votação eletrônica |
| `listadetarefas_qualityAssurance/Testes manuais.md` | Exemplo de testes manuais documentados |
| `boilerplate-mochachai/tests/1_unit-tests.js` | Suíte unitária com Mocha + Chai |
| `Central-de-noticias/tests/test_gerar.py` | Teste real de um projeto real |
| `manual-qa-completo/docs/08/scripts/quality_gate.py` | Script de gate de qualidade |
| `manual-qa-completo/docs/09/scripts/kpi.py` | Script de KPIs de qualidade |
| `manual-qa-completo/docs/11/scripts/secret_scan.py` | Varredura de segredos no repositório |
| `QA_RUN/index.html` | 71 jogos de QA para treinar entre uma aula e outra |

### 🏠 Para casa

Escrever **3 casos de teste** a mais para `docs/casos-de-teste.md` (incluindo **1 caso
negativo** e **1 caso de borda**). Adicionar **2 testes automatizados**. Rodar a suíte e
colar a saída. **2 commits.**

### 🔗 Próximo módulo

[B9 — IA para Iniciantes](#b9)

<a id="b9"></a>

## Módulo 9 — IA para Iniciantes (Aula 9)

**Duração:** 90 min · **Aula 9 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar, em linguagem simples, o que é **aprendizado de máquina**, **rede neural**,
   **processamento de linguagem natural** e **visão computacional** — e saber quais
   problemas **cada uma resolve**.
2. Escrever **prompts estruturados** (papel, contexto, tarefa, formato, restrições) e
   **avaliar** a saída com uma rubrica simples.
3. Usar IA como **ferramenta** dentro do seu projeto, com **revisão humana obrigatória**
   e **privacidade garantida** (nenhum dado pessoal ou chave em prompt).

**Objetivo secundário:** saber dizer, em uma frase, por que **IA é ferramenta, não autora**.

**Entregável do módulo:** **1 feature do seu projeto com IA** (chatbot, gerador de
resumo, classificador ou Suggestions) + **1 documento de avaliação de prompt** com
**3 prompts testados, 1 saída avaliada por rubrica e 1 decisão de não usar IA**,
tudo versionado no repositório.

### 📚 Fontes no repositório

`ia-para-iniciantes/` — **15 módulos × 6 exercícios = 90 exercícios**, todos com
**"CRITÉRIOS DE AVALIAÇÃO"** e **"DICAS"**:

| Módulo | Conteúdo |
|---|---|
| `01_o_que_e_ia` | O que é IA, o que não é |
| `02_machine_learning` | Dados, treino, modelo, previsão |
| `03_redes_neurais` | Neurônio, camadas, pesos |
| `04_processamento_linguagem_natural` | Linguagem, tokens, embeddings, LLM |
| `05_visao_computacional` | Imagem, pixels, classificação, detecção |
| `06_prompt_engeneering` | Prompt, estrutura, zero-shot, cadeia de pensamento, erros comuns |
| `07_ias_assistentes` | Assistentes, chatbots, limites |
| `08_geracao_texto` | Geração de texto e summarize |
| `09_geracao_imagens` | Geração de imagens e limites |
| `10_api_de_ia` | Chamar uma API de IA |
| `11_ia_em_python` | IA dentro do seu código |
| `12_ia_e_etica` | Ética, vieses, privacidade, regulamentação, debate |
| `13_ia_no_cotidiano` | IA no dia a dia |
| `14_projeto_chatbot` | **Projeto: chatbot** |
| `15_projeto_analise_dados` | **Projeto: análise de dados** |

**Arquivos verificados:**
`ia-para-iniciantes/06_prompt_engeneering/exercicio_01_o_que_e_prompt.txt` ·
`exercicio_02_estrutura_prompt.txt` · `exercicio_04_cadeia_pensamento.txt` ·
`exercicio_05_erros_comuns.txt` ·
`ia-para-iniciantes/12_ia_e_etica/exercicio_01_o_que_e_etica_ia.txt` ·
`exercicio_02_vieses.txt` · `exercicio_03_privacidade.txt` ·
`exercicio_06_debate_etica.txt` ·
`ia-para-iniciantes/14_projeto_chatbot/exercicio_01_planejamento_chatbot.txt` ·
`exercicio_02_configuracao_api.txt` · `exercicio_05_teste_melhoria.txt` ·
`exercicio_06_apresentacao.txt`.

**Projetos reais com IA:**
`Central-de-noticias/` (pipeline **RSS → resumo → TTS → PWA**; `scripts/gerar.py`,
`noticias.json`, `resumo.txt`, `resumo.mp3`, `audio/sao-pedro-e-regiao-*.mp3` — a IA
transformando notícia em áudio para a seção da cidade) ·
`esporte-sao-pedro/` (Supabase + RLS + **Edge Functions** + IA; `supabase/functions/send-push/index.ts`,
`SUPABASE_SECURITY_SETUP.md`) ·
`qa-automation-framework/utils/data_generator.py` (geração de dados de teste) ·
`o-despertar-qa/` (site de conteúdo sobre IA e qualidade).

**Trilha web e slides:**
`laboratorio-tech-social/site/trilhas/adolescentes/05-iot.html` ·
`laboratorio-tech-social/materiais/slides/aula-teens-05-iot.html` ·
`laboratorio-tech-social/site/exercicios/estacao-meteo.html` ·
`laboratorio-tech-social/site/exercicios/simulador-robotica.html` ·
`laboratorio-tech-social/site/exercicios/verifica-noticia.html` ·
`laboratorio-tech-social/site/exercicios/gerador-dados.html`

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **IA (IA fraca)** | "Software que segue uma regra que o humano escreveu. Regras, não aprendizado." |
| **Aprendizado de máquina** | "O programa aprende a regra a partir de **exemplos**, não de instruções." |
| **Rede neural** | "Camadas de 'células' que ajustam um peso cada vez até a resposta melhorar." |
| **LLM** | "Modelo que prevê a próxima palavra. Surpreendentemente bom nisso." |
| **Prompt** | "O pedido. Quanto mais contexto, melhor a resposta." |
| **Alucinação** | "Resposta inventada com total confiança. O risco nº 1 da IA." |
| **Viés** | "A IA aprende o viés dos dados. Ela não corrige desigualdade sozinha." |
| **Prompt engineering** | "Escrever o pedido como um briefing, não como uma frase solta." |
| **Human in the loop** | "Ninguém publica saída de IA sem ler antes." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Vocês já usaram IA 200 vezes esta semana. Filtro de spam, mapa,
tradutor, recomendação de vídeo, teclado do celular prevendo a próxima letra. Hoje a
gente desmonta a máquina por dentro e, mais importante, aprende a **usar bem** — e a
usar com **responsabilidade**."*

**Demonstração ao vivo (5 min).** Compartilhe a tela. Abra o `Central-de-noticias/` e
mostre o pipeline:

```
RSS  ──►  scripts/gerar.py  ──►  resumo.txt  ──►  resumo.mp3  ──►  PWA (app.js + sw.js)
                                             └─► seção "São Pedro e região"
```

Diga: *"Esse pipeline lê as notícias, **resume** e **transforma em áudio**. É IA de
verdade, rodando em Python, num projeto de verdade, publicado no GitHub. Mas olha a
parte importante: a escolha da fonte, a curadoria e a publicação são **humanas**."*

**Quiz de recuperação (3 min).** *"Filtro de spam do e-mail é IA? E a calculadora do
celular?"* → Spam: sim (aprende com exemplos). Calculadora: não, é regra fixa.
Esse é o critério que separa IA de software comum.

#### Fase 2 — Exploração (20 min)

**Parte 1 — O mapa das 4 famílias de IA (7 min).** Escreva no quadro:

| Família | O que faz | Exemplo no nosso projeto |
|---|---|---|
| **Aprendizado de máquina** | Aprende regra a partir de dados | Prever se o time vai vencer, com base nos jogos anteriores |
| **Rede neural** | Many camadas ajustadas juntas | Reconhecer placa de trânsito em foto |
| **Processamento de linguagem (LLM)** | Entende e escreve texto | Resumir a newsletter do bairro |
| **Visão computacional** | Entende imagem | Ler o placar de um vídeo do time |

Diga: *"Regra de bolso: se o humano escreveu a regra, **não** é IA. Se o programa
aprendeu a regra olhando exemplos, é IA."*

**Parte 2 — Anatomia de um prompt (7 min).** Escreva o modelo de 6 partes:

```
1. PAPEL      → "Você é a Helena, da Escola de Aprendizado de São Pedro."
2. CONTEXTO   → "Recebemos a lista de 40 crianças inscritas na Oficina de Robótica."
3. TAREFA     → "Classifique cada inscrição em 'confirmada', 'lista de espera' ou 'incompleta'."
4. FORMATO    → "Responda em tabela Markdown com 3 colunas: nome, situação, motivo."
5. RESTRIÇÕES → "Não invente nomes. Se faltar informação, escreva 'dado faltando'."
6. EXEMPLO    → 1 exemplo de entrada e saída esperada.
```

Diga: *"As restrições são a parte que os adolescentes esquecem. Sem elas, a IA inventa.
E 'não invente' funciona melhor do que 'seja preciso' — instrução concreta vence
adjetivo."*

**Parte 3 — Alucinação e como usar o "checar antes de publicar" (6 min).** Mostre um
exemplo de resposta inventada e pergunte: *"Como você descobre isso antes de publicar?"*
Resposta: **fonte** (a IA não tem fonte), **verificação cruzada**, **humano no circuito**.

Diga: *"Regra da casa: **toda saída de IA passa por revisão humana antes de virar
público**. Se você não entendeu a frase que a IA escreveu, você não publica."*

#### Fase 3 — Mão na massa (30 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala define **1
feature de IA** para o projeto:

| Feature | O que faz | Base na trilha |
|---|---|---|
| **Sugestões de bairro** | Recomenda oficinas e aulas gratuitas com base no bairro do usuário | "Aulas Abertas" |
| **Resumo de notícia** | Resume a notícia do bairro em 3 tópicos | "Bot de Notícias do Bairro" (inspirado no `Central-de-noticias`) |
| **Classificador de prioridade** | Classifica uma denúncia de rua em "urgente / normal / baixa" | "Estação Clima" |
| **Gerador de treino** | Gera um treino de 20 minutos para a quadra | "Placar da Cidade" |
| **Tutor de estudos** | Explica um conceito de Python para iniciante | "Despertar Kids" (QA lúdica) |

**Atividade A — Testar 3 prompts (15 min dentro do breakout).** Cada aluno escreve
**3 prompts** usando o modelo de 6 partes, com **3 tarefas diferentes**:

1. Um que **falha** de propósito (sem contexto, ambíguo) — para ver a diferença.
2. Um **estruturado** (com papel, formato e restrições) — para ver a melhora.
3. Um que **peça explicação de um erro** do próprio código.

O aluno **cola as 3 respostas** em `docs/ia/prompts.md`.

**Atividade B — Avaliar com rubrica (10 min dentro do breakout).** Cada aluno avalia
**1 resposta** com a rubrica de 4 critérios:

| Critério | 0 | 1 | 2 |
|---|---|---|---|
| **Acerto** | Errado ou inventado | Parcialmente certo | Correto |
| **Formato** | Ignorou o pedido | Formato parcial | Formato exato |
| **Segurança** | Exponde dado pessoal | Dado genérico | Nenhum dado real |
| **Utilidade** | Inutilizável | Dá uma ideia | Dá uma ideia e próximo passo |

E escreve, obrigatoriamente, **1 caso em que NÃO deve usar IA** no seu projeto.

**O que o professor diz enquanto circula:**

> *"Me mostra o prompt burro e o prompt estruturado. Agora me mostra a diferença nas
> respostas. Se a diferença for zero, teu prompt estruturado ainda está falhando —
> provavelmente falta a restrição. E se a IA sugeriu um nome de aluno que não existe,
> isso é alucinação, e o que você faz com isso?"*

**Plano B (internet caiu):** o professor desliga o breakout e distribui no chat **3
prompts-modelo prontos** (um burro, um estruturado, um de correção de código) e as
**respostas esperadas** (escritas pelo professor). Cada aluno **reescreve e analisa** o
prompt no papel e registra a análise em `docs/ia/prompts.md`. A análise de prompt
funciona offline; só a chamada ao modelo precisa de internet.

#### Fase 4 — Projeto (20 min)

**Desafio: "IA no seu projeto, com revisão humana".**

Entregue:

1. `docs/ia/prompts.md` — os **3 prompts testados**, com as respostas, a **rubrica de
   avaliação** aplicada e a **decisão de não usar IA** em 1 caso.
2. `docs/ia/politica.md` — a **política de IA do projeto**, com 5 regras:
   ```
   1. Nenhum dado pessoal (nome, RG, endereço, telefone, foto) entra em prompt.
   2. Nenhuma chave de API no navegador do aluno. Variável de ambiente, sempre.
   3. Toda saída de IA é revisada por uma pessoa antes de ser publicada.
   4. Se a IA não souber, a resposta oficial é "não sei" — não invenção.
   5. A origem do dado (fonte pública) é citada junto com o resultado.
   ```
3. `src/ia_sugestoes.py` (ou o equivalente no seu stack) — **1 função** que recebe um
   **texto de entrada do usuário** e devolve uma **sugestão**, com o prompt **fixo no
   código** (versão do professor ou variável de ambiente) e **sem chave exposta**.
4. `tests/test_ia_sugestoes.py` — **1 teste** que verifica que a função **lida com
   entrada vazia** sem quebrar.

**Critério de pronto:**
- [ ] `docs/ia/prompts.md` com **3 prompts** (um falho, um estruturado, um de correção)
- [ ] Rubrica de **4 critérios** aplicada a **1 resposta**
- [ ] **1 decisão documentada de não usar IA**
- [ ] `docs/ia/politica.md` com as **5 regras**
- [ ] **1 função** com prompt **fixo no código**, **sem chave exposta**
- [ ] **1 teste** de entrada vazia
- [ ] **Zero** dado pessoal em qualquer arquivo do repositório
- [ ] **3 commits** no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Cada sala apresenta **1 prompt** e **1 resposta** (a do prompt burro e a do estruturado,
lado a lado, em 30 segundos). A turma vota no prompt melhor. O professor fecha com:

> *"Toda vez que vocês usarem IA no projeto final, essa política vai estar no
> repositório. Ela não é burocracia: é o que separa um projeto de `\"`open source\"` de
> um projeto de verdade."*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Prompt vago** | Resposta genérica, "posso ajudar com isso" | Use o modelo de 6 partes; diga o **formato** e as **restrições** |
| **Alucinação** | A IA inventou um dado (placar, lei, nome) | Peça **fonte**; verifique fora; se não confirmar, **não publique** |
| **Chave no navegador** | `sk-...` no `script.js` | Variável de ambiente no servidor; no GitHub Pages, **não use** chave de IA |
| **Dado pessoal no prompt** | "Meu nome é João, RG 123..." | Dado **fictício**. É proibido e é ilegal (LGPD) |
| **Confiar na saída** | O código publicado sem revisão | Human in the loop: **sempre** revisar |
| **Laço infinito de prompt** | A IA pergunta de volta | Dê contexto completo no **primeiro** prompt |
| **Ponto flutuante** | `0.30000000000004` | Formate com `:.2f` ou `round()` |

> ⚠️ **Regra legal da aula:** digitar nome, RG, endereço, telefone, foto ou e-mail real
> de qualquer pessoa em um prompt de IA **viola a LGPD** (veja
> [ANPD](https://www.gov.br/anpd/)). Na prática: use sempre os dados fictícios de
> `data/`. Isso não é exagero — é a mesma regra do módulo B11.

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| `docs/ia/prompts.md` | 3 prompts + rubrica aplicada + decisão de não usar |
| `docs/ia/politica.md` | 5 regras |
| `src/ia_sugestoes.py` | Prompt fixo, sem chave exposta |
| `tests/test_ia_sugestoes.py` | 1 teste de entrada vazia |
| Privacidade | Zero dado pessoal no repositório |
| Commits | 3 commits |
| Participação | Prompt apresentado na Fase 5 |
| Pergunta de saída | "Por que a IA é ferramenta e não autora?" |

**Pergunta de escrita:**
> "Você vai usar IA para sugerir oficinas gratuitas do bairro a partir do cadastro do
> usuário. O formulário pede nome completo, endereço e telefone. O que você manda no
> prompt e o que você tira do prompt?"
>
> **Resposta:** você manda **o mínimo**: o **bairro** (ou o CEP) e a **faixa etária**,
> porque é o que define a oferta de oficinas (as oficinas são por bairro e por faixa).
> Você **não** manda nome, endereço, telefone, RG, foto nem e-mail — nem para a IA, nem
> para o banco de dados público do projeto. Tecnicamente:
> ```python
> # ERRADO
> prompt = f"Usuário {nome} de {endereco}, telefone {telefone}. Sugira oficinas."
>
> # CERTO
> prompt = f"Usuário do bairro {bairro}, faixa etária {faixa}. Sugira oficinas gratuitas."
> ```
> A justificativa é dupla: **ética** (dado mínimo é princípio de privacidade) e
> **técnica** (dado a menos no prompt = menos chance de alucinação com nome e menos
> vazamento se o prompt for registrado). E a regra de ouro continua: a sugestão final
> passa por uma pessoa antes de virar resposta pública.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `ia-para-iniciantes/02_machine_learning/` | Dados, treino, modelo |
| `ia-para-iniciantes/04_processamento_linguagem_natural/` | Tokens, embeddings, LLM |
| `ia-para-iniciantes/08_geracao_texto/` | Geração de texto |
| `ia-para-iniciantes/10_api_de_ia/` | Chamar API de IA |
| `ia-para-iniciantes/11_ia_em_python/` | IA dentro do código |
| `ia-para-iniciantes/15_projeto_analise_dados/` | Projeto final de IA |
| `Central-de-noticias/scripts/gerar.py` | Pipeline real RSS → resumo → TTS |
| `Central-de-noticias/tests/test_gerar.py` | Teste do pipeline de IA |
| `esporte-sao-pedro/supabase/functions/send-push/index.ts` | Edge Function real com IA |
| `laboratorio-tech-social/site/exercicios/estacao-meteo.html` | Estação clima (base do projeto IoT) |
| `laboratorio-tech-social/site/exercicios/verifica-noticia.html` | Checagem de notícia (MIL) |
| `laboratorio-tech-social/site/exercicios/gerador-dados.html` | Gerar dados fictícios para treinar |

### 🏠 Para casa

Testar **2 prompts novos** e anexar ao `docs/ia/prompts.md`. Ler
`ia-para-iniciantes/12_ia_e_etica/exercicio_02_vieses.txt` e escrever **3 linhas**
sobre um viés que você já viu em um serviço do dia a dia. **2 commits.**

### 🔗 Próximo módulo

[B10 — Metodologias Ágeis (Scrum/Kanban)](#b10)

<a id="b10"></a>

## Módulo 10 — Metodologias Ágeis (Scrum/Kanban) (Aula 10)

**Duração:** 90 min · **Aula 10 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar as **3 regras do Scrum** (inspeção, adaptação, empirismo) e a diferença
   entre **Scrum** e **Kanban** em 1 minuto cada.
2. Operar um **quadro Kanban real** com colunas, **limite de trabalho em progresso
   (WIP)** e **cartões de histórico**.
3. Rodar uma **Sprint completa** de 1 semana: planejamento, daily, revisão, retrospectiva —
   com **métricas** (velocity ou lead time) registradas.

**Objetivo secundário:** entender que **metodologia é para o time, não para o
currículo** — e que a turma **vai usar** isso nas três aulas de projeto final.

**Entregável do módulo:** **1 quadro Kanban** (em `docs/kanban.md` ou no
GitHub) com **8 cartões**, **colunas com limite de WIP**, **1 cartão movido 3 vezes** e
**1 retrospectiva** documentada em `docs/retrospectiva.md` com **3 ações**.

### 📚 Fontes no repositório

`formacaoScrumMaster/` — **4 estudos de caso reais** + README (verificados):

| Arquivo | Caso |
|---|---|
| `Estudo de Caso Aplicando Metodologia Agil em QA.md` | Scrum aplicado especificamente a QA |
| `Estudo de Caso na ING BANK.md` | Scrum em banco de grande porte |
| `Estudo de Caso Spotfy.md` | Scrum na Spotify (o modelo Spotify) |
| `Estudo de caso Projeto Scrum Distribuído para Ferrovias Holandesas.md` | Scrum distribuído, times remotos |
| `README.md` | Objetivo do repositório: aprender na prática e **desenvolver pensamento crítico** sobre quando usar Scrum e quando não usar |

`_framework_Scrum/` — desafio de projeto **"Completando o Framework Scrum"**:
`README.md` (passo a passo de criar um quadro no Miro, exportar e entregar via GitHub) ·
`Bruno Bertin - Desafio de Projeto - SCRUM.jpg` (o diagrama do framework) ·
`config.json`.

**Complementos:**
`git-github-iniciantes/08_issues_e_projetos/README.md` (Issues e boards) ·
`git-github-iniciantes/11_trabalho_em_equipe/README.md` (pairing e revisão) ·
`qa-exercicios-praticos/simulacoes/cenarios-role-play.md` (simulação de papéis) ·
`qa-exercicios-praticos/perguntas-respostas/perguntas-entrevista-QA.md` (perguntas
de entrevista que cobrem processo).

**Trilha web e slides:**
`laboratorio-tech-social/site/trilhas/adolescentes/06-projeto.html` ·
`laboratorio-tech-social/materiais/slides/aula-teens-06-projeto.html` ·
`laboratorio-tech-social/site/exercicios/planilha.html` ·
`laboratorio-tech-social/site/exercicios/notas.html`

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Scrum** | "Um time pequeno, uma lista de desejos e uma caixa de tempo curta para entregar valor." |
| **Kanban** | "Fluxo contínuo: você puxa o próximo cartão quando termina o anterior." |
| **Sprint** | "Caixa de tempo de 1 semana. Dentro dela, o escopo não muda." |
| **Product Backlog** | "A lista ordenada de tudo que se quer ter. Sempre priorizada." |
| **Sprint Backlog** | "O que o time **se compromete** a fazer nesta Sprint." |
| **WIP (limite)** | "Quantos cartões podem estar em andamento **ao mesmo tempo**. Sem limite, tudo trava." |
| **Definition of Done** | "O que significa 'pronto'. Escrita **antes** de começar." |
| **Velocity** | "Quantos pontos a equipe entregou por Sprint. Serve para comparar, não para premiar." |
| **Retrospectiva** | "O que funcionou, o que não funcionou, o que a gente muda **amanhã**." |
| **Kanban: tempo de fluxo** | "Do começo ao fim. Se está crescendo, tem gargalo." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Vocês já trabalharam em time. Talvez no jogo da escola, na
feira, no grupo do WhatsApp. E provavelmente já chegaram na hora da entrega com
metade pronta, porque ninguém combinou o que era 'pronto'. Metodologia ágil é uma
forma barata de resolver isso: **nada começa sem saber quando termina**."*

**Demonstração ao vivo (5 min).** Compartilhe a tela. Mostre o quadro do projeto em
andamento (pode ser uma imagem ou o `docs/kanban.md` de um aluno anterior). Depois
mostre o quadro do GitHub de Issues (que a turma vai usar nas aulas de projeto):

```
| Coluna          | Regra                        | WIP |
|-----------------|------------------------------|-----|
| A Fazer         | tudo que ainda não começou   |  —  |
| Em Progresso    | máximo 2 cartões                |  2  |
| Em Revisão      | máximo 1                     |  1  |
| Concluído       | mover para a direita quando pronto |  -  |
```

Diga: *"Repare no WIP. É a parte que ninguém faz. Se você deixa 10 cartões 'em
progresso', ninguém está terminando nada. Limite é o que cria velocidade."*

**Quiz de recuperação (3 min).** *"Qual a diferença entre Sprint e prazo final?"* →
Sprint é uma **caixa de tempo** de trabalho com escopo Combinado; prazo final é só a
data. *"Scrum ou Kanban, qual você usaria num time de 1 pessoa só?"* → Kanban
(menos ceremony, mais fluxo).

#### Fase 2 — Exploração (20 min)

**Parte 1 — Scrum em 1 diagrama (7 min).** Escreva no quadro:

```
        PRODUCT BACKLOG (lista priorizada do PO)
                    │
                    ▼  Planning: o time escolhe o que cabe na Sprint
        SPRINT BACKLOG (compromisso do time)
                    │
                    ▼  Sprint de 1 semana (scopo travado)
        INCREMENTO (algo que funciona e pode ser mostrado)
                    │
   Daily (15 min) ──┤  Revisão (stakeholder vê o incremento)
                    │  Retrospectiva (o time melhora o processo)
```

Explique os **3 papéis**: **Product Owner** (prioriza e decide o "quê"),
**Scrum Master** (cuida do processo e remove impedimentos), **Time de
Desenvolvimento** (faz). Diga: *"Numa equipe escolar, quase sempre: 1PO = o professor,
1Scrum Master = um aluno que gira o quadro, e o resto = time de desenvolvimento."*

**Parte 2 — Kanban em 4 regras (7 min).** Escreva:

1. **Visualize o trabalho** (quadro com colunas).
2. **Limite o trabalho em progresso** (WIP por coluna).
3. **Gerencie o fluxo** (mover para a direita é o trabalho; a coluna "pronto" tem prazo).
4. **Meça e melhore** (tempo de fluxo por cartão).

Diga: *"Scrum trabalha em **caixas de tempo**. Kanban trabalha em **fluxo contínuo**.
Muita equipe usa os dois: Scrum para planejar a Sprint, Kanban para o dia a dia. Não é
heresia. É o que a maioria dos times faz."*

**Parte 3 — Kanban + GitHub na prática (6 min).** Mostre:

```bash
# cartões = issues
# colunas = labels
# WIP = limite declarado no README do quadro
```

E a etiqueta de label: `status: a-fazer`, `status: em-progresso`, `status: em-revisao`,
`status: pronto`. Diga: *"O GitHub já é o seu quadro. Não precisa de ferramenta paga.
Issues + Labels + Milestones fazem tudo que a gente precisa."*

#### Fase 3 — Mão na massa (30 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala vira **um
time SCRUM** de verdade:

| Papel | Quem (dentro da sala) |
|---|---|
| Product Owner | O professor (por breakout) ou o aluno mais velho |
| Scrum Master | Um aluno que gira o quadro |
| Time de Desenvolvimento | Os demais (3–4) |

**Atividade A — Montar o quadro (10 min dentro do breakout).** Cada sala cria
`docs/kanban.md`:

```markdown
# Quadro Kanban — <Nome do Projeto>

| Coluna | WIP | Cartões |
|---|---|---|
| A Fazer | — | #12 Aulas Abertas: cadastro de oficinas · #13 Placar: tabela de classificação · ... |
| Em Progresso | 2 | #9 Leitura do CSV de ruas |
| Em Revisão | 1 | #7 Landing page |
| Concluído | — | #4 README inicial · #5 Estrutura de pastas |
```

Regras: **8 cartões** no total, **WIP declarado** em cada coluna, cada cartão com
**ID**, **título**, **responsável** e **estimativa em pontos** (1, 2, 3, 5, 8).

**Atividade B — Simular uma Sprint (12 min dentro do breakout).** Com o quadro pronto,
a sala simula **3 dias de Sprint**:

- **Planning (5 min):** o PO escolhe os cartões que somam **≤ 8 pontos** e move para
  "Em Progresso".
- **Daily (3 min):** cada um fala em **1 minuto**: o que fiz, o que vou fazer, o que
  travou. O Scrum Master **anota** os impedimentos em `docs/impedimentos.md`.
- **Revisão (4 min):** o PO "aceita" ou "rejeita" cada cartão — e o time descobre que
  **2 cartões estavam DoD errada** (isso vai acontecer, é o objetivo).

**Atividade C — Retrospectiva (8 min dentro do breakout).** Formato **"Come - Parar -
Continuar"**, em `docs/retrospectiva.md`:

```markdown
# Retrospectiva — Sprint 1

## Começamos a fazer
- ...
## Paramos de fazer
- ...
## Continuamos fazendo
- ...
## 3 AÇÕES (com responsável e prazo)
1. ...
2. ...
3. ...
```

**O que o professor diz enquanto circula:**

> *"Me mostra o WIP da coluna 'Em Progresso'. Se tem 4 cartões e o limite é 2, vocês
> estão quebrando a própria regra. E me mostra as 3 ações da retrospectiva: 'ser mais
> organizado' não é uma ação. 'Ninguém começa cartão novo sem abrir issue' é."*

**Plano B (internet caiu):** o quadro pode ser feito **inteiro em Markdown** no
repositório local, sem GitHub. O professor desliga o breakout e distribui o modelo de
`docs/kanban.md` no chat; cada sala preenche à mão. A simulação de Sprint (Planning,
Daily, Revisão) é **falada**, não precisa de ferramenta. Só o espelhamento no GitHub
fica para depois.

#### Fase 4 — Projeto (20 min)

**Desafio: "Seu time entrega".**

Cada aluno (ou cada dupla, se preferir) monta o quadro do **seu projeto de capstone**,
já com as histórias reais:

1. `docs/kanban.md` — quadro com **8 cartões**, **WIP por coluna**, cartões com ID,
   responsável, estimativa e **Definition of Done**.
2. `docs/definition-of-done.md` — a DoD do projeto, com **5 itens verificáveis**
   (ex.: "tem README", "tem 3 testes que passam", "está no GitHub Pages",
   "não tem dado pessoal", "tem licença MIT").
3. `docs/retrospectiva.md` — a retrospectiva da Sprint 0 (a preparação), com **3 ações**.
4. `docs/decisoes.md` — **+1 decisão**: *"Por que Scrum e não Kanban neste projeto?"*
   (ou o contrário — a justificativa vale igual).

**Critério de pronto:**
- [ ] `docs/kanban.md` com **8 cartões** e **WIP declarado** em cada coluna
- [ ] Cada cartão com **ID, título, responsável, estimativa**
- [ ] `docs/definition-of-done.md` com **5 itens verificáveis**
- [ ] `docs/retrospectiva.md` com **Começar / Parar / Continuar** e **3 ações** com responsável
- [ ] `docs/decisoes.md` com a justificativa Scrum × Kanban
- [ ] **3 commits** no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Duas salas apresentam o quadro. A turma responde: *"O WIP de vocês respeita o limite?"*
O professor fecha com a pergunta que abre o B11:

> *"Vocês estão organizando o trabalho de vocês. Mas e o trabalho dos outros? O que
> acontece quando alguém pega o que vocês fizeram, copia, e publica com o nome dele?"*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Sprint que muda de escopo no meio** | O backlog cresce todo dia | Regra do Scrum: o escopo da Sprint **não** muda. O que entra, entra |
| **Sprint sem Definition of Done** | "Acho que está pronto" | Escreva a DoD **antes** da Sprint. Sem ela, "pronto" vira opinião |
| **WIP ignorado** | 6 cartões em "Em Progresso" numa coluna com limite 2 | Limite existe para **parar** de começar. Respeite o número |
| **Daily de 30 minutos** | A daily virou reunião de status | Daily é **15 minutos**, de pé, com 3 perguntas |
| **Retrospectiva sem ação** | "Foi legal, vamos melhorar" | Ação precisa de **responsável** e **prazo**. Sem os dois, não é ação |
| **Velocity usada como meta individual** | "Você fez só 3 pontos essa Sprint" | Velocity é do **time**, não da pessoa. Nunca use para premiar |
| **Kanban sem limite** | Tudo "em progresso" para sempre | Sem WIP, o gargalo aparece como atraso no fim |
| **Scrum em equipe de 1 pessoa** | Cerimônia sem interlocutor | Use Kanban. Metodologia serve à situação |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| `docs/kanban.md` | 8 cartões, WIP declarado, cartões completos |
| `docs/definition-of-done.md` | 5 itens verificáveis |
| `docs/retrospectiva.md` | Formato correto + 3 ações com responsável |
| `docs/decisoes.md` | Justificativa Scrum × Kanban |
| Simulação de Sprint | Planning, Daily e Revisão executados no breakout |
| Commits | 3 commits |
| Participação | Quadro apresentado na Fase 5 |
| Pergunta de saída | "Para que serve o limite de WIP?" |

**Pergunta de escrita:**
> "Sua equipe está no meio de uma Sprint de 1 semana. Na terça-feira, o Product Owner
> chega com uma urgência nova e quer incluir mais 2 cartões. O que o time faz?"
>
> **Resposta:** o time **não** muda o escopo da Sprint. O PO pode, sim, **priorizar de
> novo o Product Backlog** — a lista do que virá depois fica mais correta. Mas os itens
> novos esperam a próxima Sprint. Se a urgência for real e inadiável, há duas saídas
> legítimas: (1) **cancelar a Sprint** e recomeçar com o novo escopo, ou (2) **tirar
> um item já quase pronto** do escopo e devolver ao backlog, para caber os 2 novos.
> O que **não** pode é meio caminho: a Sprint vira "Sprint mais 2", o time nunca termina,
> e a velocidade cai — mas o problema é organizacional, não individual. Imediatamente
> depois, o time registra isso na **retrospectiva**, porque foi uma lição aprendida sobre
> priorização.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `formacaoScrumMaster/Estudo de Caso Spotfy.md` | O modelo Spotify: papéis flexíveis |
| `formacaoScrumMaster/Estudo de Caso na ING BANK.md` | Scrum em grande escala |
| `formacaoScrumMaster/Estudo de Caso Aplicando Metodologia Agil em QA.md` | Ágil aplicado especificamente a QA |
| `formacaoScrumMaster/Estudo de caso Projeto Scrum Distribuído para Ferrovias Holandesas.md` | Time remoto — muito parecido com a nossa aula online |
| `_framework_Scrum/README.md` | Desafio de framework Scrum (quadro, exportação e entrega via GitHub) |
| `_framework_Scrum/Bruno Bertin - Desafio de Projeto - SCRUM.jpg` | Diagrama do framework |
| `git-github-iniciantes/08_issues_e_projetos/README.md` | Issues, labels e boards |
| `git-github-iniciantes/11_trabalho_em_equipe/README.md` | Pairing e revisão de código |
| `qa-exercicios-praticos/simulacoes/cenarios-role-play.md` | Simulação de papéis (PO, QA, dev) |
| `laboratorio-tech-social/site/exercicios/planilha.html` | Planilha de controle |

### 🏠 Para casa

Converter o quadro de `docs/kanban.md` em **issues reais no GitHub**, com as **labels**
`status:` e o **WIP declarado** no `README.md`. Escolher **3 cartões** e fazer **1
commit** por cartão. **3 commits.**

### 🔗 Próximo módulo

[B11 — Cibersegurança, Ética e Paradigmas](#b11)

<a id="b11"></a>

## Módulo 11 — Cibersegurança, Ética e Paradigmas (Aula 11)

**Duração:** 90 min · **Aula 11 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Reconhecer **phishing, golpe do Pix,Senha fraca e vazamento de dados** — e saber
   **o que fazer** em cada caso.
2. Aplicar **7 regras de segurança** ao seu próprio repositório (segredos fora do Git,
   `.gitignore`, validação de entrada, dados fictícios, dependências confiáveis).
3. Discutir **dilemas éticos** de tecnologia (IA e emprego, privacidade, desigualdade
   digital, saúde) e **assumir uma posição** com justificativa.
4. Escrever a **Política de Segurança e Ética** do seu projeto final.

**Objetivo secundário:** entender que **segurança é responsabilidade de quem escreve
o código** — inclusive de quem tem 15 anos.

**Entregável do módulo:** **`docs/seguranca-e-etica.md`** com 7 regras de segurança,
1 política de dados do projeto, 1 análise de risco e 1 posição ética — mais **1 quiz
respondido** e **1 commit**.

### 📚 Fontes no repositório

`pensamento_computacional/13_ciberseguranca/` — **6 exercícios**:

| Arquivo | Sobre |
|---|---|
| `exercicio_01_senhas.txt` | Senhas fortes, geradores, bases de dados vazadas |
| `exercicio_02_phishing.txt` | Phishing: e-mail, SMS, redes sociais |
| `exercicio_03_golpes.txt` | Golpes do Pix, golpe da lotérica, falso sequestro |
| `exercicio_04_boas_praticas.txt` | Boas práticas de segurança digital |
| `excenario_05_criptografia.txt` → `exercicio_05_criptografia.txt` | Criptografia, hash, chave pública |
| `exercicio_06_simulacao.txt` | Simulação de ataque e defesa |

`pensamento_computacional/15_etica_sociedade/` — **6 exercícios**:
`exercicio_01_dilemas.txt` (dilemas com dois lados) ·
`exercicio_02_privacidade.txt` ·
`exercicio_03_ia_emprego.txt` ·
`exercicio_04_desigualdade.txt` ·
`exercicio_05_saude.txt` ·
`exercicio_06_manifesto.txt` (o próprio manifesto do projeto).

**Complementos:**
`pensamento_computacional/14_tecnologias_emergentes/` (IA, IoT, nuvem, blockchain, big
data, futuro) · `pensamento_computacional/12_redes_internet/` (IP, DNS, protocolos,
infraestrutura) · `pensamento_computacional/09_sistema_binario/` ·
`manual-qa-completo/docs/11/scripts/secret_scan.py` (varredura de segredos no
repositório) · `laboratorio-tech-social/docs/seguranca-criancas.md` (checklist de
segurança para menores) · `esporte-sao-pedro/SUPABASE_SECURITY_SETUP.md` (setup real de
segurança de banco) · `esporte-sao-pedro/supabase-rls-admin.sql` (Row Level Security).

**Lúdico e interativo:**
`laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` ·
`laboratorio-tech-social/site/exercicios/gerador-senhas.html` ·
`laboratorio-tech-social/site/exercicios/validador-regex.html` ·
`laboratorio-tech-social/site/exercicios/verdadeiro-falso.html` ·
`laboratorio-tech-social/site/exercicios/verifica-noticia.html` (checagem de notícia) ·
`laboratorio-tech-social/site/exercicios/quiz-teens.html` ·
`o-despertar-qa/src/pages/Bug Hunter A Aventura QA.hvp52.js`.

**Links oficiais:**
[ANPD — Autoridade Nacional de Proteção de Dados](https://www.gov.br/anpd/) ·
[ECA — Estatuto da Criança e do Adolescente](https://www.planalto.gov.br/ccivil_03/leis/l8069.htm)

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Senha** | "Comprimento vence complexidade. `senha123` é mais fraca que `chave-longa-14`." |
| **Phishing** | "A mensagem não mente sobre o serviço. Ela mente sobre **quem** é o serviço." |
| **Hash** | "Não tem volta. Guarda a **impressão** da senha, não a senha." |
| **Segredo** | "Qualquer coisa que, se vazar, dá acesso. Chave de API, senha, `.env`." |
| **Validação de entrada** | "Não confie em nada que veio de fora: do formulário, da URL, do arquivo." |
| **LGPD** | "Dado pessoal tem dono. Coletar menos, guardar menos, avisar." |
| **Dilema ético** | "As duas opções têm custo em gente. O trabalho é escolher e justificar." |
| **Viés** | "O modelo aprende a desigualdade dos dados se ninguém a questionar." |
| **Privilégio mínimo** | "Acesse só o que precisa. Nem seu time, nem o banco, nem a IA." |
| **Prontidão** | "Saber reagir antes do incidente é metade da defesa." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Hoje é a aula mais importante do curso, e provavelmente a que
vocês vão lembrar. Não por causa de tecnologia: por causa de **poder**. Vocês já
publicaram um projeto na internet com o nome de vocês. Daqui em diante, o que vocês
publicarem é do mundo. Então vamos falar de como proteger."*

**Demonstração ao vivo (5 min).** Compartilhe a tela. Abra
`laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` e rode o quiz ao
vivo com a turma (reacts no chat). Depois mostre **1 phishing** fictício na lousa:

```
URGENTE — São Pedro Digital
Seu cartão foi bloqueado! Regularize em:
https://sao-pedro-valida.com/login
```

Pergunte: *"Três sinais de golpe. Quais?"* →
(1) urgência; (2) domínio parecido, não oficial; (3) pede dado pessoal.

Diga: *"Repare que o golpe funciona **quando você tem pressa**. Vão querer que você:
você pede dados que a sua voz, na pressa, entrega."*

**Quiz de recuperação (3 min).** *"Qual a diferença entre `git` e `GitHub`? E por que
`git` sozinho já resolve 90% dos problemas de versionamento?"* →
`git` é o programa de versionamento (local); `GitHub` é o servidor onde o repositório
fica (nuvem). Git funciona **offline**.

#### Fase 2 — Exploração (20 min)

**Parte 1 — As 4 ameaças que você vai encontrar de verdade (8 min).**

| Ameaça | Como aparece | O que fazer |
|---|---|---|
| **Senha fraca** | Mesma senha em 5 lugares | Gerador de senha + **gerenciador** |
| **Phishing** | Mensagem com urgência e link | Não clicar; conferir o domínio; digitar o endereço à mão |
| **Golpe do Pix** | "me paga que eu te transfiro" | **Nunca** transfira antes de receber; confirme por outro canal |
| **Vazamento de segredo** | Chave no GitHub | Rotacionar a chave **imediatamente** + remover do histórico |

Diga: *"A quarta é a mais perigosa para vocês, porque é a que **vocês** vão produzir.
Um `.env` commitado vaza em segundos: robôs varrem o GitHub inteiro procurando
`sk_`, `AIza`, `eyJ`."*

**Parte 2 — As 7 regras do repositório (7 min).** Escreva no quadro e explique:

```
1. SEGREDO NUNCA NO GIT      → .env, chave, senha: só variável de ambiente
2. .gitignore SEMPRE         → __pycache__/, *.pyc, .env, node_modules/, *.db
3. DADOS FICTÍCIOS           → nada de nome, RG, endereço, telefone de pessoa real
4. VALIDAR TODA ENTRADA      → formulário, URL e arquivo são "entrada não confiável"
5. DEPENDÊNCIA CONFIÁVEL     → leia o README do pacote antes de instalar
6. PERMISSÃO MÍNIMA          → só o que o projeto precisa
7. BACKUP E .gitignore       → antes de operação destrutiva
```

Mostre o `manual-qa-completo/docs/11/scripts/secret_scan.py` rodando no repositório do
aluno:

```bash
python manual-qa-completo/docs/11/scripts/secret_scan.py
```

Diga: *"Olha o que ele acha. Se aparecer qualquer chave, a gente **rotaciona** na hora.
Apagar o commit não apaga o histórico."*

**Parte 3 — Ética: o dilema e o custo em gente (5 min).** Use os dilemas de
`pensamento_computacional/15_etica_sociedade/exercicio_01_dilemas.txt`:

**Dilema 1 — A IA e o emprego.**
> A escola municipal de São Pedro abre 1 vaga de professor de programação. Uma
> ferramenta de IA já dá 80% do que se pede. A vaga ainda é necessária?

**Dilema 2 — Os dados da comunidade.**
> O projeto "Placar da Cidade" quer um ranking dos bairros por nível de
> insegurança, para ajudar na segurança. Mas 2 equipes do bairro não querem que os
> dados dos atletas sejam públicos. Faz o ranking?

Diga: *"Um dilema ético **não tem resposta certa**. Tem resposta **justificada**. O que
o professor vai avaliar é a qualidade do argumento e se você ouviu o lado que você
não escolheu."*

#### Fase 3 — Mão na massa (30 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala recebe **um
cenário** diferente (o professor sorteia por breakout):

| Cenário | O que a sala precisa produzir |
|---|---|
| **A** | Um **e-mail de phishing** fictício que engane um colega — e o **plano de defesa** (3 ações) |
| **B** | Uma **política de dados** para o projeto: o que coleta, por que, quem vê, quando apaga |
| **C** | Uma **análise de risco** do projeto: 3 riscos (probabilidade × impacto) e 2 mitigações |
| **D** | Uma **posição ética** sobre o dilema 1 (IA e emprego), com 3 argumentos contra e 2 a favor |

**Atividade A — Cenário (15 min dentro do breakout).** A sala produz o entregável do
cenário, por escrito, com **dados de São Pedro/SP** quando couber.

**Atividade B — Rodar o `secret_scan.py` (10 min dentro do breakout).** Cada aluno roda
o script no próprio repositório e **corrige** o que ele encontrar. Se o repositório
estiver limpo, o aluno **planta um segredo falso** num arquivo de teste (ex.:
`api_key = "TESTE-NAO-USAR-123"`) para ver o script funcionar, e **remove em seguida**.

**Atividade C — Quiz de cibersegurança (5 min dentro do breakout).** Rodem
`laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` em dupla, um por
dispositivo, e registrem a pontuação em `notas/`.

**O que o professor diz enquanto circula:**

> *"Me mostra a sua senha de teste. Ela tem mais de 12 caracteres, não é o nome do
> cachorro e não é '123456'. Agora me mostra: onde está a chave do seu projeto? Se
> ela está em arquivo que vai para o GitHub, a gente tem um problema — e o problema é
> de segunda-feira, não de sexta."*

**Plano B (internet caiu):** o `secret_scan.py` é **offline** (roda no Python local) e o
quiz de cibersegurança é um HTML **local**. O professor desliga o breakout, mantém o
`secret_scan.py` rodando em cada máquina e distribui os **4 cenários** em texto no
chat, para as salas resolverem por escrito.

#### Fase 4 — Projeto (20 min)

**Desafio: "A política de segurança e ética do seu projeto".**

Entregue `docs/seguranca-e-etica.md` com:

1. **7 regras de segurança** (as do quadro), cada uma com **como aplicar no seu projeto**.
2. **Política de dados**:
   - Que dados o projeto coleta?
   - Esses dados são **reais, fictícios ou públicos**?
   - Quem pode ver?
   - Quando são apagados?
   - A base legal é consentimento, interesse público ou outro? (cite a
     [LGPD](https://www.gov.br/anpd/))
3. **Análise de risco** — tabela com **3 riscos**:
   | Risco | Probabilidade | Impacto | Mitigação |
   |---|---|---|---|
   | Chave de API exposta no front-end | Média | Alto | Variável de ambiente + servidor |
   | Dados pessoais coletados sem consentimento | Baixa | Alto | Usar apenas dados fictícios |
   | Dependência abandonada com vulnerabilidade | Média | Médio | Fixar versão + atualizar mensalmente |
4. **Posição ética** — 1 parágrafo: *"Acredito que …, porque …, e o risco para … é …"*.
5. `docs/decisoes.md` — **+1 decisão** sobre privacidade ou segurança.

**Critério de pronto:**
- [ ] **7 regras** de segurança, cada uma com aplicação concreta no projeto
- [ ] Política de dados com **5 respostas** (o que, por que, quem vê, quando apaga, base legal)
- [ ] Análise de risco com **3 riscos** e **3 mitigações**
- [ ] **1 posição ética** com justificativa
- [ ] `secret_scan.py` executado **sem achado** no repositório
- [ ] `docs/decisoes.md` atualizado
- [ ] **3 commits** no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Duas salas apresentam **1 risco** e **1 mitigação** de cada um dos 4 cenários. A turma
vota no **risco mais bem avaliado**. O professor registra os pontos no quadro e
destaca:

> *"Isso que vocês fizeram agora é o que separates o projeto de vocês do projeto de
> alguém que copiou. E é o que vai aparecer na banca do Showcase."*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Segredo commitado** | `secret_scan.py` aponta chave | **Rotacione** a chave, remova do histórico, adicione ao `.gitignore` |
| **Apagar o commit não apaga o segredo** | O segredo continua no `git log` | O histórico é público para sempre. Rotacionar é obrigatório |
| **Senha `123456`** | Ela está em qualquer lista de senhas vazadas | Use gerador: `laboratorio-tech-social/site/exercicios/gerador-senhas.html` |
| **Clicar em link de mensagem** | "Ganhe um Pix" | Confirme o domínio; digite o endereço à mão |
| **Colocar dado real no formulário** | Campo "seu nome completo" no site público | Dado fictício. A regra vale para o site **público** |
| **Confiar na validação do HTML** | `required` que o JS ignora | Valide **no servidor** também; no front-end, é conveniência |
| **Ignorar o `E` do `EM` (LGPD)** | Projeto coletando sem avisar | LGPD vale para qualquer tratamento de dado pessoal |
| **Achar que hash protege tudo** | "Guardei a senha com hash, está seguro" | Hash não protege senha fraca (ataque de dicionário). Use `bcrypt`/`argon2` |
| **Coletar mais do que precisa** | Formulário pedindo endereço e telefone para um ranking | **Privilégio mínimo**: peça o mínimo |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| `docs/seguranca-e-etica.md` | 7 regras + política de dados + 3 riscos + posição ética |
| `secret_scan.py` | Sem achado no repositório |
| Quiz de cibersegurança | Registrado em `notas/` |
| `docs/decisoes.md` | Nova decisão de privacidade/segurança |
| Commits | 3 commits |
| Participação | Cenário apresentado na Fase 5 |
| Pergunta de saída | "Por que apagar o commit não resolve um vazamento de chave?" |

**Pergunta de escrita:**
> "Você commits uma chave de API no seu repositório público. 20 minutos depois você
> percebe e apaga o commit. O que ainda está errado, e o que você precisa fazer?"
>
> **Resposta:** **três coisas** ainda estão erradas:
> 1. **O segredo continua exposto.** O `git log` guarda tudo; o commit apagado continua
>    no histórico e qualquer pessoa pode achá-lo com `git log` ou no histórico do
>    repositório. Além disso, robôs de mineração de segredos já podem ter copiado a chave.
> 2. **A chave está comprometida.** O único jeito de "limpar" o vazamento é
>    **rotacionar**: gerar uma chave nova no painel do serviço, desligar a antiga e
>    atualizar a configuração do projeto com a nova.
> 3. **O procedimento está errado.** A correção é: (a) revogar e rotacionar a chave,
>    (b) remover o arquivo do histórico com `git filter-repo` ou reescrever o
>    repositório, (c) adicionar o arquivo ao `.gitignore`, (d) **nunca mais** commitar
>    segredo — use variável de ambiente (`.env`, que fica no `.gitignore`) ou secrets do
>    CI. E registre o incidente no `docs/seguranca-e-etica.md`: em trabalho de verdade,
>    incidente se anota, não se esconde.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `pensamento_computacional/13_ciberseguranca/exercicio_05_criptografia.txt` | Hash, chave pública, simetria |
| `pensamento_computacional/13_ciberseguranca/exercicio_06_simulacao.txt` | Simulação de ataque e defesa |
| `pensamento_computacional/14_tecnologias_emergentes/exercicio_02_iot.txt` | IoT (base do projeto Estação Clima) |
| `pensamento_computacional/14_tecnologias_emergentes/exercicio_04_blockchain.txt` | Blockchain (e o que ele **não** resolve) |
| `pensamento_computacional/15_etica_sociedade/exercicio_06_manifesto.txt` | Escrever o manifesto do projeto |
| `laboratorio-tech-social/docs/seguranca-criancas.md` | Checklist de segurança para menores |
| `laboratorio-tech-social/site/exercicios/verifica-noticia.html` | Verificação de notícia (MIL) |
| `esporte-sao-pedro/SUPABASE_SECURITY_SETUP.md` | Setup real de segurança de backend |
| `esporte-sao-pedro/supabase-rls-admin.sql` | Row Level Security: cada usuário vê só o que é dele |
| `manual-qa-completo/docs/11/scripts/secret_scan.py` | Varredura de segredos |
| `manual-qa-completo/docs/10/PT/glossario.md` | Glossário QA PT/EN |

### 🏠 Para casa

Escrever o **manifesto do seu projeto** (1 página): o problema, quem éчё o usuário, o
que o projeto **faz** e o que ele **não faz**, os dados que usa e os princípios que
vocês seguem. Publicar em `docs/manifesto.md`. **2 commits.**

### 🔗 Próximo módulo

[B12 — Inglês Técnico para Programadores](#b12)

<a id="b12"></a>

## Módulo 12 — Inglês Técnico para Programadores (Aula 12)

**Duração:** 90 min · **Aula 12 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Ler e escrever os **blocos do dia a dia** em inglês: mensagem de commit, README,
   descrição de bug, comentário de código e mensagem de pull request.
2. Reconhecer os **erros do Python** e do **Git** em inglês **sem dicionário**, usando
   o padrão das frases.
3. Escrever o **README do projeto em inglês** (versão curta) e manter a **versão em
   português** — os dois no mesmo repositório.

**Objetivo secundário:** perder o medo de ler documentação. **Documentação em inglês é
o preço da entrada no mercado** — e o curso é gratuito justamente para que esse preço
não exclua ninguém.

**Entregável do módulo:** **`README.en.md`** (README completo do projeto em inglês) +
**1 glossário pessoal** (`docs/glossario.md`, no mínimo **30 termos** que você realmente
já encontrou) + **1 `CONTRIBUTING.md`** em inglês. **"Commit ou não existe"** e, a
partir de hoje, **"commit em inglês, se você conseguir"**.

### 📚 Fontes no repositório

`ingles-para-programadores/` — **15 módulos × 6 exercícios = 90 exercícios**:

| Módulo | Conteúdo | Arquivos verificados |
|---|---|---|
| `01_fundamentos` | Base de inglês técnico | — |
| `02_vocabulario_computacao` | Hardware, estruturas de dados, ações de programação | `exercicio_01_hardware_software.txt`, `exercicio_04_frases_tecnicas.txt` |
| `03_vocabulario_web` | HTML, CSS, JS, navegador, responsivo | — |
| `04_vocabulario_git` | Conceitos, comandos, mensagens de commit, PR, erros | `exercicio_03_mensagens_commit.txt`, `exercicio_04_pull_request.txt`, `exercicio_05_erros_git.txt` |
| `05_vocabulario_qa` | Testes, bugs, ágil, sprint, code review | `exercicio_03_agile.txt`, `exercicio_05_code_review.txt` |
| `06_leitura_documentacao` | MDN, Stack Overflow, GitHub, estrutura de docs | `exercicio_01_mdn.txt`, `exercicio_04_estrutura_docs.txt` |
| `07_verbos_tecnicos` | Verbos de dev, de comunicação, descrever processo | `exercicio_01_verbos_dev.txt`, `exercicio_03_descrever_processo.txt` |
| `08_comandos_ingles` | Ler mensagens de erro em inglês | — |
| `09_frases_comuns` | Frases do dia a dia | — |
| `10_listening_e_pronica` | Escuta e pronúncia | — |
| `11_escrita_tecnica` | README, documentação, commits, clareza | `exercicio_01_estrutura_readme.txt`, `exercicio_04_commits.txt` |
| `12_reunioes_e_comunicacao` | Daily, review, retrospectiva | — |
| `13_aprendizado_continuo` | Como continuar estudando | — |
| `14_projeto_ler_docs` | Projeto: ler documentação | — |
| `15_projeto_contribuir` | Projeto: contribuir com open source | — |

**Documentação real para treinar (tudo gratuito):**
[MDN — Mozilla Developer Network em PT-BR](https://developer.mozilla.org/pt-BR/) ·
[W3Schools](https://www.w3schools.com/) ·
[Python docs em PT-BR](https://docs.python.org/pt-br/3/) ·
[Pro Git em PT-BR](https://git-scm.com/book/pt-br/v2) ·
[SQLite](https://sqlitebrowser.org/) · [GitHub Docs](https://docs.github.com/).

**Trilha web e slides:**
`laboratorio-tech-social/site/exercicios/validador-regex.html` ·
`laboratorio-tech-social/site/trilhas/adolescentes/08-informatica.html` ·
`laboratorio-tech-social/site/exercicios/quiz-teens.html`

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Vocabulário técnico** | "Não precisa saber falar inglês. Precisa saber 300 palavras." |
| **Commit message** | "Verbo no imperativo + escopo: `fix(login): reject empty password`" |
| **README** | "A primeira impressão do projeto. Em inglês, ela alcança o mundo." |
| **Issue** | "Um problema registrado, com contexto. Em inglês, mais gente resolve." |
| **Bug report** | "Expected / Actual / Steps — essas 3 palavras resolvem 90% dos relatórios." |
| **Pull request** | "Compare, Review, Merge — o vocabulário do GitHub inteiro." |
| **Erro em inglês** | "Não traduzir palavra por palavra. Ler como frase: o que ele tentou fazer?" |
| **Gerúndio vs infinitivo** | "`running` (agora) e `to run` (a fazer). Tudo em inglês usa os dois." |
| **Chave de API** | "`API key` — e a resposta para 'the key is exposed' é 'rotate it'." |
| **Documentação** | "Se você não escreve, o outro escreve por você — e erra." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (5 min)

**Abertura (1 min).** *"Esta aula não é de inglês. É de **independência**. A documentação
que você vai precisar está em inglês. Os erros estão em inglês. O Stack Overflow está em
inglês. Se você desiste por causa do inglês, você desiste antes de começar."*

**Demonstração ao vivo (3 min).** Compartilhe a tela. Pegue uma mensagem de erro real:

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Leia em voz alta como frase: *"unsupported operand type (s) for plus: int and str"* →
*"Não é possível somar: um inteiro e um texto."* Depois mostre um erro do Git:

```
error: failed to push some refs to 'origin'
hint: Updates were rejected because the remote contains work that you do not have locally.
```

Traduza: *"O push foi recusado porque o servidor tem commits que você não tem.
Rode `git pull` e depois `git push`."*

Diga: *"Em 30 segundos eu traduzi dois erros que travam iniciante por horas. Não foi
mágica — foi **padrão**."*

**Quiz de recuperação (1 min).** *"Em inglês técnico, `commit`, `push` e `pull` — o que
significa cada um?"* → Gravar, Enviar, Trazer.

#### Fase 2 — Exploração (15 min)

**Parte 1 — Os 30 verbos que você mais usa (7 min).** Escreva no quadro:

| Verbo | Uso técnico | Frase pronta |
|---|---|---|
| `add` | adicionar | "Add the file to the stage" |
| `commit` | gravar | "Commit your changes" |
| `push` | enviar | "Push to the remote repository" |
| `pull` | trazer | "Pull the latest changes" |
| `merge` | juntar | "Merge the branch into main" |
| `fix` | corrigir | "Fix the null pointer error" |
| `add` (feature) | adicionar recurso | "Add the ranking page" |
| `remove` | remover | "Remove the unused function" |
| `update` | atualizar | "Update the dependencies" |
| `create` | criar | "Create the database schema" |
| `read` | ler | "Read the configuration file" |
| `write` | escrever | "Write the documentation" |
| `run` | executar | "Run the tests" |
| `test` | testar | "Test the login flow" |
| `deploy` | publicar | "Deploy to GitHub Pages" |
| `refactor` | refatorar | "Refactor the data loading function" |
| `document` | documentar | "Document the public API" |
| `review` | revisar | "Review the pull request" |
| `check` | conferir | "Check the acceptance criteria" |
| `build` | construir | "Build the project" |

Diga: *"Com esses 20 verbos você já escreve 90% dos commits e dos PRs do mundo."*

**Parte 2 — O formato das 4 mensagens que você vai escrever a semana toda (5 min).**

**Commit:**
```
fix(login): reject empty password instead of crashing
```
**Pull request:**
```
## What
Adds validation for empty passwords on the login form.

## Why
The form crashed with a 500 error when the field was left blank.

## How to test
1. Open /login
2. Submit the form with an empty password
3. Expect the message "Enter your password"
```
**Bug report:**
```
Title: Ranking page shows the wrong number of teams
Environment: Chrome, Windows 11, v0.1
Steps to reproduce:
  1. Open /ranking
  2. Expect 6 teams, see 5
Expected: 6 teams
Actual: 5 teams
Severity: High
```
**README (primeiras linhas):**
```
# São Pedro Team Ranking

A simple web app that shows the standings of the local youth football league.

## Why
Kids in our neighbourhood had no way to follow the season results.
```

Diga: *"Repare no **Why**. Quem lê seu PR não só quer saber o que você fez — quer
saber **por quê**. Uma frase de 'why' vale mais que dez de 'what'."*

**Parte 3 — Lendo erro sem dicionário (3 min).** Mostre o método em 3 passos:

```
1. ACHE O TIPO DO ERRO   → TypeError / NameError / SyntaxError / ValueError
2. ACHE O "ALVO"        → o que tentava somar, chamar, abrir
3. ACHE O "ESPERADO"    → o que o Python esperava naquele ponto
```

Exemplo:
```
ValueError: invalid literal for int() with base 10: 'abc'
```
→ tipo: `ValueError` · alvo: `int()` · esperado: um número na base 10 · recebido: `'abc'`.
Diga: *"Traduzido: 'o texto abc não pode virar número'. Fim. Você já sabe onde está o
erro: na linha do `int()`."*

#### Fase 3 — Mão na massa (35 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada sala tem um
"tradutor-chefe" (o aluno com melhor inglês) e os demais praticam.

**Atividade A — Caça ao erro (12 min dentro do breakout).** Cada sala recebe **4 erros
reais** (o professor distribui em texto no chat) e escreve para cada um:
1. O **tipo** do erro (em inglês).
2. A **tradução em 1 frase** em português.
3. A **linha provável** do código que causou.
4. A **correção** em código.

**Atividade B — Reescrever o projeto em inglês (18 min dentro do breakout).** Cada aluno
reescreve, em inglês:
- O **README** completo (o professor dá o modelo em PT, com as 7 seções do módulo B7).
- **5 mensagens de commit** das últimas aulas, já em inglês e no padrão
  `tipo(escopo): descrição`.
- **1 descrição de bug** no formato do bug report.
- **1 pull request** fictício, com as seções *What / Why / How to test*.

**Atividade C — Glossário pessoal (5 min dentro do breakout).** Cada aluno monta o
começo do `docs/glossario.md` com **10 termos** que **ele já encontrou** de verdade
(neste curso, no erro do Python, no GitHub). Formato:

```markdown
| Term | Significado | Onde vi |
|---|---|---|
| commit | gravação de um instantâneo do código | aula B7 |
| traceback | sequência de erros que aponta a linha do problema | aula B3 |
```

**O que o professor diz enquanto circula:**

> *"Me mostra a sua mensagem de commit em inglês. Começa com verbo no imperativo? Tem
> escopo entre parênteses? Se você escreveu 'I have fixed the bug', reescreve: 'fix:
> handle empty list'. Commit em inglês é curto. Sempre."*

**Plano B (internet caiu):** o glossário e a reescrita do README são **100% offline**
— só precisam de dicionário (o do celular serve). O professor desliga o breakout,
distribui os 4 erros em texto no chat e mantém a reescrita em andamento. Se ninguém tiver dicionário,
use os 20 verbos do quadro do professor, que estão no chat.

#### Fase 4 — Projeto (25 min)

**Desafio: "O projeto que fala com o mundo".**

Entregue:

1. **`README.en.md`** — o README completo do projeto em inglês, com as 7 seções:
   *What it is · Why · How to run · What's inside · How it was built · Contributing ·
   License*. **Mínimo 400 palavras** em inglês.
2. **`CONTRIBUTING.md`** — guia de contribuição em inglês (5 seções: report bug ·
   suggest feature · set up locally · commit convention · code of conduct).
3. **`docs/glossario.md`** — **30 termos** do seu glossário pessoal, com a coluna
   "onde vi".
4. **10 mensagens de commit** do projeto **reescritas em inglês** (não precisa reescrever
   o histórico — basta ter a lista em `docs/commits-em-ingles.md`).
5. **`docs/decisoes.md`** — **+1 entrada**: *"Por que mantemos o README em dois idiomas"*.

**Critério de pronto:**
- [ ] `README.en.md` com as **7 seções** e **≥ 400 palavras** em inglês
- [ ] `CONTRIBUTING.md` com as **5 seções**
- [ ] `docs/glossario.md` com **30 termos** e a coluna "onde vi"
- [ ] `docs/commits-em-ingles.md` com **10 mensagens** no padrão `tipo(escopo): descrição`
- [ ] `docs/decisoes.md` com a justificativa do README bilíngue
- [ ] Zero erro de digitação nos títulos e nas seções (releia em voz alta)
- [ ] **3 commits** no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Duas salas leem **1 parágrafo** do `README.en.md` em voz alta. A turma vota na
**clareza**. O professor fecha com:

> *"O `README` em inglês é o que vai fazer o seu projeto ser encontrado por gente de
> fora. Pode ser que, em algum momento, alguém de fora ajude. Isso é open source de
> verdade."*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Commit em inglês no passado** | "fixed the bug" | Imperativo: "fix: handle empty list" |
| **README só traduzido** | Texto em português word por word | Escreva em inglês **pensando em inglês**. Se travar, use as 20 frases do quadro |
| **Mensagem de commit gigante** | "feat: implement everything" | Uma ideia por commit. "`feat: add ranking table`" |
| **Bug report sem ambiente** | "não funciona" | Add: `Environment / Steps to reproduce / Expected / Actual / Severity` |
| **Traduzir erro palavra por palavra** | "Erro de tipo não suportado" e nada mais | Aplique os 3 passos: tipo → alvo → esperado |
| **Usar `to` + verbo no infinitivo onde o inglês exige gerúndio** | "I am add the file" | `I am adding the file` / `To add the file` |
| **Confundir `raise` com `rise`** | `raise` = levantar (erro) | Em Python, `raise` levanta exceção. `rise` é subir |
| **Escrever "I'm agree"** | — | `I agree` (sem `am`) |
| **Colar saída de IA sem revisar** | Texto genérico e vazio | Releia em voz alta. Se você não diria isso, não escreva |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| `README.en.md` | 7 seções, ≥ 400 palavras, escrito em inglês |
| `CONTRIBUTING.md` | 5 seções |
| `docs/glossario.md` | 30 termos com "onde vi" |
| `docs/commits-em-ingles.md` | 10 mensagens no padrão `tipo(escopo): descrição` |
| Leitura de erro | 4 erros traduzidos corretamente (tipo, alvo, esperado) |
| `docs/decisoes.md` | Justificativa do README bilíngue |
| Commits | 3 commits |
| Participação | Leitura em voz alta na Fase 5 |
| Pergunta de saída | "O que é `expected` e o que é `actual` em um bug report?" |

**Pergunta de escrita:**
> "Você escreveu em inglês: `I have fixed the bug of the ranking that shows wrong
> number of teams`. Reescreva essa mensagem de commit no padrão do curso e explique
> cada parte."
>
> **Resposta:** o padrão é `tipo(escopo): descrição no imperativo`:
> ```
> fix(ranking): correct the number of teams displayed
> ```
> As partes são: **tipo** (`fix` = correção de bug; `feat` = recurso novo; `docs` =
> documentação; `test` = teste; `refactor` = refatoração sem mudar comportamento) ·
> **escopo** (o módulo ou arquivo afetado, entre parênteses — aqui, `ranking`) ·
> **descrição** (verbo no imperativo, minúscula, sem ponto final — "correct", não
> "corrected" nem "corrects").
> Por que funciona: o `git log --oneline` mostra **50 colunas**, e o tipo + escopo
> deixam a mensagem autoexplicativa sem abrir o diff. E a mensagem antiga ("I have
> fixed...") está errada em 3 pontos: está no **passado** ("have fixed"), tem
> **frase completa** em vez de comando, e não diz **onde** foi a mudança.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `ingles-para-programadores/03_vocabulario_web/` | HTML, CSS, JS, navegador |
| `ingles-para-programadores/08_comandos_ingles/` | Ler mensagens de erro |
| `ingles-para-programadores/09_frases_comuns/` | Frases do dia a dia |
| `ingles-para-programadores/10_listening_e_pronuncia/` | Escuta e pronúncia (bom para quem tem medo de falar) |
| `ingles-para-programadores/12_reunioes_e_comunicacao/` | Daily, review, retrospectiva |
| `ingles-para-programadores/13_aprendizado_continuo/` | Como continuar depois do curso |
| `ingles-para-programadores/15_projeto_contribuir/` | Contribuir com open source em inglês |
| `ingles-para-programadores/06_leitura_documentacao/exercicio_01_mdn.txt` | Praticar com a MDN |
| `ingles-para-programadores/11_escrita_tecnica/exercicio_02_escrever_readme.txt` | Escrever README em inglês |
| `laboratorio-tech-social/site/exercicios/quiz-teens.html` | Quiz geral da turma |

### 🏠 Para casa

Pegar **10 erros reais** do seu projeto (do terminal, do navegador, do Git) e traduzir
cada um seguindo os 3 passos. Salvar em `docs/erros-traduzidos.md`. Escolher **1
commit** real do seu projeto e reescrevê-lo em inglês no padrão do curso.
**2 commits.**

### 🔗 Próximo módulo

[B13 — Projeto Final parte 1 (escopo)](#b13)

<a id="b13"></a>

## Módulo 13 — Projeto Final parte 1: Escopo (Aula 13)

**Duração:** 90 min · **Aula 13 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Escrever a **Carta de Escopo** do seu projeto: problema, público, escopo incluído,
   escopo excluído, objetivos e **não objetivos**.
2. Converter o escopo em **histórias de usuário** com **critérios de aceite** verificáveis.
3. Montar o **backlog priorizado** (MoSCoW + valor × esforço) e **cortar escopo** com
   honestidade, até sobrar o que cabe em 2 aulas.

**Objetivo secundário:** aprender a dizer **não** para o próprio escopo — a habilidade
que separa quem entrega do quem sonha.

**Entregável do módulo:** **`docs/carta-de-escopo.md`** (a carta completa, 12 seções),
**`docs/backlog.md`** (backlog priorizado com **≥ 10 itens**) e **1 issue** aberta no
GitHub com a história principal. **"Commit ou não existe"** — a carta vai versionada.

### 📚 Fontes no repositório

**Modelos de referência (adaptados para esta aula):**
`manual-qa-completo/docs/10/PT/charter_template.md` (missão, áreas, duração, tester,
oportunidades, bugs, debrief) ·
`manual-qa-completo/docs/10/PT/test_plan_template.md` (introdução, itens de teste,
**fora de escopo**, abordagem, ambiente e dados, cronograma e responsáveis, riscos e
mitigações, critérios de entrada/saída, aprovações) ·
`manual-qa-completo/docs/10/PT/test_case_template.md` (formato de caso, que vira
**história + critério de aceite**) ·
`manual-qa-completo/docs/10/PT/matriz_rastreabilidade.md` (requisito → caso → status,
que vira **backlog → história**).

**Processo e produto:**
`laboratorio-tech-social/trilhas/adolescentes-13-20/modulo-06-projeto-social.md` ·
`laboratorio-tech-social/materiais/slides/aula-teens-06-projeto.html` ·
`laboratorio-tech-social/site/trilhas/adolescentes/06-projeto.html` ·
`laboratorio-tech-social/site/exercicios/criador-projeto.html` ·
`laboratorio-tech-social/site/exercicios/plano-testes.html` ·
`git-github-iniciantes/08_issues_e_projetos/README.md` (issues e projects) ·
`git-github-iniciantes/15_projeto_pratico/README.md`.

**Projetos de referência (para ver escopo real):**
`esporte-sao-pedro/funcionalidades_valor.txt` (a lista de funcionalidades e o **valor**
de cada uma do app real da cidade — o melhor exemplo de "escopo com justificativa"
que existe no material) ·
`esporte-sao-pedro/README.md` ·
`Central-de-noticias/README.md` (PWA de notícias com seção "São Pedro e região") ·
`Central-de-noticias/config.js` (configuração por ambiente) ·
`esporte-sao-pedro/AGENTS.md` (regras de contribuição do projeto real).

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Escopo** | "A linha do que está dentro e do que está fora. Escrever o 'fora' é o que protege o prazo." |
| **Objetivo** | "O resultado que você quer. Começa com verbo, tem prazo e tem medida." |
| **Não objetivo** | "Coisas que parecem tempting e que você **não** vai fazer. Elas salvam a entrega." |
| **História de usuário** | "Como **<persona>**, eu quero **ação**, para **benefício**." |
| **Critério de aceite** | "A frase que o tester usa para dizer 'passou'. Sem ela, não há teste." |
| **MoSCoW** | "Must, Should, Could, Won't. O corte de escopo começa pelo Should." |
| **Valor × Esforço** | "Tarefa pequena e valiosa vai primeiro. Não é a mais difícil que vem primeiro." |
| **Definition of Ready** | "A história está pronta para develop? Tem história, aceite, valor e risco." |
| **Estouro de escopo** | "Feature creep": o escopo cresce sozinho porque cada ideia nova parece pequena |
| **Cutline** | "A linha que corta: o que fica se faltar tempo." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Três aulas. Uma ideia. E essas três aulas vão decidir se o
projeto de vocês existe ou não. Hoje a aula mais importante não é a de programar: é a
de **cortar**."*

**Demonstração ao vivo (5 min).** Compartilhe a tela. Abra
`esporte-sao-pedro/funcionalidades_valor.txt` e mostre a estrutura:

```
1. NOTICIAS
   - Criar, editar e publicar noticias com titulo, corpo, imagem principal...
   - Status: publicada, em revisao, rascunho, agendada
2. CAMPEONATOS
   - Classificacao automatica (ordenada por pontos e saldo de gols)
3. CALENDARIO DE JOGOS
...
10. MAPA ESPORTIVO
```

Diga: *"Repare: cada item tem **funcionalidade** e **valor**. Isso é uma carta de
escopo disfarçada de lista. E repare que são **10 grandes** — não 40. Quando você
monta esse tipo de lista com a turma, cabe em uma tela. Quando cada item vira
micro-tarefa, cabe em um quadro de 60 cartões que nunca termina."*

**Quiz de recuperação (3 min).** *"O que é uma 'história de usuário'?"* →
"Como **<persona>**, eu quero **ação**, para **benefício**." *"Qual é a diferença entre
escopo e objetivo?"* → Objetivo é o resultado; escopo é o **limite** do que você vai
fazer para chegar lá.

#### Fase 2 — Exploração (20 min)

**Parte 1 — A carta de escopo, seção por seção (10 min).** Escreva no quadro o
esqueleto e explique cada parte:

```
1. IDENTIFICAÇÃO        — projeto, equipe, data, versão, status
2. RESUMO EXECUTIVO     — 3 frases: problema, público, solução
3. JUSTIFICATIVA        — o dado real de São Pedro/SP + a fonte
4. OBJETIVOS E NÃO OBJETIVOS
5. ESCOPO INCLUÍDO / ESCOPO EXCLUÍDO
6. HISTÓRIAS DE USUÁRIO + CRITÉRIOS DE ACEITE
7. BACKLOG PRIORIZADO
8. REQUISITOS NÃO FUNCIONAIS
9. DEPENDÊNCIAS E RISCOS
10. CRITÉRIOS DE ENTRADA E SAÍDA
11. PLANO DE ENTREGA (3 aulas)
12. APROVAÇÕES
```

Diga: *"As seções 3, 4, 5 e 10 são as que o professor vai ler com mais atenção.
Justificativa porque responde 'por que isso'. Não objetivos porque protegem o prazo.
Escopo excluído porque é a linha do 'não'. Critérios de entrada e saída porque
definem 'pronto'."*

**Parte 2 — História de usuário + critério de aceite (7 min).** Escreva 2 exemplos:

```
História 1
Como morador do bairro Centro,
eu quero ver o resultado dos jogos do torneio da minha região,
para saber quem está na liderança.

Critérios de aceite:
1. A página mostra time, jogos, vitórias, empates, derrotas, pontos e saldo.
2. A ordenação é por pontos e, em empate, por saldo de gols.
3. Times sem nenhum jogo aparecem com zeros (não desaparecem).
4. Funciona no celular (largura mínima testada: 360 px).
5. Os dados vêm de data/times.csv e nenhum dado é inventado no código.
```

```
História 2
Como organizadora de oficina gratuita,
eu quero cadastrar uma oficina com vagas e bairro,
para que os moradores vejam o que está disponível perto de casa.

Critérios de aceite:
1. Campos: título, data, horário, bairro, vagas, descrição.
2. Título e bairro são obrigatórios, com mensagem clara em português.
3. Não é possível cadastrar 2 oficinas com o mesmo título e data.
4. Nenhum campo pede CPF, RG, endereço completo ou telefone.
5. Os dados ficam no repositório do projeto, sem serviço externo.
```

Diga: *"O critério 3 é o que pega bug. 'Não é possível duplicar' — como você vai
provar que não duplicou? Escrevendo o teste. O critério de aceite é, literalmente, o
começo do seu plano de testes."*

**Parte 3 — Priorização sem achismo (3 min).** Escreva:

| Ferramenta | O que responde |
|---|---|
| **MoSCoW** | O que é **essencial** (Must) e o que pode ser cortado (Won't) |
| **Valor × Esforço** | O que entra **primeiro**: muita aucidade e pouco trabalho |
| **Ordem do backlog** | A **ordem exata** de implementação |

Diga: *"Erro clássico: começar pelo que é mais fácil. Isso entrega bonito e
atrasado. Comece pelo que tem **mais valor**, mesmo que dê trabalho."*

#### Fase 3 — Mão na massa (30 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Este módulo é
**individual**: cada aluno escreve o **seu** escopo (duplas só se combinarem
explicitamente e os dois entregarem escopos distintos).

**Atividade A — Escolher e validar a ideia (8 min dentro do breakout).** O professor
 distribui as **5 sugestões de capstone** (abaixo). Cada aluno escolhe **1** (pode
adaptar) e valida em **1 minuto** respondendo a 3 perguntas:

1. **Quem** usa isso? (persona: morador, atleta, professor, organizador)
2. **Que problema real** de São Pedro/SP isso resolve?
3. **Qual dado público** comprova que o problema existe?

**As 5 sugestões de capstone:**

| # | Ideia | Base nos repositórios | Perfil |
|---|---|---|---|
| 1 | **Placar da Cidade** — placar dos torneios de São Pedro, com classificação, artilheiros e agenda | `esporte-sao-pedro/` (app real do clube) | Web + SQL |
| 2 | **Despertar Kids** — versão lúdica de QA: jogo educativo de caça-bugs e quiz para crianças | `o-despertar-qa/`, `QA_RUN/`, `laboratorio-tech-social/site/exercicios/caca-bugs.html` | Web + JS |
| 3 | **Estação Clima** — painel de sensores do bairro (temperatura, chuva) com dados simulados | `laboratorio-tech-social/site/exercicios/estacao-meteo.html`, `simulador-robotica.html` | Web + IoT |
| 4 | **Aulas Abertas** — portal das aulas gratuitas do bairro (robótica, inglês, projetos) | `laboratorio-tech-social/trilhas/` | Web + dados |
| 5 | **Bot de Notícias do Bairro** — resume e publica as notícias locais, com PWA | `Central-de-noticias/` (pipeline RSS → resumo → TTS → PWA) | Python + PWA |

**Atividade B — Escrever a carta (15 min dentro do breakout).** Preencher
`docs/carta-de-escopo.md` com as **12 seções** (modelo completo no bloco abaixo).
Regras do professor: **máximo 4 páginas**; sem parágrafo de mais de 5 linhas; todo
dado de São Pedro/SP com **fonte citada**.

**Atividade C — Backlog priorizado (7 min dentro do breakout).** Preencher
`docs/backlog.md` com **≥ 10 itens** no modelo do bloco abaixo, com:
- **Must** = o que sem o qual o projeto não existe (≤ 4 itens).
- **Should** = importante, mas cortável.
- **Could** = bônus.
- **Won't** = fora (escreva **por quê** — isso é ouro na apresentação).

**O que o professor diz enquanto circula:**

> *"Me mostra o seu Must. Se tem 7 itens no Must, você não tem Must — tem
> desejos. Escolhe 4 e joga o resto para Should. E me mostra o seu 'Won't': se você
> não escreveu nada no Won't, você ainda não decidiu o que está fora. Quem não decide
> o que está fora, decide isso na hora de entregar — e é sempre tarde."*

**Plano B (internet caiu):** os modelos completos estão **no repositório local** e o
professor os cola no chat. O aluno escreve a carta **no `docs/carta-de-escopo.md`
local** e a issue no GitHub fica para o próximo encontro. O brainstorming da Atividade A
é falado, não precisa de nada.

#### Fase 4 — Projeto (20 min)

**Desafio: "Carta de escopo e backlog prontos para a Sprint".**

1. `docs/carta-de-escopo.md` — **12 seções**, com:
   - Dados **reais e públicos** de São Pedro/SP e **a fonte** (IBGE, Prefeitura,
     Secretaria da Educação, GESP/ESALQ).
   - **≥ 3 objetivos** mensuráveis e **≥ 3 não objetivos**.
   - **Escopo excluído** com **pelo menos 5 itens** explicitamente fora.
   - **≥ 4 histórias de usuário**, cada uma com **≥ 4 critérios de aceite**.
   - **≥ 5 requisitos não funcionais** (desempenho, acessibilidade, compatibilidade,
     privacidade, offline).
   - **3 riscos** com mitigação.
   - **Critérios de entrada e saída** da release v1.
2. `docs/backlog.md` — **≥ 10 itens** priorizados, com valor, esforço, MoSCoW,
   **Sprint** (1, 2 ou 3) e dependências.
3. **1 issue** aberta no GitHub com a **história principal** e seus **critérios de
   aceite**, com **labels** (`status: a-fazer`, `sprint: 1`) e **milestone** "v1".
4. `docs/decisoes.md` — **+1 entrada**: *"Por que este projeto e não os outros quatro"*.

**Critério de pronto:**
- [ ] `docs/carta-de-escopo.md` com **12 seções** preenchidas
- [ ] **≥ 3 objetivos** mensuráveis e **≥ 3 não objetivos**
- [ ] **≥ 5 itens** no escopo excluído
- [ ] **≥ 4 histórias** com **≥ 4 critérios de aceite** cada
- [ ] **≥ 5 requisitos não funcionais**
- [ ] **3 riscos** com mitigação
- [ ] Critérios de **entrada e saída** da v1
- [ ] `docs/backlog.md` com **≥ 10 itens** e **Must ≤ 4**
- [ ] **1 issue** no GitHub com critérios de aceite
- [ ] **3 commits** no padrão Conventional Commits

#### Fase 5 — Mostra (10 min)

Duas salas apresentam **1 história de usuário** e **1 item do "Won't"**. A turma vota:
*"Qual escopo está mais bem cortado?"* — isto é, qual projeto tem mais chance de
**ser entregue inteiro**.

O professor devolve a pergunta do começo:

> *"Vocês olharam para 5 ideias e escolheram 1. Agora olharam para 20 itens e
> escolheram 10. Isso é produto. Na próxima aula, a parte mais difícil: fazer o que
> sobrou."*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Must com 12 itens** | Tudo é essencial | Must ≤ 4. Se é essencial para tudo, não é essencial para nada |
| **Sem não objetivos** | A seção está vazia | Escreva 3 coisas que você **poderia** fazer e **não vai** |
| **Escopo sem dado real** | "Melhorar a comunidade" | Coloque o número: 23 unidades de ensino, ~5.200 alunos, IDHM 0,755, com a fonte |
| **Critério de aceite vago** | "O sistema deve ser rápido" | "A lista carrega em menos de 2 segundos com 100 itens" |
| **Critério não verificável** | "A interface deve ser bonita" | "O contraste do texto no fundo é maior que 4,5:1 e funciona no celular" |
| **Backlog sem esforço** | Tudo com valor "Alto" | Esforce o esforço (P/M/G) e o valor (Alto/Médio/Baixo) |
| **Dependência não mapeada** | Um item depende de outro que vem depois | Coluna "Depende de" no backlog |
| **Escopo que não cabe em 2 aulas** | 10 itens Must | Corte. O corte é o trabalho. A.feature entra na v2 |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Carta de escopo | 12 seções + 3 objetivos + 3 não objetivos + 5 exclusões |
| Histórias | ≥ 4 histórias com ≥ 4 critérios de aceite cada |
| Requisitos não funcionais | ≥ 5 |
| Riscos | 3 com mitigação |
| Backlog | ≥ 10 itens, Must ≤ 4, com esforço e dependências |
| Issue no GitHub | 1 issue com critérios de aceite, label e milestone |
| `docs/decisoes.md` | Justificativa da escolha do projeto |
| Commits | 3 commits |
| Participação | História e item "Won't" apresentados na Fase 5 |
| Pergunta de saída | "Por que o escopo excluído é mais importante que o incluído?" |

**Pergunta de escrita:**
> "Você escreveu que o escopo do projeto inclui 'sistema de login com e-mail e senha'.
> O que acontece com essa linha quando você descobre, na metade da Sprint 2, que não
> tem tempo de fazer cadastro de usuário, recuperação de senha, token de sessão e
> proteção contra força bruta?"
>
> **Resposta:** essa linha é **incompleta** — e é por isso que a carta de escopo exige
> "não objetivos" e "escopo excluído". O problema não é o esforço: é que "login com
> e-mail e senha" parece **1 item** e na verdade são **4 histórias**, cada uma com
> critérios de aceite, testes e risco de segurança. Quando você escreve "login" na
> carta, você prometeu um sistema de autenticação completo.
> A correção é: (1) **decompor** em histórias explícitas no backlog — "cadastro",
> "login", "logout", "recuperação de senha"; (2) mover tudo o que não cabe para
> **Should/Could** e marcar como **Won't** na v1; (3) se o login for mesmo essencial,
> escolher o **caminho mais simples** — link mágico ou login com código por e-mail
> dispensa senha, dispensa hash, dispensa recuperação de senha — e reescrever os
> critérios de aceite. É exatamente o que a carta de escopo previne: um item escrito
> em uma frase que promete quatro coisas.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `esporte-sao-pedro/funcionalidades_valor.txt` | O melhor exemplo de escopo com valor |
| `esporte-sao-pedro/AGENTS.md` | Regras de contribuição do projeto real |
| `esporte-sao-pedro/README.md` | README de projeto real com escopo e instalação |
| `Central-de-noticias/README.md` | PWA real com pipeline de conteúdo |
| `Central-de-noticias/config.js` | Configuração por ambiente |
| `manual-qa-completo/docs/10/PT/charter_template.md` | Modelo de charter (base da carta) |
| `manual-qa-completo/docs/10/PT/test_plan_template.md` | Seções de escopo, riscos e aprovações |
| `manual-qa-completo/docs/10/PT/matriz_rastreabilidade.md` | Rastreabilidade requisito → caso |
| `laboratorio-tech-social/trilhas/adolescentes-13-20/modulo-06-projeto-social.md` | Trilha de projeto social do repositório |
| `laboratorio-tech-social/site/exercicios/criador-projeto.html` | Gerador de projeto (para destravar a ideia) |
| `git-github-iniciantes/08_issues_e_projetos/README.md` | Issues, labels e milestones |

### 🏠 Para casa

Refinar a carta de escopo: cortar mais 2 itens do Must, transformar cada item em uma
**história de usuário** com **critérios de aceite** no `docs/backlog.md`, e criar **3
issues** no GitHub (uma por história). Deixar o `docs/backlog.md` com a coluna
"Depende de" preenchida. **3 commits.**

### 🔗 Próximo módulo

[B14 — Projeto Final parte 2: Implementação](#b14)

<a id="b14"></a>

## Módulo 14 — Projeto Final parte 2: Implementação (Aula 14)

**Duração:** 90 min · **Aula 14 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Transformar **história de usuário** em **código versionado**: branch, commit
   atômico, pull request.
2. Executar a **Sprint 1 do backlog** até o **MVP funcionando** (Must entregue).
3. Aplicar **code review** com um checklist objetivo e **receber** a revisão sem
   defensividade.
4. Registrar o **progresso** no kanban e no `docs/decisoes.md`.

**Objetivo secundário:** transformar a revisão em **oportunidade de aprender**, não em
julgamento da pessoa.

**Entregável do módulo:** **MVP funcionando** (todos os itens **Must** do backlog
implementados), **≥ 8 commits** com mensagens no padrão, **≥ 1 pull request revisado**
e **kanban atualizado** com a coluna "Concluído" preenchida.

### 📚 Fontes no repositório

**Processo e código:**
`git-github-iniciantes/04_branches/README.md` ·
`git-github-iniciantes/07_pull_requests/README.md` ·
`git-github-iniciantes/11_trabalho_em_equipe/README.md` ·
`git-github-iniciantes/06_github/README.md` ·
`git-github-iniciantes/07_pull_requests/exercicios/04_code_review.txt` ·
`git-github-iniciantes/15_projeto_pratico/README.md` ·
`formacaoScrumMaster/` (visão geral do Scrum, Definition of Done, eventos) ·
`_framework_Scrum/README.md` e `_framework_Scrum/config.json` (a configuração real do
framework usada na aula) ·
`manual-qa-completo/docs/08/scripts/ci.yml` (quality gate em CI, o modelo de
"verificação automática") ·
`manual-qa-completo/docs/08/scripts/quality_gate.py` ·
`manual-qa-completo/docs/03/scripts/estimate.py` (estimativa por história).

**Projeto real (referência de código limpo):**
`Central-de-noticias/scripts/gerar.py` ·
`Central-de-noticias/tests/test_gerar.py` ·
`Central-de-noticias/app.js` · `Central-de-noticias/styles.css` ·
`Central-de-noticias/noticias.json` · `Central-de-noticias/pytest.ini` ·
`Central-de-noticias/requirements.txt` ·
`esporte-sao-pedro/app.js` · `esporte-sao-pedro/index.html` ·
`esporte-sao-pedro/style.css` · `esporte-sao-pedro/manifest.json` ·
`esporte-sao-pedro/supabase/functions/send-push/index.ts` · `esporte-sao-pedro/supabase-rls-admin.sql` ·
`esporte-sao-pedro/SUPABASE_SECURITY_SETUP.md` ·
`Central-de-noticias/.github/workflows/ci-tests.yml` (workflow real de CI).

**Trilhas e slides:**
`laboratorio-tech-social/trilhas/adolescentes-13-20/modulo-06-projeto-social.md` ·
`laboratorio-tech-social/materiais/slides/aula-teens-06-projeto.html` ·
`laboratorio-tech-social/site/exercicios/lista-tarefas.html` ·
`laboratorio-tech-social/site/exercicios/code-builder.html` ·
`laboratorio-tech-social/site/trilhas/adolescentes/03-qa.html`.

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Branch** | "Uma cópia de trabalho. Toda história nova ganha uma branch: `feat/placar`." |
| **Commit atômico** | "Um commit = uma ideia. Se a mensagem precisa de 'e', são dois commits." |
| **Code review** | "Revisar é conferir se o código faz o que o critério de aceite promete." |
| **Definition of Done** | "Feito = codado, testado, documentado, revisado, no GitHub." |
| **Kanban** | "A régua do projeto: A fazer / Fazendo / Revisão / Concluído." |
| **Limite de WIP** | "Máximo 2 cards em 'Fazendo'. Multidão em andamento = ninguém termina nada." |
| **Walkthrough** | "Code review de 15 min, por alguém do time, com 3 perguntas prontas." |
| **Refactor** | "Você pode melhorar a estrutura **depois** que funciona. Antes disso, é distração." |
| **Código de ontem** | "Antes de commitar, leia o diff como se fosse de outra pessoa. E geralmente é." |
| **Ritmo** | "Um commit por aula. Não é devagar — é o que permite voltar atrás." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Semana passada vocês cortaram o escopo. Esta semana vocês
escrevem o código. E a parte mais importante dessa aula não é o código: é o
**ritmo**. Quem trava 3 dias sem commitar volta no 4º dia sem saber o que fez."*

**Demonstração ao vivo (6 min).** Compartilhe a tela e faça o ciclo completo em
**7 minutos**, narrando cada comando:

```
git switch -c feat/placar-da-cidade      # 1. branch nova
# ... editar index.html e app.js ...
git add -A                                # 2. preparar
git commit -m "feat(placar): add team ranking table"   # 3. gravar
git push -u origin feat/placar-da-cidade # 4. publicar a branch
# ... abrir o PR no GitHub ...
git log --oneline -5                      # 5. conferir a linha do tempo
```

Diga: *"Repare no nome da branch: `feat/placar-da-cidade`. Ela diz **o quê** e
**onde**. Em 6 meses, quando alguém rodar `git branch -a`, ela entende o que
aquilo faz. Compare com `teste`, `teste2`, `teste-final` — que é o equivalente
brasileiro do `fix_final_v2_AGORA`."*

**Quiz de recuperação (2 min).** *"O que é um commit atômico?"* → "Um commit que
registra **uma única ideia**, com uma mensagem que descreve só ela."

#### Fase 2 — Exploração (15 min)

**Parte 1 — A Definition of Done do curso (5 min).** Escreva no quadro e explique
que **é a mesma para todo mundo**:

```
FEITO =
  1. a história está implementada (sem "depois eu termino")
  2. existe pelo menos 1 teste (manual ou automático) que prova o critério de aceite
  3. o README documenta como usar o que você fez
  4. o código foi revisado por 1 colega (ou pelo professor, ao vivo)
  5. está commitado, com mensagem no padrão tipo(escopo): descrição
  6. está no GitHub (push feito)
```

Diga: *"Item 2 é o que separa hobby de projeto. Um código sem teste é um código
que você não entendeu. Se você não sabe testar, escreva um teste manual: 5 passos
num arquivo `docs/testes-manuais.md`."*

**Parte 2 — Como revisar o código de outra pessoa (5 min).** Escreva o **roteiro de
walkthrough de 15 minutos**:

```
1. O autor apresenta em 3 min: o que a história promete e o que foi feito
2. O revisor confirma: os critérios de aceite estão cobertos?
3. O revisor olha 3 coisas, nada mais:
   - o DIFF (git diff), não o arquivo inteiro
   - nomes de variável e função (claro?)
   - o que NÃO tem commitado (esquecimento?)
4. O revisor devolve: 2 elogios + 1 pergunta + 1 sugestão concreta
```

Diga: *"Regra de ouro da revisão: você comenta **o código**, nunca **a pessoa**.
'Nessa linha o nome `x` não diz o que é' é útil. 'Você não sabe programar' é
prejudicial e não muda nada. Quem humilha trava o time — e em uma turma de
adolescentes, isso expulsa a pessoa."*

**Parte 3 — O kanban do projeto (5 min).** Desenhe o quadro:

```
| A fazer | Fazendo (máx. 2) | Revisão | Concluído |
|---|---|---|---|
| ID3 - ... | ID1 - ... | ID2 - ... | ID0 - ... |
```

Diga: *"O **limite de 2 em 'Fazendo'** é o que impede o caos. Se você tem 5 coisas
'Fazendo', você não está fazendo 5 coisas — você está começando 5 e terminando
nenhuma. Escolha 2. Termine. Puxe a próxima."*

**Parte 4 — Onde o projeto real está (2 min).** Mostre
`Central-de-noticias/.github/workflows/ci-tests.yml` e diga: *"Quando você faz
`push`, o GitHub roda os testes sozinho, em outro computador. Se quebrar, aparece um
X vermelho. Isso se chama **Integração Contínua**. É o mesmo princípio do
'commit ou não existe': o computador confere o que você disse que fez."*

#### Fase 3 — Mão na massa (40 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Duas formas de
trabalhar:

- **Em dupla (recomendado)**: um faz, um lê e testa; trocam a cada 15 min
  (*driver* e *navigator*). É a forma de **pair programming** — mais lento no
  começo, muito mais rápido no fim, porque ninguém fica 40 minutos sozinho
  sem saber onde errou.
- **Individual**: se o aluno já tem ritmo.

**Atividade A — Kanban e primeira seleção (5 min dentro do breakout).** Cada sala
cria o quadro com os itens do `docs/backlog.md`, respeitando **Must ≤ 4** e
**WIP = 2**.

**Atividade B — Implementar o Must (25 min dentro do breakout).** Regras:
- Escolher **no máximo 2 itens** para as "Fazendo".
- Cada item vira **1 branch** com nome `feat/`, `fix/` ou `docs/`.
- Cada item vira **1 commit por ideia**, com mensagem `tipo(escopo): descrição`.
- Se algo travar por **10 minutos**, o aluno anota o problema em `docs/pendencias.md`
  e **muda de item**. Isso se chama *timeboxing* e é o que impede o travamento
  infinito.

**Atividade C — Revisão cruzada entre salas (10 min dentro do breakout).** Cada sala
**recebe o repositório (ou o branch)** de outra sala e faz o **walkthrough de 15
minutos** na sala vizinha:
- 3 min: o autor apresenta
- 5 min: o revisor confere os **critérios de aceite**
- 7 min: o revisor devolve **2 elogios + 1 pergunta + 1 sugestão**

O autor **corrige 1 coisa** antes de abrir o PR.

**O que o professor diz enquanto circula:**

> *"Me mostra o `git log --oneline`. Se a última mensagem é 'update' ou 'ajustes' ou
> 'arrumei', eu vou pedir de novo. Escreva o que você fez: 'fix(ranking): handle
> empty team list'. E olha: você está com 3 cards em 'Fazendo'. Volta pra 2."*

> *"Me mostra como você testou isso. Se a resposta for 'rodei e não deu erro', me
> mostra o que você fez para tentar quebrar. Teste é procurar erro de propósito."*

**Plano B (internet caiu):** o professor transforma a aula em **"dupla local"** —
cada aluno trabalha no computador com um colega do mesmo quarto ou da mesma casa
(quando possível), ou o professor usa **dois repositórios de demonstração** e faz
**code review ao vivo** com a turma toda. O kanban vira uma **tabela em papel** ou um
arquivo `docs/kanban.md` local. O commit local funciona sem internet — só o `push`
que precisa. Por isso a regra do curso: **faça commit antes de perder a conexão**.

#### Fase 4 — Projeto (15 min)

**Desafio: "MVP no ar, no GitHub, com histórico limpo".**

1. **Todos os itens Must** do backlog implementados e **funcionando** (nem que seja
   "funcionando de verdade" — a página abre e mostra os dados).
2. **Kanban** atualizado (em `docs/kanban.md` ou no GitHub Projects) com **todos os
   Must** na coluna "Concluído" e a **contagem de horas** de cada item.
3. **≥ 8 commits** no padrão `tipo(escopo): descrição`, **sem** mensagens
   "update"/"ajustes"/"arrumei".
4. **≥ 1 pull request** aberto, com as seções *What / Why / How to test*, e **pelo
   menos 1 comentário de revisão** real (da dupla ou do professor).
5. `README.md` do projeto **atualizado** com o que já funciona.
6. `docs/decisoes.md` — **+1 entrada**: *"Por que cortamos o item X"*.
7. `docs/testes-manuais.md` — **≥ 3 testes manuais** (passo a passo, resultado
   esperado e resultado obtido) dos itens Must.

**Critério de pronto:**
- [ ] **Todos os Must** do backlog implementados
- [ ] Kanban com "Concluído" preenchido e **horas** por item
- [ ] **≥ 8 commits** no padrão, sem mensagens vagas
- [ ] **≥ 1 PR** aberto com *What / Why / How to test*
- [ ] **≥ 1 comentário de revisão** no PR
- [ ] `README.md` atualizado
- [ ] `docs/decisoes.md` com o registro do corte
- [ ] `docs/testes-manuais.md` com **≥ 3 testes manuais**
- [ ] Push feito — projeto visível no GitHub

#### Fase 5 — Mostra (10 min)

Duas salas apresentam **30 segundos**: o que estava no Must e **o que virou Must
funcionando**. A turma responde com a pergunta de **go-live**: *"Se eu clicasse
agora no link do projeto, o que eu veria?"*

O professor fecha:

> *"Vocês cortaram 10 itens e entregaram 4. O que vocês construíram é pequeno e
> funciona. Um projeto pequeno que funciona vale muito mais do que um projeto
> grande que ficou pela metade. Semana que vem a gente prova que funciona."*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Commit "arrumei"** | `git log` cheio de `update`, `ajustes`, `correcoes` | Reescreva o histórico com `git rebase -i` ou, no próximo commit, descreva a mudança real |
| **Commit com duas ideias** | Mensagem com "e" no meio | Divida em 2 commits com `git reset --soft HEAD~1` e commite de novo |
| **Branch nomeada "teste"** | `git branch` mostra `teste`, `teste2` | `feat/nome-da-funcionalidade` |
| **"Quase pronto"** | Código com `TODO` do lado | "Quase pronto" = não pronto. Termine ou corte |
| **Revisão defensiva** | "Isso é feio, mas funciona" | Revise o **diff**, não a pessoa. Elogio + pergunta + sugestão |
| **Push sem commit** | `Everything up-to-date` mas nada novo | `git status` e `git log` antes de avisar que "subiu" |
| **Esquecer o `.gitignore`** | `node_modules/` e `.env` versionados | `.gitignore` com `node_modules/`, `.env`, `__pycache__/`, `.DS_Store` |
| **Segredo no repositório** | Chave de API no `app.js` | Nunca commite segredo. Se já foi, **rotacione** a chave |
| **Fazer 5 coisas ao mesmo tempo** | Kanban com 5 cards em "Fazendo" | Limite 2. Um termina, entra o próximo |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| MVP | Todos os **Must** implementados e funcionando |
| Commits | ≥ 8 no padrão, sem mensagens vagas |
| Pull request | ≥ 1 com *What / Why / How to test* |
| Revisão | ≥ 1 comentário de revisão real e construtivo |
| Kanban | "Concluído" preenchido + horas por item |
| `README.md` | Atualizado com o que já funciona |
| `docs/testes-manuais.md` | ≥ 3 testes manuais com resultado esperado e obtido |
| `docs/decisoes.md` | Registro do corte de escopo |
| Participação | Apresentação de 30 segundos na Fase 5 |
| Pergunta de saída | "O que é um commit atômico e por que ele protege o projeto?" |

**Pergunta de escrita:**
> "Você empurrou (`push`) o projeto e recebeu a mensagem: `error: failed to push some
> refs to 'origin'`. Ao mesmo tempo, no `git log`, você vê 6 commits, todos com
> mensagens no padrão. O que aconteceu, o que fazer e o que isso ensina sobre o
> trabalho em equipe?"
>
> **Resposta:** a mensagem significa que **o repositório remoto tem commits que você
> não tem localmente**. As causas mais comuns são: (a) alguém da equipe fez `push`
> antes de você; (b) você fez `pull` de outra branch; (c) você fez `rebase` local e
> reescreveu a história, que o GitHub não consegue reconciliar. A solução é
> `git pull --rebase origin <sua-branch>` (ou `git pull` e resolver o conflito) e
> depois `git push` de novo. Se o rebase reescreveu a história que já estava no
> remoto, o caminho é `git push --force-with-lease` — que é seguro porque falha se
> alguém mais tiver enviado commits nesse meio-tempo.
> O que isso ensina: (1) **commit não é sinônimo de push** — commit é local, push é
> compartilhamento; os 6 commits no `git log` provam que o trabalho está salvo
> localmente, mas não chegou ao servidor; (2) **trabalhar em equipe significa que o
> remoto muda sem você avisar** — por isso a branch por pessoa e o PR, para que a
> integração seja um evento explícito, e não uma surpresa; (3) **rebasear histórico já
> publicado é perigoso** — force-push pode apagar o trabalho do colega; por isso
> prefere-se merge para equipas iniciantes.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `git-github-iniciantes/04_branches/README.md` | Branch, merge e boas práticas |
| `git-github-iniciantes/07_pull_requests/README.md` | Fluxo de pull request |
| `git-github-iniciantes/11_trabalho_em_equipe/README.md` | Conflitos e como resolver |
| `git-github-iniciantes/07_pull_requests/exercicios/04_code_review.txt` | Checklist de revisão |
| `git-github-iniciantes/15_projeto_pratico/README.md` | Projeto prático completo |
| `Central-de-noticias/tests/test_gerar.py` | Testes reais em Python (pytest) |
| `Central-de-noticias/pytest.ini` | Configuração de pytest |
| `Central-de-noticias/scripts/gerar.py` | Script real do pipeline |
| `Central-de-noticias/.github/workflows/ci-tests.yml` | CI real rodando testes |
| `esporte-sao-pedro/supabase/functions/send-push/index.ts` | Código real com tipos |
| `esporte-sao-pedro/supabase-rls-admin.sql` | Segurança de banco (RLS) |
| `esporte-sao-pedro/SUPABASE_SECURITY_SETUP.md` | Setup de segurança |
| `manual-qa-completo/docs/08/scripts/quality_gate.py` | Quality gate automatizado |
| `manual-qa-completo/docs/03/scripts/estimate.py` | Estimativa de esforço |
| `laboratorio-tech-social/site/exercicios/lista-tarefas.html` | Quadro de tarefas na web |
| `laboratorio-tech-social/site/exercicios/code-builder.html` | Montar blocos de código |

### 🏠 Para casa

Terminar **todos os Must** restantes. Se algum Must não couber no tempo: **corte** e
registre em `docs/decisoes.md` — não deixe Must pela metade. Publicar o PR e pedir
revisão a um colega do breakout (ou à lista do grupo da turma). **3 commits.**

### 🔗 Próximo módulo

[B15 — Projeto Final parte 3: Testes, Deploy e Documentação](#b15)

<a id="b15"></a>

## Módulo 15 — Projeto Final parte 3: Testes, Deploy e Documentação (Aula 15)

**Duração:** 90 min · **Aula 15 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Escrever o **Plano de Testes** do projeto — o documento que diz **o que será
   testado, como, por quem e até quando**.
2. Preencher o **Checklist de Aceite** (homologação) e transformar cada linha em
   **verdadeiro ou falso**.
3. **Publicar o projeto no GitHub Pages** e escrever o `README.md` final.
4. Rodar uma **verificação de segredos** antes de publicar.

**Objetivo secundário:** entender que **publicar não é o fim** — publicar é
**assumir a responsabilidade** por aquilo que está no ar.

**Entregável do módulo:** **`docs/plano-de-testes.md`** (completo), **`docs/checklist-aceite.md`**
(marcado), **projeto publicado** no GitHub Pages, **`README.md` final** e
**`LICENSE` MIT**.

### 📚 Fontes no repositório

**Modelos oficializados neste curso (adaptados do repositório):**
`manual-qa-completo/docs/10/PT/test_plan_template.md` (modelo de Plano de Testes) ·
`manual-qa-completo/docs/10/PT/checklist_aceite.md` (modelo de Checklist de
Homologação) ·
`manual-qa-completo/docs/10/PT/test_case_template.md` (caso de teste) ·
`manual-qa-completo/docs/10/PT/bug_report_template.md` (relatório de bug) ·
`manual-qa-completo/docs/10/PT/matriz_rastreabilidade.md` ·
`manual-qa-completo/docs/10/PT/glossario.md` ·
`manual-qa-completo/docs/11/scripts/secret_scan.py` (varredura de segredos) ·
`manual-qa-completo/docs/09/scripts/kpi.py` (indicadores) ·
`manual-qa-completo/docs/08/scripts/quality_gate.py` (quality gate) ·
`manual-qa-completo/docs/08/scripts/ci.yml` (CI) ·
`manual-qa-completo/docs/03/scripts/estimate.py` (estimativa).

**Publicação e testes:**
`git-github-iniciantes/09_github_pages/README.md` ·
`git-github-iniciantes/12_ci_cd_basico/README.md` ·
`git-github-iniciantes/12_ci_cd_basico/exercicios/04_deploy_pages.txt` ·
`git-github-iniciantes/13_open_source/README.md` (licenças: MIT, CONTRIBUTING) ·
`git-github-iniciantes/15_projeto_pratico/exercicios/05_publicar_documentar.txt` ·
`Central-de-noticias/requirements.txt` ·
`Central-de-noticias/pytest.ini` ·
`Central-de-noticias/tests/test_gerar.py` ·
`Central-de-noticias/wrangler.toml` (deploy em Cloudflare Pages) ·
`Central-de-noticias/sw.js` (service worker da PWA) ·
`Central-de-noticias/manifest.webmanifest` ·
`esporte-sao-pedro/CNAME` (domínio próprio) ·
`esporte-sao-pedro/robots.txt` · `esporte-sao-pedro/sitemap.xml` ·
`esporte-sao-pedro/supabase-rls-admin.sql` (segurança de dados) ·
`QA_RUN/tests/smoke.js` (teste de fumaça real).

**Exercícios e checklists:**
`laboratorio-tech-social/site/exercicios/plano-testes.html` ·
`laboratorio-tech-social/site/exercicios/verifica-noticia.html` ·
`laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` ·
`qa-exercicios-praticos/modelos-templates/bug-report.md` ·
`qa-exercicios-praticos/tecnicas-de-teste/exercicios-tecnicas-de-teste.md` ·
`qa-exercicios-praticos/sql-para-qa/exercicios-sql.md`.

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Plano de Testes** | "O documento que diz o que vai ser testado — para ninguém testar na véspera e esquecer a tela 3." |
| **Escopo de teste** | "O que **não** será testado também precisa estar escrito. Senão é teste infinito." |
| **Critério de entrada** | "Só começa a testar quando o build está pronto e o ambiente funciona." |
| **Critério de saída** | "Só termina quando os bugs críticos fecharam e o checklist passou." |
| **Checklist de aceite** | "Uma lista de afirmações. Cada linha é **verdadeiro ou falso** — sem 'talvez'." |
| **Teste de fumaça (smoke)** | "O teste que diz 'o app ainda abre'. Rápido, todo dia, antes de tudo." |
| **Regressão** | "Rodei os testes antigos e quebrei o que funcionava. Isso é regressão." |
| **Homologação** | "A última checagem antes de dizer que está pronto." |
| **Segredo no repositório** | "Chave no GitHub é chave pública. `secret_scan.py` existe por causa disso." |
| **Deploy** | "Publicar é um evento: a partir dali, alguém pode usar e reclamar." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Vocês já têm um MVP. Hoje ele vira algo que existe de verdade
na internet: um link que você manda para a sua avó e ela abre. E o preço de ter
um link é ter **responsabilidade**: alguém vai achar o erro que vocês não acharam."*

**Demonstração ao vivo (6 min).** Compartilhe a tela e mostre o caminho completo:

```
1. Publicar: Settings > Pages > Source: main / root
   (ou o workflow: .github/workflows/deploy.yml)
2. Conferir: https://<usuario>.github.io/<repositorio>
3. Testar o link em OUTRO dispositivo (celular) e em anônimo
4. Escrever o checklist de aceite e MARCAR cada linha
5. Rodar a varredura de segredos
6. Publicar o README final + LICENSE
```

Mostre o `QA_RUN/tests/smoke.js` e diga: *"Um **teste de fumaça** faz 5 verificações
e leva 10 segundos. Ele não substitui o resto — mas se o smoke falha, não adianta
rodar mais nada."*

**Quiz de recuperação (2 min).** *"Qual a diferença entre 'critério de entrada' e
'critério de saída' do plano de testes?"* → Entrada: "quando **começo** a testar".
Saída: "quando **termino**".

#### Fase 2 — Exploração (20 min)

**Parte 1 — O Plano de Testes (modelo completo do curso) (12 min).** Escreva no
quadro. Este é o modelo que o aluno vai copiar para `docs/plano-de-testes.md`:

```
PLANO DE TESTES — <NOME DO PROJETO>

1. INTRODUÇÃO
   Objetivo: [validar a release v1 do <projeto>]
   Escopo: [módulos / histórias que entram]
   Público: [quem vai usar: moradores do bairro X, os alunos do torneio, os pais]
   Data: [dd/mm/aaaa] | Versão testada: [v1.0.0] | Autor: [seu apelido]

2. ITENS DE TESTE
   - [ID1] <história/capacidade>  -> critérios de aceite: [lista]
   - [ID2] ...

3. FORA DE ESCOPO
   - [o que NÃO será testado nesta release e por quê]

4. ABORDAGEM
   Níveis: [unitário, integração, UI]
   Tipos: [fumaça, regressão, exploratório, usabilidade]
   Ferramentas: [pytest / DevTools / navegador em modo anônimo]

5. AMBIENTE E DADOS
   Ambiente: [produção no GitHub Pages / local]
   Dados: [dados de exemplo do repositório, sem dados pessoais]
   Dispositivos: [Chrome/Edge/Firefox, celular 360 px e 768 px]

6. CRONOGRAMA E RESPONSÁVEIS
   Início: [data] | Fim: [data]
   Responsável pelos testes: [seu apelido]
   Ajudante: [apelido do colega da sala]

7. RISCOS E MITIGAÇÕES
   Risco: [internet cair no deploy] -> Mitigação: [publicar antes da aula e testar local]
   Risco: [dado inventado] -> Mitigação: [todo número vem de data/ com a fonte]

8. CRITÉRIOS DE ENTRADA E SAÍDA
   Entrada: [build pronto, README com instruções, backlog Must fechado]
   Saída: [100% dos itens Must testados, 0 bug crítico aberto, checklist de aceite
           100% marcado, 0 segredo exposto]

9. APROVAÇÕES
   Autor: [ ]  Colegas da sala: [ ]  Professor: [ ]
```

Diga: *"Repare na seção 3. **'Fora de escopo'** é a seção que protege a sua semana.
Sem ela, todo mundo acha que você vai testar 'tudo'. Com ela, fica escrito: isto
não entra nesta release."*

**Parte 2 — O Checklist de Aceite (modelo completo do curso) (6 min).** Escreva no
quadro — este é o checklist que o aluno vai marcar item a item:

```
CHECKLIST DE ACEITE (HOMOLOGAÇÃO) — <PROJETO> — data: [dd/mm/aaaa]

FUNCIONALIDADE
  [ ] Fluxos principais funcionam (caminho feliz)
  [ ] Casos de borda tratados (vazio, zero, texto muito longo, item ausente)
  [ ] Mensagens de erro claras em português
  [ ] Todos os itens "Must" do backlog funcionam de ponta a ponta

VALIDAÇÃO DE DADOS
  [ ] Campos obrigatórios validados com mensagem clara
  [ ] Formatos validados (data, número, e-mail, texto)
  [ ] Entradas maliciosas básicas bloqueadas (SQL injection, XSS)
  [ ] Nenhum dado pessoal é pedido ou salvo (sem nome completo, CPF, RG, endereço)

INTERFACE / EXPERIÊNCIA
  [ ] Responsivo (celular 360 px, tablet 768 px, desktop)
  [ ] Estados de carregando, de erro e de "vazio" tratados
  [ ] Acessibilidade: foco visível, contraste do texto, texto do botão descritivo
  [ ] Funciona sem JavaScript? (ou: a página avisa que precisa de JavaScript)

SEGURANÇA
  [ ] Sem segredos em logs, no console ou no código (roda o secret_scan)
  [ ] Nenhuma chave de API ou senha no repositório
  [ ] Links externos abrem em aba nova com segurança
  [ ] Dados do usuário não são compartilhados com terceiros

DESEMPENHO
  [ ] Carregamento em menos de 3 segundos com a quantidade de dados da demo
  [ ] A página não trava ao rolar (sem memory leak óbvio)

DADOS E AMBIENTE
  [ ] O build testado é exatamente o build publicado
  [ ] Os dados são de exemplo, com a fonte citada no README
  [ ] O README explica como rodar em 3 passos
  [ ] A LICENSE MIT está no repositório
```

Diga: *"Cada linha é **verdadeiro ou falso**. Não existe 'quase'. Se uma linha é
falsa, você **corrige** ou você **tira a linha do escopo** — e escreve isso na
seção 3 do plano de testes."*

**Parte 3 — Antes de publicar: 3 checagens de 10 segundos (2 min).** Mostre:

```
1. Tem segredo?      -> secret_scan.py  (ou: procure por 'key', 'token', 'password')
2. Tem README?       -> alguém que nunca viu o projeto consegue rodar em 3 passos?
3. Tem LICENSE?      -> sem licença, ninguém pode reutilizar de forma segura
```

#### Fase 3 — Mão na massa (30 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Nesta aula o
**duplo testador** é essencial: cada sala testa o projeto da **sala vizinha**.

**Atividade A — Plano de testes (8 min dentro do breakout).** Preencher
`docs/plano-de-testes.md` com as **9 seções** (modelo acima), usando os **itens Must**
do backlog como **itens de teste**.

**Atividade B — Testar o projeto do colega (15 min dentro do breakout).** A sala
recebe o link (ou o repositório) de outra sala e executa:
- **3 testes de fumaça** (abre? a lista carrega? o botão principal funciona?)
- **5 testes exploratórios**: tentar quebrar (campo vazio, número gigante, texto
  com `'` ou `<script>`, item inexistente, sem internet)
- **Preencher o Checklist de Aceite** do projeto do colega, marcando **verdadeiro
  ou falso** em cada linha
- Escrever **1 relatório de bug** no formato
  `qa-exercicios-praticos/modelos-templates/bug-report.md`, com **severidade**

Diga: *"Vocês são o **usuário**. O objetivo não é achar o erro para humilhar: é
achar o erro para **consertar**. Bug encontrado em aula é bug de graça — depois
do lançamento custa 10 vezes mais."*

**Atividade C — Corrigir e publicar (7 min dentro do breakout).** Cada aluno:
- Corrige os **bugs críticos** encontrados pelo colega.
- Publica no GitHub Pages e **confere o link em outro dispositivo**.
- Roda a checagem de segredo.

**O que o professor diz enquanto circula:**

> *"Me mostra o checklist marcado. Se tem uma linha que você não sabe responder,
> ela não está marcada — está em branco, e em branco é 'falso'. Me mostra o
> `secret_scan` rodando no seu projeto. Se o seu repositório tem uma chave de API
> no `app.js`, essa chave está queimada: rotacione agora, antes de publicar."*

> *"Testa em janela anônima. Se funcionar logado e não funcionar deslogado, o
> bug é de sessão e ninguém vai ver isso na sua máquina."*

**Plano B (internet caiu):** o GitHub Pages **não** funciona sem internet. O plano B
oficial: (1) testar **localmente** com `python -m http.server 8000` ou abrindo o
`index.html`; (2) o checklist de aceite é impresso pelo professor (modelo em papel)
e marcado à mão; (3) o `docs/plano-de-testes.md` é escrito localmente; (4) o
**deploy fica para a última aula** (B16), em que o professor usa **2 computadores
com internet** para publicar e o resto da turma acompanha por tela; (5) a validação
do checklist no ar vira **demonstração do professor**.

#### Fase 4 — Projeto (20 min)

**Desafio: "Publicar, documentar e assumir".**

1. **`docs/plano-de-testes.md`** — as **9 seções** preenchidas, com **≥ 6 itens de
   teste** (um por história Must), **≥ 3 itens** em "fora de escopo" e os
   **critérios de entrada e saída**.
2. **`docs/checklist-aceite.md`** — o checklist completo (6 blocos), **100% marcado**
   ou com a linha explicitamente retirada do escopo (com justificativa).
3. **`docs/matriz-rastreabilidade.md`** — tabela **história → item de teste →
   checklist → status** (o modelo `matriz_rastreabilidade.md` do manual).
4. **Projeto publicado** no GitHub Pages, com o **link no README**.
5. **`README.md` final** — 7 seções (nome, o que é, por que, como rodar, o que tem
   dentro, como contribuiu, licença) + **link publicado** + **captura de tela**
   (print) ou ** GIF curto.
6. **`LICENSE`** com **MIT** + **`CONTRIBUTING.md`** curto (o do módulo B12).
7. **`docs/decisoes.md`** — **+1 entrada**: *"Por que publicamos no GitHub Pages e
   não em outro lugar"*.
8. **≥ 3 bugs** registrados em `docs/bugs/` no formato do `bug_report_template.md`
   (se os Finds do colega forem menos de 3, registre também os seus).

**Critério de pronto:**
- [ ] `docs/plano-de-testes.md` com **9 seções**, **≥ 6 itens de teste**, **≥ 3 fora de escopo**
- [ ] `docs/checklist-aceite.md` com **6 blocos**, todos marcados
- [ ] `docs/matriz-rastreabilidade.md` com história → teste → status
- [ ] **Link publicado** funcionando, testado em **outro dispositivo** e em **anônimo**
- [ ] `README.md` final com as **7 seções** e o link
- [ ] `LICENSE` MIT + `CONTRIBUTING.md`
- [ ] `docs/decisoes.md` com a decisão de publicação
- [ ] `docs/bugs/` com **≥ 3 bugs** no formato do modelo
- [ ] **Nenhum segredo** no repositório
- [ ] **≥ 3 commits** no padrão

#### Fase 5 — Mostra (10 min)

Cada sala abre o **link do projeto de outra sala** e responde a **3 perguntas** da
plateia (o professor escolhe): *"O que esse projeto faz?" · "Quem usaria?" ·
"Qual foi o bug mais divertido que vocês acharam?"*

O professor fecha:

> *"Publicar não é o fim. É o começo de alguém reclamar. Mas reclamar de um
> projeto de bairro, feito por vocês, dentro do prazo, com checklist marcado e bug
> registrado — isso é engenharia. Nunca mais vão dizer que adolescente não
> entrega."*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Checklist com "quase"** | "Testei, mas acho que funciona" | Binário: **funciona** ou **não funciona**. Se não tem certeza, é "não" |
| **Item marcado sem evidência** | Nada no log, nada no teste | Um teste de fumaça registrado em `docs/testes-manuais.md` vale como evidência |
| **"Fora de escopo" vazio** | Seção 3 em branco | Escreva 3 itens que **não** entram e por quê |
| **Segredo no repositório** | `AIza...`, `sk-...`, `password = "..."` | Rotacione a chave **imediatamente** e remova do histórico |
| **Deploy só testado logado** | Funciona no seu navegador, não no anônimo | Teste em janela anônima e no celular |
| **README só com screenshot** | Nenhuma instrução de uso | Escreva os 3 passos **antes** de mostrar a imagem |
| **Sem LICENSE** | Repositório sem licença | MIT: permite uso, estudo e adaptação |
| **Bug sem severidade** | "tem um bug ali" | Severidade = crítico / alto / médio / baixo. Crítico bloqueia a publicação |
| **Testar só no próprio projeto** | Zero bugs encontrados | Teste o projeto do colega — sempre acha algo |
| **Dados pessoais no repositório** | Nome completo, CPF, endereço em CSV | Remova e use dados de exemplo (fictícios) |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| `docs/plano-de-testes.md` | 9 seções, ≥ 6 itens de teste, ≥ 3 fora de escopo |
| `docs/checklist-aceite.md` | 6 blocos, 100% marcado |
| `docs/matriz-rastreabilidade.md` | História → teste → status |
| Publicação | Link no ar, testado em anônimo e em outro dispositivo |
| `README.md` | 7 seções + link + imagem |
| `LICENSE` / `CONTRIBUTING.md` | MIT + guia de contribuição |
| `docs/bugs/` | ≥ 3 bugs no modelo, com severidade |
| `docs/decisoes.md` | Decisão de publicação registrada |
| Segredos | 0 segredo no repositório (verificado) |
| Commits | ≥ 3 no padrão |
| Participação | Teste do projeto de outra sala na Fase 5 |
| Pergunta de saída | "Qual a diferença entre um bug crítico e um bug baixo?" |

**Pergunta de escrita:**
> "Você preencheu o checklist de aceite e marcou 'Falso' em 4 linhas: 'Fluxos
> principais funcionam', 'Casos de borda tratados', 'Mensagens de erro claras' e
> 'Responsivo'. A data de lançamento é amanhã às 18h. O que você faz — corrijo
> tudo, corrijo o que dá, ou lanço assim mesmo?"
>
> **Resposta:** a resposta correta é **"corrijo o que dá, marco o resto como fora
> de escopo desta release e comunico"**. Em detalhe:
> (1) **Classifique as 4 linhas por severidade.** "Responsivo" falhando no celular é
> **alto** (a maioria dos usuários do bairro vai estar no celular, em dados móveis).
> "Mensagens de erro claras" falhando é **médio** (o usuário vê um erro, mas não
> entende). "Casos de borda" falhando é **médio**, a menos que o caso de borda seja
> exatamente o caminho principal.
> (2) **Bloqueadores:** o checklist tem um item que diz "todos os itens Must do
> backlog funcionam de ponta a ponta". Se isso é falso, o **critério de saída** da
> seção 8 do plano de testes não foi atendido — e por isso o lançamento **não pode
> acontecer** com a release v1 como está. Isso não é opinião: é o combinado.
> (3) **O que fazer com o resto:** ou você corta o escopo **por escrito** (mova a
> linha para a seção "fora de escopo" com a justificativa e a data prevista) ou
> você conserta. O que **não** pode é publicar com a linha em branco: isso é
> esconder defeito.
> (4) **Comunicar:** README e issue devem dizer o que não está pronto. Um
> lançamento honesto com 3 limitações declaradas gera mais confiança do que um
> lançamento "completo" que quebra na primeira vez que alguém usa.
> (5) **Por que não "lançar assim mesmo":** o custo de corrigir um bug crítico
> depois do lançamento (com gente usando) é muito maior do que corrigir agora. Por
> isso o checklist existe: é o **preço da data**.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `manual-qa-completo/docs/10/PT/test_case_template.md` | Modelo de caso de teste |
| `manual-qa-completo/docs/10/PT/bug_report_template.md` | Modelo de bug report |
| `manual-qa-completo/docs/10/PT/matriz_rastreabilidade.md` | Rastreabilidade |
| `manual-qa-completo/docs/10/PT/glossario.md` | Glossário de QA |
| `manual-qa-completo/docs/11/scripts/secret_scan.py` | Varredura de segredos |
| `manual-qa-completo/docs/09/scripts/kpi.py` | Indicadores do projeto |
| `manual-qa-completo/docs/08/scripts/quality_gate.py` | Quality gate |
| `git-github-iniciantes/09_github_pages/README.md` | Publicar no GitHub Pages |
| `git-github-iniciantes/12_ci_cd_basico/exercicios/04_deploy_pages.txt` | Deploy por workflow |
| `git-github-iniciantes/13_open_source/README.md` | Licenças e open source |
| `git-github-iniciantes/15_projeto_pratico/exercicios/05_publicar_documentar.txt` | Publicar e documentar |
| `Central-de-noticias/tests/test_gerar.py` | Testes em Python (pytest) |
| `Central-de-noticias/requirements.txt` | Dependências do projeto real |
| `Central-de-noticias/manifest.webmanifest` | Manifesto de PWA |
| `Central-de-noticias/sw.js` | Service worker (offline) |
| `esporte-sao-pedro/CNAME` | Domínio próprio |
| `esporte-sao-pedro/sitemap.xml` | Mapa do site para buscadores |
| `esporte-sao-pedro/supabase-rls-admin.sql` | Regras de acesso ao banco |
| `QA_RUN/tests/smoke.js` | Teste de fumaça real |
| `qa-exercicios-praticos/modelos-templates/bug-report.md` | Modelo de bug report |
| `laboratorio-tech-social/site/exercicios/plano-testes.html` | Montar plano de testes |

### 🏠 Para casa

Rodar o **checklist de aceite** sozinho, do zero, como se fosse a primeira vez
(critério: não reler o código antes de testar). Publicar e **mandar o link para
2 pessoas** de fora do curso (um familiar, um colega de outra escola) e anotar o
que elas acharam confuso. **3 commits.**

### 🔗 Próximo módulo

[B16 — Showcase, Demo Day e Certificação](#b16)

<a id="b16"></a>

## Módulo 16 — Showcase, Demo Day e Certificação (Aula 16)

**Duração:** 90 min · **Aula 16 de 16**

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Apresentar o projeto em **3 minutos** — problema, solução, demo ao vivo e próximo
   passo — para uma plateia que nunca viu o código.
2. Receber e dar **feedback** com o formato **"gostei / pergunto / sugiro"**.
3. Explicar **o que aprendeu** e **o que faria diferente**, com honestidade.
4. Sair com o **certificado**, o **portfólio** e um **plano de continuidade**.

**Objetivo secundário:** fechar o curso sem que o projeto morra no dia seguinte.
**Projeto que só existe na aula não é projeto — é trabalho de escola.**

**Entregável do módulo:** **pitch de 3 min** (roteiro em `docs/pitch.md`), **demo ao
vivo funcionando**, **`docs/retrospectiva.md`** (o que funcionou, o que não funcionou,
o que fazer diferente), **portfólio atualizado** e **certificado conferido**.

### 📚 Fontes no repositório

**Certificação e encerramento:**
`laboratorio-tech-social/materiais/templates/certificado/modelo-certificado.md` ·
`laboratorio-tech-social/materiais/templates/certificado/certificado.html` ·
`laboratorio-tech-social/materiais/templates/certificado/README.md` ·
`laboratorio-tech-social/site/certificado/index.html` (gerador com verificação) ·
`laboratorio-tech-social/site/certificado/verificar.html` (validação de autenticidade) ·
`laboratorio-tech-social/site/certificado/historia.html` ·
`laboratorio-tech-social/docs/plano-pedagogico.md` ·
`laboratorio-tech-social/docs/ecossistema.md` ·
`laboratorio-tech-social/docs/guia-do-voluntario.md`.

**Portfólio e continuidade:**
`portfolio/` (modelo de portfólio em HTML) ·
`portfolio/index.html` · `portfolio/style.css` ·
`laboratorio-tech-social/site/exercicios/criador-site.html` ·
`laboratorio-tech-social/trilhas/adolescentes-13-20/` ·
`git-github-iniciantes/13_open_source/README.md` ·
`git-github-iniciantes/13_open_source/exercicios/03_primeira_contribuicao.txt` ·
`git-github-iniciantes/14_ferramentas/README.md` ·
`manual-qa-completo/docs/01/PT/indice.md` (carreira e certificações) ·
`qa-exercicios-praticos/perguntas-respostas/perguntas-entrevista-QA.md`.

**Projetos para inspirar a mostra:**
`esporte-sao-pedro/` · `Central-de-noticias/` · `o-despertar-qa/` ·
`QA_RUN/` · `meu-treino/` · `anyms/` · `hubias-estudos/`.

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Pitch de 3 minutos** | "Problema (30 s) + solução (45 s) + demo (60 s) + próximo passo (45 s)." |
| **Demo ao vivo** | "Nunca dependa da internet da sala. Tenha um vídeo de 30 s de reserva." |
| **QR code** | "O jeito mais rápido de a plateia abrir o seu projeto no celular." |
| **Feedback em 3 partes** | "Gostei de… / Fiquei com a dúvida… / Eu sugeriria…" |
| **Retrospectiva** | "O que funcionou, o que não funcionou, o que farei diferente." |
| **Portfólio** | "3 projetos, 1 README cada, 1 link no ar. Não precisa ser 10." |
| **Certificado** | "Prova de que você participou e entregou. Não é diploma profissional." |
| **Continuidade** | "Projeto parado apodrece. Um commit por mês já mantém vivo." |
| **Open source** | "Seu projeto pode virar base para outra pessoa — se tiver licença e README." |
| **Comunidade** | "Ninguém continua sozinho. O grupo da turma é a primeira comunidade." |

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min).** *"Última aula. Hoje ninguém aprende comando novo. Hoje vocês
mostram o que construíram. E vou ser sincero: a parte mais difícil de programar não é
o código. É **explicar** o que você fez para alguém que não estava lá."*

**Demonstração ao vivo (5 min).** Compartilhe a tela e faça um **pitch modelo** de
3 minutos, cronometrado:

```
[0:00–0:30] PROBLEMA
"Em São Pedro, os jogos do torneio do bairro acontecem todo domingo.
 Ninguém sabe a classificação até alguém postar no grupo do WhatsApp.
 Meu vizinho perguntou 3 vezes quem estava em primeiro."

[0:30–1:15] SOLUÇÃO
"Eu fiz o Placar da Cidade: uma página que mostra a tabela, os jogos
 e os artilheiros. Os dados vêm de um arquivo do repositório, com a
 fonte. Funciona no celular, sem instalar nada."

[1:15–2:15] DEMO
(abre o link, mostra a tabela, clica em um time, mostra o celular)

[2:15–3:00] PRÓXIMO PASSO
"Na próxima versão eu quero mostrar os jogos por rodada e deixar o
 organizador cadastrar o resultado. Quem quiser ajudar, o link do
 repositório está no QR code."
```

Diga: *"Repare no que eu **não** fiz: não contei a história da minha vida, não
mostrei código, não falei 'foi muito difícil'. Falei do **problema de alguém** e
mostrei **funcionando**. O código é o meio; a mudança é o fim."*

**Quiz de recuperação (3 min).** *"Quais são as 4 partes do pitch de 3 minutos?"* →
Problema, solução, demo, próximo passo.

#### Fase 2 — Exploração (20 min)

**Parte 1 — O roteiro do pitch (6 min).** Escreva no quadro o **modelo preenchível**
que o aluno vai salvar em `docs/pitch.md`:

```markdown
# Pitch — <nome do projeto>

## 1. Problema (30 s)
Quem sofre: [persona real de São Pedro/SP]
O que acontece hoje: [situação concreta]
Dado/fonte: [número + fonte, se tiver]

## 2. Solução (45 s)
O que o projeto faz: [1 frase]
O que ele NÃO faz (para não prometer demais): [1 frase]
Para quem: [público]

## 3. Demo (60 s)
O caminho que vou mostrar: [tela 1 → tela 2 → tela 3]
Plano B se a internet cair: [vídeo de 30 s / prints / projeto local]

## 4. Próximo passo (45 s)
O que eu faria na v2: [1 coisa]
Como alguém pode ajudar: [link do repositório / issue boa para iniciante]

## Ensaio
- [ ] Cronometrado em 3 min (sem passar)
- [ ] Sem jargão: nenhuma palavra que a minha avó não entenderia
- [ ] Sem ler o slide
```

**Parte 2 — Como dar e receber feedback (4 min).** Escreva o formato:

```
GOSTEI DE...      (específico, não "muito bom")
FIQUEI COM A DÚVIDA...  (uma pergunta real)
EU SUGERIRIA...   (uma coisa concreta e pequena)
```

Diga: *"Regra: **elogio específico** vale mais que elogio genérico. 'Gostei de como
a tabela ordena por saldo de gols' mostra que você olhou. 'Gostei de tudo' não ajuda
ninguém. E sugestão precisa ser **pequena**: 'coloca um botão de voltar' é sugestão;
'refaz o app inteiro' é opinião."*

**Parte 3 — O que o certificado é e o que não é (5 min).** Mostre o modelo
`modelo-certificado.md` e o gerador `site/certificado/index.html`. Explique:

- **É**: prova de que você participou de **24 horas** de formação, entregou os
  **≥ 12 dos 16 entregáveis** e publicou **1 projeto de impacto local em open source**.
- **Não é**: diploma de ensino técnico, certificação profissional de mercado, nem
  garantia de emprego. É um **começo documentado**.
- **Código de verificação**: `TECH-XXXX-XXXX-XXXX`, gerado a partir do nome + trilha
  + um segredo (SHA-256). Qualquer pessoa pode conferir em
  `site/certificado/verificar.html`.
- **Licença**: o certificado e todo o material são **MIT** — uso livre e educativo.

**Parte 4 — O que vem depois (5 min).** Escreva 4 caminhos:

| Caminho | O que fazer na primeira semana |
|---|---|
| **Continuar o projeto** | 1 issue por semana, 1 commit por mês, 1 pessoa usando |
| **Contribuir em open source** | Ache a label `good first issue` no GitHub e comente |
| **Estudar a próxima trilha** | Trilhas `adolescentes/`, `python-do-zero`, `qa-exercicios-praticos` |
| **Ensinar** | Ajude na próxima turma como monitor (o nível 4 da rubrica exige isso) |

#### Fase 3 — Mão na massa (30 min)

**Organização:** o professor abre **breakout de 3 a 4 alunos**. Cada aluno **ensaia
o pitch** com a própria sala antes de apresentar para a turma.

**Atividade A — Escrever o pitch (8 min dentro do breakout).** Preencher
`docs/pitch.md` com as 4 seções e **cronometrar** com o celular. **Regra: 3 minutos,
sem passar.**

**Atividade B — Ensaio na sala (10 min dentro do breakout).** Cada aluno apresenta
**1 vez** para a sala. A sala devolve **gostei / pergunto / sugiro** (1 de cada). O
aluno ajusta **1 coisa** e apresenta de novo.

**Atividade C — Retrospectiva (7 min dentro do breakout).** Preencher
`docs/retrospectiva.md`:

```markdown
# Retrospectiva — <projeto>

## O que funcionou
- [3 coisas]

## O que não funcionou
- [3 coisas]

## O que eu faria diferente
- [3 coisas]

## O que eu aprendi que não estava no plano
- [1 coisa]

## Quem me ajudou
- [nomes/apelidos]
```

**Atividade D — Portfólio e QR code (5 min dentro do breakout).** Atualizar o
`portfolio/index.html` com **3 projetos** (o capstone + 2 exercícios) e gerar o
**QR code** do link publicado (qualquer gerador gratuito, ou o do próprio navegador).

**O que o professor diz enquanto circula:**

> *"Três minutos. Tira a parte de 'eu sempre gostei de computador desde pequeno'.
> Começa pelo problema de alguém. A plateia não quer saber de você — quer saber
> **quem você ajudou**."*

> *"Se a demo quebrar ao vivo, não entre em pânico e não peça desculpa 10 vezes.
> Diga 'a demo está com um problema e eu tenho um vídeo de 30 segundos' e siga.
> Quem apresenta bem não é quem nunca quebra — é quem **continua** quando quebra."*

**Plano B (internet caiu):** o pitch e a retrospectiva são **offline**. A demo usa
**vídeo de 30 s gravado antes** e **prints**. O professor projeta o **gerador de
certificado local** (`certificado.html` abre no navegador sem internet) e o QR code
é substituído pelo **link escrito no chat**. A mostra acontece normalmente — sem
GitHub ao vivo.

#### Fase 4 — Projeto (20 min)

**Desafio: "Demo Day da turma".**

Cada aluno (ou dupla) apresenta **3 minutos** para a turma toda. O professor
cronometra e o **chat/turma** registra feedback no formato *gostei / pergunto /
sugiro*.

**Critério de pronto:**
- [ ] `docs/pitch.md` com as **4 seções** e ensaiado em **≤ 3 min**
- [ ] **Demo ao vivo** (ou vídeo de 30 s de reserva) funcionando
- [ ] `docs/retrospectiva.md` com **3 itens** em cada bloco
- [ ] `portfolio/index.html` com **3 projetos** e o **link publicado**
- [ ] **QR code** do projeto gerado
- [ ] **`README.md`** com link, print e instruções em 3 passos
- [ ] Certificado **gerado e verificado** em `site/certificado/verificar.html`
- [ ] **3 commits** no padrão (pitch, retrospectiva, portfólio)

#### Fase 5 — Mostra (10 min)

**Entrega simbólica dos certificados.** O professor lê o nome de cada aluno e diz
**uma coisa específica** que aquela pessoa fez bem (não "parabéns", mas "você foi
quem achou o bug da tabela vazia"). A turma aplaude.

Fechamento do curso:

> *"Vocês começaram sem saber o que era um commit. Terminam com um projeto no ar,
> com teste, com README, com checklist e com certificado. Isso não é pouco: é a
> diferença entre **consumir tecnologia** e **fazer tecnologia**. O próximo passo é
> de vocês — e o repositório fica aberto para quem quiser continuar."*

### ⚠️ Erros comuns e como lê-los

| Erro | Sinal | Como corrigir |
|---|---|---|
| **Pitch que conta a vida** | 2 minutos falando de si | Comece pelo problema de **outra pessoa** |
| **Demo que depende da internet** | Travou ao vivo | Grave um vídeo de 30 s e tenha prints |
| **Prometer demais** | "Na v2 vai ter login, mapa e IA" | Diga 1 coisa e cumpra |
| **Feedback genérico** | "Achei legal" | Gostei de… / dúvida… / sugiro… |
| **Feedback que humilha** | "Isso está horrível" | Comente o **produto**, não a pessoa |
| **Receber crítica como ataque** | "Então faz você" | Anote, agradeça, escolha 1 sugestão |
| **Projeto que morre no dia seguinte** | Ninguém mexe mais | 1 issue e 1 commit por mês |
| **Portfólio com 10 projetos pela metade** | Tudo "em andamento" | 3 projetos **terminados** |
| **Certificado sem verificação** | Código não confere | Gere e valide no `verificar.html` |
| **Sair sem o link** | "Manda depois" | O link e o QR code saem **na aula** |

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Pitch | 4 seções, ≤ 3 min, sem jargão |
| Demo | Funciona ao vivo (ou vídeo de reserva) |
| Retrospectiva | 3 itens em cada um dos 5 blocos |
| Portfólio | 3 projetos terminados + link |
| `README.md` | Link, print e 3 passos |
| Certificado | Gerado e verificado |
| Feedback dado | ≥ 3 feedbacks no formato da aula |
| Commits | 3 no padrão |
| Presença | Aula 16 de 16 |
| Pergunta de saída | "Qual é a diferença entre o que o projeto faz e o problema que ele resolve?" |

**Pergunta de escrita:**
> "Na sua demo ao vivo, o site não carrega porque a internet da escola caiu. A
> plateia está olhando para você. O que você faz e por quê?"
>
> **Resposta:** o correto é **não improvisar em cima do erro** e **não pedir
> desculpa repetidamente**. O roteiro é: (1) **reconheça em uma frase** — "a internet
> daqui caiu, então vou mostrar o vídeo de 30 segundos que eu gravei"; (2) **mude
> para o plano B** — vídeo, prints ou o projeto rodando localmente no seu computador;
> (3) **narre o que está sendo visto** — "aqui é a tabela, aqui é o filtro por
> rodada"; (4) **volte ao roteiro** no ponto em que parou — "e o próximo passo é…".
> Por que isso funciona: a plateia não está avaliando a sua conexão, está avaliando
> se **você sabe o que construiu**. Um apresentador que troca de plano sem drama
> demonstra domínio do projeto; um que trava e se desculpa demonstra que decorou uma
> sequência de cliques. Além disso, o plano B é uma decisão de **engenharia**, não de
> sorte: quem grava o vídeo antes está fazendo **gestão de risco** — exatamente o que
> a seção 7 do plano de testes pede. E há um efeito secundário: a plateia entende que
> o projeto funciona **mesmo sem internet**, o que é uma qualidade do produto (uma
> PWA offline, por exemplo), não um defeito.

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `portfolio/index.html` | Modelo de portfólio para adaptar |
| `portfolio/style.css` | Estilo do portfólio |
| `laboratorio-tech-social/site/exercicios/criador-site.html` | Criar site pessoal |
| `laboratorio-tech-social/site/certificado/historia.html` | História do laboratório |
| `laboratorio-tech-social/docs/plano-pedagogico.md` | Plano pedagógico e metas |
| `laboratorio-tech-social/docs/ecossistema.md` | Como o ecossistema se conecta |
| `laboratorio-tech-social/docs/guia-do-voluntario.md` | Como virar monitor |
| `git-github-iniciantes/13_open_source/README.md` | Primeira contribuição |
| `git-github-iniciantes/13_open_source/exercicios/03_primeira_contribuicao.txt` | Passo a passo |
| `git-github-iniciantes/14_ferramentas/README.md` | Ferramentas do dia a dia |
| `manual-qa-completo/docs/01/PT/indice.md` | Carreira e certificações |
| `qa-exercicios-praticos/perguntas-respostas/perguntas-entrevista-QA.md` | Entrevistas |
| `meu-treino/` | Exemplo de projeto de portfólio |
| `anyms/` | Exemplo de projeto publicado |
| `hubias-estudos/` | Exemplo de repositório de estudos |

### 🏠 Para casa

**Uma coisa por semana, para sempre:** abrir **1 issue** no seu repositório com o
próximo passo (pode ser "arrumar o botão no celular"), e fazer **1 commit** naquele
mês. Marcar no calendário o **primeiro domingo do mês** como "dia do projeto".
Compartilhar o link no grupo da turma quando publicar algo novo.

### 🔗 Próximo passo

[Encerramento e Certificação](#encerramento)

---

<a id="encerramento"></a>

## Encerramento e Certificação

### O que você concluiu

Ao longo de **16 encontros de 90 minutos (24 horas)**, você percorreu a trilha
completa de quem **faz** tecnologia, não apenas usa:

| Bloco | Aulas | O que ficou |
|---|---|---|
| **Pensar** | B1–B2 | Pensamento computacional, lógica, algoritmos, fluxogramas, pseudocódigo |
| **Programar** | B3–B4 | Python do zero e projetos com arquivos, JSON e POO |
| **Construir** | B5–B6 | HTML, CSS, JavaScript e banco de dados SQL |
| **Colaborar** | B7 | Git, GitHub, issues, pull requests, code review |
| **Garantir qualidade** | B8 | QA, testes, bug report, checklist de aceite |
| **Usar IA com critério** | B9 | Prompt, viés, privacidade, uso responsável |
| **Organizar o trabalho** | B10 | Scrum, kanban, backlog, retrospectiva |
| **Proteger** | B11 | Segurança, LGPD, ética, cidadania digital |
| **Comunicar** | B12 | Inglês técnico, README bilíngue, commits em inglês |
| **Entregar** | B13–B15 | Escopo, implementação, testes, deploy, documentação |
| **Mostrar** | B16 | Pitch, demo, portfólio, certificado |

### Critérios de conclusão

O certificado é emitido quando **todos** os critérios abaixo são verdadeiros:

| # | Critério | Como se verifica |
|---|---|---|
| 1 | **Presença** em pelo menos **12 das 16 aulas** (75%) | Lista de presença por apelido |
| 2 | **≥ 12 dos 16 entregáveis** entregues ao longo do curso | Repositório do aluno, por aula |
| 3 | **Projeto final publicado** e acessível por link | URL no `README.md` |
| 4 | **Checklist de aceite** 100% marcado (ou item justificado fora de escopo) | `docs/checklist-aceite.md` |
| 5 | **Plano de testes** completo | `docs/plano-de-testes.md` |
| 6 | **README final** com as 7 seções e o link | `README.md` |
| 7 | **Licença MIT** no repositório | `LICENSE` |
| 8 | **Nenhum segredo** no repositório | `secret_scan.py` ou revisão manual |
| 9 | **Pitch de 3 minutos** apresentado no Demo Day | Registro do professor |
| 10 | **Retrospectiva** escrita | `docs/retrospectiva.md` |

> **Não há prova eliminatória.** A avaliação é **formativa**: o objetivo é o aluno
> saber **onde está** e **o que fazer a seguir**, não reprovar ninguém. Quem não
> cumprir um critério recebe **plano de recuperação** e pode concluir na turma
> seguinte, sem custo.

### Rubrica de avaliação (4 níveis)

Adaptada da rubrica de adolescentes (13–17) do guia do professor, com a mesma escala
de 1 a 4 pontos:

| Nível | Nome | Descrição | Pontos |
|---|---|---|---|
| 1 | **Iniciante** | Entregou parcialmente ou não entregou. Precisa de apoio passo a passo. | 1 |
| 2 | **Praticante** | Entregou o mínimo pedido, com erros conceituais ou sem documentação. | 2 |
| 3 | **Autônomo** | Entregou completo, código correto, testado e **documentado**. | 3 |
| 4 | **Referência** | Entregou completo, **refatorou**, documentou, **publicou** e **ajudou um colega**. | 4 |

**Como aplicar:**

- **Nível 1** não é "nota zero": é o ponto de partida. O professor registra **o que
  falta** e combina o próximo passo.
- **Nível 4** exige **ajudar um colega** — é o que transforma o aluno em monitor da
  próxima turma.
- A rubrica é aplicada **por entregável** (cada módulo tem a sua tabela de avaliação)
  e **no projeto final**.

### Pesos da avaliação

| Componente | Peso | O que entra |
|---|---|---|
| **Módulos 1–11** (fundamentos) | **30%** | Média dos 11 entregáveis, pela rubrica de 4 níveis |
| **Módulo 12** (inglês técnico) | **5%** | `README.en.md`, glossário, 10 commits em inglês |
| **Projeto final** (B13–B15) | **40%** | Escopo, implementação, plano de testes, checklist, publicação |
| **Demo Day** (B16) | **10%** | Pitch de 3 min, demo, retrospectiva, portfólio |
| **Participação e colaboração** | **15%** | Presença, feedback dado, ajuda a colegas, monitoria |
| **Total** | **100%** | — |

**Conversão para conceito (informativa, não eliminatória):**

| Média ponderada | Conceito | O que significa |
|---|---|---|
| 3,5 – 4,0 | **Referência** | Pronto para monitorar a próxima turma e contribuir em open source |
| 2,5 – 3,4 | **Autônomo** | Consegue tocar um projeto sozinho, com documentação |
| 1,5 – 2,4 | **Praticante** | Consegue com apoio; recomendado refazer 1 bloco |
| 1,0 – 1,4 | **Iniciante** | Precisa de mais uma passagem pela trilha, com acompanhamento |

### Modelo de certificado

O certificado segue o modelo de
`laboratorio-tech-social/materiais/templates/certificado/modelo-certificado.md`:

```
CERTIFICADO DE CONCLUSÃO

Laboratório de Tecnologia Social — São Pedro/SP

Certificamos que <NOME DO ALUNO>
concluiu a trilha Makers/Devs (14–18 anos),
com carga horária de 24 horas,
no Laboratório de Tecnologia Social,
projeto social gratuito e aberto.

Projeto final: <NOME DO PROJETO>
Link: <URL publicada>
Código de verificação: TECH-XXXX-XXXX-XXXX

Emitido em <DATA> por <PROFESSOR/A>.
Licença MIT — uso livre e educativo.
```

**Como o código de verificação funciona:** ele é gerado a partir de
`nome + trilha + segredo` com **SHA-256**, convertido para base36 e formatado em 12
caracteres (`TECH-XXXX-XXXX-XXXX`). Qualquer pessoa pode conferir em
`site/certificado/verificar.html` — o código é determinístico: os mesmos dados geram
sempre o mesmo código. Isso **não** é assinatura criptográfica de terceiro; é um
mecanismo de conferência interna do projeto, e o próprio material explica isso.

**O certificado não substitui** diploma de ensino técnico, certificação profissional
ou curso regulamentado. Ele documenta **24 horas de formação prática**, com projeto
publicado e critérios verificáveis.

### O que fazer depois do curso

| Prazo | Ação |
|---|---|
| **Hoje** | Salvar o link do projeto e o link do repositório no celular. Entrar no grupo da turma |
| **Esta semana** | Abrir 1 issue com o próximo passo do projeto. Ajudar 1 colega com o dele |
| **Este mês** | Fazer 1 commit. Ler 1 README de um projeto open source que você usa |
| **Próximos 3 meses** | Contribuir em 1 projeto com a label `good first issue`. Montar o portfólio com 3 projetos |
| **Próximo semestre** | Voltar como **monitor** da próxima turma (o nível 4 da rubrica) |

**Trilhas para continuar (todas no mesmo repositório, todas gratuitas):**

- `laboratorio-tech-social/site/trilhas/adolescentes/01-python.html`
- `laboratorio-tech-social/site/trilhas/adolescentes/02-web.html`
- `laboratorio-tech-social/site/trilhas/adolescentes/03-qa.html`
- `laboratorio-tech-social/site/trilhas/adolescentes/04-dados.html`
- `laboratorio-tech-social/site/trilhas/adolescentes/05-iot.html`
- `laboratorio-tech-social/site/trilhas/adolescentes/06-projeto.html`

---

<a id="inscricao"></a>

## Como se inscrever

### O curso

- **Nome:** Tecnologia na Prática — trilha **Makers/Devs (14–18 anos)**
- **Formato:** **16 encontros ao vivo online**, de **90 minutos** cada
- **Carga horária:** **24 horas**
- **Custo:** **gratuito** — sem taxa de inscrição, sem mensalidade, sem material pago
- **Pré-requisito:** nenhum. Não precisa saber programar, nem ter computador potente.
- **Certificado:** sim, ao cumprir os critérios de conclusão
- **Licença do material:** **MIT** — livre para usar, copiar, adaptar e compartilhar

### Quem pode se inscrever

- Adolescentes de **14 a 18 anos**, moradores de **São Pedro/SP** e região.
- **Não é necessário** ter experiência prévia, notebook próprio ou inglês.
- **É necessário** ter acesso a um computador com internet **durante as aulas**
  (o celular serve para acompanhar, mas não para programar confortavelmente).
- **Menores de 18 anos** precisam de **autorização do responsável** (LGPD/ECA).

### Passo a passo da inscrição

1. **Preencha o formulário** em
   `laboratorio-tech-social/inscricao/index.html` (publicado no GitHub Pages do
   projeto). Campos: nome, idade, escola/bairro, trilha, e-mail do aluno e do
   responsável, e o **termo de consentimento**.
2. **Autorização do responsável.** O responsável confirma o consentimento para
   participação e para o uso de imagem **apenas** nos registros internos do projeto
   (nunca para marketing de terceiros).
3. **Confirmação por e-mail.** A inscrição é confirmada por e-mail com o **link da
   sala**, o **calendário** e o **nome do apelido** que o aluno usará nas aulas.
4. **Entre no grupo da turma.** O grupo é o canal oficial de avisos, dúvidas e
   material. O link é enviado junto com a confirmação.
5. **Teste o acesso antes da primeira aula.** Abra o link da sala, teste o áudio e
   confira se o navegador está atualizado.

> **Não colete dados desnecessários.** O formulário pede o **mínimo**: nome, idade,
> contato e consentimento. Não pedimos CPF, RG, endereço completo, foto de documento
> ou dados de saúde. Os dados de menores **não são compartilhados com terceiros**
> para marketing (LGPD / ECA).

### Datas, vagas e lista de espera

- **Turmas:** abertas por **trimestre**, com divulgação no site do projeto e nas
  escolas parceiras.
- **Vagas:** limitadas para garantir **breakout de 3 a 4 alunos** e acompanhamento
  individual.
- **Lista de espera:** quem não entra na turma atual é chamado na próxima, **na ordem
  de inscrição**.
- **Prioridade:** alunos da rede pública, meninas e grupos subrepresentados em
  tecnologia (política de inclusão do projeto).

### O que levar no primeiro dia

- Computador com **navegador atualizado** (Chrome, Edge ou Firefox).
- **Conta gratuita no GitHub** (criada antes da aula, se possível).
- **Python 3** instalado (a instalação é feita na aula B3; se puder, instale antes).
- Um **caderno** ou um arquivo para anotações — o curso usa **muito** o `docs/`.
- Vontade de **perguntar**. Pergunta não é atrapalho; é o motor da aula.

### Acessibilidade e inclusão

- **Gratuito** e com **ferramentas gratuitas** em todas as aulas.
- **Material em PT-BR**; o módulo de inglês técnico existe para **incluir** quem
  ainda não lê inglês, não para excluir.
- **Legendas/transcrição** quando a plataforma permitir; gravações disponibilizadas
  por tempo limitado.
- **Sem exposição obrigatória:** a mostra de resultados é **voluntária**.
- **Duplas estratégicas:** alunos mais avançados são pareados com iniciantes.

### Dúvidas frequentes

**Preciso saber programar?**
Não. O curso começa do zero absoluto.

**Preciso ter computador?**
Para as aulas, sim (ou acesso a um). O celular serve para acompanhar, mas não
substitui o computador nas atividades de código.

**E se eu perder uma aula?**
As gravações e o material ficam disponíveis. O critério de presença é **12 de 16**;
quem perder mais pode concluir na turma seguinte.

**O certificado vale como curso técnico?**
Não. Ele documenta **24 horas de formação prática** com projeto publicado. Não
substitui diploma técnico nem certificação profissional.

**Tem custo?**
Não. Nem inscrição, nem mensalidade, nem material. Se alguém cobrar, não é este
projeto.

**Como ajudo o projeto?**
Sendo **monitor** na próxima turma, contribuindo com código no repositório (licença
MIT) ou divulgando a inscrição nas escolas.

### Contato

- **Site do projeto:** `laboratorio-tech-social/` (GitHub Pages)
- **Inscrição:** `laboratorio-tech-social/inscricao/index.html`
- **Certificados:** `laboratorio-tech-social/site/certificado/index.html`
- **Verificação de certificado:** `laboratorio-tech-social/site/certificado/verificar.html`
- **Código-fonte:** repositório `laboratorio-tech-social` (licença MIT)
- **Segurança de crianças e adolescentes:** `laboratorio-tech-social/docs/seguranca-criancas.md`

---

## Fim da trilha

> **“Commit ou não existe.”**
>
> Você começou esta trilha sem saber o que era um commit. Termina com um projeto
> publicado, testado, documentado, versionado e com licença aberta. O próximo passo
> não é seu professor — é seu. O repositório fica aberto. O projeto fica no ar.
> E o que você aprendeu, ninguém tira.
