# Curso "Tecnologia na Prática" — Trilha 18+ (Profissionais)

**São Pedro/SP** · 16 aulas ao vivo online · 90 min por aula · **carga total: 24 horas**

**Público:** adultos que já usam computador no trabalho — professores da rede municipal,
servidores da Secretaria de Educação, participantes da EJA, profissionais do comércio e
serviços de São Pedro e região de Piracicaba.

**Frase que abre o curso:** *"A tecnologia não falta no seu dia a dia. O que falta é o
método para usá-la a seu favor — e tempo para aprender a fundo."*

---

## 📚 Sumário

| # | Módulo | Aula | Entregável |
|---|---|---|---|
| [Módulo 1](#m01) | **P1** — Linha de Comando e Automação do Sistema (parte 1) | 1 | Script de shell com log e código de saída |
| [Módulo 2](#m02) | **P2** — Linha de Comando (parte 2: `cron` e versionamento do script) | 2 | Rotina agendada + repositório Git inicial |
| [Módulo 3](#m03) | **P3** — Python para Automatizar a Rotina (parte 1) | 3 | Script Python real rodando na sua máquina |
| [Módulo 4](#m04) | **P4** — Python para Automatizar (parte 2: backup, `--dry-run`, `unittest`) | 4 | Script com backup + dry-run + 8 testes verdes |
| [Módulo 5](#m05) | **P5** — Git e GitHub profissional (parte 1) | 5 | Repositório profissional: README, LICENSE, `.gitignore` |
| [Módulo 6](#m06) | **P6** — Git e GitHub profissional (parte 2: branch, PR, GitHub Actions) | 6 | Branch + PR revisado + pipeline verde |
| [Módulo 7](#m07) | **P7** — Dados e Planilhas (parte 1: CSV/XLSX) | 7 | Script de leitura e limpeza de dados |
| [Módulo 8](#m08) | **P8** — Dados e Planilhas (parte 2: relatório automatizado em Excel) | 8 | Relatório `.xlsx` automatizado com histórico |
| [Módulo 9](#m09) | **P9** — Segurança Digital e LGPD (parte 1: OWASP e threat model) | 9 | Política de dados + threat model de 1 página |
| [Módulo 10](#m10) | **P10** — Segurança Digital e LGPD (parte 2: scanner de segredos e checklist) | 10 | Scanner de segredos + checklist LGPD assinado |
| [Módulo 11](#m11) | **P11** — IA no Trabalho (parte 1: prompt versionado) | 11 | Prompt versionado com critério de aceite e 3 testes de saída |
| [Módulo 12](#m12) | **P12** — IA no Trabalho (parte 2: automação com revisão humana) | 12 | Automação com revisão humana + registro de uso |
| [Módulo 13](#m13) | **P13** — Projeto Final (escopo, plano de testes, backlog) | 13 | Escopo assinado + plano de testes + backlog priorizado |
| [Módulo 14](#m14) | **P14** — Projeto Final (implementação com métricas) | 14 | Implementação com KPIs medidos |
| [Módulo 15](#m15) | **P15** — Projeto Final (qualidade, pipeline, relatório de risco) | 15 | Pipeline verde + relatório de risco + documentação |
| [Módulo 16](#m16) | **P16** — Showcase e Certificado | 16 | Repositório público + apresentação + certificado |
| — | [Encerramento e Certificação](#encerramento-e-certificacao) | — | Rubrica, pesos, KPIs e modelo de certificado |
| — | [Como se inscrever](#como-se-inscrever) | — | Passo a passo de inscrição |

---

## 📌 Sobre este material

| Item | Detalhe |
|---|---|
| **Nome** | Tecnologia na Prática — Trilha **Profissionais (18+)** |
| **Formato** | 100% **ao vivo online**, 1 encontro por semana, turma de até 20 alunos |
| **Carga horária** | 16 aulas × 90 min = **24 horas** |
| **Custo** | **R$ 0,00**. Sem mensalidade, sem material pago, sem prova eliminatória |
| **Licença** | **MIT** — uso livre, inclusive comercial e educational |
| **Repositório de origem** | [`Material-Didatico-Tecnologia`](https://github.com/Marquezbertin) · [`laboratorio-tech-social`](https://marquezbertin.github.io/laboratorio-tech-social/) · [`manual-qa-completo`](https://github.com/Marquezbertin/manual-qa-completo) · [`qa-exercicios-praticos`](https://github.com/Marquezbertin) · [`QA_RUN`](https://marquezbertin.github.io/QA_RUN/) · [`Central-de-noticias`](https://github.com/Marquezbertin) · [`esporte-sao-pedro`](https://github.com/Marquezbertin) |
| **Material de apoio** | 41 exercícios interativos em [`laboratorio-tech-social/site/exercicios/`](https://marquezbertin.github.io/laboratorio-tech-social/) · 71 jogos educativos em [`QA_RUN/index.html`](https://marquezbertin.github.io/QA_RUN/) |
| **Linguagem** | Português do Brasil, terminologia técnica em inglês quando é o padrão da ferramenta |

### Pré-requisitos

| Item | Obrigatório? | Observação |
|---|---|---|
| Ler e escrever texto no computador | **Sim** | Não exige saber programar |
| Usar navegador e abrir/baixar arquivos | **Sim** | Todo o curso roda no navegador se preciso |
| Instalar software | **Sim** | Só Git e Python — ambos gratuitos |
| Terminal | **Sim** | Linux/macOS: Terminal. Windows: [WSL](https://learn.microsoft.com/pt-br/windows/wsl/install) ou Git Bash |
| Python 3.10+ | **Sim** | [python.org](https://www.python.org/downloads/) — ou [Google Colab](https://colab.research.google.com/) se não puder instalar |
| Git | **Sim** | [git-scm.com](https://git-scm.com/downloads) |
| Conta no GitHub | Sim, **a partir da aula 5** | [github.com/signup](https://github.com/signup) — gratuita |
| Programação em qualquer linguagem | Não | É uma vantagem, não um requisito |

> **Regra da sala:** quem nunca abriu um terminal não fica para trás. A aula 1 começa do
> zero absoluto — abrir, navegar, ler arquivo. Se a internet da sua casa falhar na
> primeira semana, você ainda pode fazer a tarefa pelo [Colab](https://colab.research.google.com/).

### Trilha de autostudy (4 meses)

Este material funciona **sozinho**, fora da sala. O ritmo recomendado é
**1 módulo por semana, 2 horas por sessão** — a trilha inteira leva **4 meses**.

| Semana | Módulo | Tarefa de 2 h do autostudy |
|---|---|---|
| 1–2 | P1 e P2 — Linha de comando | Script de shell + rotina agendada na sua própria máquina |
| 3–4 | P3 e P4 — Python | Script real da sua rotina + 8 testes `unittest` verdes |
| 5–6 | P5 e P6 — Git e GitHub | Repositório dos módulos anteriores, 20 commits, CI ativa |
| 7–8 | P7 e P8 — Dados e planilhas | Relatório automatizado em `.xlsx` a partir do seu CSV |
| 9–10 | P9 e P10 — Segurança e LGPD | Política de dados + scanner de segredos rodando no seu repositório |
| 11–12 | P11 e P12 — IA | Prompt versionado + automação com revisão humana registrada |
| 13–16 | P13 a P16 — Projeto final | Consolide tudo num repositório público e apresente |

**Como não travar no autostudy:**

1. Rode `man <comando>` e `--help`. A resposta está na própria ferramenta.
2. Leia o **código** dos repositórios de referência — ele é a documentação.
3. Use `git log -S "termo"` para descobrir quem mudou o quê e por quê.
4. Programe com os arquivos `.txt` do [`python-do-zero`](https://github.com/Marquezbertin):
   são 90 exercícios com "Resposta Esperada" que funcionam **100% offline**.

### Custos — tudo R$ 0

| Item | Custo | Observação |
|---|---|---|
| Aulas ao vivo | R$ 0 | 16 encontros de 90 min |
| Terminal, Python, Git, VS Code | R$ 0 | Todos com versão gratuita |
| [GitHub](https://github.com/signup) | R$ 0 | Conta gratuita, repositórios públicos ilimitados |
| [GitHub Pages](https://pages.github.com/) | R$ 0 | Hospedagem de até 1 GB por repositório |
| [Google Colab](https://colab.research.google.com/) | R$ 0 | Alternativa ao Python local |
| [SQLite Browser](https://sqlitebrowser.org/) | R$ 0 | Visualizador de banco de dados |
| [Scratch](https://scratch.mit.edu/) | R$ 0 | Para demonstrações visuais do professor |
| [QA_RUN](https://marquezbertin.github.io/QA_RUN/) | R$ 0 | 71 jogos de revisão |
| [ANPD](https://www.gov.br/anpd/) | R$ 0 | Guias oficiais da LGPD |

> ⚠️ **Nunca use dado real de cliente, aluno ou paciente sem autorização formal.**
> A regra vale mesmo quando o material é gratuito.

### Contexto de São Pedro/SP

Os exemplos desta apostila não são genéricos: eles são do seu município.

| Dado | Valor | Por que importa aqui |
|---|---|---|
| População | ~40.054 habitantes (est. IBGE 2026); 38.256 no Censo 2022 | Dimensiona o volume de dados que a rede lida por ano |
| IDHM | 0,755 | IDHM **médio**: o município tem infraestrutura digital, mas com desigualdade de acesso |
| PIB per capita | R$ 32.496,26 (2023) | Explica por que o curso precisa ser gratuito e acessível no celular |
| Área | 611 km² | dispersed: rotas de transporte e agenda escolar exigem planejamento |
| Escolas no município | 29 escolas · 7.134 matrículas · **467 docentes** | Os **467 professores** são o público-alvo mais imediato desta trilha |
| Rede municipal (Secretaria de Educação) | **23 unidades de ensino** · ~5.200 alunos · 15 unidades em tempo integral | É a estrutura que a automação vai tocar |
| Conectividade | **100% das escolas com internet**; 51,7% com laboratório de informática; 82,8% com biblioteca/sala de leitura | Já existe a base para o professor produzir material digital |
| **EJA ativa** na rede municipal | Educação de Jovens e Adultos com público 18+ | Esta trilha é a continuação natural da EJA: ela **devolve tempo** ao aluno adulto |
| EJA Profissionalizante | Parceria com **Sesi** e **Senai** (robótica, design de games, inglês) | A trilha 18+ conecta com esses cursos já existentes |
| Escola Técnica Estadual Gustavo Teixeira | Centro Paula Souza, nível médio/técnico | Fonte de egressos para o mercado de trabalho local |
| **ESALQ/USP** | **GESP (Grupo de Extensão de São Pedro/SP)**, 34 anos com agricultores familiares | Parceiro natural para mentoria e projetos de impacto |
| Identidade | "Estância Turística", região de Piracicaba | Turismo gera planilha, agenda, lista e relatório — tudo automatizável |
| Contexto técnico de referência | [`esporte-sao-pedro`](https://github.com/Marquezbertin) (app do clube da cidade com Supabase + RLS + Edge Functions + IA) e [`Central-de-noticias`](https://github.com/Marquezbertin) (pipeline RSS → resumo → TTS → PWA) | Dois projetos **reais** da cidade que a turma estuda por dentro |

**Casos de uso que você pode automatizar com este material:**

1. **Planilha de chamada** de uma unidade de ensino → CSV → relatório de frequência mensal.
2. **Controle de presença** da equipe da Secretaria de Educação → consolidação automática.
3. **Relatório de notas** por turma e por componente → `.xlsx` formatado para a reunião pedagógica.
4. **Lista de entrega de kits escolares** (material didático) → conferência e baixa automática.
5. **Agenda da Secretaria de Educação** → lembretes e consolidar compromissos em um só arquivo.

> Todos os dados dos exemplos são **fictícios** e **gerados por script**, exatamente como
> a regra da sala exige.

### Regras da sala adulta

Estas 8 regras valem em **todas** as 16 aulas. Elas não são decoração: são o que separa
um script que roda da sua empresa de um script que derruba um relatório às 3 da manhã.

| Regra | Por que ela existe |
|---|---|
| **Erro é método** | O professor **pergunta**, não entrega. Adulto aprende mais rápido testando do que ouvindo |
| **Dados fictícios por padrão** | Nada de dado real de cliente sem autorização. LGPD e ética profissional |
| **LGPD vale para tudo** | Planilha do RH, e-mail do aluno, foto do crachá. Não há "dado interno" |
| **Backup antes de operação destrutiva** | Nenhum script apaga ou sobrescreve sem cópia |
| **Nada de segredo no repositório** | Nem em arquivo, nem no histórico. `.env` no Git vaza **para sempre** |
| **Documentação é parte do trabalho** | README e log não são burocracia. O que não está escrito não existe para o próximo |
| **IA é ferramenta, não autor** | Toda saída de IA passa por **revisão humana**. O modelo responde; a responsabilidade é sua |
| **Teste que não roda é bug** | Inclusive em script pessoal. Inclusive no seu |

### Como a aula funciona (formato ao vivo online)

| Item | Regra |
|---|---|
| **Duração da aula** | 90 min, em 5 fases cronometradas (ver o roteiro de cada módulo) |
| **Tarefa de casa** | **2 h por semana**, assíncrona. O aluno termina em casa e **traz o resultado na aula seguinte** |
| **Abertura da sala** | O link do encontro fica na descrição. **5 min antes**, o professor abre a sala e testa áudio e vídeo |
| **Fala na sala** | **Mão levantada** (ícone de mão no chat) ou **reação** (👍 para "entendi", ❓ para "não entendi") |
| **Câmera** | **Obrigatória nas fases 1 e 5** (apresentação e mostra). **Opcional nas fases 2, 3 e 4** |
| **Breakout rooms** | Fase 3 — turmas de **3 a 4 alunos**, com professor circulando |
| **Provas de entende** | A cada 15 min, o professor pergunta "quem está travado?" — quem responde ganha 1 ponto de presença |
| **Presença** | Lista de chamada simples **por apelido** na primeira aba do chat |
| **Plano B (internet caiu)** | O material está no repositório: baixe o enunciado, continue offline, volte na semana seguinte com a dúvida |
| **Gravação** | Encontros gravados e publicados no repositório do curso (com consentimento) |

**Modelo de presença (o professor cola no chat):**

```
PRESENÇA — Trilha 18+ — Aula 03/16
1. Digite seu apelido + um emoji
2. Mão levantada só para falar
3. Câmera ligada nas fases 1 e 5
```

---

<a id="m01"></a>

## Módulo 1 — Linha de Comando e Automação do Sistema (Aula 1)

**Duração:** 90 min · **Aula 1 de 16** · **P1** (módulo em 2 aulas: 1 e 2)
**Entregável do módulo:** **script de shell executável com log em arquivo e código de saída correto**, mais um arquivo `notas-de-aula.md` com a saída real de cada comando.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar a diferença entre **terminal** e **interface gráfica**, e dizer com clareza quando o terminal é melhor (e quando é pior).
2. Navegar no sistema de arquivos com `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv` e `rm`, entendendo o que cada comando **realmente** faz.
3. Aplicar o **princípio do menor privilégio** ao ler permissões (`ls -l`, `chmod`, `chown`) e ao criar usuário de serviço para um script.
4. Encadear comandos com **pipes** (`|`) e **redirecionamento** (`>`, `>>`, `<`, `2>`, `2>&1`).
5. Extrair informação de arquivos de texto com `grep`, `find`, `sort`, `uniq`, `head`, `tail` e `wc`.
6. Escrever um **script de shell** com variáveis, teste condicional, laço e **código de saída** (`exit 0` / `exit 1`), e rodá-lo com `bash`.
7. Diagnosticar problemas lendo **logs** e o **código de saída** de um comando, sem adivinhar.

**Objetivo secundário:** Escrever, em uma frase, por que `rm -rf /` nunca deve ser digitado sem pensar — e por que a lixeira do desktop não existe no terminal.

---

### 📚 Fontes no repositório

A trilha adulta não tem um repositório de shell script — e isso é proposital: os comandos
desta aula são **do sistema operacional**, não do material. O que os repositórios ofrecen
são **automações reais** para ler a estrutura e servir de referência:

| Fonte real | O que mostra nesta aula |
|---|---|
| `manual-qa-completo/Makefile` | Automação real com **alvos nomeados** (`scripts`, `test-api`, `test-ui`, `check-mermaid`, `all`), cada um rodando comandos `python`/`pytest`. É um script de shell com nome |
| `manual-qa-completo/run_all.py` | O mesmo "make all" em Python: executa uma **lista de scripts**, conta falhas e devolve **código de saída** (`return 1 if failures else 0`) |
| `Central-de-noticias/.github/workflows/update-news.yml` | Bloco `run:` de shell real dentro de YAML: guarda "já atualizou hoje?", `git diff --cached --quiet` para não commitar sem mudança, `|| true` para não abortar o pipeline |
| `Central-de-noticias/.github/workflows/monitoramento.yml` | Shell que **falha de propósito** (`exit 1`) quando o arquivo esperado não existe — modelo de verificação automática |
| `qa-automation-framework/` | Estrutura de pastas profissional: `config/`, `core/`, `pages/`, `tests/`, `utils/`, `requirements.txt`, `pyproject.toml` |
| `laboratorio-tech-social/site/exercicios/` | 41 páginas de laboratório interativo para treinar fora da aula |

> **A regra do módulo:** nada de "digite e acredite". Todo comando é executado **na frente
> da turma**, com saída real. Se o comando não roda, corrige-se na hora — e o aluno vê a
> correção.

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Terminal** | "A janela de texto que conversa com o sistema. O clique é uma ótima forma de pedir — mas é lento e não se automatiza." |
| **Interface gráfica** | "O botão já faz a ordem por você. O terminal faz a ordem **na sua frente**." |
| **Prompt** | "A linha que mostra onde você está e espera o comando. `$` = usuário comum, `#` = root." |
| **`pwd` / `ls` / `cd`** | "Onde estou, o que tem aqui, ir para lá." |
| **Caminho absoluto × relativo** | "`/home/ana` é **endereço**; `../planilhas` é **referência**." |
| **`cp` / `mv` / `rm`** | "Copiar, mover, apagar. Na ordem dessa força: `cp` é reversível, `rm` **não** é." |
| **Permissão (`rwx`)** | "`r` ler, `w` escrever, `x` executar. O **dono**, o **grupo** e os **outros**." |
| **Menor privilégio** | "Dê a **menor** permissão que faz o trabalho — e só a ela." |
| **Pipe (`|`)** | "A saída de um comando vira **entrada** do próximo. Uma linha, muitas ferramentas." |
| **Redirecionamento (`>`)** | "`>` **sobrescreve**. `>>` **acrescenta**. `2>` manda o erro para outro lugar." |
| **`grep` × `find`** | "`grep` procura **dentro** do arquivo; `find` procura **o arquivo**." |
| **`sort` / `uniq` / `wc`** | "Ordenar, contar repetidos, contar linhas." |
| **Variável de shell** | "`NOME=valor` cria. `$NOME` usa. Sem `$` é só texto." |
| **Código de saída** | "O número que o comando deixa para o próximo: `0` = deu certo, `!= 0` = deu errado." |
| **`set -euo pipefail`** | "Pare na primeira falha, erro não declarado é erro, e pipe que quebra é falha." |
| **Log** | "O **diário** do sistema. Sem log, você adivinha." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura da sala online (2 min).** O link do encontro está na descrição. O professor
abre a sala 5 minutos antes, testa o áudio, escreve no chat:

```
PRESENÇA — Trilha 18+ — Aula 01/16
1. Digite seu apelido + um emoji
2. Mão levantada (ícone de mão) só para falar
3. Câmera LIGADA nesta fase. Depois pode desligar
4. Se a internet cair: eu continuo aqui. Anote e volte na próxima semana
```

**Regra de fala:** *"Não existe pergunta boba aqui. Se eu não entendi o que você perguntou,
eu pergunto de novo — e pergunto de novo é o método, não o fracasso."*

**Gancho (3 min):** *"Toda vez que você renomeia 300 arquivos, ou repara que o relatório
do mês passado foi gerado com a planilha errada, você repete o mesmo trabalho. Nenhuma
dessas tarefas precisa de um mouse. O terminal é o jeito mais rápido — e é o **único** que
automatiza. É o mesmo terminal que roda o deploy do site que você usa todo dia."*

**Demonstração ao vivo (5 min):** abra o terminal e rode, **sem explicar nada ainda**:

```bash
# 1. Onde eu estou?
pwd

# 2. O que tem aqui?
ls -la

# 3. O tamanho de cada arquivo, do maior para o menor
ls -lhS

# 4. Quantas linhas tem o arquivo de log?
wc -l /var/log/syslog
```

Depois rode, **com o mesmo resultado e sem clicar em nada**:

```bash
# A mesma informação, em uma linha só, encadeada
ls -lh | sort -k5 -h | tail -3
```

Diga: *"A segunda forma eu **escrevo**; a primeira eu **clico**. Daqui a quatro aulas você
vai escrever a segunda."*

> **Plano B (a internet caiu):** o professor manda o enunciado completo no chat e no
> repositório do curso; o aluno baixa e faz offline, retorna na semana seguinte.

#### Fase 2 — Exploração (25 min)

**Parte 1 — Terminal × interface gráfica (4 min).**

| | Interface gráfica | Terminal |
|---|---|---|
| Velocidade | 1 ação por clique | 1 linha faz 10 ações |
| Repetição | você repete | o **script** repete |
| Documentação | difícil de descrever | o comando **é** a documentação |
| Erro | botão desabilitado | mensagem de erro **com texto** |
| Automação | macro gravada | script versionável |

**Parte 2 — Navegação (7 min).**

```bash
pwd                 # onde estou (print working directory)
ls                  # lista o conteúdo
ls -la              # inclui ocultos (.git, .env) e permissões
ls -lhS             # legível, ordenado por tamanho
cd ~/Documentos      # vai para a pasta
cd ..                # sobe um nível
cd -                 # volta para a pasta anterior
mkdir ~/projeto-linha-de-comando      # cria pasta
touch notas.txt                      # cria arquivo vazio
cp notas.txt copia-notas.txt          # copia
mv copia-notas.txt documento-final.txt # move (ou renomeia)
rm documento-final.txt                # apaga
rm -r pasta-antiga                    # apaga pasta e conteúdo
```

**As 3 regras de segurança que valem para a vida toda:**

1. `rm` **não** tem "lixeira". Não existe como desfazer no terminal.
2. Antes de `rm -r`, rode `ls` **na mesma pasta** e leia o que vai ser apagado.
3. `rm -rf /` (com barra) apaga o sistema inteiro. **Nunca digite isso.**

> ⚠️ **Demonstre o perigo no slide, não no terminal.** Escreva `rm -rf /` num arquivo de
> texto do editor e mostre a tela. Explique que o comando existe de verdade e que
> **ninguém** digita na pressa.

**Parte 3 — Permissões e menor privilégio (6 min).**

```
-rwxr-xr--   1 ana  staff  4096  script.sh
│└┬┘└┬┘└┬┘
│ │  │  └── outros (r-- = só ler)
│ │  └───── grupo (r-x = ler e executar)
│ └──────── dono (rwx = ler, escrever, executar)
```

```bash
ls -l                       # mostra as permissões
chmod +x script.sh          # adiciona permissão de execução ao dono
chmod 644 notas.txt         # dono: rw; grupo e outros: só leitura
chmod 755 meu-programa.sh   # padrão para scripts executáveis
chown ana:ana script.sh     # muda dono e grupo (só root/administrador)
```

**Princípio do menor privilégio (a frase que fixa):** *"O script só precisa de ler o
arquivo de entrada e gravar o arquivo de saída. Ele **não** precisa de `chmod 777` nem de
`sudo`. Se você precisa de `sudo` para o script rodar, o script está errado — ou o
usuário do sistema está errado."*

**Parte 4 — Pipes e redirecionamento (5 min).**

```bash
# Pipe: a saída de um comando vira entrada do próximo
cat notas.txt | grep " urgente"

# Redirecionamento: > sobrescreve, >> acrescenta
python3 notas.py > resultado.txt     # guarda a saída no arquivo (apaga o que tinha)
python3 notas.py >> historico.txt    # acrescenta ao histórico

# Erro em outro lugar
python3 notas.py 2> erros.txt        # só o erro vai para o arquivo
python3 notas.py > saida.txt 2>&1    # saída e erro no mesmo arquivo
python3 notas.py 2>&1 | tee tela.txt # mostra na tela E grava no arquivo
```

**Parte 5 — As ferramentas de texto (3 min).**

```bash
grep -n "erro" app.log          # linha e número da linha
grep -rin "erro" app.log        # sem diferenciar maiúsculas/minúsculas
grep -c "erro" app.log          # só a contagem
grep -r "TODO" src/             # recursivo numa pasta

find . -name "*.log"            # arquivos pelo nome
find . -name "*.log" -mtime -7  # modificados nos últimos 7 dias
find . -type f -size +100M      # arquivos com mais de 100 MB

sort nomes.txt                  # ordena
sort -u nomes.txt | uniq -c    # conta repetidos, do mais comum ao menos comum
head -5 arquivo.txt             # primeiras 5 linhas
tail -5 arquivo.txt             # últimas 5 linhas
tail -f app.log                 # acompanha o log em tempo real (Ctrl+C para sair)
wc -l arquivo.txt               # conta linhas
```

> **Mostre ao vivo:** `tail -f` com um log sendo escrito por outro terminal. É o
> "grito" do administrador de sistemas.

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** o professor abre **4 salas de 3 a 5 alunos** (para turma de 20) e
circula. Regra da sala: **a câmera é opcional nesta fase**, e ninguém sai do breakout
sem tentar.

**Atividade A — Do clique ao comando (10 min).**
Cada aluno cria a pasta de trabalho e executa, **na ordem**, registrando a saída real de
cada comando no arquivo `notas-de-aula.md`:

```bash
mkdir -p ~/projeto-linha-de-comando/{dados,logs,scripts}
cd ~/projeto-linha-de-comando
printf 'urgente\nrotina\nurgente\nrelatorio\nurgente\n' > dados/tarefas.txt
ls -la
wc -l dados/tarefas.txt
grep -c "urgente" dados/tarefas.txt
sort dados/tarefas.txt | uniq -c
```

**Fala do professor enquanto circula (texto exato):** *"Pessoal, eu vou passar em cada sala
e fazer uma pergunta só: **qual comando eu rodei por último?** Se você não souber
responder sem olhar o histórico, tudo bem — olhe o histórico. O objetivo de hoje não é
decorar comando, é **saber onde a resposta está**. Em duas semanas esse comando vai estar
automatizado e você não vai precisar lembrar."*

**Entregável da Atividade A:** `notas-de-aula.md` com **a saída real** de cada comando
(colada, não reescrita).

**Atividade B — Script de shell completo (20 min).**
Crie `scripts/backup-relatorio.sh`:

```bash
#!/usr/bin/env bash
# backup-relatorio.sh
# Copia os relatórios do dia para a pasta de backup com data no nome.
# Uso: bash scripts/backup-relatorio.sh

set -euo pipefail   # para na primeira falha; erro não declarado é erro; pipe quebrado é falha

DATA="$(date +%Y-%m-%d)"
ORIGEM="dados"
DESTINO="backups/${DATA}"
LOG="logs/backup-${DATA}.log"

# Função auxiliar: escreve no log e na tela
registrar() {
  echo "[$(date +%H:%M:%S)] $1" | tee -a "$LOG"
}

# Garante que a pasta de logs exista ANTES de qualquer escrita no log
mkdir -p "$(dirname "$LOG")"

# Validação: a pasta de origem precisa existir
if [ ! -d "$ORIGEM" ]; then
  registrar "ERRO: a pasta de origem '$ORIGEM' não existe."
  exit 1        # código de saída 1 = falha
fi

# Cria a pasta de destino
mkdir -p "$DESTINO"

registrar "Iniciando backup de '$ORIGEM' para '$DESTINO'"

# Laço: um arquivo por vez
CONTAGEM=0
for ARQUIVO in "$ORIGEM"/*.txt; do
  [ -e "$ARQUIVO" ] || continue          # ignora o caso de nenhum arquivo encontrado
  cp -p "$ARQUIVO" "$DESTINO/"
  CONTAGEM=$((CONTAGEM + 1))
  registrar "Copiado: $(basename "$ARQUIVO")"
done

registrar "Backup finalizado: $CONTAGEM arquivo(s)."

# Código de saída 0 = tudo certo
exit 0
```

Rode e ensine a ler o resultado:

```bash
chmod +x scripts/backup-relatorio.sh
bash scripts/backup-relatorio.sh
echo "código de saída: $?"      # 0 = sucesso
cat logs/backup-$(date +%Y-%m-%d).log
```

**Demonstre a falha de propósito** (renomeie a pasta de origem e rode de novo): o script
**para**, escreve no log e devolve **código de saída 1**.

**Fala do professor (texto exato):** *"É assim que o script avisa quem agendou ele. Um
script que falha em silêncio é o pior tipo de script que existe — porque ele produz
resultado errado com cara de resultado certo. Guarda essa frase, ela vale para a aula de
Python também."*

**Entregável da Atividade B:** `scripts/backup-relatorio.sh` executável, com
`set -euo pipefail`, log em arquivo e **código de saída** correto nos dois cenários
(sucesso e falha).

> **Plano B:** se o breakout travar ou a internet cair, o professor pede para um aluno
> **compartilhar a tela** e demonstra o script do lado dele, refazendo cada comando ao
> vivo com explicação passo a passo.

#### Fase 4 — Projeto (20 min)

**Desafio: "O meu relatório, sem a minha planilha"**

Cada aluno escreve **um script de shell** para uma tarefa da sua rotina real. Exemplos
de São Pedro/SP:

| Tarefa | Entrada | Saída do script |
|---|---|---|
| Consolidar a **planilha de chamada** | `dados/chamada.csv` | `relatorios/frequencia-<mês>.csv` |
| Conferir a **lista de entrega de kits escolares** | `dados/kits.csv` | `relatorios/pendencias.txt` |
| Arquivar o **relatório de notas** do mês | `relatorios/notas-abril.xlsx` | `backups/2026-04-<timestamp>/` |
| **Limpar a pasta de downloads** | `~/Downloads` | arquivos movidos para `~/Organizados` |

**Critério de pronto:**
- [ ] O script tem `#!/usr/bin/env bash` e `set -euo pipefail`
- [ ] O script usa **variáveis** (nenhum caminho repetido 5 vezes no código)
- [ ] O script tem **teste condicional** (`if`) tratando um caso de ausência
- [ ] O script tem **laço** (`for` ou `while`) e **contador**
- [ ] O script grava **log** em arquivo e mostra na tela (`tee`)
- [ ] O script devolve **código de saída 0** no sucesso e **1** na falha (teste os dois!)
- [ ] O script **não apaga nada** sem ter feito cópia antes
- [ ] Existe `README.md` com: o que o script faz, como rodar, onde fica o log
- [ ] O `.gitignore` cobre `logs/` e `backups/`

#### Fase 5 — Mostra (5 min)

**Câmera ligada nesta fase.** Dois alunos apresentam em **60 segundos cada** (compartilhando
a tela) e respondem 2 perguntas da turma:

1. "Qual arquivo esse script mexe?"
2. "Se ele falhar amanhã às 6h30, eu descubro onde?"

> **Pergunta de saída (escrita no chat, 1 frase):** "Qual a diferença entre `>` e `>>`? E
> por que um script que executa todo dia precisa obrigatoriamente de um log?"

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| `notas-de-aula.md` | Saída **real** de cada comando, colada — não reescrita |
| Script de shell | Executa sem erro; tem `set -euo pipefail`, variáveis, `if`, `for` |
| Códigos de saída | `0` no sucesso e `1` na falha (testado e **mostrado** na aula) |
| Log | Arquivo de log gerado, com data/hora e mensagem por operação |
| Compreensão | O aluno explica o que cada comando faz **sem** ler o slide |
| Postura | Responde à pergunta de saída em 1 frase, sem "não sei" |

**Pergunta de escrita:**
> "Você agendou um backup diário às 6h30. Na quarta-feira, o log mostra que o backup parou
> de rodar no domingo. O `crontab -l` continua com a mesma linha, e o script, rodado na mão,
> funciona. O que você investiga, **nesta ordem**?"
>
> **Resposta:**
> 1. **Ambiente do cron.** O cron roda com um `PATH` e um `HOME` **mais pobres** que o seu
>    terminal. Quase sempre o culpado é um comando que existe no seu shell e não existe
>    para o cron (por exemplo, `python` instalado via `pyenv` ou `conda`). *Correção:* usar
>    caminho **absoluto** do interpretador e `set -euo pipefail` no script.
> 2. **Diretório de trabalho.** O cron inicia em `$HOME`, não no diretório do script. Por
>    isso o caminho relativo (`dados/`) quebra. *Correção:* `cd ~/projeto && bash ...` na
>    linha do cron, ou `cd "$(dirname "$0")"` dentro do script.
> 3. **Permissões.** O arquivo pode ter `chmod 600` e o cron roda como outro usuário, ou o
>    destino não tem permissão de escrita. Cheque com `ls -ld` da pasta de destino.
> 4. **Disco cheio.** `df -h`. Backup que enche o disco para e o próximo erro é "no space
>    left on device" — leia o log, não o script.
> 5. **Código de saída.** Se o script devolve `!= 0`, o cron **não avisa ninguém** (a menos
>    que você redirecione `2>&1` para um log). O log é o seu alarme.
>
> **Em resumo:** primeiro o *ambiente*, depois o *caminho*, depois as *permissões*, e
> sempre o *log* como fonte da verdade.

---

### 🧩 Exercícios extras (do repositório e do sistema)

| Onde | Sobre |
|---|---|
| `manual-qa-completo/Makefile` | Automação com alvos nomeados (`make scripts`, `make test-api`, `make all`) — o `Makefile` é um script de shell com nome |
| `manual-qa-completo/run_all.py` | Executa uma lista de scripts, conta falhas e **devolve código de saída** — o mesmo contrato do `set -e` |
| `Central-de-noticias/.github/workflows/update-news.yml` | Bloco `run:` real: guarda "já atualizou hoje?", `|| true` para não abortar o pipeline, `git diff --cached --quiet` para não commitar sem mudança |
| `Central-de-noticias/.github/workflows/monitoramento.yml` | Shell que **falha de propósito** (`exit 1`) quando o arquivo esperado não existe — modelo de verificação automática |
| `qa-automation-framework/` | Estrutura de pastas profissional (`config/`, `core/`, `tests/`, `utils/`) para organizar o projeto |
| `laboratorio-tech-social/site/exercicios/simulador-api.html` | Praticar requisição e status HTTP antes do módulo de Python |
| `QA_RUN` — jogo *Terminal Typer* | Treinar a ordem correta dos comandos de terminal |
| `QA_RUN` — jogo *Log Watch* | Separar linha de log suspeita de linha legítima |

**Exercícios de terminal para treinar fora da aula:**

1. **Descoberta do sistema:** `uname -a`, `cat /etc/os-release`, `df -h`, `free -h`, `nproc`, `whoami`.
2. **Caça ao arquivo perdido:** `find ~ -name "*.csv" -mtime -30` e `du -sh ~/Downloads/* | sort -h | tail -5`.
3. **Contador de linhas de código:** `find . -name "*.py" -exec wc -l {} + | tail -1`.
4. **Servidor de arquivos na rede local:** `python3 -m http.server 8000` — sirva a pasta do projeto e acesse de outro dispositivo na mesma rede.
5. **Portas e processos:** `ps aux | head -20`, `ss -tlnp` (ou `netstat -an` no Windows).

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Escolha **1 tarefa repetitiva da sua rotina** (backup de arquivos, renomear planilhas,
   gerar um relatório, conferir lista de entrega) e escreva um script de shell para ela,
   com **log** e **código de saída**.
2. Rode o script **2 vezes**: uma com sucesso e uma forçando falha. **Cole as duas
   saídas** no `notas-de-aula.md`.
3. Escreva no `README.md` uma seção **"Problemas conhecidos"** com 1 item. (Quem lê um
   script de automação precisa saber onde ele **falha**.)
4. Deixe o script pronto para ser agendado — a aula 2 vai agendar juntos.
5. (Opcional) Rode `man 5 crontab` no Linux e anote os 3 campos que mais confundem gente.

> **Na aula 2** você vai transformar esse script em rotina agendada e colocar no Git.

---

### 🔗 Próximo módulo

[Módulo 2 — Linha de Comando (parte 2: `cron` e versionamento do script) · Aula 2](#m02)

---

<a id="m02"></a>

## Módulo 2 — Linha de Comando (parte 2): `cron` e versionamento do script (Aula 2)

**Duração:** 90 min · **Aula 2 de 16** · **P2** (continuação do Módulo 1)
**Entregável do módulo:** **1 rotina automatizada agendada** (com `cron` ou Agendador de
Tarefas) **+ repositório Git inicial** com README e `.gitignore`.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. **Agendar** a execução automática de um script com `cron`, entendendo os **5 campos**
   e o comportamento de `PATH`, `HOME` e diretório de trabalho.
2. Fazer **equivalência** entre `cron` (Linux/macOS), `schtasks` (Windows) e o
   **Agendador de Tarefas**, e escolher a ferramenta certa para o ambiente do aluno.
3. Conhecer o `systemd timer` como alternativa moderna e explicar, em uma frase, a
   diferença entre os dois.
4. Escrever uma linha de `cron` **robusta**: caminho absoluto, redirecionamento de saída e
   erro para log, e `cd` explícito.
5. **Versionar o script no Git** — porque script sem histórico é script que ninguém
   consegue corrigir — criando `README.md`, `.gitignore` e `LICENSE`.
6. Diagnosticar uma rotina agendada que **parou de rodar**, usando log, código de saída,
   `df -h` e permissões.
7. Reconhecer o padrão **"job agendado + guarda + fallback"** usado em produção no
   `Central-de-noticias`.

**Objetivo secundário:** Escrever a linha de `cron` do seu script sem consultar a
documentação, em menos de 60 segundos.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `Central-de-noticias/.github/workflows/update-news.yml` | **Cron real** em YAML com **dois** agendamentos (horário fora do topo da hora), **guarda** "já atualizou hoje?", `|| true` para a primeira tentativa e `concurrency` para não empurrar um job por cima do outro |
| `Central-de-noticias/.github/workflows/monitoramento.yml` | Job que **verifica** se a rotina de hoje rodou e **dispara alerta** em caso contrário — é o "osso" do monitoramento |
| `Central-de-noticias/.github/workflows/limpar-historico.yml` | Cron mensal (`0 3 1 * *`), `concurrency` com o mesmo grupo e `--force` — o exemplo de que **forçar** é operação destrutiva e por isso exige backup |
| `manual-qa-completo/Makefile` | Alvos nomeados: a forma mais simples de "rodar várias coisas em ordem" |
| `manual-qa-completo/run_all.py` | Execução por lista + contagem de falhas + código de saída |
| `git-github-iniciantes/02_primeiro_repositorio/` | Passo a passo de `git init`, primeira configuração, primeiro commit |
| `git-github-iniciantes/03_trabalhando_com_mudancas/` | `git status`, `git diff`, `git add`, `git commit` |
| `qa-automation-framework/` | Estrutura de pastas para um projeto que já vai rodar sozinho |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **cron** | "O despertador do sistema: roda este comando às 6h de todo dia." |
| **5 campos** | "Minuto, hora, dia-do-mês, mês, dia-da-semana. Nessa ordem, sempre." |
| **`*/5`** | "Repete a cada 5 unidades: minutos, horas, dias..." |
| **Ambiente do cron** | "O cron é um terminal **de poverty**: `PATH` curto, `HOME` diferente, pasta errada." |
| **`schtasks`** | "O `cron` do Windows: mesmo conceito, sintaxe de PowerShell." |
| **systemd timer** | "O cron com mais controle: reinício, dependência, log próprio." |
| **Log do agendamento** | "`>> logs/cron.log 2>&1` é o que transforma 'achismo' em 'prova'." |
| **`git init`** | "Criar o histórico é cheap. Reconstruir o histórico depois é caro." |
| **`git add` × `git commit`** | "`add` = escolher o que entra. `commit` = dar nome ao que entra." |
| **`.gitignore`** | "A lista do que **nunca** entra: senha, log, backup, ambiente virtual." |
| **README** | "O manual do seu código. Sem ele, o script morre com você." |
| **Concorrência** | "Dois jobs no mesmo grupo não correm juntos — o segundo espera." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** releia o apelido da lista de presença, chame 3 alunos pelo apelido
para dizer "presente" (isso **acorda** quem entrou em modo espectador).

**Gancho (3 min):** *"Na aula passada você escreveu um script que roda quando você chama.
Hoje ele vai rodar quando você **não** estiver olhando. E adivinha o que acontece quando
uma coisa roda sem você: ela falha às 3 da manhã e ninguém vê. Por isso hoje a aula é
sobre duas coisas: **agendar** e **deixar rastro**."*

**Demonstração ao vivo (3 min):** mostre o `update-news.yml` aberto no editor e aponte as
duas linhas de cron:

```yaml
    - cron: "23 9 * * *"   # 09:23 UTC (06:23 de Brasília)
    - cron: "47 10 * * *"  # 10:47 UTC (07:47 de Brasília) — reforço, caso o primeiro seja derrubado
```

**Fala do professor (texto exato):** *"Repare no detalhe: o horário **não** é no topo da
hora. É 9h23 e 10h47. O autor descobriu na prática que job agendado no `:00` é o primeiro
a ser derrubado quando o servidor está sobrecarregado. Isso se chama **defesa por
observação** — e é exatamente o tipo de coisa que você só aprende fazendo."*

> **Plano B:** se a tela do editor não abrir, o professor cola o YAML no chat.

#### Fase 2 — Exploração (22 min)

**Parte 1 — `cron` na prática (8 min).**

```bash
crontab -e          # abre o editor do crontab do usuário
crontab -l          # mostra o que está agendado
```

**Os 5 campos, na ordem:** `minuto hora dia-do-mês mês dia-da-semana`.

| Exemplo | Quando roda |
|---|---|
| `*/5 * * * *` | a cada 5 minutos |
| `0 6 * * *` | todo dia às 6h00 |
| `30 6 * * 1-5` | de segunda a sexta, às 6h30 |
| `0 9 1 * *` | dia 1 de cada mês, às 9h |
| `0 3 1,15 * *` | dias 1 e 15 de cada mês, às 3h |

**A linha de cron robusta (a que você vai usar):**

```cron
# Backup dos relatórios todo dia às 6h30, com log no arquivo
30 6 * * * cd ~/projeto-linha-de-comando && bash scripts/backup-relatorio.sh >> logs/cron.log 2>&1
```

Três coisas que tornam essa linha **profissional**:

1. `cd ... &&` — o cron começa em `$HOME`, não no seu projeto.
2. `bash scripts/...` — caminho relativo **a partir do `cd`**, e `bash` explícito.
3. `>> logs/cron.log 2>&1` — **saída e erro** vão para o mesmo arquivo. Sem isso, o erro
   evapora e o log fica vazio num dia de falha.

**Parte 2 — As 3 armadilhas do cron (6 min).**

| Armadilha | Sintoma | Correção |
|---|---|---|
| `PATH` diferente | `command not found: python3` | caminho **absoluto** do interpretador |
| Diretório diferente | `arquivo não encontrado` | `cd` no `&&` ou `cd "$(dirname "$0")"` dentro do script |
| Sem redirecionamento | log vazio na falha | `>> logs/cron.log 2>&1` |

> **Fala do professor:** *"Três armadilhas. Todas as três aparecem na segunda-feira de um
> projeto que você fez na sexta à noite. Nenhuma delas é sua culpa — são as regras do
> ambiente. Por isso a gente **testa** o agendamento em vez de esperar até amanhã."*

**Parte 3 — Testar sem esperar (3 min).**

```bash
crontab -l                    # mostra o que está agendado

# TESTE: copie a linha trocando o horário por "a cada minuto" e espere 1 minuto
# Depois confira:
tail -20 logs/cron.log
```

**Parte 4 — Equivalências por sistema (3 min).**

| Tarefa | Linux (cron) | Windows (Agendador de Tarefas) |
|---|---|---|
| Agendar | `crontab -e` | Programador de Tarefas → Criar Tarefa |
| Testar | troque para `* * * * *` | "Executar agora" |
| Log | redirecione `>>` | campo "Argumentos" ou o próprio script |

```powershell
# Windows: schtasks (PowerShell)
schtasks /Create /TN "BackupRelatorio" /TR "C:\Users\USUARIO\projeto\scripts\backup-relatorio.sh" /SC DAILY /ST 06:30
schtasks /Run /TN "BackupRelatorio"     # testa sem esperar o relógio
schtasks /Delete /TN "BackupRelatorio" /F
```

**Parte 5 — `systemd timer` (visão geral, 2 min).**

| Recurso | `cron` | `systemd timer` |
|---|---|---|
| Reinício automático se falhar | não | sim (`RestartSec=60s`) |
| Depender de outro serviço | não | sim (`After=`/`Requires=`) |
| Log próprio e centralizado | não (você redireciona) | sim (`journalctl -u`) |
| Aviso de falha | não | sim (`OnFailure=` para notificar) |
| "Só roda entre 2h e 5h" | não | sim (`Persistent=`, `RandomizedDelaySec=`) |

```bash
systemctl list-timers                    # o que está agendado
journalctl -u backup-relatorio.service  # o log do serviço
```

> **Por que isso importa na sua rotina de trabalho:** agendar tarefa é, em boa parte das
> organizações, uma tarefa **do TI**, não do usuário. Converse com a equipe antes.

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. O professor circula com a lista de
presença impressa mentalmente e anota quem travou.

**Atividade A — Agendar e testar (15 min).**
Cada aluno pega o script da aula anterior e:

1. Cria a linha de `cron` **com caminho absoluto** e `>> logs/cron.log 2>&1`.
2. Instala com `crontab -e`.
3. **Testa** trocando temporariamente para `* * * * *` e esperando 1 minuto.
4. Confere o log: `tail -20 logs/cron.log`.
5. Volta o agendamento para o horário real.
6. Se estiver no **Windows**, faz o mesmo pelo `schtasks` (ou Agendador de Tarefas).

**Fala do professor enquanto circula (texto exato):** *"Me digam uma coisa: o log de vocês
tem alguma linha? Se o log está vazio, o script nem começou a rodar — e a causa quase
sempre é o `PATH` ou o diretório. Se o log tem linha mas o arquivo não apareceu, a causa
é permissão ou caminho dentro do script. Duas hipóteses, dois lugares. **Diagnóstico é
isso: hipótese, teste, conclusão.**"*

**Atividade B — Versionar no Git (15 min).**

```bash
cd ~/projeto-linha-de-comando
git init
git config user.name "Seu Nome"
git config user.email "seu@email.com"

# .gitignore: o que NÃO entra no histórico
printf '.venv/\n__pycache__/\nlogs/*.log\nbackups/\n*.env\n' > .gitignore

git add .
git commit -m "feat: script de backup com log e código de saída"
git log --oneline
```

**O `README.md` mínimo que já salva o seu dia:**

```markdown
# Backup de relatórios

Script de shell que copia a pasta `dados/` para `backups/<data>/`.

## Requisitos
- Bash 4 ou superior
- `date`, `tee`, `cp` (núcleo padrão do Linux/macOS)

## Como rodar
    bash scripts/backup-relatorio.sh

## Como agendar (cron)
    30 6 * * * cd ~/projeto-linha-de-comando && bash scripts/backup-relatorio.sh >> logs/cron.log 2>&1

## Onde fica o log
    logs/backup-<AAAA-MM-DD>.log  e  logs/cron.log

## Códigos de saída
- `0` — backup concluído
- `1` — pasta de origem ausente

## Problemas conhecidos
- Se o disco encher, o script falha com "No space left on device".
```

**Entregável do módulo (Atividades A e B):**
- [ ] Rotina agendada e **testada** (com evidência no log)
- [ ] Repositório Git criado, com **2 commits descritivos**
- [ ] `.gitignore` cobrindo `logs/`, `backups/` e `.env`
- [ ] `README.md` com as 6 seções acima

#### Fase 4 — Projeto (25 min)

**Desafio: "A rotina que sobrevive à sua férias"**

Agora o script não depende de você. Cada aluno define **3 rotinas** para a sua rotina real
e escreve a política de operação:

| Item a entregar | Conteúdo exigido |
|---|---|
| **Tabela de rotinas** | Nome · horário · comando · arquivo de log · código de saída esperado |
| **1 guarda (guard clause)** | Uma condição que **impede** a rotina de rodar quando não faz sentido (ex.: "só roda se o arquivo do dia existir"). Pode ser no shell (`if`) ou no `crontab` |
| **1 rotina de fallback** | O que acontece se a principal falhar: novo horário, segunda tentativa, ou aviso |
| **Plano de backup** | Onde ficam as cópias, por quantos dias, e como restaurar em 5 minutos |
| **Simulação de falha** | Você **força** a falha (renomeia a pasta, apaga o arquivo de entrada) e mostra: log gravado + código de saída 1 |

**Critério de pronto:**
- [ ] 3 rotinas documentadas em tabela, com arquivo de log e código de saída
- [ ] Pelo menos **1 rotina foi executada de verdade** e o log foi conferido
- [ ] A **simulação de falha** foi feita e o log mostra a mensagem de erro
- [ ] O `README.md` foi atualizado com a seção "Agendamentos"
- [ ] Tudo está **versionado** e o `git log` mostra a evolução

#### Fase 5 — Mostra (5 min)

**Câmera ligada.** Cada aluno (ou dupla) mostra **o `crontab -l`** na tela e responde:

1. "Qual arquivo esse script mexe?"
2. "Se ele falhar amanhã às 6h30, eu descubro onde?"

> **Pergunta de saída (no chat):** "Qual a diferença entre `>` e `>>`? E por que um script
> que executa todo dia precisa obrigatoriamente de um log?"

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Rotina agendada | `crontab -l` (ou `schtasks /Query`) mostra a rotina; **execução real testada** |
| Log do agendamento | Arquivo `logs/cron.log` existe, com `>>` e `2>&1` |
| Robustez da linha | Caminho absoluto, `cd`, `>>` e `2>&1` presentes |
| Simulação de falha | Falha provocada, log com mensagem clara, código de saída 1 |
| Git | Repositório com 2+ commits descritivos e `.gitignore` correto |
| README | 6 seções: Requisitos · Como rodar · Como agendar · Onde fica o log · Códigos de saída · Problemas conhecidos |
| Diagnóstico | O aluno consegue dizer onde o log da falha está sem ajuda |

**Pergunta de escrita:**
> "Você agendou a rotina para as 5h de segunda-feira. Ela funciona quando você roda na
> mão, mas o log mostra que ela parou no domingo. Você abre o `crontab -l` e a linha está
> lá. O que você faz **antes** de mexer na linha do cron?"
>
> **Resposta:** Antes de editar o `cron`, você **investiga o log** (`tail -50 logs/cron.log`)
> e compara com o **código de saída**. O `cron` é o **sintoma**, não a causa: a linha está
> lá e por isso o problema está no **ambiente** em que o cron executa. A ordem correta é:
> 1. **Ler o log.** A mensagem de erro diz a causa. "command not found" = `PATH`;
>    "No such file or directory" = diretório ou caminho; "Permission denied" = permissão;
>    "No space left on device" = disco.
> 2. **Conferir o código de saída** que o cron registrou. `!= 0` confirma que o script
>    percebeu a falha (se ele devolvesse `0`, o bug seria do próprio script).
> 3. **Rodar o script com o mesmo ambiente do cron**: `env -i HOME=$HOME PATH=/usr/bin:/bin
>    bash scripts/backup-relatorio.sh`. Se falhar assim, achou o ambiente.
> 4. Só **depois** mexer no `cron` — e sempre em **cópia** da linha antiga
>    (`crontab -l > ~/crontab-backup-$(date +%F).txt`), porque o `crontab` é um arquivo
>    único: uma edição errada apaga as três rotinas.
>
> **Lição:** agendamento é a parte da automação que **mais parece funcionar e menos
> funciona**. A rotina de verificação (o `monitoramento.yml` do `Central-de-noticias`)
> existe porque **ninguém** olha para o cron todo dia.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `Central-de-noticias/.github/workflows/update-news.yml` | Cron real com **dois** horários, guarda "já atualizou hoje?", `concurrency` e `|| true` no retry |
| `Central-de-noticias/.github/workflows/monitoramento.yml` | Job que **verifica** se a rotina do dia rodou e dispara alerta (e cria issue) se não rodou |
| `Central-de-noticias/.github/workflows/limpar-historico.yml` | Cron mensal + reescrita de histórico (`git checkout --orphan`) — o exemplo de operação destrutiva que exige backup |
| `manual-qa-completo/Makefile` | Alvos nomeados: `make scripts`, `make all` |
| `manual-qa-completo/run_all.py` | Execução por lista, contagem de falhas, código de saída |
| `git-github-iniciantes/02_primeiro_repositorio/` | `git init`, configuração e primeiro commit |
| `git-github-iniciantes/03_trabalhando_com_mudancas/` | `git status`, `git diff`, staging |
| `qa-automation-framework/` | Estrutura de pastas de um projeto que vai rodar sozinho |

**Exercícios para treinar fora da aula:**

1. Escreva uma rotina que rode `df -h` toda hora e **registre** o espaço em disco em um CSV — você vai ver o disco encher antes de encher.
2. Escreva uma rotina que **apague** arquivos de log com mais de 30 dias, mas **antes** mova para `arquivo/` (backup antes de operação destrutiva).
3. Descubra como o `cron` se comporta em dia de mudança de horário (horário de verão) no seu sistema — e escreva isso no README.

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Agende **2 rotinas** reais da sua rotina (uma de backup, uma de conferência) e
   **teste as duas** com o truque do `* * * * *`.
2. Escreva no `README.md` a seção **"Agendamentos"** com a tabela completa.
3. Versione tudo no Git com **3 commits**:
   - `chore: estrutura inicial e .gitignore`
   - `feat: script de backup com log e código de saída`
   - `docs: README com uso, agendamento e problemas conhecidos`
4. Force **1 falha** de propósito e **cole o log** da falha no `README.md`, na seção
   "Problemas conhecidos". (Isso é o que um profissional de verdade faz.)
5. (Opcional) Leia o capítulo de `cron` da documentação do seu sistema (`man 5 crontab`) e
   anote os 3 campos que mais confundem gente.

> **Na aula 3** você vai reescrever a automação em Python e descobrir por que a maioria
> das tarefas de verdade precisa de mais do que shell.

---

### 🔗 Próximo módulo

[Módulo 3 — Python para Automatizar a Rotina (parte 1) · Aula 3](#m03)

---

<a id="m03"></a>

## Módulo 3 — Python para Automatizar a Rotina (parte 1) (Aula 3)

**Duração:** 90 min · **Aula 3 de 16** · **P3** (módulo em 2 aulas: 3 e 4)
**Entregável do módulo:** **1 script Python real rodando** na máquina do aluno, com
`argparse`, `logging`, leitura de CSV e escrita de JSON, usando ambiente virtual (`venv`).

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar **por que Python** e não outra linguagem para automatizar a rotina (curva de
   aprendizado, biblioteca padrão enorme, é a língua da automação de dados).
2. Preparar um **ambiente isolado**: interpretador, `venv`, `requirements.txt` — ou
   [Google Colab](https://colab.research.google.com/) quando não se pode instalar nada.
3. Escrever um **script confiável**, com as 5 regras: uma tarefa por execução, log,
   falha explícita, backup antes de operação destrutiva e `--dry-run`.
4. Manipular **arquivos e pastas** com `pathlib`, sem concatenar caminho na mão.
5. Ler e gravar **CSV** (`csv.DictReader`, `csv.writer`) e **JSON** (`json`) com a
   biblioteca padrão, respeitando acentos e o BOM que o Excel brasileiro deixa.
6. Dar **interface de linha de comando** ao script com `argparse` (inclusive `--help`).
7. Configurar **`logging`** para arquivo e tela, com nível ajustável.

**Objetivo secundário:** Reconhecer, num código alheio, as 5 marcas de um script que vai
quebrar de madrugada.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `python-do-zero/10_arquivos/` | **6 exercícios** em `.txt` com bloco **"Resposta Esperada"**: `exercicio_01_escrever.txt` · `exercicio_02_ler.txt` · `exercicio_03_append.txt` · `exercicio_04_with.txt` · `exercicio_05_csv.txt` · `exercicio_06_desafio_diario.txt` |
| `python-do-zero/15_api_e_json/` | **6 exercícios**: `exercicio_01_json_dump.txt` · `exercicio_02_json_arquivo.txt` · `exercicio_03_requests_basico.txt` · `exercicio_04_api_consumo.txt` · `exercicio_05_api_dados.txt` · `exercicio_06_desafio_quiz_api.txt` |
| `python-do-zero/11_tratamento_erros/` | Base de `try` / `except` / `finally` — a "falha explícita" |
| `python-do-zero/12_modulos/` | Separar o script em módulos e `import` |
| `manual-qa-completo/docs/03/scripts/estimate.py` | Script real de referência: `from __future__ import annotations`, funções com `docstring`, tipagem e bloco `if __name__ == "__main__":` — **o padrão profissional** |
| `manual-qa-completo/run_all.py` | O padrão de **código de saída**: `return 1 if failures else 0`, execução por `subprocess.run(..., check=True)` e contagem de falhas |
| `Central-de-noticias/scripts/gerar.py` | Script real que gera o conteúdo do portal (RSS → resumo → TTS), com `sys.path` e funções auxiliares |
| `Analise-de-Dados/datasets/Gapminder.csv` | CSV real (mais de mil linhas) para treinar leitura |

> **Plano B (sem internet e sem instalação):** todos os exercícios do `python-do-zero` são
> `.txt` com "Resposta Esperada" — funcionam **offline**, com o aluno testando no
> [Google Colab](https://colab.research.google.com/) depois.

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Por que Python** | "É a língua que **fala com arquivo, planilha e API** sem pedir licença." |
| **Interpretador** | "`python` é o **programa** que lê o seu `.py`. Sem ele, o arquivo é só texto." |
| **`venv`** | "Uma caixinha isolada com as dependências **só daquele projeto**. Sem `venv`, você quebra o computador de outra pessoa." |
| **`requirements.txt`** | "A lista **versionada** do que o projeto precisa. É o que permite outra máquina rodar igual." |
| **Script confiável** | "1 tarefa · log · falha explícita · backup · dry-run." |
| **`pathlib`** | "Caminho é **objeto**, não texto. Você não concatena `/` na mão." |
| **`csv.DictReader`** | "Lê CSV linha a linha como **dicionário**: `linha['produto']`." |
| **`csv.writer`** | "Escreve CSV **com vírgula e aspas certas** — não é `print` com vírgula." |
| **`encoding='utf-8-sig'`** | "O Excel brasileiro deixa um BOM escondido. Sem esse parâmetro, a primeira coluna vem com nome quebrado." |
| **`ensure_ascii=False`** | "Para 'Operação' continuar sendo 'Operação' e não 'Opera\\u00e7\\u00e3o'." |
| **`json`** | "Texto que vira estrutura Python e volta. Formato padrão de API." |
| **`argparse`** | "O script que aceita opções é um **programa**. O que não aceita, é uma gambiarra." |
| **`logging`** | "`print` é conversa; `logging` é **diário com nível, data e arquivo**." |
| **`--dry-run`** | "Mostra o que faria **sem fazer**. Salva a sua sexta-feira." |
| **Código de saída** | "`0` deu certo, `!= 0` deu errado. É assim que o agendador descobre." |
| **As 5 marcas do script que quebra** | "Caminho concatenado na mão · sem `timeout` · `except:` genérico · sem log · sem backup." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** lista de chamada por apelido. Chame 3 nomes. Peça a 1 aluno que
compartilhe a tela do terminal — quem tem o ambiente pronto mostra o caminho, e quem não
tem vai ver o que fazer.

**Gancho (3 min):** *"Quantas vezes por semana você repete a mesma tarefa manual —
formatar planilha, juntar arquivos, conferir se o relatório bate? Toda vez que alguém faz
isso de novo, a empresa paga de novo. Automatizar não é programar: é **devolver a sua
hora**. E a sua hora, num município de 40 mil pessoas com 5.200 alunos na rede, vale
muito."*

**Demonstração ao vivo (3 min):** rode o script do módulo **antes** de explicá-lo:

```bash
# 1. Mostra o que existe
python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios --dry-run

# 2. Executa de verdade
python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios --formato todos

# 3. Mostra o log
cat logs/consolidar_vendas.log
```

**Fala do professor (texto exato):** *"Três comandos. O primeiro **não escreveu nada** —
foi o ensaio. O terceiro deixou um registro do que aconteceu. Já é mais confiável que
90% dos scripts rodando na sua empresa agora."*

> **Plano B:** se a instalação do Python travar na frente da turma, o professor usa
> [Google Colab](https://colab.research.google.com/) e explica: *"Colab para aprender, sua
> máquina para produzir."*

#### Fase 2 — Exploração (25 min)

**Parte 1 — Por que Python, e o ambiente (7 min).**

| Alternativa | Quando escolher | Custo de aprender |
|---|---|---|
| **Python** | dados, planilha, arquivo, API, automação, QA | baixo |
| Bash | uma linha de comando que vira script | médio (sintaxe estranha) |
| JavaScript | navegador, Node, front-end | médio |
| PowerShell | quem só tem Windows e nunca usou terminal | médio |

**O ambiente (o que o aluno precisa ter na máquina):**

```bash
# 1. Conferir a versão do interpretador
python --version          # Windows: python3 --version ou py --version

# 2. Criar o ambiente virtual (uma caixinha só do projeto)
python3 -m venv .venv

# 3. Ativar o ambiente virtual
source .venv/bin/activate          # Linux e macOS
# .venv\Scripts\activate           # Windows (PowerShell/CMD)

# 4. Instalar as dependências do projeto
pip install openpyxl requests

# 5. Gravar as dependências com versão (isso é que vai para o Git)
pip freeze > requirements.txt
```

> **Regra da sala:** o `.venv` **nunca** entra no Git. Ele está no `.gitignore`:
> ```gitignore
> .venv/
> __pycache__/
> *.pyc
> logs/
> .env
> ```

**Parte 2 — As 5 regras do script confiável (6 min).**

| # | Regra | O que impede |
|---|---|---|
| 1 | **Uma tarefa por execução** | script que faz 7 coisas e quebra em 1 delas |
| 2 | **Log** (tela + arquivo) | "não sei o que aconteceu" às 3 da manhã |
| 3 | **Falha explícita** (mensagem clara + `exit 1`) | erro silencioso que continua e corrompe |
| 4 | **Backup antes de operação destrutiva** | sobrescrever o relatório bom sem cópia |
| 5 | **`--dry-run`** | rodar em produção para "ver como fica" |

> **A frase que fixa:** *"O `--dry-run` é o botão de **ensaio** do script. Ninguém ensaia
> uma apresentação no palco."*

**Parte 3 — Biblioteca padrão antes da biblioteca externa (4 min).**

| Precisa de | Use | Não instale |
|---|---|---|
| Ler/escrever arquivo | `pathlib`, `open()` | nada |
| CSV | `csv` | `pandas` (para o Módulo 7) |
| JSON | `json` | nada |
| Data e hora | `datetime` | nada |
| Log | `logging` | nada |
| Teste | `unittest` | `pytest` (opcional, depois) |
| Argumentos | `argparse` | nada |
| HTTP | `urllib` (sozinho) ou `requests` (melhor) | — |
| Excel | — | `openpyxl` (esse é externo mesmo) |

**Parte 4 — `pathlib`, `csv`, `json` na prática (8 min).**

```python
"""Exemplo: ler um CSV com pathlib + csv e gravar um JSON."""

import csv
import json
from pathlib import Path

# 1. pathlib: o caminho é um objeto, não texto
pasta = Path("dados")
pasta.mkdir(parents=True, exist_ok=True)      # cria sem falhar se já existir
arquivo = pasta / "vendas.csv"

# 2. Gravar um CSV de exemplo (o "dado fictício" entra por aqui)
with arquivo.open("w", encoding="utf-8", newline="") as saida:
    escritor = csv.writer(saida)
    escritor.writerow(["data", "produto", "quantidade", "valor_unitario"])
    escritor.writerow(["2026-03-01", "Caneta", "10", "1.50"])
    escritor.writerow(["2026-03-02", "Papel", "2", "25.00"])

# 3. Ler o CSV com DictReader: cada linha vira um dicionário
with arquivo.open("r", encoding="utf-8-sig", newline="") as entrada:
    for linha in csv.DictReader(entrada):
        print(linha["produto"], linha["quantidade"], linha["valor_unitario"])

# 4. Gravar um JSON com acentos preservados
relatorio = Path("relatorios")
relatorio.mkdir(parents=True, exist_ok=True)
dados = {"gerado_em": "2026-03-05", "vendas": [{"produto": "Caneta", "total": 15.0}]}
(relatorio / "vendas.json").write_text(
    json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
)
```

> **Detalhe que separa profissional de amador:** `encoding="utf-8-sig"` ao **ler** CSV
> (remove o BOM que o Excel brasileiro deixa) e `ensure_ascii=False` ao gravar JSON (para
> "Operação" continuar sendo "Operação" e não "Opera\u00e7\u00e3o").

#### Fase 3 — Mão na massa (32 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. O professor circula com a lista de presença e
o foco é **ambiente**: a maior parte do tempo da aula 3 se perde em instalação, não em
lógica.

**Atividade A — Montar o script completo (22 min).**
Crie `consolidar_vendas.py` na raiz do projeto:

```python
#!/usr/bin/env python3
"""consolidar_vendas.py — consolida um CSV de vendas em um relatório por produto.

Ferramenta didática do Módulo 3 (Python para Automatizar a Rotina).

Uso:
    python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios
    python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios --formato todos
    python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios --dry-run

As 5 regras do script confiável, aplicadas aqui:
    1. UMA tarefa por execução: consolidar vendas.
    2. Log em tela e em arquivo.
    3. Falha explícita: mensagem clara e código de saída diferente de zero.
    4. Backup do relatório anterior antes de sobrescrever.
    5. --dry-run mostra o que faria sem escrever nada.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import shutil
import sys
from collections import defaultdict
from collections.abc import Callable
from datetime import datetime
from pathlib import Path

import openpyxl  # biblioteca externa: pip install openpyxl

# --------------------------------------------------------------------- configuração
ARQUIVO_LOG = "logs/consolidar_vendas.log"
FORMATO_LOG = "%(asctime)s [%(levelname)s] %(message)s"
COLUNAS_OBRIGATORIAS = {"data", "produto", "quantidade", "valor_unitario"}

# Tipo de uma função que grava o relatório: recebe os totais e o caminho de destino
Gravador = Callable[[dict[str, float], Path], None]


def configurar_log(nivel: str = "INFO") -> logging.Logger:
    """Configura o log para aparecer na tela e ficar gravado em arquivo."""
    # Garante que a pasta de logs exista antes de criar o arquivo de log
    Path(ARQUIVO_LOG).parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("consolidar_vendas")
    logger.setLevel(nivel)

    # Fecha e remove os handlers antigos (evita log duplicado e arquivo aberto)
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    formato = logging.Formatter(FORMATO_LOG, datefmt="%Y-%m-%d %H:%M:%S")

    # Saída 1: na tela (stdout)
    tela = logging.StreamHandler(sys.stdout)
    tela.setFormatter(formato)
    logger.addHandler(tela)

    # Saída 2: no arquivo (utf-8 para não quebrar acento)
    arquivo = logging.FileHandler(ARQUIVO_LOG, encoding="utf-8")
    arquivo.setFormatter(formato)
    logger.addHandler(arquivo)

    return logger


def ler_vendas(caminho: Path) -> list[dict[str, str]]:
    """Lê o CSV de vendas e devolve uma lista de dicionários (uma por linha).

    Lança FileNotFoundError se o arquivo não existir e ValueError se faltarem
    colunas obrigatórias ou se algum número for inválido.
    """
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {caminho}")

    with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        cabecalho = set(leitor.fieldnames or [])
        faltando = COLUNAS_OBRIGATORIAS - cabecalho
        if faltando:
            raise ValueError(
                "Colunas obrigatórias ausentes no CSV: " + ", ".join(sorted(faltando))
            )
        vendas = [
            {chave: (valor or "").strip() for chave, valor in linha.items() if chave}
            for linha in leitor
        ]

    return vendas


def total_por_produto(vendas: list[dict[str, str]]) -> dict[str, float]:
    """Soma (quantidade x valor unitário) de cada produto."""
    totais: dict[str, float] = defaultdict(float)

    for venda in vendas:
        try:
            quantidade = float(venda["quantidade"])
            valor_unitario = float(venda["valor_unitario"])
        except (KeyError, ValueError) as erro:
            raise ValueError(f"Valores inválidos na linha: {venda}") from erro
        if quantidade < 0 or valor_unitario < 0:
            raise ValueError(f"Quantidade ou valor negativo na linha: {venda}")
        totais[venda["produto"]] += quantidade * valor_unitario

    return dict(totais)


def fazer_backup(caminho: Path) -> Path | None:
    """Cria uma cópia '.bak' do arquivo antes de sobrescrevê-lo.

    Devolve o caminho da cópia ou None se o arquivo ainda não existia.
    """
    if not caminho.exists():
        return None

    backup = caminho.with_suffix(caminho.suffix + ".bak")
    shutil.copy2(caminho, backup)
    return backup


def gravar_csv(totais: dict[str, float], caminho: Path) -> None:
    """Grava o relatório por produto em CSV, do maior total para o menor."""
    caminho.parent.mkdir(parents=True, exist_ok=True)

    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["produto", "total"])
        for produto, total in sorted(totais.items(), key=lambda item: item[1], reverse=True):
            escritor.writerow([produto, f"{total:.2f}"])


def gravar_json(totais: dict[str, float], caminho: Path) -> None:
    """Grava o relatório por produto em JSON."""
    caminho.parent.mkdir(parents=True, exist_ok=True)

    dados = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "total_geral": round(sum(totais.values()), 2),
        "por_produto": {
            produto: round(total, 2)
            for produto, total in sorted(totais.items())
        },
    }
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def gravar_xlsx(totais: dict[str, float], caminho: Path) -> None:
    """Grava o relatório por produto em uma planilha Excel (.xlsx)."""
    caminho.parent.mkdir(parents=True, exist_ok=True)

    livro = openpyxl.Workbook()
    folha = livro.active
    folha.title = "Por produto"
    folha.append(["Produto", "Total (R$)"])

    for produto, total in sorted(totais.items(), key=lambda item: item[1], reverse=True):
        folha.append([produto, round(total, 2)])

    # Formata a coluna de valores como moeda e ajusta a largura das colunas
    for celula in folha["B"][1:]:
        celula.number_format = 'R$ #,##0.00'
    folha.column_dimensions["A"].width = 32
    folha.column_dimensions["B"].width = 16

    livro.save(caminho)


def analisar_argumentos(argv: list[str] | None = None) -> argparse.Namespace:
    """Lê e valida os argumentos de linha de comando."""
    analisador = argparse.ArgumentParser(
        description="Consolida um CSV de vendas em um relatório por produto."
    )
    analisador.add_argument(
        "--entrada", type=Path, required=True,
        help="Caminho do CSV de vendas (obrigatório).",
    )
    analisador.add_argument(
        "--saida", type=Path, default=Path("relatorios"),
        help="Pasta onde o relatório será gravado. Padrão: relatorios",
    )
    analisador.add_argument(
        "--formato", choices=["csv", "json", "xlsx", "todos"], default="csv",
        help="Formato do relatório. Padrão: csv",
    )
    analisador.add_argument(
        "--dry-run", action="store_true",
        help="Mostra o que faria sem gravar nada.",
    )
    analisador.add_argument(
        "--nivel-log", choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="INFO",
        help="Nível de detalhe do log. Padrão: INFO",
    )
    return analisador.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Ponto de entrada. Devolve o código de saída: 0 = sucesso, 1 = falha."""
    argumentos = analisar_argumentos(argv)
    logger = configurar_log(argumentos.nivel_log)
    logger.info("Iniciando consolidação (dry-run=%s).", argumentos.dry_run)

    # ---- Leitura e consolidação (tudo dentro do try: falha explícita)
    try:
        vendas = ler_vendas(argumentos.entrada)
        logger.info("%d venda(s) lida(s) de %s.", len(vendas), argumentos.entrada)

        totais = total_por_produto(vendas)
        logger.info(
            "%d produto(s) consolidado(s). Total geral: R$ %.2f",
            len(totais), sum(totais.values()),
        )
    except (FileNotFoundError, ValueError) as erro:
        logger.error("Falha: %s", erro)
        return 1

    # ---- Lista de arquivos de saída (o dry-run só mostra, não grava)
    alvos: list[tuple[Path, Gravador]] = []
    if argumentos.formato in ("csv", "todos"):
        alvos.append((argumentos.saida / "vendas_por_produto.csv", gravar_csv))
    if argumentos.formato in ("json", "todos"):
        alvos.append((argumentos.saida / "vendas_por_produto.json", gravar_json))
    if argumentos.formato in ("xlsx", "todos"):
        alvos.append((argumentos.saida / "vendas_por_produto.xlsx", gravar_xlsx))

    for caminho, gravador in alvos:
        if argumentos.dry_run:
            logger.info("[dry-run] Gravaria %s (nada foi gravado).", caminho)
            continue

        # Regra 4: backup antes de sobrescrever
        backup = fazer_backup(caminho)
        if backup is not None:
            logger.warning("Backup do relatório anterior em %s", backup)

        gravador(totais, caminho)
        logger.info("Relatório gravado em %s", caminho)

    logger.info("Concluído com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

**Crie o dado de entrada `dados/vendas.csv`:**

```csv
data,produto,quantidade,valor_unitario
2026-03-01,Caneta azul,10,1.50
2026-03-01,Papel A4,4,22.90
2026-03-02,Caneta azul,5,1.50
2026-03-02,Caderno,3,18.00
2026-03-03,Estojo,2,45.00
```

**Rode nesta ordem (é a ordem didática):**

```bash
# 1. Ensaio: mostra o que faria e NÃO grava nada
python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios --formato todos --dry-run

# 2. Real
python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios --formato todos

# 3. Erro proposital: apague o CSV e rode de novo
python consolidar_vendas.py --entrada dados/nao_existe.csv --saida relatorios
echo "código de saída: $?"     # deve ser 1 (e o log registra o motivo)
```

**Fala do professor enquanto circula (texto exato):** *"Duas coisas, e só duas. Primeira:
o `--dry-run` rodou? Segunda: o código de saída foi 1 no erro? Se as duas respostas forem
sim, o seu script já é melhor que muito script em produção. Se o erro foi `ModuleNotFoundError`,
o `venv` não está ativado — é só isso."*

**Entregável da Atividade A:** `consolidar_vendas.py` rodando, com as 5 regras aplicadas,
log em `logs/consolidar_vendas.log` e **código de saída** correto nos dois cenários.

**Atividade B — 3 exercícios do repositório (10 min).**
Rode, no seu ambiente, três dos exercícios abaixo (todos têm "Resposta Esperada" no
arquivo):

| Exercício | Sobre |
|---|---|
| `python-do-zero/10_arquivos/exercicio_04_with.txt` | Bloco `with` (fecha o arquivo sozinho) |
| `python-do-zero/10_arquivos/exercicio_05_csv.txt` | Ler e escrever CSV |
| `python-do-zero/15_api_e_json/exercicio_02_json_arquivo.txt` | JSON em arquivo |

#### Fase 4 — Projeto (20 min)

**Desafio: "O script do seu lugar de trabalho"**

Cada aluno reescreve o script para **uma tarefa real** da sua rotina. Escolha entre:

| Contexto | Tarefa automatizável | Dado fictício |
|---|---|---|
| Escola | Consolidar a **planilha de chamada** das turmas | `chamada.csv` com `turma,data,aluno_id,presente` |
| Secretaria | **Conferência de presença** da equipe por departamento | `presenca.csv` com `departamento,data,status` |
| Secretaria | **Relatório de notas** por turma e componente | `notas.csv` com `aluno_id,componente,nota` |
| Secretaria | **Lista de entrega de kits escolares** | `kits.csv` com `aluno_id,kit,entregue` |
| Comércio | **Fechamento de caixa por forma de pagamento** | `vendas.csv` com `data,produto,quantidade,valor_unitario` |

**Regras do desafio:**

1. **Dados fictícios** — gere o CSV com um script (`gerar_dados.py`) ou à mão. **Nunca**
   use dado real de aluno, funcionário ou cliente.
2. O script tem que rodar com **dados de entrada diferentes** dos do exemplo — ou seja,
   ele **lê o arquivo**, não tem nada fixo no código.
3. Troque os **nomes das funções e das variáveis** pelo vocabulário da sua rotina
   (`turma`, `faltas`, `kit`) — código que fala a língua do negócio é lido por quem não
   é da área.

**Critério de pronto:**
- [ ] O script roda com `python <seu_script>.py --entrada ... --saida ...`
- [ ] `--help` mostra a ajuda com todas as opções
- [ ] O script tem **log** em arquivo e em tela
- [ ] O script **falha de forma explícita** (mensagem clara + código de saída 1)
- [ ] O script tem `--dry-run` e **não grava** nada com ele
- [ ] O script faz **backup** (`.bak`) antes de sobrescrever um relatório existente
- [ ] `requirements.txt` existe com as dependências versionadas
- [ ] `.gitignore` cobre `.venv/`, `__pycache__/`, `logs/` e `.env`
- [ ] `README.md` explica: o que faz, como instalar, como rodar e onde fica o log

#### Fase 5 — Mostra (5 min)

**Câmera ligada.** Cada aluno roda o script **ao vivo** na frente da turma (30 s) e
mostra **o log** gerado. A turma pergunta:

1. "O que acontece se eu rodar com `--dry-run`?"
2. "Onde eu descubro que o script falhou às 3 da manhã?"

> **Pergunta de saída (no chat):** "Qual a diferença entre `print('erro')` e
> `logger.error('erro')`? E por que um script agendado precisa de código de saída?"

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Script principal | Roda sem erro; CLI com `argparse` e `--help` funcionando |
| Regras de script confiável | 1 tarefa · log · falha explícita · backup · dry-run — as 5 presentes |
| Log | Arquivo `logs/*.log` criado, com data/hora e nível |
| Código de saída | `0` no sucesso, `1` na falha (verificado) |
| Environment | `requirements.txt` versionado + `.gitignore` com `.venv/` e `__pycache__/` |
| Vocabulário do negócio | Nome de função/variável ligado à rotina real do aluno |
| Dados | Somente dados **fictícios** — verificado por inspeção do CSV |
| README | Requer instalado, comando de uso, agendamento e caminho do log |

**Pergunta de escrita:**
> "Você agendou o script para rodar todo dia às 7h. Segunda-feira ele rodou bem.
> Terça-feira o relatório saiu **vazio**, sem erro no terminal e sem mensagem no log.
> Quarta-feira, o mesmo. Onde você olha primeiro, e o que isso revela sobre o seu script?"
>
> **Resposta:** O sintoma "saída vazia, sem erro, sem log" aponta para **uma das três**:
> 1. **O arquivo de entrada mudou de lugar ou foi renomeado.** O script lê
>    `dados/vendas.csv` com caminho **relativo**. Se o `cron` roda em outro diretório de
>    trabalho, o caminho relativo aponta para outro lugar — ou para nada. *Correção:* use
>    caminho absoluto e, no código, valide `caminho.exists()` antes de ler (o script do
>    módulo já faz isso e **registra o erro no log** — se o log está vazio, o script nem
>    chegou a ler o arquivo, e isso muda o diagnóstico).
> 2. **O código trata "arquivo vazio" como sucesso.** Se o CSV tiver só o cabeçalho, o
>    `DictReader` devolve **zero linhas** — e `total_por_produto({})` devolve `{}`, sem
>    exceção. O script "tem sucesso" e grava um relatório vazio. *Correção:* valide o
>    resultado antes de gravar e **falhe explicitamente** ("a entrada tem 0 linhas").
> 3. **O `logging` está configurado para um caminho que não existe** (ou o usuário do
>    agendamento não tem permissão), então o log vai para outro lugar — ou para lugar
>    nenhum. *Correção:* `logging.FileHandler` com pasta criada antes
>    (`Path(...).parent.mkdir(...)`), **caminho absoluto** do arquivo de log e um `echo`
>    do caminho no início da execução.
>
> **Lição de fundo:** um script que falha em silêncio é pior que um script que não existe,
> porque ele produz **resultado errado** com aparência de resultado certo. É por isso que
> a regra 3 (falha explícita) e a regra 5 (`--dry-run`) existem.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `python-do-zero/10_arquivos/exercicio_01_escrever.txt` | Escrever arquivo de texto |
| `python-do-zero/10_arquivos/exercicio_02_ler.txt` | Ler arquivo linha a linha |
| `python-do-zero/10_arquivos/exercicio_03_append.txt` | Acrescentar ao final (`append`) |
| `python-do-zero/10_arquivos/exercicio_04_with.txt` | Bloco `with` (fecha o arquivo sozinho) |
| `python-do-zero/10_arquivos/exercicio_05_csv.txt` | Ler e escrever CSV |
| `python-do-zero/10_arquivos/exercicio_06_desafio_diario.txt` | Desafio do módulo |
| `python-do-zero/15_api_e_json/exercicio_01_json_dump.txt` | `json.dump` |
| `python-do-zero/15_api_e_json/exercicio_02_json_arquivo.txt` | JSON em arquivo |
| `python-do-zero/15_api_e_json/exercicio_03_requests_basico.txt` | `requests` básico |
| `python-do-zero/15_api_e_json/exercicio_04_api_consumo.txt` | Consumir uma API |
| `python-do-zero/11_tratamento_erros/` | `try`, `except`, `finally` — base da "falha explícita" |
| `python-do-zero/12_modulos/` | Separar o script em módulos e `import` |
| `manual-qa-completo/docs/03/scripts/estimate.py` | Script real com `docstring`, tipagem e `if __name__ == "__main__"` |
| `manual-qa-completo/run_all.py` | Padrão de código de saída e execução por subprocess |
| `Central-de-noticias/scripts/gerar.py` | Script real que gera o conteúdo do portal |
| `Analise-de-Dados/datasets/Gapminder.csv` | CSV real para treinar (mais de mil linhas) |
| `lista-de-exercicios-python-brasil/` | Exercícios em texto puro, com gabarito (funciona **offline**) |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. **Troque o problema do script pelo seu.** Pegue uma tarefa real do seu trabalho (juntar
   planilhas, conferir um arquivo, extrair um número) e reescreva o script para ela,
   mantendo as **5 regras**.
2. Gere o **CSV de entrada fictício** com um script seu (`gerar_dados.py`) — ele precisa
   gerar pelo menos 20 linhas com acentos, datas e valores varietyados.
3. Rode o script nos **dois formatos** (`--formato csv` e `--formato json`) e **cole as
   saídas** no `README.md`.
4. Force **1 falha** (CSV com coluna faltando) e **cole a mensagem do log** no README.
5. Versione no Git com **3 commits**: `chore: estrutura e requirements`,
   `feat: script de <sua tarefa>` e `docs: README com uso e limitações`.
6. Escreva no `README.md` uma seção **"Decisões e limitações"**: 2 itens que o script
   **não** resolve.

> **Na aula 4** você vai acrescentar `--dry-run`, backup e **testes automatizados**.

---

### 🔗 Próximo módulo

[Módulo 4 — Python para Automatizar (parte 2: backup, `--dry-run` e `unittest`) · Aula 4](#m04)

---

<a id="m04"></a>

## Módulo 4 — Python para Automatizar (parte 2): backup, `--dry-run` e `unittest` (Aula 4)

**Duração:** 90 min · **Aula 4 de 16** · **P4** (continuação do Módulo 3)
**Entregável do módulo:** **script com backup automático + `--dry-run` + suíte de testes
`unittest` com 8 casos verdes**, e o script agendado de verdade.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Implementar **backup automático** com carimbo de data/hora antes de qualquer operação
   destrutiva, e **restaurar** a partir do backup em menos de 1 minuto.
2. Implementar **`--dry-run`** que mostra exatamente o que faria, sem escrever nada.
3. Escrever **testes automatizados** com `unittest` (biblioteca padrão, sem instalar nada),
   incluindo **casos de falha** — não só o caminho feliz.
4. Isolar os testes com `tempfile.TemporaryDirectory`, para que o teste **não toque** nos
   dados reais.
5. Rodar a suíte com `python -m unittest -v` e interpretar `OK` / `FAILED`.
6. Agendar o script Python (`cron` ou `schtasks`) usando **caminho absoluto do
   interpretador do `.venv`**.
7. Reconhecer o padrão **"script + suíte"** usado em produção no `Central-de-noticias`.

**Objetivo secundário:** Explicar por que "teste que não roda é bug" vale para script
pessoal exatamente igual que vale para sistema de produção.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `manual-qa-completo/docs/03/scripts/estimate.py` | O **padrão profissional** de script: `from __future__ import annotations`, `docstring` em cada função, tipagem, funções puras (fácil de testar) e bloco `if __name__ == "__main__":` |
| `manual-qa-completo/run_all.py` | Execução por lista + contagem de falhas + **código de saída** (`return 1 if failures else 0`) |
| `manual-qa-completo/Makefile` | Alvo `scripts:` que roda vários scripts Python — o "suíte de scripts" como padrão de make |
| `Central-de-noticias/tests/test_gerar.py` | Suíte `pytest` real: importa funções do script (`from gerar import limpar, _finalizar, tokens, normaliza`) e testa **uma função por caso** |
| `Central-de-noticias/pytest.ini` | Configuração de pytest do projeto real |
| `Central-de-noticias/scripts/gerar.py` | Script real **testado** — a prova de que "script + teste" é o padrão do autor |
| `qa-automation-framework/utils/data_generator.py` | Gerar dados falsos com `Faker` — **nunca** use dado real de cliente |
| `qa-automation-framework/tests/` | Estrutura de testes do framework profissional |
| `python-do-zero/11_tratamento_erros/` | Base de `try`/`except`/`finally` para o tratamento de erro do script |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Backup** | "Antes de sobrescrever, copia. Não é custo, é **o seguro do carro**." |
| **`shutil.copy2`** | "Copia arquivo **e metadados** (data, permissão). Use em backup, não `copy`." |
| **Restaurar** | "Backup que você não testou não é backup. **Restaure uma vez**, agora." |
| **`--dry-run`** | "O botão de **ensaio**. Mostra o plano, não executa." |
| **`unittest`** | "Teste automatizado = **código que verifica código**. Sai da biblioteca padrão." |
| **Caso de teste** | "Uma pergunta sobre o comportamento. `test_` + o que você espera." |
| **`assertEqual`** | "`assert` é o **juiz**: se for falso, o teste explode com a mensagem." |
| **`assertRaises`** | "Testar erro é tão importante quanto testar sucesso." |
| **`setUp` / `tearDown`** | "Antes de cada teste preparo o terreno; depois, limpo. Teste não deixa rastro." |
| **`tempfile.TemporaryDirectory`** | "O teste roda numa pasta **temporária**. Ele nunca toca no seu dado real." |
| **Mocks (conceito)** | "Quando o dependente é caro (internet, tempo), você **substitui** por um dublê." |
| **Cobertura** | "Porcentagem do código exercitada pelos testes. Não é o fim, é um indicador." |
| **Código de saída em teste** | "`main()` devolve inteiro. O teste **confere** o inteiro. Fim da história." |
| **Agendamento com `.venv`** | "No `cron`, o `python` do sistema **não** é o seu. Use o caminho absoluto." |
| **Teste que não roda é bug** | "Teste quebrado é tão ruim quanto código quebrado — e até pior, porque **finge** que está tudo bem." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** lista de chamada por apelido. Pergunta rápida no chat: *"Quem já
rodou um teste automatizado na vida? Digitem `sim` ou `não`."* — a maioria responde `não`,
e isso abre a aula.

**Gancho (3 min):** *"O script da aula passada funcionava. Rodou bonito. Mas eu posso
mudar uma linha e quebrar ele sem perceber — e só vou descobrir no dia que a nota sai. Hoje
a gente resolve isso de três formas: **backup**, **ensaio** e **teste**. É o mesmo tripé
que sustenta qualquer sistema em produção."*

**Demonstração ao vivo (3 min):** rode a suíte de testes do `Central-de-noticias` e
mostre a saída:

```bash
python -m pytest -v
```

Depois rode um teste **que falha de propósito** (apague uma linha do CSV de exemplo) e
mostre o `FAILED`:

```
FAILED (failures=1)
```

**Fala do professor (texto exato):** *"Olha o valor dessa tela. Um teste vermelho te diz
**onde** está o problema, **linha por linha**. Imagina o mesmo bug chegando no relatório
final da Secretaria: aí você tem um e-mail do diretor. O teste vermelho é o e-mail do
seu computador — só que **chegando antes**."*

> **Plano B:** se o `pytest` não estiver instalado, use `unittest` (já vem com o Python) —
> o conteúdo didático é o mesmo.

#### Fase 2 — Exploração (22 min)

**Parte 1 — Backup com carimbo (6 min).**

```python
from datetime import datetime
from pathlib import Path
import shutil


def fazer_backup(caminho: Path) -> Path | None:
    """Cria uma cópia '.bak' do arquivo antes de sobrescrevê-lo.

    Devolve o caminho da cópia ou None se o arquivo ainda não existia.
    """
    if not caminho.exists():
        return None

    backup = caminho.with_suffix(caminho.suffix + ".bak")
    shutil.copy2(caminho, backup)
    return backup
```

**Versão com data/hora (para backup de vários dias):**

```python
def fazer_backup_com_data(caminho: Path, pasta_backup: Path) -> Path | None:
    """Cria a cópia datada e a devolve. None se o original não existia."""
    if not caminho.exists():
        return None

    pasta_backup.mkdir(parents=True, exist_ok=True)
    carimbo = datetime.now().strftime("%Y%m%d-%H%M%S")
    destino = pasta_backup / f"{caminho.stem}-{carimbo}{caminho.suffix}"
    shutil.copy2(caminho, destino)
    return destino
```

**E o script de restauração** (o que faz o backup ser backup de verdade):

```bash
#!/usr/bin/env bash
# restaurar.sh — restaura o backup mais recente de um relatório
# Uso: bash scripts/restaurar.sh relatorios/relatorio.csv
set -euo pipefail

ORIGEM="$1"
[ -n "$ORIGEM" ] || { echo "Uso: bash scripts/restaurar.sh <arquivo>" >&2; exit 1; }

MAIS_RECENTE=$(ls -1t "${ORIGEM}.bak"* 2>/dev/null | head -1 || true)
if [ -z "$MAIS_RECENTE" ]; then
  echo "ERRO: nenhum backup encontrado para '$ORIGEM'." >&2
  exit 1
fi

echo "Restaurando: $MAIS_RECENTE -> $ORIGEM"
cp -p "$MAIS_RECENTE" "$ORIGEM"
echo "Restauração concluída."
```

**Parte 2 — `--dry-run` bem feito (5 min).**

A parte difícil do `--dry-run` não é "não escrever": é **dizer o que seria escrito**.

```python
def gravar_csv(totais: dict[str, float], caminho: Path, dry_run: bool = False) -> None:
    """Grava o relatório por produto em CSV.

    Com dry_run=True, apenas informa o que faria e NÃO grava nada.
    """
    caminho.parent.mkdir(parents=True, exist_ok=True)

    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["produto", "total"])
        for produto, total in sorted(totais.items(), key=lambda item: item[1], reverse=True):
            escritor.writerow([produto, f"{total:.2f}"])
```

O `--dry-run` fica **no laço de chamada**, não dentro da função de escrita:

```python
    for caminho, gravador in alvos:
        if argumentos.dry_run:
            logger.info("[dry-run] Gravaria %s (nada foi gravado).", caminho)
            continue
        ...
```

**Parte 3 — `unittest` (9 min).**

A anatomia de um teste:

```python
import unittest


class TestAlgo(unittest.TestCase):
    """Cada método test_* é um caso de teste independente."""

    def setUp(self) -> None:
        """Roda antes de cada teste: prepara o terreno."""

    def tearDown(self) -> None:
        """Roda depois de cada teste: limpa o terreno."""

    def test_comportamento_esperado(self) -> None:
        """Docstring com o que este caso garante."""
        self.assertEqual(algo, esperado)
```

**As 4 asserções que você vai usar 90% das vezes:**

```python
self.assertEqual(a, b)          # igualdade
self.assertAlmostEqual(a, b)    # igualdade com tolerance (float)
self.assertTrue(x)              # verdadeiro
self.assertIn(item, lista)      # está contido
self.assertRaises(Erro, callable)  # levanta o erro esperado
```

**Execução:**

```bash
python -m unittest -v test_consolidar_vendas.py     # verbose: mostra cada caso
python -m unittest -v                             # roda tudo que achar
python -m unittest -v test_consolidar_vendas.TestConsolidarVendas.test_soma_por_produto
```

**Parte 4 — Isolar com `tempfile` (2 min).**

```python
import tempfile
from pathlib import Path

self.pasta = tempfile.TemporaryDirectory()
self.raiz = Path(self.pasta.name)
# ... usa self.raiz ...
self.pasta.cleanup()   # no tearDown
```

> **Por que isso importa:** sem isolamento, o teste **sobrescreve o relatório real** do
> aluno. Já vi esse acidente acontecer. Teste que mexe no dado de produção é **teste
> quebrado**.

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. O professor circula conferindo **uma coisa
só**: o `assert` do teste.

**Atividade A — Suíte de testes (18 min).**
Crie `test_consolidar_vendas.py`:

```python
#!/usr/bin/env python3
"""test_consolidar_vendas.py — testes automatizados do script de consolidação.

Executar:  python -m unittest -v test_consolidar_vendas.py
"""

import csv
import json
import tempfile
import unittest
from pathlib import Path

import consolidar_vendas as cv


class TestConsolidarVendas(unittest.TestCase):
    """Cada método test_* é um caso de teste independente."""

    def setUp(self) -> None:
        """Roda antes de cada teste: cria uma pasta temporária e um CSV de exemplo."""
        self.pasta = tempfile.TemporaryDirectory()
        self.raiz = Path(self.pasta.name)
        self.csv = self.raiz / "vendas.csv"
        self.csv.write_text(
            "data,produto,quantidade,valor_unitario\n"
            "2026-03-01,Caneta,10,1.50\n"
            "2026-03-02,Caneta,5,1.50\n"
            "2026-03-02,Papel,2,25.00\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        """Roda depois de cada teste: apaga a pasta temporária."""
        self.pasta.cleanup()

    def test_le_todas_as_vendas(self) -> None:
        """O CSV de exemplo tem 3 linhas de venda."""
        vendas = cv.ler_vendas(self.csv)
        self.assertEqual(len(vendas), 3)

    def test_soma_por_produto(self) -> None:
        """Caneta: 10x1.50 + 5x1.50 = 22.50 | Papel: 2x25.00 = 50.00."""
        totais = cv.total_por_produto(cv.ler_vendas(self.csv))
        self.assertAlmostEqual(totais["Caneta"], 22.50)
        self.assertAlmostEqual(totais["Papel"], 50.00)

    def test_arquivo_inexistente_falha(self) -> None:
        """Arquivo ausente precisa levantar FileNotFoundError."""
        with self.assertRaises(FileNotFoundError):
            cv.ler_vendas(self.raiz / "nao_existe.csv")

    def test_coluna_ausente_falha(self) -> None:
        """CSV sem a coluna 'valor_unitario' precisa levantar ValueError."""
        ruim = self.raiz / "sem_coluna.csv"
        ruim.write_text("data,produto\n2026-03-01,Caneta\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            cv.ler_vendas(ruim)

    def test_valor_invalido_falha(self) -> None:
        """Quantidade não numérica precisa levantar ValueError."""
        ruim = self.raiz / "valor_invalido.csv"
        ruim.write_text(
            "data,produto,quantidade,valor_unitario\n2026-03-01,Caneta,abc,1.50\n",
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            cv.total_por_produto(cv.ler_vendas(ruim))

    def test_grava_csv_com_cabecalho(self) -> None:
        """O CSV gerado tem o cabeçalho e uma linha por produto."""
        saida = self.raiz / "relatorios" / "vendas.csv"
        cv.gravar_csv(cv.total_por_produto(cv.ler_vendas(self.csv)), saida)
        with saida.open(encoding="utf-8", newline="") as arquivo:
            linhas = list(csv.reader(arquivo))
        self.assertEqual(linhas[0], ["produto", "total"])
        self.assertEqual(len(linhas), 3)

    def test_grava_json_com_total_geral(self) -> None:
        """O JSON gerado tem 'gerado_em' e o total geral correto (22.50 + 50.00)."""
        saida = self.raiz / "relatorios" / "vendas.json"
        cv.gravar_json(cv.total_por_produto(cv.ler_vendas(self.csv)), saida)
        dados = json.loads(saida.read_text(encoding="utf-8"))
        self.assertIn("gerado_em", dados)
        self.assertAlmostEqual(dados["total_geral"], 72.50)

    def test_backup_copia_o_arquivo(self) -> None:
        """O backup guarda o conteúdo anterior do relatório."""
        alvo = self.raiz / "relatorio.csv"
        alvo.write_text("conteudo antigo", encoding="utf-8")
        backup = cv.fazer_backup(alvo)
        self.assertIsNotNone(backup)
        self.assertEqual(backup.read_text(encoding="utf-8"), "conteudo antigo")

    def test_dry_run_nao_grava_arquivo(self) -> None:
        """Com --dry-run nada é gravado, mas o código de saída é 0."""
        saida = self.raiz / "relatorios"
        codigo = cv.main([
            "--entrada", str(self.csv),
            "--saida", str(saida),
            "--formato", "todos",
            "--dry-run",
        ])
        self.assertEqual(codigo, 0)
        self.assertFalse((saida / "vendas_por_produto.csv").exists())

    def test_main_devolve_1_quando_falta_arquivo(self) -> None:
        """Entrada inexistente: o script falha com código de saída 1."""
        codigo = cv.main([
            "--entrada", str(self.raiz / "nao_existe.csv"),
            "--saida", str(self.raiz / "relatorios"),
        ])
        self.assertEqual(codigo, 1)


if __name__ == "__main__":
    unittest.main()
```

Rode:

```bash
python -m unittest -v test_consolidar_vendas.py
```

> ⚠️ O `main()` em modo teste **cria a pasta `logs/`** no diretório atual (por causa do
> `logging.FileHandler`). Isso é esperado — e é exatamente o tipo de detalhe que um
> profissional percebe e documenta.

**Atividade B — Agendar de verdade (12 min).**

```cron
# Consolida as vendas todo dia às 7h (o log vai para arquivo, o erro também)
0 7 * * * cd ~/meu-projeto && /home/USUARIO/meu-projeto/.venv/bin/python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios --formato todos >> logs/cron.log 2>&1
```

> **Use o caminho absoluto do Python do `.venv`.** É o erro número 1 de cron: o `python`
> do sistema não é o seu.

```powershell
# Windows: schtasks (PowerShell)
schtasks /Create /TN "ConsolidarVendas" /TR "C:\Users\USUARIO\meu-projeto\.venv\Scripts\python.exe C:\Users\USUARIO\meu-projeto\consolidar_vendas.py --entrada C:\Users\USUARIO\meu-projeto\dados\vendas.csv --saida C:\Users\USUARIO\meu-projeto\relatorios --formato todos" /SC DAILY /ST 07:00

# Testar sem esperar o relógio
schtasks /Run /TN "ConsolidarVendas"

# Remover a tarefa
schtasks /Delete /TN "ConsolidarVendas" /F
```

**Fala do professor enquanto circula (texto exato):** *"Duas perguntas. Primeira: o
`--dry-run` rodou e **não** criou arquivo? Segunda: existe **um** teste que verifica um
**erro**? Se a resposta da segunda for 'não', seu script está happy-path — funciona
quando tudo dá certo e ninguém sabe o que acontece quando dá errado. É pra isso que serve
o `assertRaises`."*

**Entregável do módulo:**
- [ ] `consolidar_vendas.py` roda e gera **os 3 formatos** (CSV, JSON, XLSX)
- [ ] O script tem **log** em arquivo e em tela
- [ ] O script **falha de forma explícita** (mensagem clara + código de saída 1)
- [ ] O script faz **backup** (`.bak`) antes de sobrescrever um relatório existente
- [ ] O script tem `--dry-run` e **não grava** nada com ele
- [ ] `test_consolidar_vendas.py` tem **pelo menos 8 testes** e todos passam
- [ ] `requirements.txt` existe com as dependências versionadas
- [ ] `.gitignore` cobre `.venv/`, `__pycache__/`, `logs/` e `.env`
- [ ] O script está **agendado** (cron ou `schtasks`) e você **testou** a execução
- [ ] `README.md` explica: o que o script faz, como instalar, como rodar, como agendar e onde fica o log

#### Fase 4 — Projeto (25 min)

**Desafio: "O script que sobrevive a você"**

Cada aluno eleva o script da aula anterior em 3 níveis:

**Nível 1 — Backup com data (8 min).**
Troque o `.bak` fixo por um backup **datado** em `backups/`, e escreva o script
`restaurar.sh`. **Restaure uma vez, na aula**, para provar que o backup funciona.

**Nível 2 — Dry-run completo (7 min).**
O `--dry-run` tem que mostrar: **quantos registros** serão lidos, **quantas linhas**
serão gravadas, **onde** será gravado e **qual backup** será criado. Não basta dizer
"não fez nada".

**Nível 3 — Suíte de testes da sua rotina (10 min).**
Escreva **10 casos** para o seu script:

| # | Tipo de caso | Exemplo (chamada) |
|---|---|---|
| 1 | Caminho feliz | arquivo válido gera relatório com N linhas |
| 2 | Quantidade | total somado está correto |
| 3 | Arquivo ausente | levanta erro / devolve código 1 |
| 4 | Coluna ausente | valida erro claro |
| 5 | Valor não numérico | valida erro claro |
| 6 | Arquivo vazio (só cabeçalho) | **falha explicitamente** (não gera relatório vazio) |
| 7 | Backup | arquivo anterior é preservado |
| 8 | Dry-run | nada é gravado e o código é 0 |
| 9 | Acentuação | "Operação" e "Atividade" sobrevivem ao CSV |
| 10 | Idempotência | rodar 2 vezes produz o mesmo resultado |

**Critério de pronto:**
- [ ] Backup **datado** funcionando e **restauração testada na aula**
- [ ] `--dry-run` informa volume, destino e backup — não só "não fiz nada"
- [ ] **10 testes** no `unittest`, todos verdes, com **pelo menos 2 de falha**
- [ ] A suíte roda com **1 comando** e o resultado está colado no `README.md`
- [ ] O script está agendado e a **execução real foi testada** (com evidência no log)
- [ ] `README.md` tem uma seção **"Testes"** com o comando e a última saída

#### Fase 5 — Mostra (5 min)

**Câmera ligada.** Cada aluno roda **um teste** filtrado, na frente da turma, e mostra
o `OK`:

```bash
python -m unittest -v test_consolidar_vendas.TestConsolidarVendas.test_backup_copia_o_arquivo
```

A turma pergunta:

1. "O que acontece se eu rodar com `--dry-run`?"
2. "Onde eu descubro que o script falhou às 3 da manhã?"

> **Pergunta de saída (no chat):** "Qual a diferença entre `print('erro')` e
> `logger.error('erro')`? E por que um script agendado precisa de código de saída?"

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Script principal | Roda sem erro; gera os 3 formatos; CLI com `argparse` e `--help` funcionando |
| Regras de script confiável | 1 tarefa · log · falha explícita · backup · dry-run — as 5 presentes |
| Log | Arquivo `logs/*.log` criado, com data/hora e nível |
| Código de saída | `0` no sucesso, `1` na falha (verificado) |
| Backup | Datado, com script de restauração **testado ao vivo** |
| Dry-run | Informa volume, destino e backup previsto; não grava nada |
| Testes | **10 casos** em `unittest`, todos verdes, nomes descritivos em português, **pelo menos 2 de falha** |
| Agendamento | Tarefa criada **e testada** (cron ou `schtasks`), com caminho absoluto do `.venv` |
| Ambiente | `requirements.txt` versionado + `.gitignore` com `.venv/` e `__pycache__/` |
| README | Seções: Instalar · Usar · Agendar · Onde fica o log · Testes · Limitações |

**Pergunta de escrita:**
> "Você tem um script que roda todo dia e grava um relatório. Ontem ele rodou e gravou um
> relatório **vazio** (só o cabeçalho). O log não registrou erro — registrou
> `'0 venda(s) lida(s)'`. O script saiu com código 0. O que está errado e o que você
> muda?"
>
> **Resposta:** O script está **errado em dois lugares**, e o log entregou a pista:
> 1. **A entrada vazia foi tratada como sucesso.** `ler_vendas()` devolveu `[]` (lista
>    vazia, **sem exceção**) e `total_por_produto([])` devolveu `{}`. Não havia nada para
>    a função "falhar". O `main()` gravou um relatório com só o cabeçalho e devolveu 0.
>    *Correção:* validar **no `main()`**, logo depois da leitura:
>    ```python
>    if not vendas:
>        logger.error("A entrada %s não tem nenhuma linha de dados.", argumentos.entrada)
>        return 1
>    ```
>    Só depois disso o script grava o relatório. Note que a validação **não** fica dentro
>    de `ler_vendas()`: função de leitura devolve dados, quem decide o que é "vazio demais"
>    é o-script-que-chama.
> 2. **Falta a checagem de "mudou de lugar ou truncou".** O arquivo existia, mas estava
>    vazio — normalmente porque a rotina que gera a entrada rodou **antes** e falhou, ou
>    rodou **depois**. *Correção:* o script de entrada e o de relatório precisam de
>    **ordem** (o `&&` no `cron` resolve) e o relatório deve registrar o **número de
>    registros de origem** junto com a data: `gerado_em`, `registros_origem`, `linhas_saida`.
>    Sem isso, você nunca descobre *quando* o dado parou de vir.
> 3. **A lição maior:** o log estava **funcionando**. O que faltava era a **regra** que
>    transforma "0 registro lido" em falha. Um script sem invariantes é um script que
>    produz arquivo vazio **com aparência de relatório** — e relatório vazio aprovado é
>    pior que erro, porque **ninguém questiona**.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `Central-de-noticias/tests/test_gerar.py` | Suíte real: `from gerar import limpar, _finalizar, tokens, normaliza` — uma função por caso |
| `Central-de-noticias/pytest.ini` | Configuração de pytest do projeto |
| `Central-de-noticias/scripts/gerar.py` | Script real **coberto** por testes — o padrão "script + teste" |
| `manual-qa-completo/docs/03/scripts/estimate.py` | Script com `docstring`, tipagem e `if __name__ == "__main__"` |
| `manual-qa-completo/run_all.py` | Padrão de código de saída e execução por `subprocess` |
| `manual-qa-completo/Makefile` | Alvo `scripts:` que roda vários scripts Python |
| `qa-automation-framework/utils/data_generator.py` | Gerar dados falsos com `Faker` (nunca use dado real de cliente) |
| `qa-automation-framework/tests/` | Estrutura de testes do framework profissional |
| `python-do-zero/11_tratamento_erros/` | `try`, `except`, `finally` |
| `python-do-zero/12_modulos/` | Separar o script em módulos e `import` |

**Exercícios para treinar fora da aula:**

1. Escreva um teste que **quebre de propósito** e veja a mensagem do `assert`. Depois escreva o `assert` correto.
2. Escreva um **dublê** (mock) de uma função que chama a internet, para testar sem internet.
3. Meça o **tempo** do seu script com `time python script.py ...` e registre no README.

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Escreva **pelo menos 3 testes novos** para o seu caso — e inclua **um teste de
   falha** (entrada inválida) e **um teste de arquivo vazio**.
2. Agende o script e **teste** a execução real (no `cron`, use `* * * * *` por 1 minuto;
   no Windows, use `schtasks /Run`).
3. Versione tudo no Git com **3 commits**:
   - `feat: backup datado e dry-run informativo`
   - `test: 10 casos de teste automatizados`
   - `docs: README com testes e limitações`
4. Escreva no `README.md` a seção **"Problemas conhecidos"** com 2 itens: 1 do script e
   1 do **ambiente** (horário, permissão, espaço em disco).
5. (Opcional) Refaça o mesmo script com a **biblioteca padrão** (`csv` + `json` +
   `logging`), sem `openpyxl` e sem `requests`, e compare o tamanho do código.

> **Na aula 5** você vai publicar esse projeto no GitHub. Sem histórico, sem prova.

---

### 🔗 Próximo módulo

[Módulo 5 — Git e GitHub profissional (parte 1) · Aula 5](#m05)

---

<a id="m05"></a>

## Módulo 5 — Git e GitHub profissional (parte 1) (Aula 5)

**Duração:** 90 min · **Aula 5 de 16** · **P5** (módulo em 2 aulas: 5 e 6)
**Entregável do módulo:** **repositório Git local profissional** — com `README.md`,
`LICENSE`, `.gitignore`, `requirements.txt`, estrutura de pastas e **20+ commits
descritivos** — pronto para ser publicado.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar o **modelo de 3 estados** do Git (working directory, staging area, repositório)
   e o que cada comando faz com os arquivos.
2. Escrever **mensagens de commit** no formato `tipo: descrição` (Conventional Commits),
   que explicam **por quê**, não só **o quê**.
3. Usar `git status`, `git diff`, `git log --oneline`, `git show` e `git restore` para
   **diagnosticar** o estado do repositório sem medo.
4. Criar e configurar um repositório com `git init`, `git config user.name` e
   `git config user.email` — **localmente**, sem depender de conta global.
5. Escrever um **`.gitignore` correto**, que exclui `.venv/`, `__pycache__/`, `logs/`,
   `backups/`, `.env` e dados.
6. Criar um **`README.md` profissional** com as 7 seções que um repositório precisa ter.
7. Publicar o repositório no **GitHub**, criando conta e verificando e-mail.

**Objetivo secundário:** Explicar por que "commit" é **uma unidade de mudança com
sentido**, e por que 40 commits "fix" não valem nada.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `git-github-iniciantes/01_o_que_e_git/` | Conceitos de versionamento: Working Directory, Staging Area, Repositório |
| `git-github-iniciantes/02_primeiro_repositorio/` | `git init`, configuração, primeiro commit |
| `git-github-iniciantes/03_trabalhando_com_mudancas/` | `git status`, `git diff`, staging, `--amend` |
| `git-github-iniciantes/05_remotes_e_push/` | `git remote add`, `git push`, `git pull` |
| `git-github-iniciantes/06_github/` | Criar conta, criar repositório, configurar remoto |
| `git-github-iniciantes/13_open_source/` | Licença e publicação pública |
| `manual-qa-completo/README.PT-BR.md` | **Modelo real** de README em português de um projeto técnico |
| `manual-qa-completo/.gitignore` | `.gitignore` real de projeto Python |
| `manual-qa-completo/LICENSE` | Licença real usada no projeto (MIT) |
| `manual-qa-completo/CONTRIBUTING.md` | Como pedir e revisar contribuição — o padrão de "documentação é parte do trabalho" |
| `manual-qa-completo/CHANGELOG.md` | Formato de registro de mudanças |
| `Central-de-noticias/.gitignore` | `.gitignore` de um projeto JavaScript/Python real |
| `Central-de-noticias/requirements.txt` | Dependências mínimas versionadas |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Versionamento** | "Um **histórico** que responde: quem mudou, quando e por quê." |
| **3 estados** | "Working directory → Staging area → Repositório. Três portas, três comandos." |
| **`git status`** | "Meu estado agora: o que eu alterei, o que está pronto e o que falta." |
| **`git add`** | "Escolher **o que entra** no próximo commit." |
| **`git commit`** | "Dar **nome e contexto** ao que entra." |
| **`git diff`** | "Mostrar o que mudou, linha por linha, antes de gravar." |
| **Conventional Commits** | "`feat:`, `fix:`, `docs:`, `chore:`, `test:`. O prefixo é o **tipo** da mudança." |
| **`.gitignore`** | "A lista do que **nunca** entra: senha, log, backup, ambiente virtual." |
| **`git log --oneline`** | "O resumo do projeto em uma linha por mudança." |
| **`git restore`** | "Desfazer mudança **não commitada** (o botão 'desfazer' do Git)." |
| **`git show`** | "Ver o que um commit fez, com o diff." |
| **README** | "A vitrine do repositório. É o que a pessoa lê **antes** de rodar o seu código." |
| **LICENSE** | "Sem licença, por padrão **ninguém** pode usar. Com MIT, todo mundo pode." |
| **`requirements.txt`** | "A lista **versionada** do que o projeto precisa." |
| **Segredo no Git** | "Um segredo no histórico **não some**. Nunca. Rotacione a chave." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (2 min):** lista de chamada por apelido. Se for a primeira vez de alguém, peça
para o aluno escrever no chat o apelido e o **nome completo** que ele quer no certificado
(isso é usado no Módulo 16).

**Gancho (4 min):** *"Vocês já worked com planilha compartilhada: alguém mexeu numa
célula, outra pessoa sobrescreveu, e o dado do mês anterior sumiu. Ou Worse: o arquivo
`relatorio_final_v2_agora_vai.xlsx` que ninguém sabe o que é. O Git resolve as duas
coisas — mas só se você **commitar com sentido**. Um commit sem sentido é uma letra
solta; vinte commits com sentido são a história do seu trabalho."*

**Demonstração ao vivo (4 min):** mostre o histórico real do `manual-qa-completo`:

```bash
git log --oneline -15
git show --stat HEAD
```

E mostre um arquivo `.gitignore` real de projeto Python.

**Fala do professor (texto exato):** *"Repare que os commits não dizem 'arrumei um
 negócio'. Dizem **o quê** e **por quê**. 'feat: adiciona modo dry-run ao consolidador' é
 um commit. 'update' não é commit — é ruído. Seis meses depois, você é a pessoa que mais
 vai agradecer a você mesmo."*

> **Plano B:** se o `git` não estiver instalado na máquina de algum aluno, o professor
> usa o [GitHub Desktop](https://desktop.github.com/) — mesma lógica, botões. Ou o aluno
> acompanha no Colab.

#### Fase 2 — Exploração (20 min)

**Parte 1 — Os 3 estados (6 min).**

```
   Working Directory          Staging Area            Repository
   (seus arquivos)  --git add-->  (index)  --git commit-->  (histórico)
        ^                                |                        |
        |---------- git restore ---------|   git reset --soft    |
```

```bash
git status                     # em que estado está cada arquivo
git add arquivo.py             # Working -> Staging
git diff                       # Working vs Staging (o que NÃO foi adicionado ainda)
git diff --staged              # Staging vs Repository (o que VAI entrar)
git commit -m "mensagem"       # Staging -> Repository
git restore arquivo.py         # descarta mudança do Working (cuidado!)
git reset --soft HEAD~1        # desfaz o último commit, mantém tudo no Staging
```

**Parte 2 — Mensagem de commit que vale a pena (5 min).**

Formato Conventional Commits:

```bash
git commit -m "feat(consolidador): adiciona saída em XLSX com openpyxl"
git commit -m "fix: corrige BOM na leitura de CSV gravado pelo Excel"
git commit -m "docs: explica como agendar a rotina no cron"
git commit -m "chore: adiciona .gitignore e requirements.txt"
git commit -m "test: cobre arquivo vazio e coluna ausente"
git commit -m "refactor: extrai a função de backup"
```

| Tipo | Quando usar |
|---|---|
| `feat` | funcionalidade nova |
| `fix` | correção de defeito |
| `docs` | só documentação |
| `chore` | manutenção que não muda comportamento (dependência, `.gitignore`) |
| `test` | só testes |
| `refactor` | reestruturar sem mudar comportamento |
| `perf` | ganho de desempenho |

**A regra de ouro:** a mensagem responde **por quê**, não **o quê**. O "o quê" já está
no diff. Exemplo: `feat: adiciona relatório de frequência por turma` é fraco;
`feat: relatório por turma para a reunião pedagógica do Conselho (req. SE-2026-014)` é forte.

**Parte 3 — `.gitignore` (4 min).**

```gitignore
# Ambiente virtual
.venv/
venv/
env/

# Python
__pycache__/
*.pyc
*.pyo
.pytest_cache/
.coverage
htmlcov/

# Logs e artefatos de execução
logs/
*.log
backups/
relatorios/*.bak

# Segredos (NUNCA versione)
.env
.env.*
!.env.example
*.pem
*.key

# Dados de trabalho — versione o GERADOR, não o dado
dados/*.csv
dados/*.xlsx

# Sistema operacional e editores
.DS_Store
Thumbs.db
.vscode/
.idea/
```

> **Regra da sala:** **versione o gerador, não o dado.** O script que cria o CSV falso
> entra no repositório; o CSV falso, não. E se o dado for real, ele **jamais** entra.

**Parte 4 — README profissional (3 min).**

As 7 seções que todo repositório precisa ter:

```markdown
# Nome do Projeto

Uma frase: o que este projeto faz e para quem.

## Índice
- [Instalação](#instalação)
- [Uso](#uso)
- [Como funciona](#como-funciona)
- [Testes](#testes)
- [Agendamento](#agendamento)
- [Licença](#licença)
- [Contribuindo](#contribuindo)

## Instalação
    git clone https://github.com/SEU_USUARIO/SEU_PROJETO.git
    cd SEU_PROJETO
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Uso
    python consolidar_vendas.py --entrada dados/vendas.csv --saida relatorios

## Como funciona
1. Lê o CSV de entrada
2. Valida as colunas obrigatórias
3. Consolida por produto
4. Grava CSV, JSON e XLSX (com backup do anterior)

## Testes
    python -m unittest -v

## Agendamento
    0 7 * * * cd ~/meu-projeto && /caminho/absoluto/.venv/bin/python consolidar_vendas.py ...

## Licença
MIT — veja o arquivo [LICENSE](LICENSE).

## Contribuindo
Leia [CONTRIBUTING.md](CONTRIBUTING.md).
```

**Parte 5 — Publicar no GitHub (2 min).**

```bash
# 1. Crie o repositório VAZIO no GitHub (sem README, sem .gitignore, sem licença)
#    https://github.com/new

# 2. Conecte o remoto
git remote add origin https://github.com/SEU_USUARIO/SEU_PROJETO.git

# 3. Verifique onde o push vai
git remote -v

# 4. Envie
git push -u origin main
```

> ⚠️ **Se o repositório do GitHub foi criado com README**, o push vai **rejeitar**.
> Solução: `git pull origin main --allow-unrelated-histories` e depois `git push -u origin main`.

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. O professor circula conferindo **uma coisa
só**: a mensagem do commit.

**Atividade A — Repositório limpo (12 min).**
Cada aluno pega o projeto das aulas 2–4 e:

```bash
cd ~/meu-projeto
git init
git config user.name "Nome Completo do Aluno"
git config user.email "email@exemplo.com"

# .gitignore
cat > .gitignore <<'EOF'
.venv/
__pycache__/
*.pyc
logs/
backups/
.env
dados/*.csv
EOF

git add .
git status                      # confira ANTES de commitar: o que entrou?
git commit -m "chore: estrutura inicial do projeto de automação"
```

**Fala do professor enquanto circula (texto exato):** *"Antes de dar `commit`, olhe o
`git status` **com calma**. Se aparecer `.env` ou `logs/`, o `gitignore` está errado.
Esse é o momento mais barato de evitar um vazamento — e o único. Depois que o segredo
entra no histórico, ele **sai do repositório** — mas continua lá para sempre."*

**Atividade B — Commits com sentido (18 min).**
Cada aluno faz **8 a 12 commits pequenos**, um por mudança lógica. Sugestão de sequência:

```bash
git add scripts/backup-relatorio.sh
git commit -m "feat: script de backup com log em arquivo e código de saída"

git add .gitignore requirements.txt
git commit -m "chore: ignora ambiente virtual, logs, backups e dados locais"

git add consolidar_vendas.py
git commit -m "feat(consolidador): lê CSV, valida colunas e consolida por produto"

git add consolidar_vendas.py
git commit -m "feat(consolidador): adiciona --dry-run para ensaio sem gravação"

git add consolidar_vendas.py
git commit -m "feat(consolidador): faz backup datado antes de sobrescrever relatório"

git add test_consolidar_vendas.py
git commit -m "test: cobre caminho feliz, entrada inválida e dry-run"

git add README.md
git commit -m "docs: README com instalação, uso, agendamento e limitações"
```

> **Dica de ouro:** se o `git status` mostrar **5 arquivos** modificados, **não** commite
> tudo de uma vez. Faça `git add` de um, commite, adicione o próximo. Commits pequenos
> são reversíveis; commit grande é um mistério.

**Entregável da Atividade B:** repositório com **20+ commits** descritivos ao final do módulo
(hoje já são ~8; as aulas seguintes somam o resto).

#### Fase 4 — Projeto (25 min)

**Desafio: "Repositório que passa na avaliação"**

Cada aluno deixa o repositório no padrão que uma empresa (ou uma escola, ou a Secretaria)
aceitaria receber:

| Item | Exigência |
|---|---|
| `README.md` | As 7 seções, com **comando de instalação que funciona** |
| `LICENSE` | MIT, com o nome do autor no ano |
| `.gitignore` | Cobre `.venv/`, `__pycache__/`, `logs/`, `backups/`, `.env`, `dados/` |
| `requirements.txt` | Gerado por `pip freeze`, com versões fixadas |
| `CONTRIBUTING.md` | 1 parágrafo: como contribuir e o que será aceito |
| `CHANGELOG.md` | Versão 1.0.0 com as funcionalidades entregues |
| `.env.example` | **Modelo** com as chaves **vazias** e comentário do que é cada uma |
| Commits | 20+ commits com mensagens no formato `tipo: descrição` |
| `.github/` | 1 pasta com `ISSUE_TEMPLATE/bug_report.md` (copiar do `manual-qa-completo`) |

**Modelo de `LICENSE` (MIT):**

```text
MIT License

Copyright (c) 2026 Nome Completo do Aluno

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Critério de pronto:**
- [ ] `README.md` com as 7 seções e **comando testado por outra pessoa** (peer review)
- [ ] `LICENSE` MIT com nome e ano
- [ ] `.gitignore` verificado: `git status` **não mostra** nenhum arquivo ignorado
- [ ] `requirements.txt` versionado
- [ ] `CONTRIBUTING.md` e `CHANGELOG.md` presentes
- [ ] `.env.example` presente com chaves **vazias**
- [ ] **20+ commits** no padrão `tipo: descrição`
- [ ] `git log --oneline` **lido de ponta a ponta** sem puzzling — a história faz sentido
- [ ] Nenhum **segredo** no repositório (checagem manual do `git log -p`)

#### Fase 5 — Mostra (5 min)

**Câmera ligada.** Cada aluno mostra **1 comando do terminal**:

```bash
git log --oneline | head -20
```

E responde 2 perguntas:

1. "Qual foi o commit mais recente e por que ele existe?"
2. "Se eu clonasse esse repositório agora, em quantos minutos eu teria o relatório rodando?"

> **Pergunta de saída (no chat):** "Por que `git add .` antes de todo commit é um risco,
> e qual é a alternativa?"

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Repositório | `git init` feito, `user.name` e `user.email` configurados **localmente** |
| Commits | 20+ commits, mensagens no padrão `tipo: descrição`, **sem** "update" ou "ajustes" |
| `.gitignore` | `git status` limpo; nenhum `.env`, `logs/` ou `dados/` versionado |
| README | 7 seções; o comando de instalação foi **executado** com sucesso por um colega |
| `LICENSE` | MIT, com nome e ano |
| `requirements.txt` | Versionado, gerado por `pip freeze` |
| `.env.example` | Presente, com chaves vazias e comentário |
| Sigilo | Nenhum segredo no repositório (nem no histórico) |
| Diagnóstico | O aluno usa `git status`, `git diff` e `git log` **sem ajuda** |

**Pergunta de escrita:**
> "Você fez `git add .` e commitou. Deu para frente, você percebeu que o arquivo `.env`
> — com a chave da API do portal — foi junto. O repositório ainda é privado e ninguém
> mais tem acesso. O que você faz?"
>
> **Resposta:** A resposta profissional tem **duas partes**, e a ordem importa:
> 1. **Remover do índice e do próximo commit, imediatamente.** Enquanto o commit não foi
>    publicado, o estrago é local:
>    ```bash
>    git rm --cached .env
>    echo ".env" >> .gitignore
>    git add .gitignore
>    git commit -m "chore: remove .env do versionamento e ignora no futuro"
>    ```
>    Isso limpa o **último** commit. Se houver outros commits com o `.env`, use
>    `git filter-repo` (ou `git filter-branch`) para reescrever o histórico.
> 2. **Rotacionar a chave — sempre, mesmo com repositório privado.** O arquivo `.env`
>    fica gravado no **objeto** do commit, e objeto antigo continua no repositório local
>    (e no `.git/objects`, e em qualquer backup). O único jeito de "tirar" o segredo do
>    mundo é **trocar a chave**. Vá no painel do serviço, gere uma chave nova, e atualize
>    o `.env` local e o `.env.example` do repositório (com valor vazio).
> 3. **Se já foi publicado** (push feito, repo público): o procedimento é reescrever o
>    histórico (`git filter-repo --path .env --invert-paths`), forçar o push
>    (`git push --force`), avisar a plataforma e **rotacionar a chave** imediatamente.
> 4. **A lição que vale para a vida profissional:** o `.env` **nunca** entra no Git. E
>    "repo privado" **não** é backup de sigilo — é só mais uma cópia do arquivo, com
>    histórico e sem revogação.
>
> **Por que o professor conta esse caso na aula:** porque **é** assim que acontece. A
> diferença entre o aluno que aprende e o que repete o erro é que um deles leu esta
> resposta antes de dar `git add .`.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `git-github-iniciantes/01_o_que_e_git/` | Working Directory, Staging Area, Repositório |
| `git-github-iniciantes/02_primeiro_repositorio/` | `git init`, configuração, primeiro commit |
| `git-github-iniciantes/03_trabalhando_com_mudancas/` | `git status`, `git diff`, `git add`, `git commit` |
| `git-github-iniciantes/05_remotes_e_push/` | `git remote`, `git push`, `git pull` |
| `git-github-iniciantes/06_github/` | Criar conta e repositório |
| `git-github-iniciantes/13_open_source/` | Licença e publicação |
| `manual-qa-completo/README.PT-BR.md` | README real em português de projeto técnico |
| `manual-qa-completo/.gitignore` | `.gitignore` real de projeto Python |
| `manual-qa-completo/LICENSE` | Licença usada no projeto |
| `manual-qa-completo/CONTRIBUTING.md` | Padrão de contribuição |
| `manual-qa-completo/CHANGELOG.md` | Formato de registro de mudanças |
| `Central-de-noticias/.gitignore` | `.gitignore` de projeto JavaScript/Python real |

**Exercícios para treinar fora da aula:**

1. Clone um repositório público e rode `git log --oneline --graph --all` para ver a ramificação.
2. Use `git log -S "dry-run"` num repositório e veja **quem** introduziu o conceito e **quando**.
3. Escreva um `.gitignore` de projeto e **teste** criando arquivos `senha.txt`, `build/`, `a.log` e veja se foram ignorados.

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Publique o repositório no **GitHub** (conta criada e e-mail verificado).
2. Adicione **10 commits** novos — cada um com uma mudança real (ajuste de log, novo
   argumento, novo teste, documentação, correção de erro de digitação, etc.).
3. Escreva o `CONTRIBUTING.md` e o `CHANGELOG.md`.
4. Crie `.github/ISSUE_TEMPLATE/bug_report.md` adaptando o modelo de
   `manual-qa-completo/docs/10/PT/bug_report_template.md`.
5. **Peça revisão a um colega** da turma: ele clone o repositório, segue o README e tenta
   rodar. Anote no README as dúvidas dele — são os **bugs de documentação**.
6. (Opcional) Marque o repositório com uma **descrição de 1 linha** e **topics** no GitHub.

> **Na aula 6** você vai trabalhar em *branch*, abrir *pull request* e deixar a CI verde.

---

### 🔗 Próximo módulo

[Módulo 6 — Git e GitHub profissional (parte 2: branch, PR e GitHub Actions) · Aula 6](#m06)

---

<a id="m06"></a>

## Módulo 6 — Git e GitHub profissional (parte 2): branch, PR e GitHub Actions (Aula 6)

**Duração:** 90 min · **Aula 6 de 16** · **P6** (continuação do Módulo 5)
**Entregável do módulo:** **1 branch** publicado, **1 pull request** com revisão de um
colega, e **GitHub Actions rodando a cada push** com a suíte de testes.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar **por que existe branch** e o que é **merge**, **rebase** e **conflito**.
2. Criar, trocar e apagar branch com `git switch -c`, `git switch`, `git branch -d`.
3. Resolver um **conflito de merge** lendo os marcadores `<<<<<<<`, `=======`, `>>>>>>>`
   e decidindo conscientemente.
4. Abrir um **pull request** com **título, descrição, checklist e revisor**, e fazer
   **revisão de código** com comentário **por linha** — approve ou request changes.
5. Escrever um **workflow de GitHub Actions** em YAML que roda a suíte de testes em
   **cada push** e em **cada pull request**.
6. Ler os **resultados da CI** (verde/vermelho) e usar o log do CI para encontrar o erro.
7. Entender **concorrência** (`concurrency`) e **segredos** (`secrets`) em workflows.

**Objetivo secundário:** Reconhecer, num repositório alheio, os 5 sinais de um projeto
que não é profissional (sem README, sem licença, sem CI, sem `.gitignore`, commit único).

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `git-github-iniciantes/04_branches/` | Criar, trocar e mesclar branches |
| `git-github-iniciantes/07_pull_requests/` | Fluxo de pull request e revisão |
| `git-github-iniciantes/08_issues_e_projetos/` | Issues e Projects como organização do trabalho |
| `git-github-iniciantes/11_trabalho_em_equipe/` | Convenção de commits, CODE_OF_CONDUCT, revisão |
| `git-github-iniciantes/12_ci_cd_basico/` | Introdução a CI/CD |
| `manual-qa-completo/.github/workflows/ci.yml` | Workflow real: **matriz** de versões do Python (`3.10`, `3.11`), `fail-fast: false`, `actions/upload-artifact` com `if: always()` e jobs separados (`test`, `scripts`, `mermaid`) |
| `Central-de-noticias/.github/workflows/ci-tests.yml` | Workflow real mínimo: `push` e `pull_request` em `main`, `setup-python` com `cache: pip`, `pytest -v` |
| `Central-de-noticias/.github/workflows/monitoramento.yml` | `permissions:` restritas (`contents: read`, `issues: write`) e `se: failure()` — o padrão de **princípio do menor privilégio** em CI |
| `QA_RUN/.github/workflows/static.yml` | Workflow de site estático |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Branch** | "Uma **linha do tempo paralela**. Você testa a ideia sem estragar a linha principal." |
| **`git switch -c`** | "Cria e já entra na branch. Atalho moderno do `git checkout -b`." |
| **Merge** | "Junta a branch na principal, criando um commit de junção." |
| **Rebase** | "Reaplica seus commits **em cima** da main, deixando o histórico linear." |
| **Conflito** | "O Git parou porque **ele não sabe** qual das duas versões é a certa. Só você sabe." |
| **Pull Request** | "Um pedido de revisão. Você pede **antes** de mudar a linha principal." |
| **Revisão por linha** | "Comente **na linha**, não no arquivo. A conversa fica no lugar certo." |
| **Request changes** | "Eu não aprovei — e eu disse **por quê**. Isso é revisão, não bloqueio." |
| **CI (Integração Contínua)** | "Toda vez que alguém envia código, o servidor **testa sozinho**." |
| **Workflow (YAML)** | "O roteiro do robô: quando rodar, com qual Python, o que executar." |
| **`on: [push, pull_request]`** | "Testa nos **dois** casos: envio direto e pedido de integração." |
| **Matriz de versões** | "Testa em Python 3.10 **e** 3.11. O seu código funciona na sua máquina — e na do outro?" |
| **`fail-fast: false`** | "Se uma versão quebra, as **outras** continuam rodando. Mais informação, não menos." |
| **`if: always()`** | "Guarda o artefato **mesmo** quando o teste falhou — é justamente aí que ele vale." |
| **`permissions:`** | "O robô só recebe o poder que precisa. Menor privilégio, até na CI." |
| **`secrets`** | "Senha de verdade **nunca** vai no YAML. Vai em `secrets`." |
| **`concurrency`** | "Dois jobs do mesmo grupo **não** correm juntos." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** lista de chamada por apelido. Mostre no chat o **placar da turma**:
quantos repositórios já estão publicados, quantos commits somados. Motiva mais que
nota.

**Gancho (3 min):** *"Até aqui você VERSIONA sozinho. A partir de agora você entra no
mundo real: alguém **revisa** o seu código, e um **robô** testa o seu código a cada
push. Se você tem vergonha do seu código — bom. Agora ele vai ser lido por gente, e
testado por máquina. É esse o salto de 'fiz um script' para 'entreguei software'."*

**Demonstração ao vivo (3 min):** abra o repositório do `manual-qa-completo` e mostre a aba
**Actions** rodando. Depois mostre o `Central-de-noticias` e a aba **Pull requests**.

**Fala do professor (texto exato):** *"Repare no detalhe da matriz: o CI do manual roda os
testes em **duas versões** do Python. Por quê? Porque na sua máquina tem uma versão, e
na máquina de quem vai rodar o seu script tem outra. O CI é o lugar onde você descobre
isso **antes** de alguém reclamar. Reclamação é feedback caro; CI verde é feedback
grátis."*

> **Plano B:** se o GitHub estiver fora do ar, o professor explica o conceito com o
> repositório local (`git switch -c`, `git merge`) e demonstra o YAML no editor. O
> workflow é **copiado** no Módulo 15 se o aluno precisar.

#### Fase 2 — Exploração (22 min)

**Parte 1 — Branch (7 min).**

```bash
git switch -c feature/relatorio-frequencia   # cria e entra na branch
git branch                                   # lista as branches
git switch main                              # volta para a principal
git merge feature/relatorio-frequencia       # traz a branch para a main
git branch -d feature/relatorio-frequencia   # apaga a branch (já mesclada)
```

**Fluxo profissional (o que você vai usar a partir de agora):**

```
main  ──●──●──────────────●─────────●──►   (sempre estável e testada)
         \              /
          ●──●──●──●──/                  (sua branch de trabalho)
            \    /
             ●──●                          (commits pequenos e focados)
```

**Parte 2 — Conflito (5 min).** Provoque um de propósito:

```bash
git switch -c teste/conflito
# Em um terminal:
echo "Versão A" >> notas.txt
git commit -am "chore: nota da branch"
git switch main
# Em outro terminal:
echo "Versão B" >> notas.txt
git commit -am "chore: nota da main"
# Volta para a branch:
git switch teste/conflito
git merge main
```

O Git mostra:

```text
Auto-merging notas.txt
CONFLICT (content): Merge conflict in notas.txt
<<<<<<< HEAD
Versão A
=======
Versão B
>>>>>>> main
```

**Resolução (o procedimento profissional, na ordem):**

```bash
# 1. Abrir o arquivo e ESCOLHER o conteúdo certo (manualmente)
# 2. Marcar como resolvido
git add notas.txt
# 3. Concluir
git commit -m "merge: resolve conflito entre branch e main"
```

> **Fala do professor:** *"O conflito não é erro do Git. O Git fez a parte dele: parou e
> avisou que **ele não sabe**. Só quem conhece o projeto decide. Se você resolveu o
> conflito com `git checkout --ours` às cegas, você não resolveu — você **apostou**."*

**Parte 3 — Pull request (5 min).** O que um PR profissional precisa ter:

```markdown
## O que muda
Consolida o relatório de frequência por turma, com total de faltas e presença.

## Por quê
A planilha de chamada vem de 12 unidades e a consolidação manual levava 3 horas
(req. SE-2026-014).

## Como testar
    python consolidar.py --entrada dados/chamada.csv --saida relatorios --dry-run
    python -m unittest -v

## Checklist
- [x] Testes passam
- [x] README atualizado
- [x] Nenhum dado real no repositório
- [ ] Revisado por um colega da turma

## Riscos
- Se o CSV de entrada vier com coluna faltando, o script falha (com mensagem clara).
```

**Parte 4 — GitHub Actions (5 min).** O workflow real do `Central-de-noticias`
(`ci-tests.yml`), anotado:

```yaml
name: CI - Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read          # menor privilégio: o robô só lê

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: pip
      - name: Instalar dependências
        run: pip install -r requirements.txt pytest
      - name: Executar testes
        run: python -m pytest -v
```

**E o workflow do `manual-qa-completo` (`ci.yml`), que usa matriz:**

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false                 # uma versão quebrada não cancela as outras
      matrix:
        python-version: ["3.10", "3.11"]
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Setup Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Run tests
        run: |
          pytest --version
          pytest --tb=short -q
      - name: Upload test results
        if: always()                  # guarda o artefato mesmo se o teste falhou
        uses: actions/upload-artifact@v4
        with:
          name: test-results-${{ matrix.python-version }}
          path: ./
```

**As 6 linhas que mudam tudo:**

| Linha | O que faz |
|---|---|
| `on: [push, pull_request]` | roda nos dois casos |
| `permissions: contents: read` | o robô só lê |
| `strategy.matrix` | testa em várias versões |
| `fail-fast: false` | uma falha não cancela o resto |
| `if: always()` | guarda o artefato mesmo na falha |
| `cache: pip` | instala dependências 5× mais rápido |

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. O professor circula e, em cada sala, pede
para **dois alunos trocarem de papel**: um é o autor, o outro é o revisor. Isso é
obrigatório — **revisão só existe com duas pessoas**.

**Atividade A — Branch + PR (15 min).**

```bash
# 1. Criar a branch
git switch -c feature/relatorio-frequencia

# 2. Fazer a mudança (ex.: novo formato de saída)
#    edite o script, rode os testes, e commit:
git add .
git commit -m "feat: relatório de frequência por turma com total de faltas"

# 3. Publicar a branch
git push -u origin feature/relatorio-frequencia
```

Depois, no GitHub: **Compare & pull request** → preencha título, descrição e checklist →
**Reviewers** → escolha o colega da turma.

**O revisor (papel do segundo aluno):**

1. Abrir o **Files changed**.
2. **Comentar em 1 linha específica** do código (clique na linha → "Add a comment").
3. Classificar o comentário:
   - **Comment** — sugestão (não bloqueia).
   - **Request changes** — precisa corrigir antes.
   - **Approve** — está bom.
4. Escrever um **comentário geral** na conversa do PR: "Testei localmente com
   `python -m unittest -v`; tudo verde. Só ajustei o nome da coluna para português."

**Fala do professor enquanto circula (texto exato):** *"Quero ver o autor **respondendo**
o comentário do revisor. Isso é o que acontece em equipe de verdade: não é só
aprovar ou rejeitar, é **conversar em cima do código**. Se ninguém respondeu o seu
comentário, o PR não termina — e o autor fica sem saber se pode seguir."*

**Atividade B — GitHub Actions (15 min).**
Crie `.github/workflows/ci.yml` no repositório do aluno:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  tests:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.10", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: pip
      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Executar testes
        run: |
          python -m unittest -v
```

```bash
git add .github/workflows/ci.yml
git commit -m "ci: roda a suíte de testes em cada push e pull request"
git push
```

Depois: abra a aba **Actions** no repositório e **espere o workflow rodar**.

**Fala do professor:** *"Esperem o workflow terminar. Se ficar vermelho, **não DESFAÇA** o
commit — abra o log do CI. O log do CI é o mesmo `unittest` rodando em outra máquina, e a
mensagem de erro é exatamente a mesma. Mas tem uma vantagem: ele roda **sem você**."*

**Entregável do módulo:**
- [ ] 1 branch publicada com commits pequenos
- [ ] 1 pull request aberto, com título, descrição e checklist preenchidos
- [ ] **1 revisão feita por colega** (comentário por linha, com `Approve` ou `Request changes`)
- [ ] Workflow `.github/workflows/ci.yml` no repositório
- [ ] A CI rodou **verde** em pelo menos 1 push
- [ ] A CI rodou **vermelha** pelo menos 1 vez (proposital) e o aluno sabe ler o log

#### Fase 4 — Projeto (25 min)

**Desafio: "Repositório que passa na revisão"**

Cada aluno entrega o repositório no padrão de **projeto que recebe contributions**:

| Item | Exigência |
|---|---|
| Branches | `main` (protegida) + ao menos 1 `feature/...` já mesclada |
| Pull request | 1 PR **fechado e mergeado**, com revisão de colega registrada |
| CI | `.github/workflows/ci.yml` verde nos últimos 3 pushes |
| Matriz | Testes em **2 versões** do Python |
| `fail-fast` | `false` configurado |
| Artefato | `actions/upload-artifact` com `if: always()` |
| Permissões | `permissions: contents: read` no workflow |
| Issues | 1 **issue** real aberta (por você ou pelo colega) descrevendo um bug/melhoria |
| `CODE_OF_CONDUCT` | 1 arquivo curto de conduta (opcional, mas recomendado) |

**Modelo de `CODE_OF_CONDUCT.md` (curto e honesto):**

```markdown
# Código de Conduta

Este projeto segue o Código de Conduta Contributor Covenant.

## Em resumo
- Seja respeitoso e acolhedor.
- Discuta a ideia, não a pessoa.
- Assume que o outro está tentando ajudar.

## Denúncias
Abra uma issue privada ou contate o mantenedor pelo e-mail do repositório.
```

**Critério de pronto:**
- [ ] `main` está **protegida** (Settings → Branches → Require a pull request)
- [ ] Existe 1 PR mergeado **com revisão de colega**
- [ ] A CI está **verde** nos últimos 3 pushes
- [ ] A CI roda em **2 versões** do Python com `fail-fast: false`
- [ ] Há **1 issue** aberta com descrição clara
- [ ] O `git log --graph --oneline --all` mostra a **história** da branch mergeada
- [ ] O repositório está **público** (ou pronto para ficar)

#### Fase 5 — Mostra (5 min)

**Câmera ligada.** Cada aluno mostra **a aba Actions** do próprio repositório, com a CI
verde, e conta uma história:

1. "Qual foi o commit que quebrou a CI, e o que a CI revealed?"
2. "O que um revisoravlancou no meu código?"

> **Pergunta de saída (no chat):** "Por que a CI roda também em `pull_request` e não só
> em `push`?"

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Branch | Criada, publicada, com commits pequenos e focados |
| Pull request | Título, descrição com "o que muda" e "como testar", checklist |
| Revisão | Feita **por colega**, com comentário por linha e veredito (`Approve` ou `Request changes`) |
| Conflito | Resolvido conscientemente (a aula provoca um) |
| Workflow | YAML válido, com `on`, `permissions`, matriz, `fail-fast: false`, `if: always()` |
| CI verde | Últimos 3 pushes verdes |
| Leitura de log | O aluno sabe dizer **qual** arquivo/linha quebrou, usando o log do CI |
| Repositório | `main` protegida, 1 issue aberta, histórico legível com `git log --graph` |

**Pergunta de escrita:**
> "Você abriu um pull request. A CI do repositório ficou **vermelha**, e o log mostra:
> `ModuleNotFoundError: No module named 'openpyxl'`. O código funciona perfeitamente na
> sua máquina. O que aconteceu e o que você corrige?"
>
> **Resposta:** A causa é quase sempre **uma das três**, e o CI **já** disse qual:
> 1. **A dependência não está no `requirements.txt`.** O `openpyxl` estava instalado na
>    sua máquina (você rodou `pip install openpyxl` na aula), mas a **lista versionada**
>    não tem a linha. O CI cria um ambiente **novo e limpo** e instala só o que está no
>    `requirements.txt` — então ele não tem o `openpyxl`. *Correção:*
>    ```bash
>    pip install openpyxl
>    pip freeze > requirements.txt
>    git add requirements.txt
>    git commit -m "chore: adiciona openpyxl às dependências do projeto"
>    ```
>    **Isso é exatamente o motivo de existir o `requirements.txt`.** A CI não está
>    "quebrada": ela está **mostrando** que a sua máquina tem mais do que o projeto
>    declara.
> 2. **O CI roda em versão diferente do Python.** Se o seu `from __future__ import
>    annotations` ou alguma sintaxe depende de 3.12 e a matriz roda 3.10, o erro muda
>    de forma. *Correção:* alinhar a matriz com a versão documentada no README, ou
>    escrever código compatível com a **menor** versão da matriz.
> 3. **O `cache: pip` está com hash antigo.** Raro, mas acontece: o cache serve o índice
>    de pacotes de antes da última alteração do `requirements.txt`. *Correção:* limpar o
>    cache (`Settings → Actions → Caches → Delete`) ou reescrever o `requirements.txt`
>    (mudar a ordem das linhas invalida o hash).
>
> **A lição de fundo:** "funciona na minha máquina" **não é** evidência de nada — é
> apenas a sua máquina. A CI é a **máquina neutra**: ela instala o que o projeto
> declara, na versão que o projeto declara, e roda o teste. Quando a CI falha, **a
> primeira hipótese sempre é o `requirements.txt`** — e, no fim, quase sempre é mesmo.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `git-github-iniciantes/04_branches/` | Criar, trocar e mesclar branches |
| `git-github-iniciantes/07_pull_requests/` | Fluxo de pull request e revisão |
| `git-github-iniciantes/08_issues_e_projetos/` | Issues e Projects |
| `git-github-iniciantes/11_trabalho_em_equipe/` | Convenção de commits e revisão |
| `git-github-iniciantes/12_ci_cd_basico/` | Introdução a CI/CD |
| `manual-qa-completo/.github/workflows/ci.yml` | Workflow real com matriz, `fail-fast: false` e `upload-artifact` |
| `Central-de-noticias/.github/workflows/ci-tests.yml` | Workflow mínimo real com `setup-python` e `cache: pip` |
| `Central-de-noticias/.github/workflows/monitoramento.yml` | `permissions:` restritas e `if: failure()` |
| `Central-de-noticias/.github/workflows/update-news.yml` | `concurrency` e guarda de execução |
| `QA_RUN/.github/workflows/static.yml` | Workflow de site estático |

**Exercícios para treinar fora da aula:**

1. Pratique o ciclo completo: `switch -c` → commit → `push` → PR → revisão → merge → delete branch.
2. Escreva um workflow que rode **dois** jobs: testes **e** verificação do `.gitignore` (falha se algum `.env` estiver versionado).
3. Use `git rebase -i HEAD~3` para reescrever as mensagens dos últimos 3 commits antes de abrir o PR.

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Abra **1 pull request** novo no seu repositório, com uma melhoria real (um argumento
   novo, um teste a mais, uma seção de documentação).
2. Peça a **revisão** de 2 colegas da turma e **responda** os comentários deles.
3. Amplie a CI: adicione um job de **segredos** (copie a lógica do
   `manual-qa-completo/docs/11/scripts/secret_scan.py`) e um job de **cobertura**.
4. Configure a proteção da branch `main` (exige PR e 1 aprovação).
5. Escreva no `README.md` uma seção **"Como contribuir"** com o passo a passo do fork,
   branch, PR e revisão.
6. (Opcional) Versione sua própria pasta de exercises em um repositório e use issue
   labels para organizar.

> **Na aula 7** você vai ler e limpar dados de verdade (fictícios, mas com cara de real).

---

### 🔗 Próximo módulo

[Módulo 7 — Dados e Planilhas (parte 1: CSV/XLSX) · Aula 7](#m07)

---

<a id="m07"></a>

## Módulo 7 — Dados e Planilhas (parte 1): CSV e XLSX (Aula 7)

**Duração:** 90 min · **Aula 7 de 16** · **P7** (módulo em 2 aulas: 7 e 8)
**Entregável do módulo:** **script de leitura, limpeza e validação de dados** que lê CSV e
XLSX, detecta sujeira (coluna faltando, valor não numérico, data em formato errado,
duplicata) e grava um **JSON de diagnóstico**.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar por que **planilha não é banco de dados** — e quando o Excel ainda é a
   resposta certa.
2. Ler **CSV** com `csv.DictReader` tratando BOM, delimitador `;` (padrão do Excel
   brasileiro) e acentuação.
3. Ler **XLSX** com `openpyxl` — linhas, colunas, tipos, e a primeira linha como
   cabeçalho.
4. Ler **CSV** com `pandas.read_csv` (incluindo `sep=';'`, `encoding`, `na_values`) e
   **XLSX** com `pandas.read_excel`.
5. **Diagnosticar sujeira**: coluna ausente, valor não numérico, data ambígua,
   duplicata, linha em branco, valor com espaço sobrando.
6. **Normalizar** dados: `strip`, `lower`, padronizar data para `YYYY-MM-DD`, converter
   número com `,` decimal para `float`.
7. Escrever um **relatório de qualidade dos dados** em JSON, com contagem de problemas
   por tipo.
8. Escolher entre **CSV**, **JSON** e **SQLite** para um cenário concreto da Secretaria.

**Objetivo secundário:** Explicar por que **"deu erro na linha 47"** é uma informação
inútil, e o que um diagnóstico útil precisa ter.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `Analise-de-Dados/datasets/Gapminder.csv` | CSV real com **mais de mil linhas**, cabeçalho e acentuação — material de teste de leitura |
| `Analise-de-Dados/datasets/AdventureWorks.xlsx` | XLSX real de vendas (AdventureWorks) — o arquivo mais próximo de um relatório de escola/comércio |
| `Analise-de-Dados/datasets/Aracaju.xlsx` · `Fortaleza.xlsx` · `Natal.xlsx` · `Recife.xlsx` · `Salvador.xlsx` | Mais 5 planilhas reais para treinar leitura de múltiplas abas e formatos |
| `Analise-de-Dados/population_data_ analysis.ipynb` | Notebook real de análise — referência de fluxo de trabalho com dados |
| `python-do-zero/10_arquivos/exercicio_05_csv.txt` | Exercício oficial de CSV da biblioteca padrão |
| `python-do-zero/14_projetos_praticos/` | Projetos práticos que combinam arquivos e dados |
| `planilhaeletronicas/app.py` | Aplicação real **Flask + Pandas → Excel** com `pd.read_excel`, `pd.to_numeric(..., errors='coerce')` e `pd.ExcelWriter` — o modelo do Módulo 8 |
| `laboratorio-tech-social/site/exercicios/planilha.html` | Exercício interativo de planilha no navegador (sem instalar nada) |
| `laboratorio-tech-social/site/exercicios/gerador-dados.html` | **Gerador de dados fictícios** — o jeito certo de criar massa de teste |
| `laboratorio-tech-social/site/exercicios/visualizador-dados.html` | Visualizador de dados no navegador |
| `laboratorio-tech-social/materiais/slides/aula-teens-04-dados.html` | Slide de ciência de dados (referência de ritmo) |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Planilha ≠ banco** | "A planilha é uma **tabela única** com interface. O banco é um **motor** com regras." |
| **CSV** | "Texto separado por vírgula (ou `;`). Qualquer programa lê. Não guarda tipo." |
| **BOM** | "O Excel brasileiro deixa 3 bytes invisíveis no começo. Sem `utf-8-sig`, a primeira coluna se chama `﻿data`." |
| **`;` × `,`** | "O Excel em pt-BR usa `;`. Use `sep=';'` e `decimal=','`." |
| **XLSX** | "Um `.xlsx` é um **ZIP com XML dentro**. Só `openpyxl` (ou `pandas`) sabe ler." |
| **Aba (sheet)** | "Uma planilha pode ter várias abas. `sheet_name=None` lê todas." |
| **`pandas`** | "DataFrame = **tabela com tipos**. `df.head()`, `df.info()`, `df.describe()`." |
| **`pd.to_numeric(errors='coerce')`** | "Valor que não é número vira `NaN` **em vez de** explodir. Depois você conta os `NaN`." |
| **`NaN`** | "O valor que falta. Trate como **fato a investigar**, não como zero." |
| **Duplicata** | "Linha repetida distorce todo relatório. `df.duplicated()` acha." |
| **Normalizar** | "Antes de somar, **limpe**: `strip`, `lower`, data padrão, número padrão." |
| **Data ambígua** | "`01/02/2026` — é 1º de fevereiro ou 2 de janeiro? Nunca assuma." |
| **Qualidade dos dados** | "Você não tem um problema de dados. Você tem um **relatório** de problemas de dados." |
| **Dicionário de dados** | "O que é cada coluna, de onde vem, e qual o tipo. **Se ninguém sabe, ninguém usa.**" |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** lista de chamada por apelido. Pergunta no chat: *"Quem já recebeu
uma planilha que o Excel não conseguiu abrir? Digitem `sim`."* — quase todos respondem
`sim`, e isso é a porta de entrada.

**Gancho (3 min):** *"Na sua rotina, a planilha chega 'suja': tem uma coluna que
mudou de nome, tem número com vírgula e ponto, tem a mesma linha repetida duas vezes por
erro de dedo, tem data que pode ser de dois jeitos. O erro não está na planilha — o erro
está em **não haver regra** para o que fazer com cada sujeira. Hoje a gente escreve a
regra, e o script passa a **contar** os problemas em vez de você descobrir um a um."*

**Demonstração ao vivo (3 min):** abra o `Analise-de-Dados/datasets/Gapminder.csv` no
editor e mostre a primeira linha. Depois rode:

```bash
python - <<'PY'
import csv
with open("dados/chamada.csv", encoding="utf-8-sig", newline="") as f:
    linhas = list(csv.DictReader(f))
print("linhas:", len(linhas))
print("colunas:", list(linhas[0].keys()))
PY
```

**Fala do professor (texto exato):** *"Repare que eu usei `utf-8-sig`. Sem isso, a
primeira coluna chama `﻿data` — com um caracterinho invisível na frente. Você vai
achar que o programa está bugado, e o culpado é o Excel. Isso vai acontecer **hoje**,
no seu trabalho. Anota."*

> **Plano B:** sem Python instalado, o aluno usa
> `laboratorio-tech-social/site/exercicios/gerador-dados.html` e
> `planilha.html` no navegador e anota as observações para o script.

#### Fase 2 — Exploração (25 min)

**Parte 1 — CSV: os 3 dialetos do Brasil (7 min).**

| Dialeto | Separador | Decimal | Como abrir |
|---|---|---|---|
| "CSV americano" | `,` | `.` | `csv.DictReader` / `pd.read_csv` padrão |
| **"CSV brasileiro" (Excel pt-BR)** | `;` | `,` | `pd.read_csv(..., sep=';', decimal=',')` |
| "CSV com separador tab" | `\t` | `.` | `pd.read_csv(..., sep='\t')` |

```python
import csv

# Detectar o separador pelo cabeçalho (estratégia robusta)
def detectar_separador(caminho: str) -> str:
    """Devolve o separador do CSV olhando a primeira linha."""
    with open(caminho, "r", encoding="utf-8-sig", newline="") as arquivo:
        cabecalho = arquivo.readline()
    for candidato in (";", ",", "\t", "|"):
        if cabecalho.count(candidato) > 1:
            return candidato
    return ","


with open("dados/chamada.csv", encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=detectar_separador("dados/chamada.csv"))
    for linha in leitor:
        print(linha)
```

**Parte 2 — XLSX com `openpyxl` (7 min).**

```python
from pathlib import Path

import openpyxl


def ler_planilha(caminho: Path) -> list[dict[str, object]]:
    """Lê a PRIMEIRA aba de um .xlsx e devolve uma lista de dicionários.

    A primeira linha é o cabeçalho (nomes das colunas).
    """
    if not caminho.exists():
        raise FileNotFoundError(f"Planilha não encontrada: {caminho}")

    livro = openpyxl.load_workbook(caminho, data_only=True, read_only=True)
    folha = livro.active

    linhas = folha.iter_rows(values_only=True)
    cabecalho = next(linhas, None)
    if cabecalho is None:
        raise ValueError(f"A planilha {caminho} está vazia (sem cabeçalho).")

    nomes = [str(coluna).strip() for coluna in cabecalho]
    registros: list[dict[str, object]] = []

    for linha in linhas:
        if all(valor is None for valor in linha):
            continue          # linha em branco: pula
        registros.append(dict(zip(nomes, linha)))

    return registros
```

> **Detalhe profissional:** `data_only=True` lê o **valor** da fórmula (o resultado
> calculado) em vez da fórmula em si. Sem isso, você recebe `"=SUM(B2:B10)"` em vez de
> `85`. E `read_only=True` usa menos memória em planilha grande.

**Parte 3 — `pandas` para quando o volume cresce (6 min).**

```python
import pandas as pd


def carregar(caminho: str) -> pd.DataFrame:
    """Carrega CSV ou XLSX num DataFrame, detectando o formato pela extensão."""
    if caminho.endswith(".csv"):
        return pd.read_csv(
            caminho,
            sep=";",
            decimal=",",
            encoding="utf-8-sig",
            na_values=["", "ND", "N/D", "-"],
        )
    if caminho.endswith((".xlsx", ".xlsm")):
        return pd.read_excel(caminho, sheet_name=None)
    raise ValueError(f"Formato não suportado: {caminho}")
```

```python
df = carregar("dados/chamada.csv")

df.head()                 # 5 primeiras linhas
df.info()                 # tipos e contagem de nulos
df.describe()             # estatística das colunas numéricas
df.columns                # nomes das colunas
df.shape                  # (linhas, colunas)
df["presente"].value_counts()   # contagem de cada valor
```

**A linhagem que salva mais tempo na vida real:**

```python
# Converte texto em número sem explodir: o que não é número vira NaN
df["nota"] = pd.to_numeric(df["nota"], errors="coerce")

# Agora eu SEI quantos dados se perderam:
perdidos = int(df["nota"].isna().sum())
```

**Parte 4 — Os 6 tipos de sujeira (5 min).**

| Sujeira | Como aparece | Como detecta |
|---|---|---|
| **Coluna ausente** | faltou a coluna "presente" | `set(esperadas) - set(df.columns)` |
| **Coluna extra** | veio "obs_curvas" que ninguém pediu | `set(df.columns) - set(esperadas)` |
| **Valor não numérico** | "8,5" ou "N/A" em coluna numérica | `pd.to_numeric(errors="coerce")` + `isna()` |
| **Data ambígua** | `01/02/2026` | `pd.to_datetime(..., dayfirst=True, errors="coerce")` |
| **Duplicata** | a mesma presença lançada 2× | `df.duplicated()` |
| **Espaço sobrando** | `" Presente "` | `df[col].str.strip()` |

```python
# Data brasileira: dayfirst=True evita o erro de 01/02 virar 2 de janeiro
df["data"] = pd.to_datetime(df["data"], dayfirst=True, errors="coerce")

# Duplicatas por chave de negócio (a mesma presença 2x)
duplicadas = df[df.duplicated(subset=["turma", "data", "aluno_id"], keep=False)]

# Espaço sobrando em todas as colunas de texto
for coluna in df.select_dtypes(include="object").columns:
    df[coluna] = df[coluna].str.strip()
```

**Parte 5 — SQLite: quando a planilha já não dá (0 min, só menção).**

| Situação | Ferramenta certa |
|---|---|
| Uma tabela, até 50 mil linhas, alguém vai abrir no Excel | **CSV/XLSX** |
| Várias tabelas que se relacionam, consultas, muitos usuários | **SQLite** ([DB Browser for SQLite](https://sqlitebrowser.org/)) |
| Relatório repetido com filtro e agregação | **Script + XLSX** (é o Módulo 8) |

#### Fase 3 — Mão na massa (32 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. O professor circula com o `gerador-dados.html`
aberto, para quem não tem dados.

**Atividade A — Gerar o dado fictício (8 min).**
Use `laboratorio-tech-social/site/exercicios/gerador-dados.html` **ou** escreva o
gerador em Python (melhor — ele entra no repositório):

```python
#!/usr/bin/env python3
"""gerar_dados.py — gera um CSV de presença FICTÍCIO para testes.

Uso: python gerar_dados.py --saida dados/chamada.csv --linhas 200
"""

from __future__ import annotations

import argparse
import csv
import random
from datetime import date, timedelta
from pathlib import Path

TURMAS = ["7A", "7B", "8A", "8B", "9A", "1M"]
ALUNOS = [f"ALU{numero:04d}" for numero in range(1, 61)]   # identificadores, não nomes


def gerar_linhas(quantidade: int, semente: int) -> list[dict[str, str]]:
    """Gera registros de presença fictícios, com repetição proposital."""
    gerador = random.Random(semente)     # semente = resultado reproduzível
    inicio = date(2026, 4, 1)
    registros: list[dict[str, str]] = []

    for _ in range(quantidade):
        dia = inicio + timedelta(days=gerador.randint(0, 20))
        registros.append({
            "turma": gerador.choice(TURMAS),
            "data": dia.isoformat(),
            "aluno_id": gerador.choice(ALUNOS),
            "presente": gerador.choice(["S", "N", "N", "S", "S", "F"]),
        })

    return registros


def main() -> int:
    analisador = argparse.ArgumentParser(description="Gera CSV de presença fictício.")
    analisador.add_argument("--saida", type=Path, default=Path("dados/chamada.csv"))
    analisador.add_argument("--linhas", type=int, default=200)
    analisador.add_argument("--semente", type=int, default=42)
    argumentos = analisador.parse_args()

    argumentos.saida.parent.mkdir(parents=True, exist_ok=True)

    with argumentos.saida.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=["turma", "data", "aluno_id", "presente"],
        )
        escritor.writeheader()
        escritor.writerows(gerar_linhas(argumentos.linhas, argumentos.semente))

    print(f"{argumentos.linhas} linha(s) gravada(s) em {argumentos.saida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

> **Por que identificador (`ALU0001`) e não nome?** Porque nome é **dado pessoal** (LGPD,
> Módulo 9). Identificador é dado de negócio. A regra da sala: nos seus exemplos, use
> **identificador**, nunca nome de pessoa. É a diferença entre um projeto de exemplo e
> um projeto publicável.

**Atividade B — Diagnóstico de qualidade (24 min).**
Crie `diagnostico_dados.py`:

```python
#!/usr/bin/env python3
"""diagnostico_dados.py — aponta os problemas de um CSV de presença.

Uso:
    python diagnostico_dados.py --entrada dados/chamada.csv
    python diagnostico_dados.py --entrada dados/chamada.csv --saida relatorios/diagnostico.json
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

COLUNAS_ESPERADAS = {"turma", "data", "aluno_id", "presente"}
VALORES_PRESENCA = {"S", "N", "F"}


def analisar(caminho: Path) -> dict[str, object]:
    """Analisa o CSV e devolve um relatório de qualidade dos dados."""
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        cabecalho = set(leitor.fieldnames or [])
        linhas = [{(k or "").strip(): (v or "").strip() for k, v in linha.items()}
                  for linha in leitor]

    problemas: Counter[str] = Counter()
    detalhes: list[str] = []

    # 1. Colunas ausentes e extras
    ausentes = COLUNAS_ESPERADAS - cabecalho
    extras = cabecalho - COLUNAS_ESPERADAS
    if ausentes:
        problemas["coluna_ausente"] += 1
        detalhes.append(f"Colunas ausentes: {', '.join(sorted(ausentes))}")
    if extras:
        problemas["coluna_extra"] += 1
        detalhes.append(f"Colunas extras: {', '.join(sorted(extras))}")

    # 2. Linhas em branco
    linhas_vazias = sum(1 for linha in linhas if not any(linha.values()))
    if linhas_vazias:
        problemas["linha_em_branco"] += linhas_vazias
        detalhes.append(f"{linhas_vazias} linha(s) em branco")

    # 3. Data inválida
    datas_invalidas = 0
    for indice, linha in enumerate(linhas, start=2):
        valor = linha.get("data", "")
        try:
            datetime.strptime(valor, "%Y-%m-%d")
        except ValueError:
            datas_invalidas += 1
            if datas_invalidas <= 3:
                detalhes.append(f"Linha {indice}: data inválida '{valor}'")
    if datas_invalidas:
        problemas["data_invalida"] += datas_invalidas

    # 4. Valor de presença fora do padrão
    valores_invalidos = 0
    for indice, linha in enumerate(linhas, start=2):
        valor = linha.get("presente", "").upper()
        if valor and valor not in VALORES_PRESENCA:
            valores_invalidos += 1
            if valores_invalidos <= 3:
                detalhes.append(f"Linha {indice}: presença inválida '{valor}'")
    if valores_invalidos:
        problemas["valor_invalido"] += valores_invalidos

    # 5. Duplicatas (mesma chave de negócio repetida)
    vistas: set[tuple[str, str, str]] = set()
    duplicadas = 0
    for linha in linhas:
        chave = (linha.get("turma", ""), linha.get("data", ""), linha.get("aluno_id", ""))
        if chave in vistas:
            duplicadas += 1
        vistas.add(chave)
    if duplicadas:
        problemas["duplicata"] += duplicadas
        detalhes.append(f"{duplicadas} registro(s) duplicado(s)")

    return {
        "arquivo": str(caminho),
        "analisado_em": datetime.now().isoformat(timespec="seconds"),
        "total_linhas": len(linhas),
        "colunas_encontradas": sorted(cabecalho),
        "problemas": dict(problemas),
        "detalhes": detalhes,
        "veredito": "APROVADO" if not problemas else "REPROVADO",
    }


def main() -> int:
    analisador = argparse.ArgumentParser(description="Diagnostica a qualidade de um CSV.")
    analisador.add_argument("--entrada", type=Path, required=True)
    analisador.add_argument("--saida", type=Path, default=None)
    argumentos = analisador.parse_args()

    try:
        relatorio = analisar(argumentos.entrada)
    except FileNotFoundError as erro:
        print(f"ERRO: {erro}", file=sys.stderr)
        return 1

    texto = json.dumps(relatorio, ensure_ascii=False, indent=2)

    if argumentos.saida:
        argumentos.saida.parent.mkdir(parents=True, exist_ok=True)
        argumentos.saida.write_text(texto, encoding="utf-8")
        print(f"Diagnóstico gravado em {argumentos.saida}")
    else:
        print(texto)

    # Código de saída 1 quando há problema: o agendador e a CI conseguem ver
    return 0 if relatorio["veredito"] == "APROVADO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

**Rode:**

```bash
python gerar_dados.py --saida dados/chamada.csv --linhas 200
python diagnostico_dados.py --entrada dados/chamada.csv
echo "código de saída: $?"     # 1 se houver problema
```

**Fala do professor enquanto circula (texto exato):** *"Olha o código de saída no fim do
script. Se o arquivo está com problema, ele devolve 1. Isso significa que dá para
**colocar isso na CI** ou no `cron` e ser avisado. É o mesmo contrato do script de
consolidação — e agora você pode **encadear**: se o diagnóstico reprova, o relatório
não é gerado."*

**Entregável da Atividade B:** `diagnostico_dados.py` rodando, com relatório JSON
gerado e **veredito** APROVADO/REPROVADO.

#### Fase 4 — Projeto (20 min)

**Desafio: "A planilha que não tem dono"**

Cada aluno escolhe **um** conjunto de dados real da sua rotina (ficto por enquanto) e
entrega:

1. **Gerador** (`gerar_dados.py`) versionado, com **semente fixa** (resultado
   reproduzível).
2. **Dicionário de dados** (`dicionario_dados.md`) com, para cada coluna: nome, tipo,
   origem, obrigatoriedade, valores aceitos e **o que fazer quando estiver vazia**.

```markdown
| Coluna | Tipo | Origem | Obrigatória? | Valores aceitos | Se vazia |
|---|---|---|---|---|---|
| `turma` | texto | SGA | sim | 7A..9A, 1M | descartar a linha |
| `data` | data ISO | SGA | sim | `AAAA-MM-DD` | descartar a linha |
| `aluno_id` | texto | matrícula | sim | `ALU####` | descartar a linha |
| `presente` | código | ficha | sim | S, N, F | registrar como "não informado" |
```

3. **Diagnóstico** rodando com pelo menos **4 tipos de problema** detectados no seu
   gerador (você precisa **plantar** a sujeira de propósito, senão o diagnóstico não tem
   o que encontrar).
4. **Limpeza** implementada como função separada (`limpar()`), testável, que devolve o
   **relatório do que foi removido** — nada de descartar em silêncio.
5. **CSV limpo** gravado com as colunas normalizadas.

**Critério de pronto:**
- [ ] `gerar_dados.py` com `--semente` e resultado **reproduzível** (rode 2× e compare)
- [ ] `dicionario_dados.md` com todas as colunas
- [ ] `diagnostico_dados.py` detecta **pelo menos 4** tipos de problema
- [ ] A sujeira foi **plantada** no gerador (e está documentada no README)
- [ ] A limpeza **reporta** o que removeu (nada de sumir sem aviso)
- [ ] Código de saída **1** quando o diagnóstico reprova
- [ ] `pandas` **e** `openpyxl` aparecem no `requirements.txt`

#### Fase 5 — Mostra (5 min)

**Câmera ligada.** Cada aluno mostra o **diagnóstico** do seu CSV e explica **1** problema
que ele **não** tinha visto antes.

> **Pergunta de saída (no chat):** "Seu script leu o CSV e encontrou 3 datas inválidas.
> Você apaga as 3 linhas, apaga só a coluna, ou pede correção na origem? Justifique."

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Leitura de CSV | Trata BOM (`utf-8-sig`), separador `;` e decimal `,` |
| Leitura de XLSX | `openpyxl` com `data_only=True`, ignora linha em branco, cabeçalho treated |
| Diagnóstico | Detecta **pelo menos 4** tipos de sujeira e **reprova** com código 1 |
| Gerador | Versionado, com semente, **reproduzível**, e dados **fictícios** |
| Dicionário de dados | Todas as colunas documentadas, com regra para valor vazio |
| Limpeza | Função **separada**, **testável**, que **relata** o que removeu |
| Normalização | Data em `AAAA-MM-DD`, número em `float`, texto sem espaço sobrando |
| Dados | **Nenhum nome de pessoa real** — apenas identificadores |
| Git | Tudo versionado com mensagens `tipo: descrição` |

**Pergunta de escrita:**
> "Você recebe a planilha de chamada da unidade. 6 das 250 linhas têm a data em branco
> e 3 têm a data como `01/02/2026`. O relatório de frequência do mês é para **amanhã
> de manhã**. O que você faz, e o que você **escreve** no relatório para que a coordenação
> entenda o que aconteceu?"
>
> **Resposta:** O que você faz **não** é apagar as 9 linhas em silêncio, e não é "corrigir"
> a data adivinhando. É:
> 1. **Preservar a verdade.** As 9 linhas entram no relatório como
>    `data_informada = ""` e `situacao = "DATA_NAO_INFORMADA"`. Se você as apagar, o
>    relatório vai dizer que faltaram **menos** faltas do que realmente faltaram — e o
>    número errado é pior do que o número faltando, porque **ninguém questiona um número
>    que parece completo**.
> 2. **Nunca adivinhar a data.** `01/02/2026` pode ser 1º de fevereiro (se a
>    ausência foi em fevereiro) ou 2 de janeiro (se foi em janeiro). A ordem
>    `dayfirst=True` do `pandas` é uma **hipótese**, não uma verdade — e ela **erraria**
>    nas linhas que fossem de janeiro. *Correção:* interpretar com a mesma convenção do
>    sistema de origem (o SGA), transformar a coluna em `data_registro` (data de hoje) e
>    **guardar o texto original** em `data_original`. Se a origem é ambígua, o problema é
>    **de processo** e vai para a lista de correções.
> 3. **Escrever no relatório, em 3 linhas:**
>    - `Total de registros recebidos: 250`
>    - `Registros com data não informada: 6 (2,4%) — não computados na frequência`
>    - `Data ambígua (dd/mm): 3 — tratados como dia/mês conforme convenção da origem`
>    E **assinar** (data e responsável). Isso transforma um problema de dados em uma
>    **decisão documentada** — que é exatamente o que se pede de quem assina um relatório
>    na Secretaria.
> 4. **Automatizar o aviso.** O `diagnostico_dados.py` desta aula já devolve **código de
>    saída 1** quando há problema. Agende-o **antes** da geração do relatório e faça o
>    relatório **não ser gerado** se o diagnóstico reprovar — ou, melhor: gerar e anexar o
>    diagnóstico ao relatório. O problema de dados **vira visível**, não vira surpresa.
>
> **A lição de fundo:** o relatório não é só o número — é o número **mais a lista do que
> ficou de fora e por quê**. Relatório que esconde a própria sujeira é relatório que
> mente com confiança.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `Analise-de-Dados/datasets/Gapminder.csv` | CSV real com milhares de linhas |
| `Analise-de-Dados/datasets/AdventureWorks.xlsx` | XLSX real de vendas |
| `Analise-de-Dados/datasets/Aracaju.xlsx` | Mais planilhas reais |
| `Analise-de-Dados/datasets/Fortaleza.xlsx` | Mais planilhas reais |
| `Analise-de-Dados/datasets/Natal.xlsx` | Mais planilhas reais |
| `Analise-de-Dados/datasets/Recife.xlsx` | Mais planilhas reais |
| `Analise-de-Dados/datasets/Salvador.xlsx` | Mais planilhas reais |
| `Analise-de-Dados/population_data_ analysis.ipynb` | Notebook real de análise de dados |
| `python-do-zero/10_arquivos/exercicio_05_csv.txt` | Exercício oficial de CSV |
| `python-do-zero/14_projetos_praticos/` | Projetos práticos com arquivos |
| `planilhaeletronicas/app.py` | Flask + Pandas → Excel com `to_numeric(errors='coerce')` e `ExcelWriter` |
| `planilhaeletronicas/templates/index.html` | Interface web do relatório |
| `laboratorio-tech-social/site/exercicios/planilha.html` | Exercício interativo de planilha |
| `laboratorio-tech-social/site/exercicios/gerador-dados.html` | Gerador de dados fictícios |
| `laboratorio-tech-social/site/exercicios/visualizador-dados.html` | Visualizador de dados |
| `laboratorio-tech-social/materiais/slides/aula-teens-04-dados.html` | Slide de ciência de dados |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Gere o dataset da sua rotina com **pelo menos 300 linhas**, plantando **5 tipos
   de sujeira** propositalmente.
2. Escreva o `dicionario_dados.md` completo.
3. Implemente a função `limpar()` e faça ela **reportar** cada remoção.
4. Adicione **4 testes** ao seu projeto: um para BOM, um para coluna ausente, um para
   duplicata e um para data inválida.
5. Grave o **diagnóstico** em JSON e comite-o no repositório (é a **prova** de que o
   diagnóstico roda).
6. (Opcional) Teste a leitura com `pandas.read_excel` no `.xlsx` gerado e compare com
   o resultado do `openpyxl`.

> **Na aula 8** você vai transformar esse diagnóstico em um **relatório em Excel
> pronto para a reunião** — com histórico e backup.

---

### 🔗 Próximo módulo

[Módulo 8 — Dados e Planilhas (parte 2): relatório automatizado em Excel · Aula 8](#m08)

<a id="m08"></a>

## Módulo 8 — Dados e Planilhas (parte 2): relatório automatizado em Excel (Aula 8)

**Duração:** 90 min · **Aula 8 de 16** · **P8** (módulo em 2 aulas: 7 e 8)
**Entregável do módulo:** **relatório `.xlsx` automatizado** que lê o CSV limpo da aula 7,
gera três abas (Dados, Resumo, Histórico), guarda a versão anterior em backup com
carimbo de data/hora e registra no log o que foi gerado.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar por que **"gerar relatório" não é "copiar e colar"** — e por que o arquivo
   gerado por script é **reprodutível** enquanto o feito à mão não é.
2. Gerar um `.xlsx` com **`pandas.ExcelWriter`** e com **`openpyxl`** para quem precisa
   formatar células depois.
3. Criar **abas separadas**: `Dados` (tabela bruta), `Resumo` (indicadores agregados) e
   `Histórico` (linha a linha de cada execução).
4. Aplicar **formatação professional**: largura de coluna, número com 2 casas, cor de
   cabeçalho, congelar painel, autofiltro.
5. Implementar **backup do relatório anterior** antes de sobrescrever (regra da sala).
6. Garantir **idempotência**: rodar duas vezes com os mesmos dados gera o mesmo
   relatório, exceto pelo carimbo de tempo — e isso é documentado.
7. **Agendar** o relatório (o `cron` da aula 2 + o script Python da aula 3).
8. Escrever o **log de execução** no formato que já existe no Módulo 1.

**Objetivo secundário:** Perceber que o relatório que vai para a reunião pedagógica não
é só um número — ele é um **produto**, com dono, data de geração, origem dos dados e
uma aba que mostra o que ficou de fora.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `planilhaeletronicas/app.py` | Aplicação real **Flask + Pandas → Excel**: `pd.to_numeric(..., errors='coerce')`, `pd.ExcelWriter(output, engine='xlsxwriter')` com `BytesIO` e envio por e-mail — é o modelo do relatório |
| `planilhaeletronicas/templates/index.html` | Interface web real que dispara o relatório |
| `planilhaeletronicas/casosdeteste.py` | Casos de teste reais da aplicação de planilha |
| `planilhaeletronicas/casosdeuso` · `planilhaeletronicas/documentacao` | Documentação de requisitos e de comportamento esperado |
| `planilhaeletronicas/README.md` · `planilhaeletronicas/requirements.txt` | Como o projeto declara dependências (`pandas`, `xlsxwriter`) |
| `Analise-de-Dados/datasets/AdventureWorks.xlsx` | `.xlsx` real com várias abas — teste de leitura e de reescrita |
| `Analise-de-Dados/datasets/Aracaju.xlsx` · `Fortaleza.xlsx` · `Natal.xlsx` · `Recife.xlsx` · `Salvador.xlsx` | Mais 5 planilhas reais com formatos diferentes |
| `laboratorio-tech-social/site/exercicios/planilha.html` | Exercício interativo de planilha (navegador, sem instalar nada) |
| `laboratorio-tech-social/site/exercicios/gerador-dados.html` | Gerador de dados fictícios — a entrada do relatório |
| `laboratorio-tech-social/site/exercicios/visualizador-dados.html` | Visualizador de dados para conferir o resultado antes de formatar |
| `python-do-zero/10_arquivos/exercicio_05_csv.txt` | Exercício oficial de CSV da biblioteca padrão |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Relatório automatizado** | "O script roda; você só aperta o botão. O relatório não depende do seu humor às 18h de uma sexta." |
| **`pd.ExcelWriter`** | "O escritor é quem cria as abas. `to_excel(writer, sheet_name='...')` decide o nome de cada uma." |
| **`BytesIO`** | "Planilha em memória: você gera, valida e só depois grava no disco." |
| **`xlsxwriter`** | "Motor de escrita do `.xlsx` — rápido, com gráfico e formatação. `openpyxl` é o motor de leitura e de ajuste fino." |
| **Aba `Resumo`** | "Quem lê relatório não quer 300 linhas. Quer 8 números, e o resto escondido atrás do link." |
| **Aba `Histórico`** | "Toda execução deixa uma linha: data, arquivo de origem, quantidade de linhas, código de saída. É o log de negócio." |
| **Backup com carimbo** | "Antes de sobrescrever, copie com `nome_AAAAMMDD_HHMMSS.xlsx`. Sem carimbo, o backup é inútil." |
| **Idempotência** | "Rodar 2 vezes com o mesmo dado tem que dar o mesmo resultado. Se não dá, existe estado escondido." |
| **Autofiltro e congelar painel** | "Duas cliques que transformam uma tabela em um relatório usável por uma coordenação." |
| **Dado fictício** | "O relatório de demonstração usa `ALU0001`, não o nome do aluno. Ponto final." |
| **Reprodutibilidade** | "Se eu rodar de novo, com o mesmo comando, eu tenho que chegar no mesmo arquivo. Isso é o que separa script de trabalho manual." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** lista de chamada por apelido no quadro de presença. Regra do dia:
**câmera ligada** nesta fase e na Fase 5. Quem não pode, manda uma reação no chat.

**Gancho (3 min):** *"Levanta a mão quem já preencheu uma planilha de chamada, salvou como
'final_v2_corrigido' e mandou no grupo da equipe? Mão. Pois é. Hoje a gente faz a
planilha se gerar sozinha — e, mais importante, faz o **histórico**: cada vez que roda,
sobra um registro. Isso é o que separa 'eu fiz' de 'a equipe fez'."*

**Demonstração ao vivo (3 min):** mostre o `planilhaeletronicas/app.py` aberto no editor e
aponte a função `gerar_relatorio()`:

```python
def gerar_relatorio(data_dict):
    tabela_vendas = pd.DataFrame(data_dict)
    tabela_vendas['Quantidade'] = pd.to_numeric(tabela_vendas['Quantidade'], errors='coerce').fillna(0).astype(int)
    tabela_vendas['Valor Final'] = tabela_vendas['Quantidade'] * tabela_vendas['Valor Unitário']

    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        tabela_vendas.to_excel(writer, sheet_name='Vendas', index=False)
    output.seek(0)
    return output
```

**Fala do professor (texto exato):** *"Repare em três coisas. Um: `errors='coerce'` — o
que não é número vira vazio em vez de derrubar o relatório. Dois: o `ExcelWriter` com
`sheet_name` — cada aba tem nome. Três: `BytesIO` — o arquivo é montado em memória e só
vai para o disco no final. Se algo der errado no meio, o seu arquivo antigo continua
intacto. Isso se chama **falha segura**."*

> **Plano B:** sem Python instalado, o aluno abre
> `laboratorio-tech-social/site/exercicios/planilha.html` e
> `visualizador-dados.html` no navegador, gera o CSV fictício com `gerador-dados.html`
> e anota a estrutura de abas que vai implementar depois.

#### Fase 2 — Exploração (22 min)

**Parte 1 — As três portas de saída do Excel (7 min).**

| Biblioteca | Quando usar | Modo |
|---|---|---|
| `pandas.ExcelWriter` | Quando a prioridade é **dados** | Modo `write` |
| `openpyxl` | Quando a prioridade é **formatação** (célula, cor, largura) | Modo `write` + `edit` |
| `xlsxwriter` | Motor que o `pandas` usa por baixo com `engine='xlsxwriter'` | Modo `write` |

```python
from pathlib import Path

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


def caminho_de_backup(destino: Path) -> Path:
    """Monta o nome do backup com carimbo de data e hora (AAAAMMDD_HHMMSS)."""
    carimbo = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
    pasta = destino.parent / "backup"
    pasta.mkdir(parents=True, exist_ok=True)
    return pasta / f"{destino.stem}_{carimbo}{destino.suffix}"


def gerar_relatorio(entrada: Path, destino: Path) -> dict[str, object]:
    """Lê o CSV limpo, gera o .xlsx com 3 abas e devolve um resumo da execução."""
    if not entrada.exists():
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {entrada}")

    tabela = pd.read_csv(entrada, sep=";", encoding="utf-8-sig")

    resumo = (
        tabela.groupby("turma", dropna=False)
        .agg(
            presencas=("presente", lambda serie: (serie == "S").sum()),
            faltas=("presente", lambda serie: (serie == "N").sum()),
            registros=("presente", "size"),
        )
        .reset_index()
    )
    resumo["percentual_presenca"] = (
        resumo["presencas"] / resumo["registros"] * 100
    ).round(1)

    historico = pd.DataFrame(
        [
            {
                "gerado_em": pd.Timestamp.now().isoformat(timespec="seconds"),
                "origem": str(entrada),
                "linhas": len(tabela),
                "turmas": tabela["turma"].nunique(),
            }
        ]
    )

    destino.parent.mkdir(parents=True, exist_ok=True)
    backup = caminho_de_backup(destino)
    if destino.exists():
        destino.replace(backup)          # o antigo vira backup; o novo entra no lugar

    with pd.ExcelWriter(destino, engine="openpyxl") as escritor:
        tabela.to_excel(escritor, sheet_name="Dados", index=False)
        resumo.to_excel(escritor, sheet_name="Resumo", index=False)
        historico.to_excel(escritor, sheet_name="Histórico", index=False)

    return {
        "destino": str(destino),
        "backup": str(backup) if backup.exists() else None,
        "linhas": len(tabela),
        "abas": ["Dados", "Resumo", "Histórico"],
    }
```

> **Detalhe profissional:** `destino.replace(backup)` é **atômico** no mesmo disco — ou o
> arquivo antigo está lá, ou o novo está lá. Nunca os dois, nunca nenhum. É o mesmo
> princípio de "backup antes de operação destrutiva" que vale para o seu banco.

**Parte 2 — Formatação com `openpyxl` (8 min).**

```python
def formatar(destino: Path) -> None:
    """Aplica cabeçalho, larguras, formato de número e autofiltro."""
    livro = load_workbook(destino)
    for folha in livro.worksheets:
        folha.freeze_panes = "A2"                    # congela o cabeçalho
        folha.auto_filter.ref = folha.dimensions     # autofiltro no cabeçalho

        cabecalho = folha[1]
        for celula in cabecalho:
            celula.font = Font(bold=True, color="FFFFFF")
            celula.fill = PatternFill("solid", fgColor="2F5597")
            celula.alignment = Alignment(horizontal="center", vertical="center")

        for indice, coluna in enumerate(folha.iter_cols(), start=1):
            largura = max(len(str(celula.value or "")) for celula in coluna) + 2
            folha.column_dimensions[get_column_letter(indice)].width = min(largura, 50)

        if folha.title == "Resumo" and folha.max_row >= 2:
            coluna_percentual = folha.max_column
            for linha in range(2, folha.max_row + 1):
                folha.cell(row=linha, column=coluna_percentual).number_format = "0.0"

    livro.save(destino)
```

**Parte 3 — Onde o log entra (7 min).**

Reaproveite o padrão do Módulo 1 e grave **uma linha por execução**:

```python
from datetime import datetime
from pathlib import Path


def registrar_log(caminho_log: Path, resumo: dict[str, object]) -> None:
    """Grava uma linha de log por execução do relatório."""
    caminho_log.parent.mkdir(parents=True, exist_ok=True)
    carimbo = datetime.now().isoformat(timespec="seconds")
    linha = (
        f"{carimbo} OK destino={resumo['destino']} "
        f"linhas={resumo['linhas']} backup={resumo['backup']}\n"
    )
    with caminho_log.open("a", encoding="utf-8") as arquivo:
        arquivo.write(linha)
```

E o **script completo** que orquestra tudo:

```python
#!/usr/bin/env python3
"""relatorio.py — gera o relatório .xlsx da sua rotina.

Uso:
    python relatorio.py --entrada dados/chamada_limpa.csv --saida relatorios/relatorio.xlsx
    python relatorio.py --entrada dados/chamada_limpa.csv --dry-run
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from relatorio_modulo import formatar, gerar_relatorio, registrar_log


def main() -> int:
    analisador = argparse.ArgumentParser(description="Gera o relatório em Excel.")
    analisador.add_argument("--entrada", type=Path, required=True)
    analisador.add_argument("--saida", type=Path, default=Path("relatorios/relatorio.xlsx"))
    analisador.add_argument("--log", type=Path, default=Path("logs/relatorio.log"))
    analisador.add_argument("--dry-run", action="store_true")
    argumentos = analisador.parse_args()

    if argumentos.dry_run:
        print(f"[ENSAIO] ia ler {argumentos.entrada} e gravar {argumentos.saida}")
        print("[ENSAIO] NADA foi gravado.")
        return 0

    try:
        resumo = gerar_relatorio(argumentos.entrada, argumentos.saida)
        formatar(argumentos.saida)
    except FileNotFoundError as erro:
        print(f"ERRO: {erro}", file=sys.stderr)
        return 2
    except Exception as erro:                       # noqa: BLE001 - erro vira log, não traceback
        print(f"ERRO inesperado: {erro}", file=sys.stderr)
        return 1

    registrar_log(argumentos.log, resumo)
    print(json.dumps(resumo, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

> **Por que `--dry-run` vem antes de qualquer escrita?** Porque o Módulo 4 já te ensinou
> isso: quem roda em produção precisa poder **ver o que vai acontecer** antes de
> acontecer. O `--dry-run` responde "o que eu faria" sem tocar em nada. Em agenda
> (cron), rode **sempre** o `--dry-run` na primeira semana.

#### Fase 3 — Mão na massa (32 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. O professor circula com o
`gerador-dados.html` aberto para quem ainda não tem CSV.

**Atividade A — Pegar o CSV limpo (5 min).**
Pegue o `dados/chamada_limpa.csv` gerado na aula 7 (ou gere de novo com
`gerar_dados.py --linhas 300`). Confirme que ele tem **uma linha por presença** e que
as colunas são `turma`, `data`, `aluno_id`, `presente`.

**Atividade B — Montar o script (17 min).**
Crie `relatorio.py` com as **três funções** vistas na Fase 2, em arquivos separados para
ficar testável:

```
scripts/
├── relatorio_modulo.py      # gerar_relatorio, formatar, registrar_log
├── relatorio.py             # interface de linha de comando
└── restaurar.py             # volta o backup mais recente
```

```python
# scripts/restaurar.py — volta o backup mais recente do relatório
from pathlib import Path

import relatorio_modulo


def restaurar(destino: Path) -> Path | None:
    """Copia o backup mais recente de volta para o destino. Devolve o caminho usado."""
    backups = sorted(
        destino.parent.glob(f"backup/{destino.stem}_*{destino.suffix}"),
        reverse=True,
    )
    if not backups:
        return None
    escolhido = backups[0]
    escolhido.replace(destino)
    return escolhido


if __name__ == "__main__":
    alvo = Path("relatorios/relatorio.xlsx")
    usado = restaurar(alvo)
    print(f"Restaurado de {usado}" if usado else "Nenhum backup encontrado.")
```

**Atividade C — Rodar, conferir, formatar (10 min).**

```bash
# 1. Ensaio: nada é gravado
python scripts/relatorio.py --entrada dados/chamada_limpa.csv --dry-run

# 2. Execução real
python scripts/relatorio.py --entrada dados/chamada_limpa.csv --saida relatorios/relatorio.xlsx

# 3. Roda de novo — agora deve existir um backup
python scripts/relatorio.py --entrada dados/chamada_limpa.csv --saida relatorios/relatorio.xlsx

# 4. Vê o que existe
ls -1 relatorios/ relatorios/backup/

# 5. Confere o log
cat logs/relatorio.log
```

Abra o `.xlsx` no Excel ou no LibreOffice e confira, **uma por uma**:

- [ ] A aba `Dados` tem todas as linhas e todas as colunas
- [ ] A aba `Resumo` tem **uma linha por turma** e o percentual de presença
- [ ] A aba `Histórico` tem **uma linha por execução**
- [ ] O cabeçalho está em negrito, com cor e congelado
- [ ] O autofiltro funciona na aba `Dados`
- [ ] Existe **um backup** em `relatorios/backup/`
- [ ] O `logs/relatorio.log` tem **duas linhas** (as duas execuções)

> **Erro comum:** o aluno abre o `.xlsx`, edita uma célula "só para ajustar" e salva.
> Daí em diante o arquivo **não é mais reproduzível** — o script vai sobrescrever a
> mão dele. Isso se chama **dado manual em arquivo gerado**, e é o início de todo
> relatório que "só funciona na minha máquina". **Regra:** o `.xlsx` gerado é
> **descartável**. Se alguém editou, regere.

#### Fase 4 — Projeto (23 min)

**Desafio:** transformar o script em um **relatório de verdade** da sua rotina, com
**histórico acumulado** entre execuções.

**O que fazer:**

1. Escolha **uma** tarefa da sua lista: presença, notas, kits escolares, agenda.
2. Adapte as colunas do seu CSV real (sem dado sensível) para o gerador fictício.
3. Faça o script ler o **histórico anterior** e **acrescentar** a linha nova, em vez de
   sobrescrever a aba `Histórico`. Dica: leia o `.xlsx` antigo com
   `pd.read_excel(destino, sheet_name="Histórico")` e concatene com o novo.
4. Agende a execução (Módulo 2) **depois** de testar 3 vezes na mão.
5. Escreva um `RELATORIO.md` com: o que o relatório mostra, quem é o dono, de onde vêm
   os dados, com que frequência e o que **não** está no relatório.

**Critério de pronto:**
- [ ] Script roda com `--dry-run` **e** sem ele
- [ ] **3 abas** com os nomes exatos: `Dados`, `Resumo`, `Histórico`
- [ ] **Backup automático** do relatório anterior, com carimbo `AAAAMMDD_HHMMSS`
- [ ] Histórico **acumulado** entre 3 execuções
- [ ] Log de execução em arquivo, **uma linha por execução**
- [ ] Agendamento criado (`cron` ou `schtasks`)
- [ ] `RELATORIO.md` escrito, com dono e origem dos dados
- [ ] **Nenhum nome de pessoa real** nos dados
- [ ] Tudo comitado no Git, com mensagem `feat: relatório automatizado em Excel`

#### Fase 5 — Mostra (5 min)

**Câmera ligada.** Cada aluno mostra o `.xlsx` aberto e responde **uma** pergunta:

- "Quantas linhas tem o seu histórico?"
- "O que aconteceria se o disco encheu?"
- "Se eu rodar o script duas vezes com o mesmo CSV, o resultado muda?"

> **Pergunta de saída (no chat):** "O seu `.xlsx` foi editado à mão depois de gerado.
> O que você faz: apaga a edição, ou continua usando? Justifique em uma linha."

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Geração do `.xlsx` | Script cria o arquivo **sem erro** e sem intervenção manual |
| Abas | `Dados`, `Resumo` e `Histórico` presentes e **preenchidas** |
| Formatação | Cabeçalho com cor, painel congelado, autofiltro, largura de coluna |
| Backup | Relatório anterior **preservado** com carimbo de data/hora antes de sobrescrever |
| Idempotência | 2 execuções com o mesmo dado geram o **mesmo conteúdo** (fora o carimbo) |
| Log | Uma linha por execução, com destino, contagem de linhas e backup |
| `--dry-run` | Existe e **não grava nada** |
| Agendamento | Tarefa `cron`/`schtasks` criada e testada |
| Documentação | `RELATORIO.md` com dono, origem dos dados e o que fica de fora |
| Dados | **Somente identificadores** — nenhum nome de pessoa real |
| Git | Código, `requirements.txt` e documentação versionados |

**Pergunta de escrita:**
> "O seu relatório é gerado todo dia às 6h da manhã. Na quarta-feira, às 6h05, o
> coordinator pergunta no grupo: 'por que a Schools de hoje mostra só 40% de presença,
> sendo que ontem mostrava 92%?'. O seu script rodou sem erro (o log diz `OK`). O que
> aconteceu, e o que o seu relatório deveria ter mostrado para responder a essa
> pergunta sozinho?"
>
> **Resposta:** A causa mais provável **não é o script quebrar** — o log diz `OK`, e
> código de saída 0 é a prova de que o script rodou. As quatro hipóteses, em ordem de
> probabilidade:
> 1. **A entrada mudou.** O arquivo `dados/chamada_limpa.csv` foi regerado por outra
>    pessoa, com outro período (só a manhã, não o dia inteiro) ou com a coluna `presente`
>    recodificada (`P`/`F` em vez de `S`/`N`). O script não errou: ele leu um dado
>    diferente e fez a conta certinha sobre ele.
> 2. **O filtro de turma mudou.** Se o relatório agrega por turma e a Schools aparece
>    duas vezes com nomes parecidos, o agrupamento soma linhas de turmas diferentes.
> 3. **Backup restaurado errado.** Alguém rodou `restaurar.py` e pegou um backup de
>    março.
> 4. **Dados faltando.** As 6h da manhã, o sistema de origem ainda não tinha exportado
>    o dia anterior — e o CSV estava **vazio**. Script com entrada vazia gera relatório
>    vazio, com exit code 0. **Esse é o bug de verdade.**
>
> O que o relatório deveria ter mostrado para responder sozinho:
> - **Contagem de linhas por turma** na aba `Resumo` — se `Escola` veio com 12 linhas
>   em vez de 250, isso aparece.
> - **Período coberto** (`data_min` e `data_max` na aba `Resumo`) — se o período foi de
>   1 dia em vez de 30, isso aparece.
> - **Uma aba `Qualidade` (ou uma coluna na `Resumo`)** com a contagem de valores em
>   branco e de valores fora do conjunto esperado (`S`, `N`, `F`). 40% de presença
>   costuma ser **40% de valores em branco contados como falta** — não 40% de falta real.
> - **Validação de volume mínimo**: se o total de linhas for menor que um limiar
>   (por exemplo, 80% da média das últimas execuções), o script deve **avisar no log e
>   na planilha**, e idealmente **não gerar** o relatório — porque o número errado é
>   pior do que o número faltando.
>
> **A lição de fundo:** um relatório que só mostra o número final é um relatório que
> **pode estar errado sem ninguém perceber**. Reportar é mostrar o número **e** os
> dados que o produziram — volume, período, origem e exceções. É o que a regra da sala
> chama de "documentação é parte do trabalho".

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `planilhaeletronicas/app.py` | Flask + Pandas → Excel com `ExcelWriter`, `BytesIO` e `to_numeric` |
| `planilhaeletronicas/templates/index.html` | Interface web que dispara o relatório |
| `planilhaeletronicas/casosdeteste.py` | Casos de teste reais da aplicação |
| `planilhaeletronicas/casosdeuso` | Requisitos funcionais do sistema de planilhas |
| `planilhaeletronicas/documentacao` | Documentação de comportamento esperado |
| `planilhaeletronicas/README.md` | Como rodar o projeto e quais são as dependências |
| `Analise-de-Dados/datasets/AdventureWorks.xlsx` | Planilha real com múltiplas abas |
| `Analise-de-Dados/datasets/Aracaju.xlsx` | Planilha real com layout diferente |
| `Analise-de-Dados/datasets/Fortaleza.xlsx` | Planilha real com layout diferente |
| `Analise-de-Dados/datasets/Natal.xlsx` | Planilha real com layout diferente |
| `Analise-de-Dados/datasets/Recife.xlsx` | Planilha real com layout diferente |
| `Analise-de-Dados/datasets/Salvador.xlsx` | Planilha real com layout diferente |
| `laboratorio-tech-social/site/exercicios/planilha.html` | Exercício interativo de planilha |
| `laboratorio-tech-social/site/exercicios/gerador-dados.html` | Gerador de dados fictícios |
| `laboratorio-tech-social/site/exercicios/visualizador-dados.html` | Visualizador de dados |
| `python-do-zero/10_arquivos/exercicio_05_csv.txt` | Exercício oficial de CSV |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Rode o `relatorio.py` com o CSV da sua rotina **3 vezes** e confirme que o
   histórico acumula e que os backups aparecem.
2. Escreva **2 testes** que automatizem a sua verificação:
   - `teste_gerar_relatorio_cria_arquivo` — o `.xlsx` existe depois da execução;
   - `teste_backup_guarda_anterior` — o conteúdo do relatório anterior está no backup.
3. Escreva o `RELATORIO.md` (dono, origem, periodicidade, o que não está no relatório).
4. Crie o agendamento (`cron` ou `schtasks`) e **não** o deixe rodando sozinho ainda:
   rode **à mão** 2 vezes na semana para conferir.
5. (Opcional) Adicione uma aba `Qualidade` com contagem de valores em branco e fora do
   conjunto esperado — é o que responde à pergunta do coordinator.

> **Na aula 9** o seu script vai para produção — e produção significa **segurança**.
> Vamos escrever a política de dados e o modelo de ameaça do seu projeto.

---

### 🔗 Próximo módulo

[Módulo 9 — Segurança Digital e LGPD (parte 1): OWASP e modelo de ameaça · Aula 9](#m09)

<a id="m09"></a>

## Módulo 9 — Segurança Digital e LGPD (parte 1): OWASP e modelo de ameaça (Aula 9)

**Duração:** 90 min · **Aula 9 de 16** · **P9** (módulo em 2 aulas: 9 e 10)
**Entregável do módulo:** **política de dados do projeto** (1 página) + **modelo de
ameaça de 1 página** com as 6 perguntas respondidas, os riscos priorizados e os
controles implementados.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Diferenciar **ameaça**, **vulnerabilidade** e **risco** — e escrever isso sem
   confundir os três termos (quem confunde, planeja o controle errado).
2. Ler a **OWASP Top 10** e reconhecer 5 dela em código e planilha do dia a dia.
3. Explicar a **tríade CIA** (confidencialidade, integridade, disponibilidade) com
   exemplo do próprio setor público.
4. Dizer o que a **LGPD** exige de quem trata dado pessoal: base legal, finalidade,
   minimização, transparência, segurança e descarte.
5. Classificar um dado como **pessoal**, **pessoal sensível** ou **não pessoal** — e
   entender que a resposta muda tudo no tratamento.
6. Construir um **modelo de ameaça** respondendo 6 perguntas: o que eu protejo, contra
   quem, por qual ponto de entrada, o que pode dar errado, qual o impacto e o que eu
   já faço.
7. Aplicar **controles reais** já existentes em projetos da cidade: **RLS** (controle de
   acesso por linha), **secrets via variável de ambiente**, **RLS + `admin_users`**.
8. Escrever a **política de dados** do seu projeto: o que entra, o que não entra,
   onde fica, quem acessa e quando é apagado.

**Objetivo secundário:** Entender que **"é só uma planilha"** é a frase que antecede
quase todo vazamento de dado no serviço público.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `esporte-sao-pedro/SUPABASE_SECURITY_SETUP.md` | Setup real de segurança com **custo zero**: criar usuário admin, aplicar RLS, bloquear cadastro público, deixar o portal público em leitura |
| `esporte-sao-pedro/supabase-rls-admin.sql` | RLS em SQL puro: `create table admin_users`, `enable row level security`, `create policy ... using (auth.uid() = user_id)` |
| `laboratorio-tech-social/docs/seguranca-criancas.md` | Regras reais de proteção de menores: **nunca compartilhar dados de alunos**, consentimento dos responsáveis, ECA/LGPD, canal oficial de denúncia |
| `manual-qa-completo/docs/11/scripts/secret_scan.py` | Scanner de segredos (SAST leve): regex para `AKIA…`, chave privada e `password=` |
| `manual-qa-completo/docs/10/PT/checklist_aceite.md` | Checklist de aceite para revisar a política antes de aprovar |
| `manual-qa-completo/docs/10/PT/charter_template.md` | Carta de QA: escopo, papéis, responsabilidades — modelo de política |
| `QualityHub/Documentação (Docs)/Testes de Segurança.md` | Tipos de teste de segurança (o que se testa e por quê) |
| `QualityHub/Documentação (Docs)/Tipos de Testes de Software.md` | Panorama dos tipos de teste, incluindo segurança |
| `pensamento_computacional/13_ciberseguranca` | Módulo de segurança do material de pensamento computacional |
| `ia-para-iniciantes/12_ia_e_etica/exercicio_03_privacidade.txt` | Exercício de privacidade e IA |
| `ia-para-iniciantes/12_ia_e_etica/exercicio_05_regulamentacao.txt` | Exercício de regulação e IA |
| `laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` | Quiz de cibersegurança no navegador (revisão rápida) |
| `laboratorio-tech-social/site/exercicios/validador-regex.html` | Validador de regex no navegador — usado para montar a regra de CPF/e-mail |
| `qa-exercicios-praticos/simulacoes` · `qa-exercicios-praticos/tecnicas-de-teste` | Simulações e técnicas de teste para a parte prática |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Ameaça** | "Quem pode machucar. O hacker, o colega curioso, o erro do operador." |
| **Vulnerabilidade** | "A fresta por onde a ameaça entra. Pasta aberta, senha fraca, script sem backup." |
| **Risco** | "Vulnerabilidade × impacto. É o que a gente prioriza." |
| **OWASP Top 10** | "As 10 falhas que mais aparecem no mundo real. Não é theory: é estatística." |
| **Tríade CIA** | "Confidencialidade (ninguém vê), integridade (ninguém mexe), disponibilidade (funciona quando precisa)." |
| **Dado pessoal** | "Ligado a uma pessoa identificável. Nome, CPF, matrícula, IP, crachá." |
| **Dado pessoal sensível** | "Origem racial, saúde, religião, biometria, opinião política. Aqui a LGPD aperta." |
| **Base legal** | "Por que você pode tratar. Necesidade pública, execução de contrato, consentimento, obrigação legal." |
| **Minimização** | "Colete o mínimo. Se a planilha não precisa do CPF, não peça o CPF." |
| **Finalidade** | "Para quê coletou. Se o uso muda, é nova finalidade — e precisa de nova base legal." |
| **RLS (Row Level Security)** | "Controle de acesso por **linha**, no banco. O usuário só vê o que é dele — mesmo com senha certa." |
| **Modelo de ameaça** | "Antes de proteger, escreva **o que você protege** e **contra quem**." |
| **Controle** | "A medida concreta: `.gitignore`, RLS, variável de ambiente, backup, log." |
| **Engenharia social** | "O ataque mais barato é convince a pessoa a entregar a senha. Não é hacking: é conversa." |
| **Descarte** | "O fim do ciclo também é sua responsabilidade. Dado que não serve mais, se apaga." |
| **ANPD** | "Autoridade Nacional de Proteção de Dados. Guias oficiais, gratuitos, em português." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** lista de chamada por apelido. **Câmera ligada** nesta fase e na
Fase 5. Quem preferir, responde no chat com a reação 👍.

**Gancho (3 min):** *"Me diz uma coisa: a planilha de chamada da sua unidade, no seu
computador, tem nome completo de aluno? Claro que tem. E o seu e-mail? Tem a lista dos
alunos anexada? Provavelmente sim, pelo menos uma vez. Agora a pergunta: se esse
computador for roubado, ou se você compartilhar a pasta com um colega de outra
escola 'só para dar uma olhada', o que acontece? Nada? Não. Hoje a gente escreve a
política do projeto e pensa nos riscos de verdade — não em medo, em **método**."*

**Demonstração ao vivo (3 min):** abra o `esporte-sao-pedro/SUPABASE_SECURITY_SETUP.md`
e mostre o bloco de criação do admin:

```sql
alter table public.admin_users enable row level security;

drop policy if exists "Admin users can read own row" on public.admin_users;
create policy "Admin users can read own row"
on public.admin_users
for select
to authenticated
using (auth.uid() = user_id);
```

**Fala do professor (texto exato):** *"Isso aqui diz, em português: 'o usuário só lê a
própria linha'. Não é o programa que esconde o dado — é o **banco** que recusa a linha.
Isso se chama **controle de acesso no nível da linha**, e é a diferença entre 'o
sistema tem senha' e 'o sistema tem **regra**'. Vamos aplicar a mesma lógica aos
nossos scripts."*

> **Plano B:** sem terminal, o aluno abre
> `laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` e responde às
> perguntas; a resposta anota as 6 perguntas do modelo de ameaça.

#### Fase 2 — Exploração (22 min)

**Parte 1 — OWASP Top 10 traduzida para a sua rotina (8 min).**

| OWASP (versão resumida) | Como aparece na sua rotina |
|---|---|
| **Controle de acesso quebrado** | "`permissao == 'admin'` testado no cliente. A pessoa troca a URL e vira admin." |
| **Falha de criptografia** | Arquivo `.xlsx` com CPF e nota em uma pasta compartilhada sem senha. |
| **Injeção** | `SELECT * FROM alunos WHERE nome = '` + o que o usuário digitou. O `;` no fim quebra a consulta. |
| **Design inseguro** | Script que **apaga** a planilha antes de gerar a nova, sem backup. |
| **Configuração errada** | `app.secret_key = 'supersecretkey'` fixo no código (exatamente o que existe em `planilhaeletronicas/app.py`). |
| **Componente vulnerável** | Biblioteca instalada sem atualizar, com falha de segurança conhecida. |
| **Falha de identificação** | Senha `123456` compartilhada por 5 pessoas na mesma unidade. |
| **Falha de integridade de dados** | Relatório gerado, editado à mão e assinado — ninguém sabe se os dados são os reais. |
| **Falha de log e monitoramento** | Script rodou, deu erro às 3h e **ninguém soube** porque o log não existe. |
| **SSRF** | Script que baixa "planilha" de uma URL que o usuário mandou — e a URL aponta para a rede interna. |

**Parte 2 — Tríade CIA aplicada ao setor público (6 min).**

| Princípio | Pergunta | Exemplo em São Pedro |
|---|---|---|
| **Confidencialidade** | "Quem pode ver?" | Lista de alunos com notas: só a equipe da própria unidade. |
| **Integridade** | "Alguém pode alterar sem deixar rastro?" | A nota digitada no sistema e o `.xlsx` da reunião divergem. |
| **Disponibilidade** | "Funciona quando é preciso?" | A planilha de presença trava no dia da reunião. |

> **A tríade é um triângulo de Tensões, não um interruptor.** Se você deixa o arquivo
> aberto na rede da Secretaria para facilitar o acesso de todo mundo, você quebrou a
> confidencialidade. Se você deixa trancado em uma máquina só, quebrou a disponibilidade.
> **Toda decisão de segurança é um trade-off, e o trade-off precisa estar escrito.**

**Parte 3 — LGPD em 60 segundos (8 min).**

| Conceito da LGPD | O que significa na prática |
|---|---|
| **Dado pessoal** | Toda informação ligada a pessoa identificável |
| **Controlador** | Quem decide **por que** e **para que** os dados são tratados (a Secretaria) |
| **Operador** | Quem trata em nome do controlador (o fornecedor, o script, a plataforma) |
| **Base legal** | A permissão que justifica o tratamento |
| **Finalidade** | O objetivo declarado — e só ele |
| **Minimização** | Coletar o mínimo necessário para a finalidade |
| **Segurança** | Medidas técnicas e administrativas para proteger |
| **Incidente** | Vazamento ou acesso indevido — **comunicação à ANPD** quando houver risco |

**Os 5 erros que a turma mais comete:**

1. Coletar **mais** do que precisa (CPF, endereço, telefone de tudo).
2. Usar o dado para **outro fim** ("como não tenho mais professor, usei a lista para
   avisar sobre a reunião").
3. Compartilhar com **quem não precisa**.
4. **Não ter** base legal escrita.
5. **Guardar para sempre**, sem descarte.

> Fonte oficial: [ANPD](https://www.gov.br/anpd/). Leia o guia de tratamento de dados
> pessoais antes de usar dado real em qualquer projeto.

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. Cada sala monta o modelo de ameaça **do
mesmo projeto**, em uma folha (papel ou documento compartilhado).

**Atividade A — Inventário de dados (8 min).**
Liste **todas** as entidades que o seu projeto toca. Para cada uma, preencha:

| Entidade | Campos | Dado pessoal? | Sensível? | Onde fica | Quem acessa |
|---|---|---|---|---|---|
| Registro de presença | `aluno_id`, `data`, `presente` | Sim (via `aluno_id`) | Não | `dados/chamada_limpa.csv` | Professor da unidade |
| Cadastro de docente | nome, CPF, e-mail, unidade | Sim | Sim (CPF) | Sistema da Secretaria | RH e gestão |

> **Regra da sala:** se o identificador `ALU0001` consegue voltar ao nome da pessoa,
> **é dado pessoal**. Anonimizar de verdade é caro; reduzir o identificador já ajuda.

**Atividade B — As 6 perguntas do modelo de ameaça (12 min).**

Escreva no seu documento, respondendo em uma frase cada:

1. **O que eu preciso proteger?** (o relatório, a lista, o código, a credencial)
2. **De quem?** (aluno, colleague, fornecedor, hacker, erro próprio)
3. **Por onde entra?** (upload de arquivo, e-mail, link, terminal, USB)
4. **O que pode dar errado?** (vazamento, exclusão, alteração, indisponibilidade)
5. **Qual o impacto?** (o que quebra para a pessoa e para o serviço)
6. **O que eu já faço?** (o controle que já existe — `.gitignore`, senha, backup, log)

Exemplo preenchido:

| # | Pergunta | Resposta do exemplo |
|---|---|---|
| 1 | O que proteger? | O relatório mensal de presença e o código que o gera |
| 2 | De quem? | De colega de outra unidade e de erro de envio de e-mail |
| 3 | Por onde entra? | Pelo `.xlsx` anexado a e-mail e pelo terminal |
| 4 | O que dá errado? | O relatório sai para destinatário errado e a planilha antiga é sobrescrita |
| 5 | Qual o impacto? | Dado de aluno de uma unidade exposto a terceiros; perda de histórico |
| 6 | O que já faço? | Backup com carimbo, `.gitignore` com `dados/`, identificadores no lugar de nomes |

**Atividade C — Teste de ameaça com o scanner real (10 min).**
Rode o scanner de segredos do repositório contra o **seu** projeto. Copie o script
`manual-qa-completo/docs/11/scripts/secret_scan.py` para a sua pasta `scripts/` e
escreva o verificador:

```python
#!/usr/bin/env python3
"""verificar_segredos.py — procura segredos óbvios nos arquivos do projeto.

Uso: python scripts/verificar_segredos.py
Saída: código 0 (nada encontrado) ou 1 (segredo encontrado).
"""

from __future__ import annotations

import sys
from pathlib import Path

from secret_scan import scan

PASTAS_IGNORADAS = {".git", ".venv", "__pycache__", "logs", "backup", "node_modules"}
EXTENSOES = {".py", ".txt", ".md", ".cfg", ".ini", ".toml", ".yaml", ".yml", ".json", ".env"}


def arquivos_candidatos(raiz: Path) -> list[Path]:
    """Devolve os arquivos de texto que vale a pena varrer."""
    achados: list[Path] = []
    for caminho in raiz.rglob("*"):
        if not caminho.is_file():
            continue
        if any(parte in PASTAS_IGNORADAS for parte in caminho.parts):
            continue
        if caminho.suffix.lower() not in EXTENSOES:
            continue
        achados.append(caminho)
    return achados


def main() -> int:
    raiz = Path(".")
    total = 0
    for caminho in arquivos_candidatos(raiz):
        try:
            conteudo = caminho.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for nome, trecho in scan(conteudo):
            total += 1
            print(f"[{nome}] {caminho}: {trecho}")
    if total:
        print(f"\n{total} segredo(s) encontrado(s). Não comite isso.")
        return 1
    print("Nenhum segredo encontrado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

```bash
# Instale o scanner oficial do manual de QA
cp "manual-qa-completo/docs/11/scripts/secret_scan.py" scripts/

# Rode no seu projeto
python scripts/verificar_segredos.py

# Teste de propósito: crie um arquivo com uma senha e veja o scanner achar
printf 'password="supersecret123"\n' > /tmp/teste_segredo.txt
python -c "from secret_scan import scan; print(scan(open('/tmp/teste_segredo.txt').read()))"
```

> **Detalhe profissional:** o `secret_scan.py` real usa três regex: `AKIA[0-9A-Z]{16}`
> (chave AWS), `-----BEGIN .*PRIVATE KEY-----` (chave privada) e
> `password\s*=\s*['\"]?[^\s'\"]{6,}` (senha em código). Ele **não** é um produto
> pronto — é uma base. O seu scanner é o **seu**: eu ensinei o padrão, você escreve o
> seu com as suas regras.

#### Fase 4 — Projeto (25 min)

**Desafio:** escrever a **política de dados** e o **modelo de ameaça** do seu projeto
final ("Automação Real da Minha Rotina"), em **duas páginas**, e **publicar no
repositório** do projeto.

**Modelo da política de dados** (cabeçalhos prontos):

```markdown
# Política de Dados — <nome do projeto>

## 1. Finalidade
Este projeto existe para <finalidade>. Nenhum uso fora deste está autorizado.

## 2. Dados tratados
| Dado | Tipo | Pessoal? | Sensível? | Base legal | Onde fica | Prazo |
|---|---|---|---|---|---|---|
| aluno_id | identificador | Sim (vinculável) | Não | Necessidade pública (LIE) | dados/*.csv | 5 anos |

## 3. Quem pode acessar
| Papel | Pode ler | Pode escrever | Como é identificado |
|---|---|---|---|
| Professor da unidade | Sim | Sim | Conta individual do SGA |

## 4. Onde os dados ficam
- Caminho local: ...
- Backup: ... (frequência, retenção)
- Fora da máquina: **nunca**, exceto ...

## 5. O que NÃO entra no projeto
- Nome completo, CPF, endereço, telefone, foto
- Dado de menor sem autorização do responsável
- Dado real sem autorização formal

## 6. Descarte
Quando o prazo termina, o arquivo é apagado de forma segura (criptografia de disco
ou exclusão definitiva do diretório sincronizado).

## 7. Incidente
Se houver suspeita de acesso indevido: <quem avisar> em <prazo>. Registrar na aba de
incidentes do projeto.

## 8. Responsável
Nome, cargo, data, assinatura.
```

**Critério de pronto:**
- [ ] Política de dados com **8 seções**, no repositório
- [ ] Tabela de dados com **classificação** e **base legal** de cada um
- [ ] Seção explícita de **"o que NÃO entra"**
- [ ] Plano de **descarte** com prazo
- [ ] Modelo de ameaça com as **6 perguntas** respondidas
- [ ] **3 riscos** priorizados por probabilidade × impacto
- [ ] Para cada risco: o **controle** que já existe ou o que será implementado
- [ ] `verificar_segredos.py` rodando no repositório, **encontrando 0 segredos**
- [ ] `secret_scan.py` **versionado** no projeto (é código seu agora)
- [ ] Tudo comitado no Git

#### Fase 5 — Mostra (5 min)

**Câmera ligada.** Cada aluno lê em voz alta **uma** linha da sua política que ele não
tinha pensado antes — normalmente a linha de descarte ou a de base legal.

> **Pergunta de saída (no chat):** "Seu script roda no seu notebook. O notebook é
> roubado na hora do almoço. Duas respostas: qual é o pior que acontece, e o que você
> mudaria **hoje** (não no futuro ideal)?"

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Política de dados | 8 seções preenchidas, com responsável e data |
| Classificação | Cada dado classificado como pessoal, sensível ou não pessoal |
| Base legal | Preenchida **por dado**, não genérica |
| Minimização | Lista explícita do que **não** entra no projeto |
| Descarte | Prazo definido e método de descarte escrito |
| Modelo de ameaça | As 6 perguntas respondidas com frase, não com "não se aplica" |
| Priorização | 3 riscos com probabilidade, impacto e prioridade explícita |
| Controles | Cada risco tem pelo menos **1 controle** (`.gitignore`, RLS, log, backup, senha de variável de ambiente) |
| Scanner | `verificar_segredos.py` roda e devolve **0** no repositório |
| Segredos | Nenhuma chave, senha ou `.env` no histórico do Git |
| LGPD | Mínima: minimização e descarte presentes |
| Git | Política e modelo de ameaça versionados |

**Pergunta de escrita:**
> "Você é o responsável pela automação da lista de entrega de kits escolares da
> Secretaria. A planilha que você automatiza tem: nome do aluno, turma, endereço e
> data de retirada do kit. Um colega do outro setor, que você conhece e gosta, pede:
> 'me manda essa planilha que eu preciso comparar com a minha'. Você pode mandar? O que
> você responde, e o que você muda no projeto para que essa pergunta nem precise ser
> feita?"
>
> **Resposta:** **Não**, você não pode mandar — e o motivo não é o colega, é o
> **princípio**:
> 1. **Minimização.** A planilha precisa de `turma` e `data_retirada` para conferir a
>    baixa do kit. `nome` e `endereço` são dados pessoais **sem finalidade** nesse
>    processo. A planilha do projeto **não deve conter** nome nem endereço — e, se
>    contiver, você tem um problema de coleta que precisa ser corrigido na origem.
> 2. **Finalidade.** O dado do aluno foi coletado para **registrar a retirada do kit**.
>    Usar a mesma base para uma comparação de outro setor é **outra finalidade**.
>    Isso exige base legal própria e, na prática, o consentimento/autorização que
>    você não tem.
> 3. **Canal e registro.** Mesmo que o pedido fosse legítimo, "me manda por WhatsApp"
>    é o oposto de rastreabilidade. A transferência tem que ser por **canal oficial**,
>    com **registro** de quem pediu, por quê e quem autorizou.
>
> O que responder ao colega, na prática:
> > "Não consigo te mandar essa planilha — ela tem dados de aluno e a finalidade dela
> > é a conferência de retirada do kit. O que eu posso fazer é te passar o **relatório
> > agregado** por turma, sem identificação de aluno, e te dizer a data do corte. Se o
> > seu setor precisar de dado individual, o pedido precisa vir por escrito para a
> > gestão da Secretaria, que evaluate a base legal — eu não libero isso por WhatsApp."
>
> E o que mudar no projeto:
> - **Remover** nome e endereço do gerador e do `.gitignore` do dado pessoal.
> - Gerar **dois artefatos**: o **operacional** (com `aluno_id`, só para a baixa) e o
>   **agregado** (por turma e por dia, para quem pede comparação).
> - Escrever na **política de dados** a seção "quem pode acessar" com **papéis** e não
>   com nomes.
> - Registrar o pedido e a resposta no log de acesso.
>
> **A lição de fundo:** a pergunta "posso mandar?" é a pergunta errada. A pergunta certa
> é "**para que** eu coletei isso, e **quem mais** precisa?" Se a resposta da segunda é
> "ninguém além do processo", o dado não deveria estar com você desde o começo.
> **Minimização é o controle mais barato e mais eficiente que existe.**

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `esporte-sao-pedro/SUPABASE_SECURITY_SETUP.md` | Setup real de segurança com custo zero |
| `esporte-sao-pedro/supabase-rls-admin.sql` | RLS em SQL: `admin_users` e política por `auth.uid()` |
| `laboratorio-tech-social/docs/seguranca-criancas.md` | Regras de proteção de menores (LGPD/ECA) |
| `manual-qa-completo/docs/11/scripts/secret_scan.py` | Scanner de segredos com regex para AWS, chave privada e senha |
| `manual-qa-completo/docs/10/PT/checklist_aceite.md` | Checklist de aceite para revisar a política |
| `manual-qa-completo/docs/10/PT/charter_template.md` | Carta de QA (escopo, papéis, responsabilidades) |
| `QualityHub/Documentação (Docs)/Testes de Segurança.md` | Tipos de teste de segurança |
| `QualityHub/Documentação (Docs)/Tipos de Testes de Software.md` | Panorama dos tipos de teste |
| `pensamento_computacional/13_ciberseguranca` | Módulo de segurança do material de pensamento computacional |
| `ia-para-iniciantes/12_ia_e_etica/exercicio_03_privacidade.txt` | Exercício de privacidade e IA |
| `ia-para-iniciantes/12_ia_e_etica/exercicio_05_regulamentacao.txt` | Exercício de regulação e IA |
| `laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` | Quiz de cibersegurança |
| `laboratorio-tech-social/site/exercicios/validador-regex.html` | Validador de regex no navegador |
| `qa-exercicios-praticos/simulacoes` | Simulações de falha para treinar resposta |
| `qa-exercicios-praticos/tecnicas-de-teste` | Técnicas de teste |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Escreva a **política de dados** completa do seu projeto e comite no repositório.
2. Escreva o **modelo de ameaça** com as 6 perguntas e **3 riscos priorizados**.
3. Copie o `secret_scan.py` para o seu projeto e rode `verificar_segredos.py`.
4. **Plante um segredo de mentira** num arquivo e confirme que o scanner acha —
   depois apague o arquivo e confirme que o scanner volta a dizer 0.
5. Configure o `.gitignore` para **nunca** versionar: `dados/`, `logs/`, `backup/`,
   `.env`, `*.xlsx` com dado real.
6. (Opcional) Escreva o `INCIDENTES.md` — o registro zerado de onde você vai anotar
   qualquer suspeita de acesso indevido.

> **Na aula 10** vamos **automatizar** essa verificação: o scanner vira pipeline, a
> política vira checklist que reprova, e você assina o que passou.

---

### 🔗 Próximo módulo

[Módulo 10 — Segurança Digital e LGPD (parte 2): scanner de segredos e checklist · Aula 10](#m10)

<a id="m10"></a>

## Módulo 10 — Segurança Digital e LGPD (parte 2): scanner de segredos e checklist (Aula 10)

**Duração:** 90 min · **Aula 10 de 16** · **P10** (módulo em 2 aulas: 9 e 10)
**Entregável do módulo:** **scanner de segredos rodando no repositório** (script próprio,
com as suas regras) + **checklist de LGPD assinado** + `INCIDENTES.md` criado.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar o que é **segredo** (credencial, chave, token, senha) e por que ele **nunca**
   entra no repositório — nem agora, nem no histórico do Git.
2. Reconhecer os 5 formatos de segredo que mais vazam: chave AWS, chave privada, senha
   em código, token de API e string de conexão de banco.
3. **Automatizar** a verificação: transformar a política do módulo 9 em um script que
   roda e **reprova** o commit.
4. Limpar um segredo que **já foi commitado** — e entender por que trocar a senha é
   obrigatório, mesmo depois de apagar o arquivo.
5. Aplicar o **checklist de LGPD** de 10 itens ao próprio projeto e assinar o que passou.
6. Registrar um **incidente** (real ou simulado) no formato certo: o que aconteceu,
   quando, impacto, contenção e prevenção.
7. Ligar o scanner ao **GitHub Actions**, de forma que todo `push` seja verificado.
8. Entender que segurança não é produto que se compra: é **rotina** que se mantém.

**Objetivo secundário:** Perceber que o maior risco não é o hacker distante — é o
`print(config)` esquecido no código e o `.env` anexado no grupo da equipe.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `manual-qa-completo/docs/11/scripts/secret_scan.py` | Scanner de referência com 3 regex: `AKIA[0-9A-Z]{16}`, chave privada e `password=` |
| `manual-qa-completo/docs/11/` | Módulo completo de segurança: OWASP Top 10, secret scan, boas práticas |
| `manual-qa-completo/docs/10/PT/checklist_aceite.md` | Modelo de checklist de aceite — base do checklist de LGPD |
| `manual-qa-completo/docs/10/PT/glossario.md` | Glossário PT/EN para padronizar os termos do time |
| `esporte-sao-pedro/SUPABASE_SECURITY_SETUP.md` | Segurança real com **custo zero**: RLS, usuário admin, cadastro público bloqueado |
| `esporte-sao-pedro/supabase-rls-admin.sql` | Exemplo real de política de acesso por linha em SQL |
| `laboratorio-tech-social/docs/seguranca-criancas.md` | Regras de proteção de menores: consentimento, canal oficial, denúncia |
| `git-github-iniciantes/12_ci_cd_basico` | Como ligar um script a um workflow do GitHub Actions |
| `git-github-iniciantes/03_trabalhando_com_mudancas` | `diff`, `stash` e `restore` — usados ao remover um segredo do projeto |
| `qa-exercicios-praticos/modelos-templates/checklist-smoke-e-aceite.md` | Checklist de fumaça e aceite para a revisão final |
| `laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` | Quiz de revisão (10 min, no navegador) |
| `ia-para-iniciantes/12_ia_e_etica` | Exercícios de privacidade e regulamentação aplicada |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Segredo** | "Tudo que dá acesso a algo e não pode ser lido por terceiro: senha, chave, token." |
| **Secret scanning** | "Um script que varre o repositório procurando o que não deveria estar lá." |
| **Falso positivo** | "O scanner acha, mas não é segredo. Toda regra precisa de exceção documentada." |
| **`.gitignore`** | "A lista do que o Git deve fingir que não existe. Coloque `.env` na primeira linha." |
| **Variável de ambiente** | "O lugar certo do segredo: fora do código, dentro da máquina ou do CI." |
| **Histórico do Git** | "Arquivo apagado continua no histórico. Por isso a senha **tem** de ser trocada." |
| **Quality gate** | "Um portão que reprova. Pipeline vermelho não vai para produção." |
| **Incidente** | "Aconteceu. Agora é registrar, conter, avisar e corrigir — nessa ordem." |
| **LGPD — segurança** | "Medidas técnicas e administrativas. Não é só criptografia: é processo." |
| **Menor privilégio** | "Dê o mínimo de acesso necessário para a tarefa. Nada de admin para todo mundo." |
| **Checklist assinado** | "Quem assina, responde. O checklist vira prova de diligência." |
| **Rotação de credencial** | "Trocar a senha periodicamente e sempre que houver suspeita." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** chamada por apelido. Reação 👍 no chat para confirmar presença.

**Gancho (3 min):** *"Semana passada a gente escreveu a política de dados. Hoje a gente
faz ela acontecer — porque política no papel não protege ninguém. E vou começar com uma
pergunta desconfortável: quantos de vocês já colaram uma senha num arquivo `.txt` e
depois apagaram? Apagar não resolve. O arquivo pode estar no backup, no e-mail, no
histórico do Git. A boa notícia: dá para descobrir isso em segundos, com um script. E
é isso que a gente vai construir hoje."*

**Demonstração ao vivo (3 min):** rode o scanner de referência contra uma pasta com
um segredo plantado:

```bash
# cria um arquivo de teste com um segredo de mentira
printf 'password="senha123456"\n' > /tmp/teste_segredo.txt

# roda o scanner do repositório
python -c "from secret_scan import scan; print(scan(open('/tmp/teste_segredo.txt').read()))"
```

**Fala do professor (texto exato):** *"Olhem o que ele devolveu: o nome da regra e o
trecho. Ele não sabe o que é o arquivo — ele só compara com padrões. Um scanner de
segredos não é inteligência artificial: é uma lista de formatos conhecidos. E é
justamente por ser simples que ele funciona. Hoje vocês vão escrever o de vocês."*

> **Plano B:** sem internet, abra o `secret_scan.py` no editor e leia as 3 regex em voz
> alta com a turma. A aula continua no papel: cada aluno desenha a regra que criaria.

#### Fase 2 — Exploração (22 min)

**Parte 1 — Os 5 segredos que mais vazam (7 min).**

| Tipo | Formato típico | Onde costuma aparecer |
|---|---|---|
| **Chave AWS** | `AKIA` + 16 caracteres maiúsculos | Script de upload de arquivo para a nuvem |
| **Chave privada** | `-----BEGIN ... PRIVATE KEY-----` | Certificado, acesso SSH |
| **Senha em código** | `password = "..."` · `senha = "..."` | `app.py` de teste, exemplo do tutorial |
| **Token de API** | `ghp_...`, `sk-...`, `xoxb-...` | Integração com GitHub, IA, Slack |
| **String de conexão** | `postgres://usuario:senha@host/banco` | Backend, script de banco de dados |

> **Regra de ouro:** se o segredo está no arquivo, ele **vazou no momento em que o
> arquivo saiu do seu computador**. Não existe "só eu tenho acesso" quando o arquivo
> está num repositório, num e-mail ou num grupo.

**Parte 2 — Por que apagar não resolve (7 min).**

Mostre ao vivo (sem dado real) como o histórico guarda tudo:

```bash
# Um arquivo com segredo é commitado...
printf 'TOKEN=abc123\n' > .env
git add .env && git commit -m "config"
git rm --cached .env && git commit -m "remove .env"

# ...e continua recuperável no histórico
git log --all --oneline -- .env
git show HEAD~1:.env
```

**Fala do professor:** *"Vejam: eu apaguei, commitei a remoção, e o arquivo continua
aqui. O Git é um histórico — ele não esquece. Por isso, quando um segredo vaza: 1)
troca a credencial; 2) só depois limpa o histórico. A troca é o que resolve. A limpeza
é higiene."*

**Parte 3 — O checklist de LGPD em 10 itens (8 min).**

| # | Item | Como verificar |
|---|---|---|
| 1 | Sei **por que** trato cada dado (finalidade) | A política de dados do módulo 9 responde |
| 2 | Tenho **base legal** para cada dado | Necessidade pública, obrigação legal, consentimento... |
| 3 | Coleto **só o mínimo** | Se não uso o CPF, não peço o CPF |
| 4 | Sei **quem** pode acessar | Tabela de papéis com "pode ler / pode escrever" |
| 5 | Sei **onde** o dado fica | Caminho local, backup, nuvem |
| 6 | Tenho **backup** com retenção definida | Script de backup com carimbo de data |
| 7 | Tenho **descarte** definido | O que apagar, quando e como |
| 8 | Nenhum **segredo** no repositório | Scanner verde |
| 9 | Tenho **plano de incidente** | `INCIDENTES.md` com contato e prazo |
| 10 | **Revisei** tudo nos últimos 6 meses | Data da última revisão na política |

> O checklist vira um arquivo `LGPD-CHECKLIST.md` no repositório. Cada item marcado
> recebe a data e o nome de quem verificou. **Assinatura é compromisso, não decoração.**

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. Cada aluno trabalha no próprio projeto;
a sala compara resultados.

**Atividade A — Escrever o scanner próprio (15 min).**
Copie o `secret_scan.py` para `scripts/` e crie o seu `verificar_segredos.py` com
**as suas** regras. Comece pelas 3 do repositório e acrescente uma regra sua (por
exemplo, o padrão de token da plataforma que você usa).

```python
# scripts/verificar_segredos.py — estratégia:
# 1. listar arquivos de texto do projeto (ignorando .git, .venv, backup, logs)
# 2. para cada arquivo, aplicar as regras
# 3. imprimir [regra] arquivo: trecho
# 4. código de saída 1 se achou algo, 0 se está limpo

REGRAS = {
    "aws_key":       r"AKIA[0-9A-Z]{16}",
    "private_key":   r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "senha_em_codigo": r"(?i)(senha|password)\s*=\s*['\"][^'\"]{6,}['\"]",
    "token_github":  r"ghp_[A-Za-z0-9]{20,}",
    "token_ia":      r"sk-[A-Za-z0-9]{20,}",
}
```

**Atividade B — Rodar o scanner e corrigir (8 min).**

```bash
python scripts/verificar_segredos.py
# saída esperada quando está limpo:
# Nenhum segredo encontrado.
echo $?          # deve devolver 0
```

Se achou algo: **troque a credencial primeiro**, depois apague o arquivo, adicione ao
`.gitignore` e commite a remoção.

**Atividade C — Checklist assinado (7 min).**
Preencha o `LGPD-CHECKLIST.md`, item por item, com data e nome (apelido serve). Item
que não se aplica recebe "N/A — motivo". Item que falha vira tarefa no backlog.

**Fala do professor durante a circulação:** *"Não tente deixar perfeito. Tente deixar
**verificável**. Um checklist com 6 itens marcados e 4 em branco vale mais que um
checklist de 10 itens todos marcados sem conferir."*

> **Plano B:** sem Python instalado, o aluno faz a versão em papel: lista os 5 formatos e
> procura manualmente nos arquivos do projeto, anotando o que encontrou.

#### Fase 4 — Projeto (25 min)

**Desafio:** deixar o projeto final **"pronto para auditoria"** — o que significa:

- [ ] `scripts/verificar_segredos.py` rodando e devolvendo `0`
- [ ] `.gitignore` com `.env`, `dados/`, `logs/`, `backup/`
- [ ] `LGPD-CHECKLIST.md` preenchido e assinado
- [ ] `POLITICA-DE-DADOS.md` (do módulo 9) linkado no README
- [ ] `INCIDENTES.md` criado (pode estar vazio, mas com o modelo)
- [ ] workflow do GitHub Actions chamando o scanner em cada `push`

**Modelo do `INCIDENTES.md`:**

```markdown
# Registro de Incidentes — <projeto>

## Modelo (copie para cada incidente)
- **Data/hora:**
- **O que aconteceu:**
- **Dado afetado:**
- **Pessoas afetadas:**
- **Como foi descoberto:**
- **Contenção (o que fiz agora):**
- **Prevenção (o que muda para não repetir):**
- **Quem avisei e quando:**

## Incidentes registrados
<!-- nenhum até o momento -->
```

**Modelo do workflow (`.github/workflows/seguranca.yml`):**

```yaml
name: Verificação de segurança
on: [push, pull_request]
jobs:
  segredos:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python scripts/verificar_segredos.py
```

**Critério de pronto:** o pipeline fica **vermelho** quando você planta um segredo de
teste e **verde** quando remove. Se não fica vermelho, o scanner não está ligado.

#### Fase 5 — Mostra (5 min)

- 2 alunos mostram o scanner rodando: um com o projeto limpo, outro plantando um
  segredo de propósito para ver o pipeline reprovar.
- 1 aluno lê um item do checklist que **não** conseguiu marcar e por quê. (Aprender com
  o que falta vale mais que exibir o que sobrou.)

**Pergunta de saída (oral):** *"Se eu apagar o `.env` e commitar, o segredo está seguro?
Por quê?"*

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Scanner próprio | Roda sem erro, acha o segredo plantado e devolve código 1 |
| `.gitignore` | Contém `.env`, `dados/`, `logs/`, `backup/` e pelo menos 1 regra própria |
| Checklist de LGPD | 10 itens preenchidos, com data e nome; os que falham estão no backlog |
| `INCIDENTES.md` | Existe e tem o modelo completo |
| Pipeline | Fica vermelho com segredo e verde sem segredo |
| Pergunta de saída | Explica que a troca da credencial é o que resolve |

**Pergunta de escrita:**
> "Um colega commitou uma senha do banco no repositório público e apagou o arquivo 5
> minutos depois. Ele disse: 'já resolvi, apaguei'. O que você responde?"
> **Resposta:** Que **não está resolvido**. O arquivo continua no histórico do Git (e
> possivelmente em forks, caches e no e-mail de notificação). O segredo deve ser
> considerado **vazado**: a primeira ação é **trocar a senha** no banco; depois vem a
> limpeza do histórico, o `.gitignore` e o scanner no CI. Apagar o arquivo é o começo,
> não o fim.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `manual-qa-completo/docs/11/scripts/secret_scan.py` | Ler o scanner de referência linha a linha |
| `manual-qa-completo/docs/11/` | OWASP Top 10 e segurança aplicada |
| `manual-qa-completo/docs/10/PT/checklist_aceite.md` | Adaptar o checklist de aceite para segurança |
| `esporte-sao-pedro/supabase-rls-admin.sql` | Ler a política de RLS de um projeto real da cidade |
| `laboratorio-tech-social/site/exercicios/quiz-ciberseguranca.html` | Revisão em quiz |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Plante **três segredos** de formatos diferentes e confirme que o scanner acha os três.
2. **Adicione uma regra sua** ao scanner (um formato que você usa no trabalho) e
   documente no README por que ela existe.
3. Corrija **um vazamento real ou simulado** do seu projeto: troque a credencial, limpe,
   commite e registre no `INCIDENTES.md` (mesmo que seja um exercício).
4. Rode o checklist de LGPD no projeto de um colega e escreva **duas sugestões** para ele.

> **Na aula 11** a gente entra em IA — e a primeira regra é a mesma desta aula: **nada de
> segredo no prompt, nada de dado real na conversa.**

---

### 🔗 Próximo módulo

[Módulo 11 — IA no Trabalho (parte 1): prompt versionado — Aula 11](#m11)

---

<a id="m11"></a>

## Módulo 11 — IA no Trabalho (parte 1): prompt versionado com critério de aceite (Aula 11)

**Duração:** 90 min · **Aula 11 de 16** · **P11** (módulo em 2 aulas: 11 e 12)
**Entregável do módulo:** **prompt versionado** (arquivo `.md` no repositório) com
**critério de aceite** escrito e **3 testes de saída** registrados.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Explicar o que um modelo de linguagem **faz bem** e o que ele **não faz** — sem
   mito de um lado nem desprezo do outro.
2. Escrever um prompt com as 6 partes: **papel, tarefa, contexto, formato, restrições e
   exemplos**.
3. Definir um **critério de aceite** para a saída: o que torna a resposta "boa o
   suficiente para usar".
4. Criar **3 testes de saída** com entradas diferentes e comparar o resultado com o
   critério.
5. Versionar o prompt no Git, com **histórico e motivo da mudança**.
6. Reconhecer **alucinação** e **viés** em uma resposta, e saber o que fazer.
7. Aplicar a regra de privacidade: **nada de dado real** no prompt.
8. Usar IA para **acelerar o trabalho repetitivo** — e não para terceirizar o julgamento.

**Objetivo secundário:** Entender que o prompt é **código**: se não tem versão, teste e
critério, não está pronto para uso em trabalho.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `ia-para-iniciantes/06_prompt_engeneering` | Módulo de prompt engineering: estrutura, exemplos e exercícios |
| `ia-para-iniciantes/07_ias_assistentes` | Panorama das IAs assistentes e quando usar cada uma |
| `ia-para-iniciantes/08_geracao_texto` | Geração de texto: forças e limites |
| `ia-para-iniciantes/12_ia_e_etica` | Ética, viés, privacidade e regulamentação |
| `ia-para-iniciantes/13_ia_no_cotidiano` | Casos de uso reais no dia a dia |
| `ia-para-iniciantes/10_api_de_ia` | Como chamar uma IA por código (prévia da aula 12) |
| `ia-para-iniciantes/02_machine_learning` | Para quem quiser entender o que está por baixo |
| `agente_qaIA/GUIA_PROMPTS_QA_AGENT.md` | Prompts reais de QA usados por um agente |
| `agente_qaIA/README.md` | Arquitetura de um agente de IA que atua como QA sênior |
| `hubias-estudos` | Exemplo de app que organiza IAs, prompts e estudo |
| `Central-de-noticias/scripts/gerar.py` | Uso real de IA para resumir notícias (leitura crítica) |
| `laboratorio-tech-social/site/exercicios/flashcards.html` | Fixação por cartões (revisão do vocabulário) |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Modelo de linguagem** | "Prevê o próximo trecho provável. Não consulta a verdade: consulta o padrão." |
| **Prompt** | "A instrução. Quanto mais clara, menos o modelo adivinha." |
| **As 6 partes** | "Papel, tarefa, contexto, formato, restrições, exemplos." |
| **Critério de aceite** | "O que a resposta precisa ter para eu poder usar. Escrito **antes** de gerar." |
| **Alucinação** | "Resposta confiante e errada. Ninguém te avisa — por isso se testa." |
| **Viés** | "O padrão dos dados entra na resposta. Se os dados excluem, a resposta exclui." |
| **Contexto** | "O que o modelo precisa saber para responder. Se não estiver no prompt, ele inventa." |
| **Few-shot** | "Mostrar 2 ou 3 exemplos do que você quer. Vale mais que 10 linhas de adjetivo." |
| **Temperatura** | "O quanto a resposta varia. Baixa para tarefa objetiva, alta para brainstorm." |
| **Prompt versionado** | "Prompt é código: `prompts/resumo-v3.md`, com histórico e motivo." |
| **Revisão humana** | "O modelo responde; a responsabilidade é sua. Sempre." |
| **Dado no prompt** | "O que você cola, sai da sua posse. Nada de dado real, de aluno, de paciente." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** chamada por apelido. Câmera nas fases 1 e 5.

**Gancho (3 min):** *"Vou fazer uma pergunta e quero resposta sincera no chat: quem aqui
já pediu para a IA 'escrever um relatório' e recebeu um texto bonito, genérico e
inútil? Todo mundo. Hoje a gente aprende por que isso acontece — e como escrever um
prompt que entrega algo que dá para **usar**, não para **admirar**."*

**Demonstração ao vivo (3 min):** peça duas vezes a mesma tarefa, com prompts
diferentes:

```text
Prompt ruim:
"Escreva um relatório sobre presença escolar."

Prompt bom:
"Você é assistente administrativo de uma escola municipal.
Tarefa: escrever um resumo de 1 parágrafo sobre a frequência do 5º ano em setembro.
Contexto: 32 alunos; 30 presentes em média; 2 alunos faltaram 5 dias seguidos.
Formato: 1 parágrafo, no máximo 80 palavras, tom formal, sem opinião.
Restrições: não invente nome de aluno; não sugira punição.
Exemplo de tom: 'A frequência do 5º ano em setembro foi de 93,8%...'"
```

**Fala do professor:** *"O primeiro pede ao modelo que **adivinhe** o que eu quero. O
segundo **diz**. A diferença não é a IA: é o prompt. E tem uma coisa que o prompt bom
faz e o ruim não faz: ele me obriga a decidir, antes, **o que é uma boa resposta**.
Isso se chama critério de aceite — e é a próxima coisa que vocês vão escrever."*

> **Plano B:** sem acesso à IA, a turma analisa os dois prompts no papel e escreve, em
> duplas, qual produziria a resposta mais útil e por quê.

#### Fase 2 — Exploração (22 min)

**Parte 1 — As 6 partes do prompt (8 min).**

| Parte | Pergunta que responde | Exemplo |
|---|---|---|
| **Papel** | Quem o modelo deve ser? | "Você é analista de dados da Secretaria de Educação." |
| **Tarefa** | O que ele deve fazer? | "Resumir a tabela de frequência em 3 achados." |
| **Contexto** | O que ele precisa saber? | "Dados de setembro, 5º ano, 32 alunos." |
| **Formato** | Como a saída deve aparecer? | "3 bullets, no máximo 20 palavras cada." |
| **Restrições** | O que ele **não** pode fazer? | "Não invente números; não cite nome de aluno." |
| **Exemplos** | Como é uma resposta boa? | 1 ou 2 exemplos curtos do tom desejado |

> **Regra:** se falta uma das 6, o modelo preenche com o palpite dele. E o palpite dele
> é a média da internet — que raramente é o que você precisa.

**Parte 2 — Critério de aceite (7 min).**

Critério de aceite é uma **lista curta e verificável**. Não é "boa qualidade": é
"tem 3 bullets", "cada bullet cita um número da tabela", "não usa nome próprio",
"tem no máximo 60 palavras".

| Ruim (não verificável) | Bom (verificável) |
|---|---|
| "Texto claro e objetivo" | "Máximo 80 palavras; tom formal; 1 parágrafo" |
| "Sem erros" | "Todos os números batem com a tabela de entrada" |
| "Útil para o professor" | "Diz **o que fazer** em 1 frase no fim" |

**Parte 3 — Alucinação e viés (7 min).**

Mostre um exemplo de alucinação (o modelo inventa uma lei, uma estatística, um nome) e
pergunte: *"Como você descobre que isso é falso?"* Respostas esperadas: conferir na
fonte oficial, pedir a citação, comparar com o documento.

**Fala do professor:** *"A IA não mente porque quer. Ela completa o padrão. Se o padrão
mais provável é uma resposta plausível, ela entrega plausível — mesmo que seja falsa. O
seu trabalho não é confiar: é **verificar**. E verificar é o que a gente já sabe fazer,
porque é QA."*

> **Dado real nunca entra no prompt.** Use dados fictícios ou anonimizados. Cole no
> chat só o que você colocaria num mural da sala.

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. Cada aluno escreve o prompt do **seu**
projeto final.

**Atividade A — Escrever o prompt com as 6 partes (12 min).**
Crie `prompts/<tarefa>-v1.md` no seu repositório:

```markdown
# Prompt: resumo de frequência mensal
Versão: 1 · Data: 2026-10-22 · Autor: <apelido>

## Papel
Você é assistente administrativo de uma escola municipal de São Pedro/SP.

## Tarefa
Resumir a tabela de frequência do mês em 3 achados.

## Contexto
<tabela fictícia com 5 linhas>

## Formato
3 bullets, no máximo 20 palavras cada, tom formal.

## Restrições
- Não invente números.
- Não cite nome de aluno.
- Se um dado faltar, escreva "dado ausente".

## Exemplos
- "A turma A teve 95% de presença em setembro."
- "Dois alunos faltaram 5 dias seguidos; recomenda-se contato com a família."

## Critério de aceite
- [ ] Exatamente 3 bullets
- [ ] Cada bullet cita um número da tabela
- [ ] Nenhum nome próprio
- [ ] Termina com 1 recomendação prática
```

**Atividade B — Rodar os 3 testes de saída (10 min).**
Escolha 3 entradas diferentes: uma normal, uma com dado faltando e uma com número
estranho. Para cada uma, registre no arquivo:

```markdown
## Testes de saída
| # | Entrada | Resultado | Passou? |
|---|---|---|---|
| 1 | tabela completa | 3 bullets, números certos | ✅ |
| 2 | uma célula vazia | escreveu "dado ausente" | ✅ |
| 3 | total maior que o número de alunos | não percebeu a inconsistência | ❌ |
```

**Atividade C — Corrigir o prompt (8 min).**
Para cada teste que falhou, ajuste **uma** parte do prompt (restrição, exemplo,
formato). Suba como `v2` e registre o motivo da mudança no cabeçalho.

**Fala do professor durante a circulação:** *"Se o teste 3 falhou, o problema não é a
IA: é o seu prompt, que não disse o que fazer com dado inconsistente. Acrescente a
regra. Prompt é código — e código se corrige com teste."*

> **Plano B:** sem IA, o aluno escreve o prompt e o critério de aceite, e um colega faz o
> papel do modelo, respondendo de forma literal. O exercício de clareza fica ainda melhor.

#### Fase 4 — Projeto (25 min)

**Desafio:** entregar o **pacote de prompt do projeto final** — a versão pronta para o
módulo 12 (automação com revisão humana):

- [ ] `prompts/<tarefa>-v1.md` com as 6 partes
- [ ] **Critério de aceite** em checklist `- [ ]`
- [ ] **3 testes de saída** preenchidos, com pelo menos 1 falha registrada e corrigida
- [ ] **Changelog do prompt** (o que mudou de v1 para v2 e por quê)
- [ ] Seção "Privacidade": o que **nunca** vai no prompt
- [ ] Campanha de exemplo com **dados fictícios** (nunca reais)

**Modelo do changelog:**

```markdown
## Changelog
| Versão | Data | Mudança | Motivo |
|---|---|---|---|
| v1 | 2026-10-22 | versão inicial | — |
| v2 | 2026-10-22 | adicionada regra "dado inconsistente → avisar" | teste 3 falhou |
```

**Critério de pronto:** outra pessoa da turma consegue ler o seu prompt e **reproduzir**
a mesma resposta com o mesmo critério. Se não consegue, falta contexto.

#### Fase 5 — Mostra (5 min)

- 2 alunos leem o **prompt v1 e v2** lado a lado e mostram a diferença na saída.
- 1 aluno conta um caso de **alucinação** que encontrou e como descobriu.
- A turma vota: qual prompt da sala é o mais **reprodutível**?

**Pergunta de saída (oral):** *"Qual a diferença entre 'prompt bom' e 'prompt bonito'?"*

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Prompt versionado | Tem as 6 partes e está no Git com histórico |
| Critério de aceite | Itens verificáveis, escritos **antes** de gerar |
| 3 testes de saída | Tabela preenchida; falha identificada e corrigida |
| Changelog | Motivo da mudança registrado |
| Privacidade | Seção "o que nunca vai no prompt" presente |
| Pergunta de saída | Distingue "bonito" de "reprodutível" |

**Pergunta de escrita:**
> "Um colega colou a planilha real de notas dos alunos num chat de IA para 'pedir uma
> análise'. Qual é o problema e o que ele deveria fazer?"
> **Resposta:** O problema é **privacidade/LGPD**: dado pessoal de menor foi enviado a
> um serviço externo sem base legal nem consentimento, e pode ser retido pelo provedor.
> Ele deveria usar **dados fictícios ou anonimizados** (trocar nomes por códigos,
> arredondar ou remover identificadores) e, se precisar de análise real, usar uma
> ferramenta aprovada pela instituição, com contrato e política de retenção. A IA pode
> ajudar — mas não com dado que não pode sair da escola.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `ia-para-iniciantes/06_prompt_engeneering` | Estrutura de prompt e exercícios com critérios de avaliação |
| `ia-para-iniciantes/12_ia_e_etica` | Viés, privacidade, regulamentação |
| `ia-para-iniciantes/08_geracao_texto` | Limites da geração de texto |
| `agente_qaIA/GUIA_PROMPTS_QA_AGENT.md` | Prompts reais de QA para comparar com o seu |
| `laboratorio-tech-social/site/exercicios/flashcards.html` | Revisão do vocabulário de IA |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Escreva **2 prompts** para tarefas reais da sua rotina (um de texto, um de análise
   de tabela) com as 6 partes e critério de aceite.
2. Rode **3 testes de saída** em cada um e registre no arquivo.
3. Escolha **um** prompt e escreva a `v2` corrigindo o que os testes revelaram.
4. Escreva a seção "Privacidade: o que nunca vai no prompt" para o seu projeto.

> **Na aula 12** a gente liga o prompt ao código: automação com IA, **revisão humana
> obrigatória** e registro de uso.

---

### 🔗 Próximo módulo

[Módulo 12 — IA no Trabalho (parte 2): automação com revisão humana — Aula 12](#m12)

---

<a id="m12"></a>

## Módulo 12 — IA no Trabalho (parte 2): automação com revisão humana (Aula 12)

**Duração:** 90 min · **Aula 12 de 16** · **P12** (módulo em 2 aulas: 11 e 12)
**Entregável do módulo:** **automação com IA rodando**, com **revisão humana
obrigatória** e **registro de uso** (log de cada execução) + documento de limites.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Chamar um modelo de IA **por código** (API) ou por ferramenta de automação, sem medo.
2. Estruturar o fluxo **entrada → prompt → saída → revisão → aprovação → registro**.
3. Implementar um **portão de revisão humana**: a saída não é usada sem aprovação.
4. Registrar **cada execução** em log: quando, com qual prompt, com qual entrada, com
   qual resultado e quem aprovou.
5. Definir **limites** claros: o que a automação pode decidir sozinha e o que **nunca**
   pode (decisão que afeta pessoa, dado sensível, comunicação oficial).
6. Calcular **custo e tempo** por execução (tokens, chamadas, minutos).
7. Tratar **falha da IA** com graça: timeout, resposta vazia, resposta fora do formato.
8. Entregar o "manual de uso" da automação para outra pessoa rodar sem você.

**Objetivo secundário:** Compreender que **"a IA fez" não é desculpa**. Quem aperta o
botão responde pelo resultado.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `ia-para-iniciantes/10_api_de_ia` | Como chamar uma API de IA por código, com exemplos |
| `ia-para-iniciantes/11_ia_em_python` | IA em Python: chamadas, tratamento de erro, JSON |
| `ia-para-iniciantes/14_projeto_chatbot` | Projeto completo de chatbot (referência de fluxo) |
| `ia-para-iniciantes/15_projeto_analise_dados` | IA aplicada a análise de dados |
| `ia-para-iniciantes/06_prompt_engeneering` | O prompt versionado do módulo 11 |
| `agente_qaIA/` | Agente real de QA: `main.py`, `core/`, `config/`, `tests/` |
| `agente_qaIA/opencode_mcp_server.py` | Integração com ferramentas via MCP (leitura) |
| `agente_qaIA/.env.example` | Modelo de variável de ambiente — segredo fora do código |
| `Central-de-noticias/scripts/gerar.py` | Pipeline real de IA para resumo de notícias |
| `Central-de-noticias/.github/workflows/update-news.yml` | Automação agendada em produção |
| `manual-qa-completo/docs/10/PT/bug_report_template.md` | Como registrar a falha da automação |
| `QA_RUN/index.html` | Jogos de revisão (Deploy Simulator, Log Watch) |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **API** | "A porta do serviço. Você manda um pedido, recebe uma resposta." |
| **Chave de API** | "O segredo que identifica você. Vai no `.env`, **nunca** no código." |
| **Fluxo com revisão** | "Entrada → prompt → saída → **pessoa aprova** → uso. Sem aprovação, não usa." |
| **Human-in-the-loop** | "A pessoa no meio do fluxo. Não é atraso: é o controle." |
| **Log de uso** | "Quem rodou, quando, com qual prompt, com qual entrada, aprovado por quem." |
| **Limite de decisão** | "O que a automação pode fazer sozinha e o que **jamais** pode." |
| **Timeout** | "O tempo máximo de espera. Sem timeout, o script trava para sempre." |
| **Fallback** | "O plano B quando a IA falha: mensagem clara e tarefa para a pessoa." |
| **Custo por execução** | "Tokens × preço + tempo. Automação que gasta demais não escala." |
| **Idempotência** | "Rodar duas vezes dá o mesmo resultado. Evita duplicar registro." |
| **Registro de aprovação** | "Assinatura digital ou nome + data no log. Prova de que alguém viu." |
| **Manual de uso** | "Se outra pessoa não consegue rodar sem você, a automação não está pronta." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** chamada por apelido.

**Gancho (3 min):** *"Na semana passada a gente escreveu o prompt. Hoje a gente liga ele
no piloto automático — mas com um freio. Porque tem uma diferença entre 'a IA escreveu
o resumo' e 'a IA escreveu o resumo, alguém leu, aprovou e assinou'. A primeira é
automação. A segunda é automação **profissional**. E é a segunda que sobrevive a uma
auditoria."*

**Demonstração ao vivo (3 min):** mostre o log de uma execução real (fictícia):

```text
[2026-10-22 14:03:11] prompt=resumo-v2 entrada=chamada_set.csv saida=resumo.txt
[2026-10-22 14:03:11] status=AGUARDANDO_REVISAO
[2026-10-22 14:31:07] aprovado_por=maria.silva decisao=APROVADO obs="números conferidos"
[2026-10-22 14:31:08] publicado=relatorio_setembro.pdf
```

**Fala do professor:** *"Reparem na linha do meio: AGUARDANDO_REVISAO. O script não
publicou sozinho. Ele parou e esperou uma pessoa. Esse é o freio. Sem ele, um erro de
prompt vira um relatório oficial errado — e ninguém sabe de onde veio."*

> **Plano B:** sem internet, o aluno desenha o fluxo em papel (caixas e setas) e escreve
> o log à mão para uma execução fictícia.

#### Fase 2 — Exploração (22 min)

**Parte 1 — O fluxo profissional (8 min).**

```text
┌─────────┐   ┌────────┐   ┌────────┐   ┌──────────┐   ┌──────────┐   ┌────────┐
│ Entrada │ → │ Prompt │ → │  IA    │ → │ Revisão  │ → │ Aprovação│ → │Registro│
│ (dados) │   │version.│   │ (API)  │   │ humana   │   │ (nome)   │   │ (log)  │
└─────────┘   └────────┘   └────────┘   └──────────┘   └──────────┘   └────────┘
                                   │
                                   └── falha → mensagem clara → tarefa manual
```

Cada caixa tem uma responsabilidade. Se a "Revisão humana" não existe, o fluxo é
**incompleto** — não importa quão bom seja o prompt.

**Parte 2 — O que a automação nunca decide sozinha (7 min).**

| Pode automatizar | **Nunca** automatizar sem aprovação |
|---|---|
| Resumir um texto | Comunicar algo oficial em nome da instituição |
| Classificar e-mail por assunto | Decidir nota, aprovação ou punição de pessoa |
| Extrair dados de um PDF | Tratar dado sensível (saúde, biometria) |
| Gerar rascunho de relatório | Publicar em canal público |
| Sugerir resposta | Deletar dado definitivamente |
| Traduzir um trecho | Tomar decisão jurídica ou financeira |

> **Regra:** se a saída afeta **uma pessoa**, tem que ter **uma pessoa** no meio.

**Parte 3 — Log e custo (7 min).**

| Campo do log | Por que existe |
|---|---|
| Data/hora | Saber quando aconteceu |
| Versão do prompt | Reproduzir o resultado |
| Hash da entrada | Provar qual dado entrou |
| Saída (ou hash) | Provar o que saiu |
| Status | Aguardando / aprovado / rejeitado |
| Quem aprovou | Responsabilidade |
| Custo (tokens) | Controle de gasto |
| Duração | Controle de tempo |

**Fala do professor:** *"Log não é para desconfiar de você: é para você conseguir
**provar** o que fez. No dia em que alguém perguntar 'de onde veio esse número?', o log
é a resposta em 5 segundos."*

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos.

**Atividade A — Ligar o prompt ao código (15 min).**
Use o exemplo do `ia-para-iniciantes/10_api_de_ia` como base. Estrutura mínima:

```python
# scripts/resumo_com_revisao.py
import json, os, time
from datetime import datetime
from pathlib import Path

PROMPT = Path("prompts/resumo-v2.md").read_text(encoding="utf-8")
LOG = Path("logs/uso_ia.jsonl")

def chamar_ia(entrada: str) -> str:
    """Chamada real à API (ou simulada, para a aula)."""
    # a chave vem do ambiente, NUNCA do código
    chave = os.environ.get("IA_API_KEY")
    if not chave:
        raise RuntimeError("Configure IA_API_KEY no ambiente.")
    # ... chamada real aqui ...
    return "[saída simulada para a aula]"

def registrar(entrada_hash, saida, status, aprovado_por="—", custo=0):
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "quando": datetime.now().isoformat(timespec="seconds"),
            "prompt": "resumo-v2",
            "entrada": entrada_hash,
            "saida": saida[:200],
            "status": status,
            "aprovado_por": aprovado_por,
            "custo_tokens": custo,
        }, ensure_ascii=False) + "\n")
```

**Atividade B — Implementar o portão de revisão (10 min).**
O script **grava a saída e para**. Quem aprova é uma pessoa, por comando:

```bash
python scripts/resumo_com_revisao.py dados/chamada.csv
# → status=AGUARDANDO_REVISAO; arquivo saidas/resumo_pendente.md criado

# a pessoa revisa, abre o arquivo, confere e aprova:
python scripts/aprovar.py saidas/resumo_pendente.md --por "maria.silva"
# → status=APROVADO; aprovado_por=maria.silva
```

**Atividade C — Testar falha e custo (5 min).**
Simule os 3 problemas e veja o comportamento:

| Problema | O que o script deve fazer |
|---|---|
| Sem `IA_API_KEY` | Mensagem clara, código de saída 1, **não** usa fallback silencioso |
| Timeout | Tenta de novo 1 vez; se falhar, registra e pede revisão manual |
| Resposta vazia | Registra o fato e marca como `REVISAO_MANUAL` |

**Fala do professor:** *"Automação boa não é a que nunca falha. É a que falha de forma
**previsível** e **avisa**."*

> **Plano B:** sem API, o script usa uma função `chamar_ia` que devolve a saída de um
> arquivo `.txt`. O fluxo, o log e o portão de revisão funcionam igual.

#### Fase 4 — Projeto (25 min)

**Desafio:** entregar a **automação com IA do projeto final**, pronta para uso por outra
pessoa. Critérios:

- [ ] Fluxo com as 6 caixas (entrada, prompt, IA, revisão, aprovação, registro)
- [ ] Prompt versionado (do módulo 11), carregado de arquivo — não digitado no código
- [ ] Chave no `.env` / variável de ambiente, nunca no código
- [ ] Portão de revisão: **sem aprovação, não publica**
- [ ] Log em `logs/uso_ia.jsonl` com os 8 campos
- [ ] Tratamento de 3 falhas (chave, timeout, resposta vazia)
- [ ] Documento `LIMITES-DA-AUTOMACAO.md` (o que pode e o que nunca pode)
- [ ] `MANUAL-DE-USO.md` (como outra pessoa roda)
- [ ] Estimativa de custo por execução (tokens × preço + tempo)

**Modelo do `LIMITES-DA-AUTOMACAO.md`:**

```markdown
# Limites da Automação — <projeto>

## A automação PODE, sem aprovação
- <lista>

## A automação NUNCA faz sem aprovação humana
- <lista>

## O que a automação NUNCA faz, em hipótese alguma
- Enviar comunicação oficial
- Decidir sobre pessoa
- Tratar dado sensível
- Apagar dado definitivamente

## Quem aprova
| Papel | Nome | Como aprova |
|---|---|---|
| Gestor | <nome> | comando `aprovar.py --por` |
```

**Critério de pronto:** você entrega o repositório e uma pessoa que **nunca viu o
projeto** consegue rodar a automação seguindo só o `MANUAL-DE-USO.md`.

#### Fase 5 — Mostra (5 min)

- 1 aluno roda a automação ao vivo e mostra o **status AGUARDANDO_REVISAO**.
- 1 aluno aprova e mostra o log completo, com o nome de quem aprovou.
- A turma discute: qual limite do projeto do colega vocês **aumentariam** e qual
  **diminuiriam**?

**Pergunta de saída (oral):** *"Por que a aprovação humana precisa estar no log, e não
só no combinado verbal?"*

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Fluxo | As 6 etapas existem e estão encadeadas |
| Portão de revisão | Sem aprovação, a saída não é publicada |
| Log | 8 campos, uma linha por execução |
| Tratamento de falhas | 3 falhas tratadas com mensagem clara |
| Custo | Estimativa por execução documentada |
| Manual de uso | Outra pessoa roda sem ajuda |
| Limites | Documento com "pode", "nunca sem aprovação" e "nunca" |
| Pergunta de saída | Explica que o log é a prova de responsabilidade |

**Pergunta de escrita:**
> "O script gera um relatório de frequência e publica automaticamente na pasta
> compartilhada. Um dia, a IA troca dois números. Ninguém revisou. Quem é responsável?"
> **Resposta:** A responsabilidade é de **quem projetou e de quem aprovou o fluxo** —
> não da IA. O sistema foi desenhado **sem portão de revisão**, o que é uma falha de
> projeto. A correção é: (1) inserir a etapa de revisão humana obrigatória; (2) registrar
> aprovação no log; (3) adicionar um teste que confira os totais contra a fonte;
> (4) assumir e comunicar o erro conforme o `INCIDENTES.md`. "A IA errou" não transfere
> responsabilidade.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `ia-para-iniciantes/10_api_de_ia` | Chamada de API passo a passo |
| `ia-para-iniciantes/11_ia_em_python` | IA em Python com tratamento de erro |
| `ia-para-iniciantes/14_projeto_chatbot` | Fluxo completo de um chatbot |
| `agente_qaIA/README.md` | Arquitetura de um agente com revisão |
| `Central-de-noticias/scripts/gerar.py` | Pipeline real de IA agendada |
| `QA_RUN/index.html` | Jogos Deploy Simulator e Log Watch |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Rode a automação **3 vezes** com entradas diferentes e guarde o log das 3.
2. Escreva o `MANUAL-DE-USO.md` e peça para **alguém de fora** seguir. Anote onde travou.
3. Calcule o **custo** de 1 execução e estime o custo de 1 mês de uso.
4. Escreva **1 teste automatizado** que confira um número da saída contra a entrada.

> **Na aula 13** começa o projeto final: escopo, plano de testes e backlog priorizado.

---

### 🔗 Próximo módulo

[Módulo 13 — Projeto Final: escopo, plano de testes e backlog — Aula 13](#m13)

---

<a id="m13"></a>

## Módulo 13 — Projeto Final (parte 1): escopo, plano de testes e backlog (Aula 13)

**Duração:** 90 min · **Aula 13 de 16** · **P13** (módulo em 4 aulas: 13 a 16)
**Entregável do módulo:** **carta de escopo assinada** + **plano de testes** +
**backlog priorizado** + **critérios de aceite** do projeto final.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Escrever uma **carta de escopo** de 1 página: problema, público, solução, o que
   **não** está no escopo e critério de sucesso.
2. Transformar o escopo em **backlog** com histórias pequenas e priorizadas (MoSCoW).
3. Escrever **critérios de aceite** verificáveis para cada história (formato
   "dado / quando / então").
4. Montar o **plano de testes**: o que testar, como, com que dado e qual é o critério
   de aprovação.
5. Estimar com **PERT** (otimista, provável, pessimista) e explicar por que a estimativa
   é uma faixa, não um número.
6. Ligar cada requisito a um teste por meio da **matriz de rastreabilidade**.
7. Definir a **definição de pronto** (Definition of Done) do projeto.
8. Perceber que escopo inchado é a causa número 1 de projeto que não termina.

**Objetivo secundário:** Compreender que **planejar não é burocracia**: é o que permite
dizer "não" a uma ideia nova sem perder o foco.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `manual-qa-completo/docs/10/PT/charter_template.md` | Modelo de carta de projeto/QA |
| `manual-qa-completo/docs/10/PT/test_plan_template.md` | Modelo de plano de testes |
| `manual-qa-completo/docs/10/PT/test_case_template.md` | Modelo de caso de teste |
| `manual-qa-completo/docs/10/PT/matriz_rastreabilidade.md` | Matriz requisito × teste |
| `manual-qa-completo/docs/10/PT/checklist_aceite.md` | Checklist de aceite |
| `manual-qa-completo/docs/03/scripts/estimate.py` | Estimativa PERT rodando de verdade |
| `manual-qa-completo/docs/03/` | Planejamento, política, estratégia e plano |
| `manual-qa-completo/docs/04/PT/` | Casos de teste manuais e exploratórios |
| `qa-exercicios-praticos/modelos-templates/test-plan.md` | Plano de teste simplificado |
| `qa-exercicios-praticos/modelos-templates/test-case.md` | Caso de teste simplificado |
| `qa-exercicios-praticos/modelos-templates/checklist-smoke-e-aceite.md` | Smoke + aceite |
| `formacaoScrumMaster/` | Estudos de caso de Scrum (backlog e sprint) |
| `git-github-iniciantes/08_issues_e_projetos` | Issues e Projects no GitHub (o backlog vive aqui) |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Escopo** | "O que entra. E, mais importante, o que **não** entra." |
| **Carta de escopo** | "Uma página que qualquer pessoa lê e entende o projeto." |
| **História** | "Uma frase de valor: 'como X, quero Y para Z'." |
| **Critério de aceite** | "Dado / quando / então. Verificável, não adjetivo." |
| **MoSCoW** | "Must, Should, Could, Won't. Prioridade com nome." |
| **Backlog** | "A lista viva do que falta. Priorizada, não alfabética." |
| **PERT** | "(O + 4P + Pe) / 6. Estimativa é faixa, não certeza." |
| **Definição de pronto** | "O combinado que vale para **toda** história: testado, documentado, commitado." |
| **Plano de testes** | "O que testar, como, com que dado e quando aprovar." |
| **Rastreabilidade** | "Todo requisito tem teste. Todo teste tem requisito." |
| **Risco** | "O que pode dar errado e o quanto dói. Prioriza o teste." |
| **Sprint** | "Um pedaço de tempo com meta. Não é sinônimo de pressa." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** chamada por apelido.

**Gancho (3 min):** *"Já vi projeto de 3 meses virar projeto de 1 ano porque ninguém
escreveu, no primeiro dia, o que **não** ia fazer. Hoje a gente escreve isso. Uma
página. Se não cabe numa página, o projeto é grande demais para 4 aulas — e a gente
corta."*

**Demonstração ao vivo (3 min):** mostre a carta de escopo de 1 página (fictícia) e
destaque a seção **"Fora do escopo"**:

```markdown
# Carta de Escopo — Relatório de Frequência Automatizado

## Problema
A secretaria gasta 6 h/mês consolidando presença em planilhas manuais.

## Público
Coordenadores das 23 unidades de ensino.

## Solução
Script Python que lê os CSVs e gera 1 relatório mensal em .xlsx.

## Fora do escopo
- Login e senha (usa o sistema atual)
- Envio automático por e-mail
- App no celular
- Dados de aluno além de frequência

## Critério de sucesso
Relatório gerado em menos de 2 min, com totais conferidos e zero dado pessoal exposto.
```

**Fala do professor:** *"A parte mais importante está aqui: 'Fora do escopo'. É ali que
o projeto se protege. Toda vez que aparecer uma ideia nova — e vai aparecer — você
olha para esta lista e decide: entra agora e sai outra coisa, ou fica para a versão 2."*

> **Plano B:** sem computador, a carta é escrita no papel e fotografada para o
> repositório.

#### Fase 2 — Exploração (22 min)

**Parte 1 — Do escopo ao backlog (7 min).**

| História (formato) | Critério de aceite (dado/quando/então) |
|---|---|
| Como coordenador, quero gerar o relatório do mês para levar à reunião. | **Dado** um CSV de setembro, **quando** eu rodar o script, **então** um `.xlsx` é criado com o total por turma. |
| Como coordenador, quero conferir a frequência por aluno. | **Dado** o relatório, **quando** eu abrir a aba "detalhe", **então** cada aluno aparece com o percentual do mês. |

**Regra:** história que não cabe num critério verificável é **grande demais**. Quebre.

**Parte 2 — MoSCoW e a definição de pronto (7 min).**

| Prioridade | Significado | Exemplo |
|---|---|---|
| **M**ust | Sem isso, não existe | Gerar o `.xlsx` |
| **S**hould | Importante, mas dá para esperar | Gráfico por turma |
| **C**ould | Seria bom | Exportar PDF |
| **W**on't | Não entra agora | App mobile |

**Definição de pronto (vale para toda história):**

- [ ] Código no Git, com commit descritivo
- [ ] Teste automatizado cobrindo o caminho principal
- [ ] README atualizado
- [ ] Revisado por outra pessoa (mesmo que seja um colega de turma)
- [ ] Sem segredo no código

**Parte 3 — Plano de testes e rastreabilidade (8 min).**

| # | O que testar | Tipo | Dado | Critério de aprovação |
|---|---|---|---|---|
| 1 | Leitura do CSV | unitário | CSV fictício de 5 linhas | soma confere |
| 2 | Cálculo do percentual | unitário | 30 presentes de 32 | 93,75% |
| 3 | Geração do `.xlsx` | integração | CSV completo | arquivo abre e tem 3 abas |
| 4 | Dado faltando | exceção | célula vazia | escreve "dado ausente" |
| 5 | Nenhum nome real | segurança | relatório final | 0 nome próprio |

**Matriz de rastreabilidade (modelo):**

| Requisito | História | Teste |
|---|---|---|
| R1 — gerar relatório | H1 | T1, T3 |
| R2 — conferir por aluno | H2 | T2 |
| R3 — sem dado pessoal | H1, H2 | T5 |

**Fala do professor:** *"Se um requisito não tem teste, ele não está no plano. E se um
teste não tem requisito, ele está testando o quê? A matriz evita os dois buracos."*

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos.

**Atividade A — Carta de escopo em 1 página (12 min).**
Preencha o modelo com o **seu** projeto final. Regra: se passar de 1 página, corte.

**Atividade B — Backlog priorizado (10 min).**
Crie no GitHub Issues (ou numa tabela) **no máximo 8 histórias**, cada uma com:
título, história no formato "como/quero/para", critério de aceite e prioridade MoSCoW.
Marque **1** como `Won't` — a que você decidiu não fazer.

**Atividade C — Plano de testes + PERT (8 min).**
Preencha a tabela de 5 testes e rode a estimativa:

```bash
python manual-qa-completo/docs/03/scripts/estimate.py
# informe: otimista=3, provável=5, pessimista=12 (dias)
# resultado: (3 + 4*5 + 12) / 6 = 5,83 dias
```

Escreva no projeto: *"Estimativa: 5,8 dias. Vou entregar na aula 15 se não houver
imprevisto. Risco: acesso ao ambiente do trabalho."*

**Fala do professor durante a circulação:** *"Se você tem 12 histórias, você tem
escopo grande demais. Corte para 8. Se você não consegue dizer o que **não** vai fazer,
você não terminou de planejar."*

> **Plano B:** sem computador, o backlog é uma tabela no papel e a estimativa PERT é
> feita à mão com calculadora do celular.

#### Fase 4 — Projeto (25 min)

**Desafio:** deixar o planejamento do projeto final **aprovado** — o que significa:

- [ ] `ESCOPO.md` com as 5 seções, no máximo 1 página
- [ ] Backlog com 8 histórias e critérios de aceite
- [ ] `PLANO-DE-TESTES.md` com a tabela de testes
- [ ] `RASTREABILIDADE.md` ligando requisito → teste
- [ ] Definição de pronto escrita
- [ ] Estimativa PERT com faixa e riscos
- [ ] **Aprovação**: um colega leu, entendeu e assinou ("li e entendi")

**Critério de pronto:** outra pessoa da turma lê o `ESCOPO.md` e consegue explicar o
projeto em 30 segundos, **sem** perguntar nada.

#### Fase 5 — Mostra (5 min)

- 2 alunos apresentam a carta de escopo em 1 min cada.
- 1 aluno mostra a história que decidiu **não** fazer e justifica.
- A turma dá "2 pontinhos": 1 coisa boa + 1 sugestão de corte.

**Pergunta de saída (oral):** *"Por que a lista 'fora do escopo' é mais importante que a
lista do que entra?"*

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Carta de escopo | 1 página, 5 seções, com "fora do escopo" preenchido |
| Backlog | 8 histórias, critério de aceite em dado/quando/então, MoSCoW |
| Plano de testes | 5 testes com dado e critério de aprovação |
| Rastreabilidade | Todo requisito ligado a teste |
| PERT | Faixa estimada + riscos listados |
| Definição de pronto | Escrita e aceita pela turma |
| Pergunta de saída | Explica que o "fora" protege o foco |

**Pergunta de escrita:**
> "No meio do projeto, o gestor pede para incluir 'enviar o relatório por WhatsApp'.
> O que você faz?"
> **Resposta:** Não incluo automaticamente. A inclusão é uma **mudança de escopo**:
> (1) registro o pedido no backlog como `Could` ou `Won't`; (2) mostro o custo (dias,
> risco, teste novo); (3) pergunto o que **sai** para essa entrada (a regra é trocar,
> não somar); (4) se aprovado, atualizo escopo, plano de testes e estimativa, com
> commit. O gestor pode decidir — mas com o custo na frente.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `manual-qa-completo/docs/10/PT/charter_template.md` | Adaptar para a carta de escopo |
| `manual-qa-completo/docs/10/PT/test_plan_template.md` | Plano de testes completo |
| `manual-qa-completo/docs/10/PT/matriz_rastreabilidade.md` | Matriz pronta para copiar |
| `manual-qa-completo/docs/03/scripts/estimate.py` | Rodar PERT com outros números |
| `formacaoScrumMaster/` | Ler 1 estudo de caso e anotar como o backlog foi priorizado |
| `git-github-iniciantes/08_issues_e_projetos` | Criar o backlog como Issues |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Crie as **8 histórias** como Issues no GitHub, com labels de prioridade.
2. Escreva o **primeiro caso de teste** completo no formato de `test_case_template.md`.
3. Rode o `estimate.py` com **3 cenários** (otimista, real, pessimista) e registre.
4. Peça para **uma pessoa de fora** ler o `ESCOPO.md` e escrever, em 1 frase, o que
   entendeu. Se a frase não bater com o seu objetivo, corrija o escopo.

> **Na aula 14** a implementação começa — com **métricas** desde o primeiro commit.

---

### 🔗 Próximo módulo

[Módulo 14 — Projeto Final: implementação com métricas — Aula 14](#m14)

---

<a id="m14"></a>

## Módulo 14 — Projeto Final (parte 2): implementação com métricas (Aula 14)

**Duração:** 90 min · **Aula 14 de 16** · **P14** (módulo em 4 aulas: 13 a 16)
**Entregável do módulo:** **implementação funcionando** das histórias `Must` +
**painel de métricas** (KPIs medidos: cobertura, tempo, defeitos, custo).

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Implementar as histórias `Must` do backlog **na ordem de prioridade**, com commit
   por história.
2. Escrever **teste junto com o código** (não depois), mesmo que simples.
3. Medir **4 KPIs mínimos**: cobertura de teste, defeitos encontrados, tempo por
   história e custo de execução.
4. Interpretar um **relatório de cobertura** e decidir onde testar mais.
5. Distinguir **defeito** de **melhoria** e registrá-los separadamente.
6. Usar **branch por história** e **pull request** com descrição e checklist.
7. Manter o **log de decisões** (ADR simplificado): cada decisão técnica com data e motivo.
8. Entregar um incremento **utilizável** ao fim da aula — não um esqueleto.

**Objetivo secundário:** Entender que **métrica que não leva a decisão é enfeite**.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `manual-qa-completo/docs/09/scripts/kpi.py` | Cálculo real de KPIs de qualidade |
| `manual-qa-completo/docs/08/scripts/quality_gate.py` | Gate de qualidade por cobertura |
| `manual-qa-completo/docs/08/PT/` | Qualidade de código e CI/CD |
| `manual-qa-completo/docs/05/scripts/` | Automação com Playwright e Pytest |
| `manual-qa-completo/docs/04/PT/` | Casos de teste e bug report |
| `manual-qa-completo/docs/10/PT/bug_report_template.md` | Modelo de registro de defeito |
| `manual-qa-completo/docs/10/PT/checklist_aceite.md` | Checklist antes de aceitar a história |
| `qa-exercicios-praticos/modelos-templates/bug-report.md` | Bug report simplificado |
| `git-github-iniciantes/04_branches` | Branch por história |
| `git-github-iniciantes/07_pull_requests` | PR com descrição e revisão |
| `git-github-iniciantes/12_ci_cd_basico` | Pipeline rodando os testes |
| `boilerplate-mochachai/tests/1_unit-tests.js` | Exemplo de teste automatizado simples |
| `meu-treino` | Projeto real com PWA e localStorage (referência) |
| `anyms` | Projeto real com IndexedDB e 17 tabelas (referência) |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Incremento** | "Algo que funciona e dá para usar. Não é 'quase pronto'." |
| **Commit por história** | "Um commit, uma história, uma mensagem que explica o porquê." |
| **Teste junto** | "Se o teste vem depois, ele vem nunca." |
| **Cobertura** | "Quanto do código é exercitado. 100% não garante qualidade, mas 0% garante risco." |
| **KPI** | "Número que orienta decisão. Se não muda comportamento, não é KPI." |
| **Defeito × melhoria** | "Defeito: faz errado o que foi combinado. Melhoria: ideia nova." |
| **ADR** | "Architecture Decision Record: decisão, data, motivo e alternativas." |
| **Quality gate** | "Portão que reprova abaixo do mínimo de cobertura." |
| **Estimado × real** | "Comparar os dois é o que melhora a próxima estimativa." |
| **Refatorar** | "Melhorar o código sem mudar o comportamento. Sempre com teste verde." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** chamada por apelido.

**Gancho (3 min):** *"Hoje é o dia de construir. Mas construir **com prova**. Vou pedir
uma coisa que ninguém gosta: um commit por história, com teste. Não é para dificultar —
é para, no fim da aula, você conseguir mostrar **o que funciona** e **como você sabe
que funciona**."*

**Demonstração ao vivo (3 min):** mostre o painel de métricas do `kpi.py` e um
relatório de cobertura:

```bash
python manual-qa-completo/docs/09/scripts/kpi.py
python -m pytest --cov=src --cov-report=term-missing tests/
```

**Fala do professor:** *"Olhem essa coluna 'Missing'. É onde o teste não passou. Não
preciso testar tudo: preciso testar o que **importa**. Mas o que importa tem que estar
coberto."*

> **Plano B:** sem ambiente, o aluno registra as métricas à mão (histórias concluídas /
> total, defeitos, tempo) numa tabela simples.

#### Fase 2 — Exploração (22 min)

**Parte 1 — Os 4 KPIs mínimos (7 min).**

| KPI | Como medir | Meta inicial |
|---|---|---|
| **Cobertura de teste** | `pytest --cov` | ≥ 60% nas histórias `Must` |
| **Defeitos encontrados** | contagem no bug tracker | registrar todos |
| **Aderência à estimativa** | real ÷ estimado | entre 0,7 e 1,3 |
| **Custo por execução** | tokens × preço + tempo | documentado |

**Parte 2 — Defeito × melhoria (7 min).**

| Defeito (bug) | Melhoria (feature) |
|---|---|
| O total do relatório está errado | Seria bom ter gráfico |
| O script quebra com CSV vazio | Seria bom exportar PDF |
| Aparece nome de aluno no relatório | Seria bom escolher o mês |
| **Regra:** vira tarefa urgente | **Regra:** vai para o backlog |

**Parte 3 — O ADR de 1 página (8 min).**

```markdown
# ADR-001 — Usar pandas para ler o CSV
Data: 2026-10-22 · Status: aceito

## Contexto
Preciso ler CSV, limpar e agrupar por turma.

## Decisão
Usar pandas.

## Alternativas consideradas
- csv da biblioteca padrão (mais simples, mas mais código manual)
- openpyxl direto (só para xlsx)

## Consequências
+ Menos código, mais legível
- Dependência extra (instalar via requirements)
```

**Fala do professor:** *"O ADR é a memória do projeto. Daqui a 6 meses, você vai
perguntar 'por que usei isso?'. A resposta está aqui — com a alternativa que você
descartou."*

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. Cada aluno implementa; o professor circula
e faz perguntas em vez de dar respostas.

**Atividade A — Implementar a primeira história `Must` (18 min).**

```bash
git checkout -b feat/gerar-relatorio
# implementa + escreve o teste
git add .
git commit -m "feat: gera relatorio mensal a partir do CSV

- le CSV com pandas
- calcula percentual por aluno
- gera xlsx com 3 abas
- teste: soma confere com a entrada"
git push -u origin feat/gerar-relatorio
```

**Atividade B — Rodar a métrica e registrar (7 min).**

```bash
python -m pytest --cov=src --cov-report=term-missing
```

Registre numa tabela do projeto:

| História | Estimado | Real | Cobertura | Defeitos |
|---|---|---|---|---|
| H1 — gerar relatório | 5,8 d | 3 h | 72% | 1 |

**Atividade C — Registrar 1 defeito e 1 ADR (5 min).**
Abra o bug report mesmo que o defeito seja seu. O registro vale mais que a vergonha.

**Fala do professor durante a circulação:** *"Não me diga que está pronto. Me diga como
você sabe que está pronto. Se a resposta for 'eu testei', eu pergunto: testou com qual
entrada? E se a entrada for diferente?"*

> **Plano B:** sem Git instalado, o aluno usa o editor e faz "commit" numa pasta com
> data no nome; migra para o Git na aula 15.

#### Fase 4 — Projeto (25 min)

**Desafio:** fechar o **incremento da aula** — o que significa:

- [ ] Pelo menos **2 histórias `Must`** implementadas e commitadas
- [ ] Teste para cada história implementada
- [ ] Cobertura medida e registrada (≥ 60% nas histórias `Must`)
- [ ] 1 ADR escrito
- [ ] Defeitos encontrados registrados (mesmo que já corrigidos)
- [ ] Tabela estimado × real preenchida
- [ ] PR aberto com descrição e checklist de pronto

**Modelo de descrição de PR:**

```markdown
## O que muda
Implementa H1 e H2 (gerar relatório e detalhar por aluno).

## Como testar
1. `pytest` → todos verdes
2. `python src/gerar.py dados/ficticios.csv` → gera `saida.xlsx`

## Checklist
- [ ] Testes verdes
- [ ] Cobertura ≥ 60%
- [ ] README atualizado
- [ ] Sem segredo no código
- [ ] Sem nome real de aluno
```

**Critério de pronto:** o PR pode ser aceito por outra pessoa **sem pedir explicação**.

#### Fase 5 — Mostra (5 min)

- 1 aluno mostra o PR aberto e o teste verde.
- 1 aluno mostra a tabela **estimado × real** e comenta a diferença.
- A turma escolhe: qual KPI foi mais útil hoje?

**Pergunta de saída (oral):** *"Para que serve medir cobertura, se 100% não garante
qualidade?"*

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Histórias implementadas | ≥ 2 `Must`, com commit por história |
| Testes | Cada história tem teste; suíte verde |
| Cobertura | Medida e registrada; ≥ 60% nas `Must` |
| ADR | 1 decisão documentada com alternativas |
| Defeitos | Registrados com o template |
| Estimado × real | Tabela preenchida |
| PR | Descrição e checklist completos |
| Pergunta de saída | Explica que cobertura é indicador de risco, não de perfeição |

**Pergunta de escrita:**
> "Sua cobertura está em 85%, mas o relatório ainda mostra nome de aluno. A cobertura
> provou qualidade?"
> **Resposta:** Não. Cobertura mede **quanto código foi executado**, não **se o
> comportamento está correto**. O teste pode executar a linha que imprime o nome sem
> verificar que ele deveria estar anonimizado. Qualidade exige **teste com asserção
> sobre o requisito** (no caso, "nenhum nome próprio na saída"), não só execução de
> linha. Cobertura alta com teste fraco é falsa sensação de segurança.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `manual-qa-completo/docs/09/scripts/kpi.py` | Ver como os KPIs são calculados |
| `manual-qa-completo/docs/08/scripts/quality_gate.py` | Gate de cobertura |
| `manual-qa-completo/docs/05/scripts/` | Testes com Playwright e Pytest |
| `boilerplate-mochachai/tests/1_unit-tests.js` | Teste unitário simples para comparar |
| `anyms` | Ler a estrutura de um projeto real com muitas tabelas |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Implemente **mais 1 história `Must`** com teste.
2. Rode a cobertura e tente subir 10 pontos onde faz sentido.
3. Escreva **1 ADR** de uma decisão que você tomou hoje.
4. Encontre e corrija **1 defeito** no seu projeto; registre no bug tracker com
   "antes / depois".

> **Na aula 15** é qualidade e entrega: pipeline completo, relatório de risco e
> documentação final.

---

### 🔗 Próximo módulo

[Módulo 15 — Projeto Final: qualidade, pipeline e relatório de risco — Aula 15](#m15)

---

<a id="m15"></a>

## Módulo 15 — Projeto Final (parte 3): qualidade, pipeline e relatório de risco (Aula 15)

**Duração:** 90 min · **Aula 15 de 16** · **P15** (módulo em 4 aulas: 13 a 16)
**Entregável do módulo:** **pipeline verde** (testes + segurança + cobertura) +
**relatório de risco** + **documentação final** (README, manual, changelog).

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Montar um **pipeline de CI** que roda testes, cobertura e scanner de segredos em
   cada `push`.
2. Configurar um **quality gate**: abaixo do mínimo, o merge é bloqueado.
3. Escrever um **relatório de risco** com probabilidade, impacto, mitigação e responsável.
4. Produzir **documentação final** que outra pessoa usa sem você: README, manual,
   changelog e ADRs.
5. Fazer **revisão de código** de um colega com comentários úteis (não destrutivos).
6. Preparar a **apresentação de 5 minutos** do showcase.
7. Fazer o **checklist de entrega** e assinar.
8. Entender que **entrega não é "funciona na minha máquina"**: é reprodutível.

**Objetivo secundário:** Perceber que o pipeline é o **funcionário que nunca esquece** —
ele roda o mesmo teste toda vez, sem cansaço e sem má vontade.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `manual-qa-completo/docs/08/PT/` | Qualidade de código, cobertura e CI/CD |
| `manual-qa-completo/docs/08/scripts/quality_gate.py` | Gate de qualidade real |
| `manual-qa-completo/docs/09/PT/` | KPIs, TMMi, PDCA, risk-based testing |
| `manual-qa-completo/docs/09/scripts/kpi.py` | KPIs para o relatório |
| `manual-qa-completo/docs/11/scripts/secret_scan.py` | Scanner no pipeline |
| `manual-qa-completo/.github/workflows/ci.yml` | Workflow real de CI do manual |
| `manual-qa-completo/docs/10/PT/checklist_aceite.md` | Checklist de entrega |
| `qa-exercicios-praticos/modelos-templates/relatorio-teste.md` | Modelo de relatório de teste |
| `git-github-iniciantes/12_ci_cd_basico` | CI/CD do zero |
| `git-github-iniciantes/07_pull_requests` | Code review e PR |
| `Central-de-noticias/.github/workflows/` | 4 workflows reais (ci-tests, update-news, monitoramento, limpar-historico) |
| `qa-automation-framework` | Framework de automação com CI real |
| `esporte-sao-pedro/.github/` | Exemplos de configuração de projeto real |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **CI (Integração Contínua)** | "Cada push roda os testes. O erro aparece em minutos, não em semanas." |
| **Pipeline** | "A esteira: instalar → testar → medir → verificar → publicar." |
| **Quality gate** | "O portão. Abaixo do mínimo, não passa." |
| **Reprodutível** | "Qualquer pessoa, em qualquer máquina, chega ao mesmo resultado." |
| **Relatório de risco** | "Probabilidade × impacto × mitigação × responsável." |
| **Changelog** | "O que mudou em cada versão, em linguagem de quem usa." |
| **Code review** | "Pergunta, não sentença. 'O que acontece se...?'" |
| **Checklist de entrega** | "A última barreira antes de dizer 'está pronto'." |
| **Rollback** | "Como voltar atrás. Toda entrega precisa de um caminho de volta." |
| **Documentação viva** | "README que acompanha o código. Se desatualizou, é bug." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (8 min)

**Abertura (2 min):** chamada por apelido.

**Gancho (3 min):** *"Semana que vem é o showcase. Hoje é o dia de deixar o projeto
**apresentável**. E apresentável não é bonito: é **reprodutível**. Se eu clonar o seu
repositório agora e seguir o README, funciona? Se a resposta for 'depende', a gente
conserta hoje."*

**Demonstração ao vivo (3 min):** rode o pipeline real do `manual-qa-completo` e mostre
o log:

```bash
# exemplo de saída de um CI verde
✓ instalar dependências (12s)
✓ rodar testes (34s) — 87 passed
✓ cobertura (2s) — 78% (mínimo 70%) ✓
✓ scanner de segredos (1s) — 0 encontrados
✓ quality gate — APROVADO
```

**Fala do professor:** *"Esse '✓' não é vaidade. É a prova de que o projeto pode ser
entregue por qualquer pessoa. Se o pipeline fica vermelho, a gente não faz merge. Simples
assim — e é isso que separa projeto de hobby de projeto profissional."*

> **Plano B:** sem GitHub Actions, rode os mesmos comandos localmente e cole a saída no
> PR como "evidência de execução".

#### Fase 2 — Exploração (22 min)

**Parte 1 — O pipeline mínimo (7 min).**

```yaml
name: CI
on: [push, pull_request]
jobs:
  qualidade:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest --cov=src --cov-fail-under=60
      - run: python scripts/verificar_segredos.py
```

**Parte 2 — Relatório de risco (8 min).**

| Risco | Prob. | Impacto | Severidade | Mitigação | Responsável |
|---|---|---|---|---|---|
| Acesso ao ambiente de produção negado | Média | Alto | **Alta** | Usar dados fictícios até liberar | Coordenação |
| Dependência quebrar após atualização | Baixa | Médio | Média | Fixar versão no `requirements.txt` | Aluno |
| Dado pessoal escapar no relatório | Baixa | Alto | **Alta** | Teste T5 + anonimização | Aluno |
| Internet cair na apresentação | Média | Baixo | Baixa | Vídeo gravado de 2 min | Aluno |

**Fala do professor:** *"Reparem que o risco alto não é 'o código não funcionar'. É
'dado pessoal escapar'. Porque o impacto é maior. Risco se mede pelo **dano**, não pela
probabilidade sozinha."*

**Parte 3 — Documentação final (7 min).**

| Documento | O que tem | Quem lê |
|---|---|---|
| `README.md` | O que é, como instalar, como rodar, como testar | Qualquer pessoa |
| `MANUAL-DE-USO.md` | Passo a passo para o usuário final | Usuário |
| `CHANGELOG.md` | O que mudou em cada versão | Quem mantém |
| `docs/decisoes.md` | ADRs | Quem mantém |
| `RELATORIO-DE-RISCO.md` | A tabela de risco | Gestão |
| `LICENSE` | MIT | Todo mundo |

#### Fase 3 — Mão na massa (30 min)

**Breakout rooms:** 4 salas de 3 a 5 alunos. Metade do tempo implementa; metade revisa
o projeto do colega.

**Atividade A — Fechar o pipeline (12 min).**
Adicione o workflow, faça um push e **veja o verde**. Se ficar vermelho, leia o log e
conserte — o log é a aula.

**Atividade B — Escrever o relatório de risco (8 min).**
Preencha a tabela com **pelo menos 5 riscos** do seu projeto. Marque os 2 de severidade
alta e escreva a mitigação de cada um.

**Atividade C — Revisão de código do colega (10 min).**
Abra o PR de um colega e comente usando o padrão:

```text
Pergunta (não afirmação): "O que acontece se o CSV vier vazio?"
Sugestão: "Talvez valha um teste com 0 linhas."
Elogio específico: "Gostei de separar a leitura do cálculo — ficou testável."
```

**Regra da revisão:** **2 perguntas + 1 sugestão + 1 elogio específico**. Nunca "está
errado" sem dizer onde e por quê.

**Fala do professor durante a circulação:** *"Revisão boa faz o autor pensar. Revisão
ruim faz o autor se defender. Se você escreveu 'está errado', apague e escreva 'o que
acontece quando...?'."*

> **Plano B:** sem GitHub, a revisão é feita no papel: imprima o trecho de código e
> escreva os comentários com post-it.

#### Fase 4 — Projeto (25 min)

**Desafio:** fechar a **entrega** do projeto. Checklist:

- [ ] Pipeline verde (testes + cobertura + segredos)
- [ ] Quality gate configurado (cobertura mínima)
- [ ] `RELATORIO-DE-RISCO.md` com 5 riscos e 2 mitigações de alta severidade
- [ ] `README.md` completo (instalar, rodar, testar, arquitetura)
- [ ] `MANUAL-DE-USO.md`
- [ ] `CHANGELOG.md` com a versão 1.0
- [ ] `docs/decisoes.md` com os ADRs
- [ ] `LICENSE` MIT
- [ ] PR revisado por um colega, com os comentários respondidos
- [ ] Checklist de entrega assinado

**Modelo do `CHANGELOG.md`:**

```markdown
# Changelog
Formato baseado em Keep a Changelog. Versionamento semântico.

## [1.0.0] — 2026-10-22
### Adicionado
- Geração de relatório mensal em .xlsx
- Detalhamento por aluno
- Cobertura de teste 72%

### Corrigido
- Nome de aluno aparecia no resumo (agora anonimizado)

### Segurança
- Scanner de segredos no CI
- Dados fictícios por padrão
```

**Critério de pronto:** você entrega o link do repositório e um colega **clona e roda**
seguindo só o README. Se travar, falta documentação.

#### Fase 5 — Mostra (5 min)

- 1 aluno mostra o pipeline verde e o gate.
- 1 aluno lê o risco de severidade alta e a mitigação.
- 1 aluno conta o comentário de revisão que mais o fez pensar.

**Pergunta de saída (oral):** *"Por que 'funciona na minha máquina' não é entrega?"*

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Pipeline | Verde em push e PR; roda testes, cobertura e segredos |
| Quality gate | Cobertura mínima configurada e respeitada |
| Relatório de risco | 5 riscos, probabilidade × impacto, mitigação e responsável |
| Documentação | README, manual, changelog, ADRs, LICENSE |
| Code review | 2 perguntas + 1 sugestão + 1 elogio específico |
| Reprodutibilidade | Um colega clona e roda seguindo o README |
| Pergunta de saída | Explica que entrega é reprodutível |

**Pergunta de escrita:**
> "O projeto passa em todos os testes e o pipeline está verde. Ainda assim, você
> considera que ele pode não estar pronto. Cite duas situações em que isso acontece."
> **Resposta:** (1) **Testes fracos**: eles executam o código mas não verificam o
> requisito (ex.: cobertura alta sem asserção sobre anonimização de dado pessoal).
> (2) **Documentação divergente**: o README descreve um comportamento que o código não
> faz mais; quem clonar não consegue usar. Outras: dependência não fixada (funciona hoje,
> quebra amanhã), ausência de tratamento de erro em entrada real, e falta de plano de
> rollback. Pipeline verde é **condição necessária, não suficiente**.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `manual-qa-completo/.github/workflows/ci.yml` | Workflow real para copiar |
| `manual-qa-completo/docs/08/scripts/quality_gate.py` | Entender o gate |
| `manual-qa-completo/docs/09/PT/` | Risk-based testing |
| `Central-de-noticias/.github/workflows/` | 4 workflows de um projeto em produção |
| `qa-exercicios-praticos/modelos-templates/relatorio-teste.md` | Relatório de teste |
| `QA_RUN/index.html` | Jogo Deploy Simulator (revisão) |

---

### 🏠 Para casa (tarefa assíncrona de 2 h)

1. Deixe o pipeline **verde** e o README testado por alguém de fora.
2. Escreva o **roteiro de 5 min** do showcase (ver o modelo no módulo 16).
3. Grave um **vídeo de 2 min** demonstrando o projeto (plano B da apresentação).
4. Revise o PR de **outro** colega, com o padrão de revisão.
5. Faça o **checklist de entrega** e assine.

> **Na aula 16** é o showcase: apresentação, publicação e certificado.

---

### 🔗 Próximo módulo

[Módulo 16 — Showcase e Certificado — Aula 16](#m16)

---

<a id="m16"></a>

## Módulo 16 — Showcase e Certificado (Aula 16)

**Duração:** 90 min · **Aula 16 de 16** · **P16** (módulo em 4 aulas: 13 a 16)
**Entregável do módulo:** **repositório público** + **apresentação de 5 min** +
**certificado emitido** + **autoavaliação** e **plano de continuidade**.

---

### 🎯 Objetivo

Ao final da aula, o aluno será capaz de:

1. Apresentar um projeto técnico em **5 minutos**, para público leigo, sem jargão.
2. Demonstrar **ao vivo** com plano B (vídeo gravado) e tempo controlado.
3. Responder a **3 perguntas** sobre o próprio projeto com honestidade técnica.
4. Publicar o projeto de forma **acessível** (GitHub Pages + README em português claro).
5. Fazer a **autoavaliação** com a rubrica de 4 níveis.
6. Emitir e **verificar** o certificado pelo modelo do laboratório.
7. Escrever o **plano de continuidade**: o que estudar nas próximas 12 semanas.
8. Celebrar o processo — não só o resultado.

**Objetivo secundário:** Entender que **explicar bem é a última prova de que aprendeu**.

---

### 📚 Fontes no repositório

| Fonte real | O que usar nesta aula |
|---|---|
| `laboratorio-tech-social/site/certificado/index.html` | Gerador de certificado com validação por código |
| `laboratorio-tech-social/site/certificado/verificar.html` | Verificação de autenticidade |
| `laboratorio-tech-social/materiais/templates/certificado/modelo-certificado.md` | Modelo em Markdown |
| `laboratorio-tech-social/materiais/templates/certificado/README.md` | Como preencher e imprimir |
| `laboratorio-tech-social/site/voluntarios.html` | Como continuar como voluntário |
| `laboratorio-tech-social/projetos/README.md` | Onde publicar o projeto da turma |
| `laboratorio-tech-social/docs/plano-pedagogico.md` | Princípios e ciclo (para o discurso final) |
| `QA_RUN/index.html` | Jogos para a "feira" final |
| `git-github-iniciantes/09_github_pages` | Publicar o projeto no GitHub Pages |
| `git-github-iniciantes/13_open_source` | Como contribuir depois do curso |
| `ingles-para-programadores/13_aprendizado_continuo` | Trilha de estudo contínuo |

---

### 🧠 Conceitos-chave

| Conceito | Frase que fixa |
|---|---|
| **Showcase** | "Mostrar o processo, não só o resultado." |
| **Pitch de 5 min** | "Problema → solução → demonstração → aprendizado → próximo passo." |
| **Público leigo** | "Se a sua avó não entendeu, o problema é seu, não dela." |
| **Plano B** | "Vídeo de 2 min pronto. Internet cai, apresentação não." |
| **Autoavaliação** | "O nível que você se dá, com a prova que justifica." |
| **Portfólio** | "O link que vale mais que o certificado: o que você construiu." |
| **Plano de continuidade** | "O que estudar nas próximas 12 semanas, com data." |
| **Certificado** | "Prova de participação e aprendizagem. Não é diploma técnico." |
| **Verificação** | "Código que confere se o certificado é real." |
| **Comunidade** | "O curso termina; o grupo continua." |

---

### ⏱️ Roteiro (90 min)

#### Fase 1 — Apresentação (10 min)

**Abertura (3 min):** chamada final por apelido. Frase de abertura:

> *"Quando a gente começou, 16 semanas atrás, a maioria aqui não tinha aberto um
> terminal. Hoje cada um de vocês tem um projeto que roda, que está no GitHub e que
> outra pessoa consegue usar. Isso não é sorte: é método. E hoje é o dia de mostrar."*

**Organização (4 min):** explique o formato:

| Tempo | O que acontece |
|---|---|
| 5 min | Apresentação individual (2 alunos por vez em salas paralelas, se a turma for grande) |
| 2 min | Perguntas da banca (professor + 1 colega) |
| 1 min | Feedback "2 pontinhos" |
| 82 min | Rodízio até todos apresentarem |

**Regra do showcase (3 min):** *"A mostra é sobre **processo**, não sobre perfeição. Um
projeto simples e bem explicado vale mais que um complexo e confuso. Quem não quiser
apresentar ao vivo pode enviar o vídeo de 2 min — a participação vale igual."*

> **Plano B:** se a turma for grande, divida em 2 salas simultâneas com um coapresentador
> voluntário. Se a internet cair, use os vídeos de 2 min já gravados.

#### Fase 2 — Exploração (15 min)

**Parte 1 — Anatomia do pitch de 5 min (7 min).**

| Tempo | Bloco | O que dizer |
|---|---|---|
| 0:00–0:30 | **Problema** | "Na minha unidade, a secretaria gastava 6 h por mês..." |
| 0:30–1:30 | **Solução** | "Eu fiz um script que lê o CSV e gera o relatório em 2 min." |
| 1:30–3:30 | **Demonstração** | Tela ao vivo: rodar o script, mostrar a saída |
| 3:30–4:30 | **Aprendizado** | "Aprendi que teste não é enfeite: achei 3 bugs..." |
| 4:30–5:00 | **Próximo passo** | "Quero adicionar gráfico por turma no próximo mês." |

**Parte 2 — Como responder perguntas (4 min).**

| Pergunta | Resposta boa | Resposta ruim |
|---|---|---|
| "Quanto custa rodar?" | "R$ 0 em ferramenta; 5 min de máquina por mês." | "Não sei." |
| "E se o dado vier errado?" | "O script avisa e não gera; tem teste para isso." | "Acho que funciona." |
| "Por que não usou Excel?" | "Precisava automatizar e versionar; Excel não versiona bem." | "Porque sim." |

**Parte 3 — Certificado e verificação (4 min).**
Mostre o `site/certificado/index.html`, preencha um exemplo e valide em
`verificar.html`. Explique o código `TECH-XXXX-XXXX-XXXX` e o histórico local.

#### Fase 3 — Apresentações (40 min)

Cada aluno tem **8 min** (5 de pitch + 2 de perguntas + 1 de feedback). O professor
cronometra e avisa em 1 min e em 30 s.

**Ficha de avaliação da banca (usar uma por aluno):**

| Critério | 1 | 2 | 3 | 4 | Observação |
|---|---|---|---|---|---|
| Clareza do problema | ☐ | ☐ | ☐ | ☐ | |
| Demonstração funcionou | ☐ | ☐ | ☐ | ☐ | |
| Explicação do processo | ☐ | ☐ | ☐ | ☐ | |
| Resposta às perguntas | ☐ | ☐ | ☐ | ☐ | |
| Honestidade sobre limites | ☐ | ☐ | ☐ | ☐ | |

**Feedback "2 pontinhos" (1 min):** cada ouvinte dá **1 coisa que gostou** + **1
sugestão**. Nunca só "muito bom".

**Fala do professor ao final de cada apresentação:** *"O que você consegue fazer agora
que não conseguia na primeira aula?"* — a pergunta de saída de todo o curso.

#### Fase 4 — Publicação e autoavaliação (20 min)

**Parte 1 — Publicar o projeto (10 min).**

- [ ] Repositório público no GitHub
- [ ] README em português claro, com print ou GIF
- [ ] GitHub Pages ligado (se for site)
- [ ] Link do projeto no `laboratorio-tech-social/projetos/README.md` (via PR)
- [ ] `LICENSE` MIT
- [ ] Sem dado pessoal real no repositório

**Parte 2 — Autoavaliação com a rubrica (5 min).**

| Nível | Descrição | Eu me dou |
|---|---|---|
| **1** | Não entregou. | ☐ |
| **2** | Entregou com falha funcional ou sem documentação. | ☐ |
| **3** | Entregou, testado, documentado. | ☐ |
| **4** | Entregou, testado, documentado, com **métricas** e **análise de risco**. | ☐ |

Regra: cada nível marcado precisa de **uma prova** (link, print, teste, log). Sem prova,
desce um nível.

**Parte 3 — Plano de continuidade (5 min).**

```markdown
# Meu plano — próximas 12 semanas
| Semana | O que vou estudar | Fonte | Entrega |
|---|---|---|---|
| 1–2 | Testes com pytest | python-do-zero/11 e 12 | 5 testes no meu projeto |
| 3–4 | SQL | banco-de-dados-sql/05 a 08 | Consulta no meu banco |
| 5–6 | Git avançado | git-github-iniciantes/10 | 1 PR em projeto open source |
| 7–8 | IA aplicada | ia-para-iniciantes/10 | 1 automação com revisão |
| 9–12 | Contribuir em open source | listade-exercicios-python-brasil (107 stubs) | 1 contribuição aceita |
```

#### Fase 5 — Encerramento (5 min)

**Entrega simbólica do certificado** (emitido pelo `site/certificado/index.html`).

**Mural da turma:** cada aluno cola (ou digita no chat) **1 frase** do que descobriu e
**1 frase** do que quer aprender agora.

**Fala de encerramento (texto exato):**

> *"Vocês não terminaram um curso. Vocês começaram um portfólio. A partir de hoje, cada
> projeto que vocês fizerem vai para esse mesmo lugar — e daqui a um ano, quando alguém
> perguntar 'o que você sabe fazer?', vocês não vão precisar de currículo: vão mandar o
> link. O curso acaba hoje. O hábito começa hoje também."*

**Convite:** continuar como **voluntário** (`site/voluntarios.html`), mentor de projeto
ou monitor da próxima turma.

---

### 📝 Avaliação

| Instrumento | Critério |
|---|---|
| Pitch de 5 min | Segue os 5 blocos e cabe no tempo |
| Demonstração | Funciona; tem plano B (vídeo) |
| Perguntas | Responde com honestidade técnica |
| Repositório | Público, com README claro, LICENSE e sem dado real |
| Autoavaliação | Nível marcado com prova |
| Plano de continuidade | 12 semanas com fonte e entrega |
| Pergunta de saída | Explica o que aprendeu a fazer |

**Pergunta de escrita:**
> "Qual é a diferença entre o certificado e o portfólio?"
> **Resposta:** O **certificado** prova que você participou e concluiu a trilha — é um
> reconhecimento do processo. O **portfólio** (o repositório público) prova o que você
> **sabe fazer** — é a evidência do resultado, que qualquer pessoa pode abrir, testar e
> usar. O certificado abre a conversa; o portfólio fecha a contratação. Por isso o
> projeto final precisa ser público, documentado e reprodutível.

---

### 🧩 Exercícios extras (do repositório)

| Arquivo | Sobre |
|---|---|
| `laboratorio-tech-social/site/certificado/index.html` | Emitir e validar o certificado |
| `laboratorio-tech-social/site/voluntarios.html` | Continuar como voluntário |
| `laboratorio-tech-social/projetos/README.md` | Publicar o projeto da turma |
| `git-github-iniciantes/09_github_pages` | Publicar o site |
| `listade-exercicios-python-brasil` | 107 stubs esperando contribuição |
| `ingles-para-programadores/15_projeto_contribuir` | Contribuir em open source |

---

### 🏠 Para casa (tarefa final)

1. Publique o repositório e envie o link no grupo da turma.
2. Grave o vídeo de 2 min do projeto (se ainda não gravou).
3. Comece a **semana 1** do plano de continuidade.
4. Envie **1 contribuição** (issue ou PR) para um repositório do ecossistema.

---

### 🔗 Encerramento

Este é o último módulo da trilha. Continue para [Encerramento e Certificação](#encerramento-e-certificacao).

---

<a id="encerramento-e-certificacao"></a>

## Encerramento e Certificação

### Rubrica de avaliação (4 níveis)

| Nível | Descrição | Prova exigida |
|---|---|---|
| **1** | Não entregou. | — |
| **2** | Entregue com falha funcional ou sem documentação. | Link do repositório |
| **3** | Entregue, testado e documentado. | Pipeline verde + README |
| **4** | Entregue, testado, documentado, com **métricas** (cobertura, KPI, tempo) e **análise de risco**. | Tudo do nível 3 + `RELATORIO-DE-RISCO.md` + métricas |

### Pesos da avaliação da trilha

| Componente | Peso | Onde é medido |
|---|---|---|
| Participação e exercícios práticos | 20% | Scripts entregues e rodando |
| Qualidade do código e dos testes | 25% | Testes automatizados + tratamento de erro |
| Versionamento e documentação | 20% | Commits, README, estrutura de pastas |
| Projeto final | 25% | Módulos 13 a 16 |
| Showcase | 10% | Apresentação de 5 min |

### KPIs do curso (para a coordenação)

| KPI | Como medir | Meta |
|---|---|---|
| Taxa de conclusão | Alunos com projeto publicado / matriculados | ≥ 60% |
| Cobertura média dos projetos | `pytest --cov` | ≥ 60% |
| Projetos com pipeline verde | CI verde no último push | ≥ 70% |
| Satisfação | Formulário final (escala 0–10) | ≥ 8,5 |
| Continuidade | Alunos que viram voluntários / concluintes | ≥ 20% |

### Como emitir o certificado

1. Abra `laboratorio-tech-social/site/certificado/index.html` no navegador.
2. Preencha: **nome**, **trilha** ("Profissionais 18+"), **carga horária**
   (24 horas) e **data**.
3. Clique em **Gerar Certificado** e depois em **Imprimir / Salvar PDF**.
4. O sistema gera um **código de verificação** (`TECH-XXXX-XXXX-XXXX`).
5. O aluno confere a autenticidade em `site/certificado/verificar.html`.
6. Entregue impresso ou envie o PDF por e-mail ao próprio aluno.

> ⚠️ **Regra obrigatória (LGPD/ECA):** na trilha 18+, os dados do certificado são do
> próprio aluno, com autorização. Nunca publique nome completo, CPF, e-mail ou
> matrícula no repositório público. Registre a emissão na planilha interna de
> certificados da coordenação, não no GitHub.

### Para quem quer continuar

| Caminho | Onde |
|---|---|
| Ser voluntário (professor, mentor, divulgação) | `laboratorio-tech-social/site/voluntarios.html` |
| Contribuir com código | `laboratorio-tech-social/CONTRIBUTING.md` |
| Continuar estudando | `ingles-para-programadores/13_aprendizado_continuo` |
| Entrar em open source | `git-github-iniciantes/13_open_source` |

---

<a id="como-se-inscrever"></a>

## Como se inscrever

### Requisitos

| Item | Detalhe |
|---|---|
| **Idade** | 18 anos ou mais |
| **Pré-requisito** | Ler e escrever no computador; usar navegador; instalar software |
| **Equipamento** | Computador com Windows, Linux ou macOS e internet |
| **Custo** | **R$ 0,00** — nenhuma taxa, nenhum material pago |

### Passo a passo

1. Acesse o formulário: [`laboratorio-tech-social/inscricao/index.html`](https://marquezbertin.github.io/laboratorio-tech-social/inscricao/).
2. Preencha: **nome**, **idade**, **trilha** ("Profissionais 18+"), **e-mail** e
   **telefone/WhatsApp** (opcional).
3. Marque o **consentimento LGPD** e envie.
4. Você recebe a confirmação e o **link da sala** da primeira aula por e-mail.
5. Antes da primeira aula, instale: [Python 3.10+](https://www.python.org/downloads/),
   [Git](https://git-scm.com/downloads), [VS Code](https://code.visualstudio.com/) e crie
   a conta no [GitHub](https://github.com/signup).

### Calendário sugerido

| Encontro | Dia | Horário | Turma |
|---|---|---|---|
| Semanal | Terça ou quinta | 19h30–21h00 | Profissionais 18+ |
| Plantão de dúvidas | Sábado | 10h00–11h00 | Todos |

> **Nota ao professor:** a turma adulta tem horário de trabalho. Evite segunda-feira às
> 19h. A abordagem que funciona melhor é **aula de 90 min com entrega assíncrona**: o
> aluno termina a tarefa em casa e traz o resultado na aula seguinte.

### Dúvidas

- E-mail da coordenação: `bertinmarquez84@gmail.com`
- Repositório do material: [github.com/Marquezbertin](https://github.com/Marquezbertin)
- Laboratório Tech Social: [marquezbertin.github.io/laboratorio-tech-social](https://marquezbertin.github.io/laboratorio-tech-social/)

---

**Fim da trilha Profissionais (18+).** Volte ao início pelo [Sumário](#-sumário).


