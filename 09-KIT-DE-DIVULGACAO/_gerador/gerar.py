# -*- coding: utf-8 -*-
"""Gera o kit de divulgação do curso Tecnologia na Prática (São Pedro/SP)."""
from __future__ import annotations

import json
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import (  # noqa: E402
    AMARELO, AZUL, BRANCO, CINZA, CREME, GRAFITE, LINHA, NOITE, REPO, SITE,
    TRILHAS, VERMELHO, canvas, display, draw_mark, fit_display, font, gradient,
    hx, icon, logo_h, logo_v, motif_blocks, motif_circuit, motif_code,
    motif_mosaic, motif_terminal, overlay, para, paste_alpha, pattern_dots,
    pattern_grid, pill, qr, rrect, save_jpg, save_pdf, save_png, shadowed_card,
    tag, text, text_height, tracked, wrap,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = []


def out(*parts):
    p = os.path.join(ROOT, *parts)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p


def add(path, titulo, formato, uso):
    MANIFEST.append({"arquivo": os.path.relpath(path, ROOT).replace("\\", "/"),
                     "titulo": titulo, "formato": formato, "uso": uso})


# ================================================================ blocos
def header(img, track="geral", tag_text=None, dark=False):
    d = ImageDraw.Draw(img)
    m = 72
    col = BRANCO if dark else AZUL
    sub = "#B9CBE6" if dark else CINZA
    logo_h(img, m, 62, height=64, color=col, sub=True, sub_color=sub)
    if tag_text:
        f = display(22, "semibold")
        w = d.textlength(tag_text.upper(), font=f) + 0.10 * 22 * len(tag_text) + 48
        tag(img, (1080 - m - w, 74), tag_text, TRILHAS[track]["cor"] if not dark else AMARELO,
            NOITE if dark else BRANCO)
    return d


def footer(img, cta="INSCREVA-SE", sub=None, dark=False, h=160):
    d = ImageDraw.Draw(img)
    bg = AMARELO if dark else NOITE
    fg = NOITE if dark else BRANCO
    y0 = img.height - h
    d.rectangle((0, y0, img.width, img.height), fill=hx(bg))
    f = display(34, "bold")
    d.text((72, y0 + h * 0.44), cta, font=f, fill=hx(fg), anchor="lm")
    icon(img, "arrow", 72 + d.textlength(cta, font=f) + 22, y0 + h * 0.44 - 17, 34, fg)
    if sub:
        f2 = font("medium", 22)
        d.text((img.width - 72, y0 + h * 0.36), sub, font=f2, fill=hx(fg), anchor="ra")
        f3 = font("regular", 19)
        d.text((img.width - 72, y0 + h * 0.36 + 30), SITE, font=f3, fill=hx(fg), anchor="ra")


def kicker(d, x, y, s, color=CINZA, size=24, tracking=0.13):
    f = font("semibold", size)
    tracked(d, (x, y), s.upper(), f, color, tracking)
    return y + size * 1.5


def big_title(d, x, y, s, maxw, size=96, color=GRAFITE, weight="bold", lh=1.06):
    lines = wrap(d, s, display(size, weight), maxw)
    while len(lines) > 4 and size > 56:
        size -= 6
        lines = wrap(d, s, display(size, weight), maxw)
    f = display(size, weight)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=hx(color), anchor="la")
        y += int(size * lh)
    return y


def body(d, x, y, s, maxw, size=30, color=CINZA, lh=1.42):
    return para(d, (x, y), s, font("regular", size), color, maxw, lh)


def bullets(d, x, y, items, maxw, size=28, color=GRAFITE, gap=18, icol=AMARELO):
    f = font("medium", size)
    for it in items:
        d.ellipse((x, y + size * 0.28, x + 12, y + size * 0.28 + 12), fill=hx(icol))
        yy = para(d, (x + 30, y), it, f, color, maxw - 30, 1.35)
        y = yy + gap
    return y


def numero(d, x, y, n, size=300, color=AZUL, alpha=28):
    f = display(size, "black")
    d.text((x, y), str(n), font=f, fill=hx(color, alpha), anchor="la")


# ================================================================ FEED
def feed_convite(track):
    t = TRILHAS[track]
    img = canvas(1080, 1080, CREME)
    pattern_dots(img, 54, NOITE, 12)
    d = header(img, track)

    y = 235
    w, _ = pill(d, (72, y), t["rotulo"].upper(), display(22, "semibold"), t["cor"], BRANCO, 26, 12, 0.08)
    y += 78
    if track == "geral":
        title = "Aprender\ntecnologia\nfazendo."
        sub = "Curso gratuito, ao vivo, uma aula por semana.\nPara crianças, jovens e adultos de São Pedro/SP."
    elif track == "exploradores":
        title = "Seu primeiro\njogo começa\nterça."
        sub = "12 aulas ao vivo para crianças de 8 a 13 anos.\nProjeto final, mostra e certificado."
    elif track == "makers":
        title = "Seu primeiro\nprojeto no\nGitHub."
        sub = "16 aulas ao vivo para jovens de 14 a 18 anos.\nDo zero ao deploy, com portfólio público."
    else:
        title = "Automatize\no que toma\nseu tempo."
        sub = "16 aulas ao vivo para adultos 18+.\nPython, dados, segurança e projeto real."
    y = big_title(d, 72, y, title, 640, 96, GRAFITE, "bold")
    y += 18
    para(d, (72, y), sub, font("regular", 28), CINZA, 600, 1.4)

    box = (640, 640, 1008, 940)
    if track == "geral":
        motif_mosaic(img, box, [AZUL, "#0F7B5A", "#C2570A", "#5B3FA8", AMARELO], 235)
    elif track == "exploradores":
        motif_blocks(img, box, t["cor"], 255)
        # estrela
        icon(img, "star4", 858, 690, 110, AMARELO)
    elif track == "makers":
        motif_code(img, (620, 700, 1010, 930), AMARELO, NOITE)
    else:
        motif_terminal(img, (620, 700, 1010, 930), AMARELO)

    footer(img, "INSCREVA-SE")
    p = out("redes-sociais", "feed", f"feed-convite-{track}.png")
    save_png(img, p)
    add(p, f"Convite — {t['nome']}", "1080x1080", "Instagram/Facebook feed")
    save_jpg(img, out("whatsapp", f"whatsapp-convite-{track}.jpg"))
    return img


def feed_gratis():
    img = canvas(1080, 1080, NOITE)
    pattern_grid(img, 54, BRANCO, 10)
    d = header(img, "geral", "100% GRÁTIS", True)
    d.text((72, 250), "GRÁTIS", font=display(190, "black"), fill=hx(AMARELO), anchor="la")
    d.text((72, 450), "de verdade.", font=display(76, "semibold"), fill=hx(BRANCO), anchor="la")
    body(d, 72, 570, "Sem mensalidade, sem taxa de material\ne sem venda de curso no fim.", 620, 30, "#C9D8EC")
    y = 720
    for i, s in enumerate(["Ferramentas gratuitas", "Material que roda no celular", "Certificado ao final"]):
        icon(img, "check", 72, y + i * 74, 42, AMARELO)
        d.text((134, y + i * 74 + 12), s, font=font("medium", 28), fill=hx(BRANCO), anchor="la")
    motif_circuit(img, (600, 640, 1010, 960), BRANCO, 50)
    footer(img, "GARANTA SUA VAGA", dark=True)
    p = out("redes-sociais", "feed", "feed-gratis-de-verdade.png")
    save_png(img, p)
    add(p, "É grátis de verdade", "1080x1080", "Feed — quebra de objeção")


def feed_prova():
    img = canvas(1080, 1080, CREME)
    d = header(img, "exploradores")
    d.text((60, 210), "“", font=display(260, "black"), fill=hx(AMARELO), anchor="la")
    y = 330
    f = display(54, "medium")
    for ln in ["Uma ideia.", "Uma primeira", "tentativa.", "Um projeto."]:
        d.text((96, y), ln, font=f, fill=hx(GRAFITE), anchor="la")
        y += 76
    d.text((96, y + 30), "TECNOLOGIA NA PR\u00c1TICA \u00b7 APRENDER FAZENDO",
           font=font("semibold", 20), fill=hx(CINZA), anchor="la")
    motif_mosaic(img, (96, 830, 984, 900), ["#0F7B5A", "#1657A8", AMARELO, "#C2570A"], 255)
    footer(img, "QUERO FAZER TAMBÉM")
    p = out("redes-sociais", "feed", "feed-prova-depoimento.png")
    save_png(img, p)
    add(p, "Aprender fazendo", "1080x1080", "Feed institucional sem depoimento")


def feed_trilhas():
    img = canvas(1080, 1080, CREME)
    d = header(img, "geral")
    kicker(d, 72, 190, "Escolha pelo momento de vida", TRILHAS["geral"]["cor"])
    big_title(d, 72, 230, "Três trilhas.\nUm mesmo jeito\nde aprender.", 900, 64)
    rows = [("exploradores", "8 a 13 anos", "12 aulas · projeto no Scratch ou site"),
            ("makers", "14 a 18 anos", "16 aulas · projeto no GitHub com deploy"),
            ("profissionais", "18+", "16 aulas · automação real da rotina")]
    y = 470
    for key, idade, desc in rows:
        t = TRILHAS[key]
        shadowed_card(img, (72, y, 1008, y + 140), 24, BRANCO, 18, (0, 8), 35)
        d = ImageDraw.Draw(img)
        d.rectangle((72, y, 84, y + 140), fill=hx(t["cor"]))
        d.text((112, y + 24), t["nome"], font=display(34, "bold"), fill=hx(t["cor"]), anchor="la")
        d.text((112, y + 72), f"{idade} · {desc}", font=font("regular", 23), fill=hx(CINZA), anchor="la")
        icon(img, "arrow", 920, y + 48, 40, t["cor"])
        y += 150
    footer(img, "ESCOLHA A SUA")
    p = out("redes-sociais", "feed", "feed-tres-trilhas.png")
    save_png(img, p)
    add(p, "As três trilhas", "1080x1080", "Feed — visão geral")


def feed_como_funciona():
    img = canvas(1080, 1080, CREME)
    d = header(img, "geral")
    kicker(d, 72, 188, "Simples assim", AZUL)
    big_title(d, 72, 226, "Como funciona\no curso.", 700, 76)
    steps = [("1", "Inscreva-se", "Formulário de 3 minutos."),
             ("2", "Receba o link", "Aula ao vivo, toda semana."),
             ("3", "Faça junto", "Turma pequena, salas de 3 a 4."),
             ("4", "Construa", "Projeto desde a 1ª semana."),
             ("5", "Mostre", "Mostra final e certificado.")]
    y = 400
    for i, (n, tt, ss) in enumerate(steps):
        col = [AZUL, "#0F7B5A", "#C2570A", "#5B3FA8", AZUL][i]
        d.ellipse((72, y, 136, y + 64), fill=hx(col))
        d.text((104, y + 32), n, font=display(30, "bold"), fill=hx(BRANCO), anchor="mm")
        d.text((158, y + 6), tt, font=display(30, "semibold"), fill=hx(GRAFITE), anchor="la")
        d.text((158, y + 42), ss, font=font("regular", 22), fill=hx(CINZA), anchor="la")
        if i < 4:
            d.line([(104, y + 64), (104, y + 88)], fill=hx(LINHA), width=4)
        y += 112
    motif_blocks(img, (800, 660, 1010, 940), AZUL, 45)
    footer(img, "FAÇA SUA INSCRIÇÃO")
    p = out("redes-sociais", "feed", "feed-como-funciona.png")
    save_png(img, p)
    add(p, "Como funciona (5 passos)", "1080x1080", "Feed — explicação")


def feed_sem_computador():
    img = canvas(1080, 1080, "#DCE8F7")
    d = header(img, "exploradores")
    kicker(d, 72, 190, "Você não precisa de notebook", TRILHAS["exploradores"]["cor"])
    big_title(d, 72, 230, "Dá para\naprender pelo\ncelular.", 600, 82)
    body(d, 72, 520, "As primeiras aulas rodam no navegador e até no papel.\nSe precisar, a escola empresta o computador.", 560, 28, GRAFITE)
    # celular desenhado
    d.rounded_rectangle((690, 470, 950, 920), radius=44, fill=hx(NOITE))
    d.rounded_rectangle((710, 500, 930, 870), radius=26, fill=hx(CREME))
    d.rounded_rectangle((770, 884, 870, 898), radius=7, fill=hx("#B9CBE6"))
    motif_blocks(img, (740, 560, 900, 760), TRILHAS["exploradores"]["cor"], 255)
    d.ellipse((798, 470, 842, 486), fill=hx(NOITE))
    footer(img, "INSCREVA-SE")
    p = out("redes-sociais", "feed", "feed-sem-computador.png")
    save_png(img, p)
    add(p, "Aprender pelo celular", "1080x1080", "Feed — quebra de objeção")


def feed_inscricoes():
    img = canvas(1080, 1080, AMARELO)
    d = header(img, "geral")
    kicker(d, 72, 200, "Turma 2027 · 1º semestre", NOITE)
    big_title(d, 72, 240, "Inscrições\nabertas.", 900, 118, NOITE, "black")
    body(d, 72, 520, "120 vagas gratuitas · 3 trilhas · aulas ao vivo\nterça-feira, 19h · certificado ao final", 800, 30, NOITE)
    # cartões de data
    shadowed_card(img, (72, 650, 470, 880), 26, BRANCO, 22, (0, 10), 50)
    d = ImageDraw.Draw(img)
    d.text((110, 682), "INSCRIÇÕES", font=font("semibold", 20), fill=hx(CINZA), anchor="la")
    d.text((110, 716), "15 jan", font=display(60, "black"), fill=hx(AZUL), anchor="la")
    d.text((110, 792), "até 10 de fevereiro", font=font("medium", 22), fill=hx(GRAFITE), anchor="la")
    shadowed_card(img, (500, 650, 1008, 880), 26, NOITE, 22, (0, 10), 50)
    d = ImageDraw.Draw(img)
    d.text((538, 682), "PRIMEIRA AULA", font=font("semibold", 20), fill=hx("#B9CBE6"), anchor="la")
    d.text((538, 716), "17 fev", font=display(60, "black"), fill=hx(AMARELO), anchor="la")
    d.text((538, 792), "terça-feira, 19h", font=font("medium", 22), fill=hx(BRANCO), anchor="la")
    footer(img, "INSCREVA-SE AGORA", dark=True)
    p = out("redes-sociais", "feed", "feed-inscricoes-abertas.png")
    save_png(img, p)
    add(p, "Inscrições abertas", "1080x1080", "Feed — lançamento")
    save_jpg(img, out("whatsapp", "whatsapp-inscricoes-abertas.jpg"))


def feed_ultima_chamada():
    img = canvas(1080, 1080, NOITE)
    motif_circuit(img, (60, 60, 1020, 1000), BRANCO, 22)
    d = header(img, "geral", "ÚLTIMAS VAGAS", True)
    d.text((72, 240), "ÚLTIMA", font=display(150, "black"), fill=hx(BRANCO), anchor="la")
    d.text((72, 380), "CHAMADA", font=display(150, "black"), fill=hx(AMARELO), anchor="la")
    body(d, 72, 580, "As inscrições encerram em 3 dias.\nDepois disso, só na próxima turma.", 620, 30, "#C9D8EC")
    d.text((72, 720), "20", font=display(120, "black"), fill=hx(AMARELO), anchor="la")
    d.text((200, 748), "vagas por turma", font=font("medium", 28), fill=hx(BRANCO), anchor="la")
    d.text((200, 790), "3 turmas por semestre", font=font("regular", 22), fill=hx("#B9CBE6"), anchor="la")
    footer(img, "GARANTA A SUA", dark=True)
    p = out("redes-sociais", "feed", "feed-ultima-chamada.png")
    save_png(img, p)
    add(p, "Última chamada", "1080x1080", "Feed — escassez real (usar só se houver vaga)")


def feed_mostra():
    img = canvas(1080, 1080, "#E8E1F7")
    pattern_grid(img, 54, "#5B3FA8", 12)
    d = header(img, "profissionais", "ABERTO AO PÚBLICO")
    d.text((72, 230), "MOSTRA", font=display(150, "black"), fill=hx("#5B3FA8"), anchor="la")
    d.text((72, 365), "DE PROJETOS", font=display(88, "bold"), fill=hx(GRAFITE), anchor="la")
    body(d, 72, 500, "O que a cidade construiu em um semestre.\nProjetos reais, aulas abertas e certificação.", 620, 30, GRAFITE)
    d.text((72, 640), "SÁBADO · 10H", font=display(56, "bold"), fill=hx(NOITE), anchor="la")
    d.text((72, 710), "Online e gratuito · link na bio", font=font("medium", 24), fill=hx(CINZA), anchor="la")
    icon(img, "star4", 800, 540, 190, AMARELO)
    icon(img, "star4", 720, 760, 90, "#5B3FA8")
    footer(img, "ASSISTIR À MOSTRA")
    p = out("redes-sociais", "feed", "feed-mostra-de-projetos.png")
    save_png(img, p)
    add(p, "Mostra de projetos", "1080x1080", "Feed — evento")


def feed_certificado():
    img = canvas(1080, 1080, CREME)
    d = header(img, "geral")
    kicker(d, 72, 190, "O que você leva", AZUL)
    big_title(d, 72, 228, "Um projeto\ne um certificado.", 900, 78)
    # certificado mock
    shadowed_card(img, (72, 450, 700, 790), 20, BRANCO, 26, (0, 12), 50)
    d = ImageDraw.Draw(img)
    rrect(d, (72, 450, 700, 790), 20, outline=AZUL, width=4)
    d.text((110, 490), "CERTIFICADO", font=display(34, "bold"), fill=hx(AZUL), anchor="la")
    d.text((110, 540), "Tecnologia na Prática", font=display(26, "semibold"), fill=hx(GRAFITE), anchor="la")
    d.line([(110, 590), (660, 590)], fill=hx(LINHA), width=2)
    d.text((110, 610), "Nome do aluno", font=font("medium", 22), fill=hx(CINZA), anchor="la")
    d.text((110, 650), "12 ou 16 aulas · carga horária", font=font("regular", 20), fill=hx(CINZA), anchor="la")
    d.text((110, 720), "Código de verificação", font=font("regular", 17, mono=True), fill=hx(CINZA), anchor="la")
    icon(img, "cert", 760, 500, 200, AMARELO)
    bullets(d, 72, 840, ["Presença mínima de 75%", "Projeto apresentado na mostra"], 600, 24, GRAFITE, 10)
    footer(img, "QUERO MEU CERTIFICADO")
    p = out("redes-sociais", "feed", "feed-certificado.png")
    save_png(img, p)
    add(p, "Certificado", "1080x1080", "Feed — benefício")


def feed_projeto():
    img = canvas(1080, 1080, CREME)
    d = header(img, "makers", "PROJETO EM DESTAQUE")
    kicker(d, 72, 188, "Feito na aula 7", TRILHAS["makers"]["cor"])
    big_title(d, 72, 226, "Placar da\nCidade.", 700, 90)
    body(d, 72, 430, "Um site que mostra os jogos do torneio do bairro,\ncom dados abertos e deploy automático.", 600, 28, CINZA)
    motif_code(img, (560, 560, 1010, 900), AMARELO, NOITE)
    d.text((72, 640), "HTML · CSS · JavaScript", font=font("semibold", 22, mono=True), fill=hx("#C2570A"), anchor="la")
    d.text((72, 680), "GitHub Pages · licença MIT", font=font("regular", 22, mono=True), fill=hx(CINZA), anchor="la")
    footer(img, "VER PROJETOS")
    p = out("redes-sociais", "feed", "feed-projeto-destaque.png")
    save_png(img, p)
    add(p, "Projeto em destaque", "1080x1080", "Feed — prova de resultado")


def feed_local():
    img = canvas(1080, 1080, "#D9F2E6")
    d = header(img, "exploradores")
    kicker(d, 72, 192, "Orgulho local", TRILHAS["exploradores"]["cor"])
    big_title(d, 72, 230, "Feito em\nSão Pedro,\npara São Pedro.", 760, 78)
    body(d, 72, 500, "Os exemplos são daqui: a praça, a feira, a escola,\no time da cidade, a estrada do bairro.", 600, 28, GRAFITE)
    motif_circuit(img, (640, 590, 1010, 900), TRILHAS["exploradores"]["cor"], 110)
    icon(img, "pin", 800, 700, 100, TRILHAS["exploradores"]["cor"])
    footer(img, "PARTICIPE")
    p = out("redes-sociais", "feed", "feed-feito-em-sao-pedro.png")
    save_png(img, p)
    add(p, "Feito em São Pedro", "1080x1080", "Feed — pertencimento")


def feed_faq():
    img = canvas(1080, 1080, CREME)
    d = header(img, "geral")
    kicker(d, 72, 188, "Perguntas frequentes", AZUL)
    big_title(d, 72, 226, "Tirando as\ndúvidas.", 800, 82)
    qs = [("É grátis mesmo?", "Sim. Sem mensalidade e sem taxa."),
          ("Precisa de computador?", "Não para começar: dá para usar o celular."),
          ("Tem certificado?", "Sim, com carga horária e código de verificação."),
          ("Meu filho de 8 anos pode?", "Sim, na trilha Exploradores."),
          ("E se eu perder aula?", "A tarefa fica no grupo; 75% de presença garante o certificado.")]
    y = 400
    for q, a in qs:
        d.text((72, y), q, font=display(27, "semibold"), fill=hx(AZUL), anchor="la")
        d.text((72, y + 38), a, font=font("regular", 22), fill=hx(CINZA), anchor="la")
        d.line([(72, y + 82), (1008, y + 82)], fill=hx(LINHA), width=2)
        y += 104
    footer(img, "FALAR COM A EQUIPE")
    p = out("redes-sociais", "feed", "feed-tirando-duvidas.png")
    save_png(img, p)
    add(p, "Tirando dúvidas", "1080x1080", "Feed — objeções")


# ================================================================ STORIES
def story_base(track="geral", bg=CREME, dark=False, top_tag=None):
    img = canvas(1080, 1920, bg)
    d = ImageDraw.Draw(img)
    m = 84
    logo_h(img, m, 180, height=70, color=BRANCO if dark else AZUL,
           sub=True, sub_color="#B9CBE6" if dark else CINZA)
    if top_tag:
        tag(img, (m, 300), top_tag, TRILHAS[track]["cor"] if not dark else AMARELO,
            NOITE if dark else BRANCO, 24)
    return img, d


def story_footer(img, s="LINK NA BIO", dark=False):
    d = ImageDraw.Draw(img)
    y = 1660
    bg = AMARELO if dark else NOITE
    fg = NOITE if dark else BRANCO
    rrect(d, (84, y, 996, y + 104), 52, fill=bg)
    f = display(30, "bold")
    d.text((540, y + 52), s, font=f, fill=hx(fg), anchor="mm")
    icon(img, "arrow", 828, y + 30, 42, fg)
    d.text((540, 1820), "Tecnologia na Prática · São Pedro/SP", font=font("medium", 20),
           fill=hx(fg if dark else CINZA), anchor="ma")


def story_contagem(n):
    img, d = story_base("geral", NOITE, True, "CONTAGEM REGRESSIVA")
    d.text((84, 430), "FALTAM", font=display(64, "semibold"), fill=hx("#B9CBE6"), anchor="la")
    d.text((84, 510), str(n), font=display(420, "black"), fill=hx(AMARELO), anchor="la")
    d.text((84, 980), "dias" if n != 1 else "dia", font=display(110, "bold"), fill=hx(BRANCO), anchor="la")
    d.text((84, 1140), "Aula 1 · terça, 19h" if n > 1 else "É amanhã · 19h", font=font("medium", 34), fill=hx("#C9D8EC"), anchor="la")
    d.text((84, 1200), "Online, ao vivo e gratuito.", font=font("regular", 28), fill=hx("#B9CBE6"), anchor="la")
    motif_circuit(img, (520, 900, 1000, 1300), BRANCO, 45)
    story_footer(img, "GARANTIR MINHA VAGA", True)
    p = out("redes-sociais", "stories", f"story-contagem-{n}.png")
    save_png(img, p)
    add(p, f"Contagem regressiva — {n} dia(s)", "1080x1920", "Stories")


def story_hoje():
    img, d = story_base("exploradores", "#0F7B5A", True, "AO VIVO HOJE")
    d.text((84, 420), "É HOJE.", font=display(170, "black"), fill=hx(BRANCO), anchor="la")
    d.text((84, 620), "19h", font=display(300, "black"), fill=hx(AMARELO), anchor="la")
    d.text((84, 960), "Aula 1 · Exploradores", font=display(44, "semibold"), fill=hx(BRANCO), anchor="la")
    d.text((84, 1030), "Traga papel e caneta. O link está no grupo.", font=font("regular", 28), fill=hx("#D9F2E6"), anchor="la")
    icon(img, "play", 760, 560, 190, AMARELO)
    story_footer(img, "ENTRAR NA SALA", True)
    p = out("redes-sociais", "stories", "story-hoje-tem-aula.png")
    save_png(img, p)
    add(p, "É hoje — aula ao vivo", "1080x1920", "Stories no dia da aula")


def story_inscricoes():
    img, d = story_base("geral", AMARELO, False, "INSCRIÇÕES ABERTAS")
    d.text((84, 430), "120", font=display(300, "black"), fill=hx(NOITE), anchor="la")
    d.text((84, 730), "vagas\ngratuitas", font=display(96, "bold"), fill=hx(NOITE), anchor="la")
    d.text((84, 990), "3 trilhas · aulas ao vivo\nterça, 19h · certificado", font=font("medium", 32), fill=hx(NOITE), anchor="la")
    d.text((84, 1180), "8 a 13 · 14 a 18 · 18+", font=display(38, "semibold"), fill=hx(NOITE), anchor="la")
    story_footer(img, "ARRASTE PARA CIMA", True)
    p = out("redes-sociais", "stories", "story-inscricoes-abertas.png")
    save_png(img, p)
    add(p, "Inscrições abertas", "1080x1920", "Stories de lançamento")


def story_enquete():
    img, d = story_base("geral", CREME, False, "ENQUETE")
    d.text((84, 430), "Qual trilha\né a sua?", font=display(92, "bold"), fill=hx(GRAFITE), anchor="la")
    opts = [("exploradores", "8 a 13 anos"), ("makers", "14 a 18 anos"), ("profissionais", "18+")]
    y = 720
    for key, idade in opts:
        t = TRILHAS[key]
        rrect(d, (84, y, 996, y + 170), 32, fill=t["claro"])
        d.rectangle((84, y, 104, y + 170), fill=hx(t["cor"]))
        d.text((140, y + 34), t["nome"], font=display(40, "bold"), fill=hx(t["cor"]), anchor="la")
        d.text((140, y + 92), idade, font=font("medium", 26), fill=hx(CINZA), anchor="la")
        y += 200
    story_footer(img, "RESPONDA NA ENQUETE")
    p = out("redes-sociais", "stories", "story-enquete-trilha.png")
    save_png(img, p)
    add(p, "Enquete: qual trilha", "1080x1920", "Stories — engajamento")


def story_bastidor():
    img, d = story_base("makers", NOITE, True, "BASTIDOR")
    d.text((84, 430), "Como a gente\nprepara a aula.", font=display(76, "bold"), fill=hx(BRANCO), anchor="la")
    d.text((84, 620), "Testamos tudo antes. Se trava na nossa tela,\nnão vai travar na sua.", font=font("regular", 28), fill=hx("#C9D8EC"), anchor="la")
    motif_code(img, (84, 780, 996, 1240), AMARELO, "#061C3A")
    d.text((84, 1320), "É por isso que a aula funciona.", font=display(34, "semibold"), fill=hx(AMARELO), anchor="la")
    story_footer(img, "VER A PRÓXIMA AULA", True)
    p = out("redes-sociais", "stories", "story-bastidor-equipe.png")
    save_png(img, p)
    add(p, "Bastidor da equipe", "1080x1920", "Stories — humanização")


def story_mostra():
    img, d = story_base("profissionais", "#5B3FA8", True, "HOJE É DIA")
    icon(img, "star4", 320, 420, 440, AMARELO)
    d.text((84, 900), "MOSTRA", font=display(150, "black"), fill=hx(BRANCO), anchor="la")
    d.text((84, 1050), "DE PROJETOS", font=display(70, "bold"), fill=hx("#E8E1F7"), anchor="la")
    d.text((84, 1180), "10h · online e gratuito", font=font("medium", 32), fill=hx(AMARELO), anchor="la")
    story_footer(img, "ASSISTIR AGORA", True)
    p = out("redes-sociais", "stories", "story-mostra-hoje.png")
    save_png(img, p)
    add(p, "Mostra hoje", "1080x1920", "Stories — evento")


def story_depoimento():
    img, d = story_base("exploradores", "#D9F2E6", False, "DEPOIMENTO")
    d.text((84, 420), "“", font=display(240, "black"), fill=hx(TRILHAS["exploradores"]["cor"]), anchor="la")
    d.text((110, 620), "Eu não sabia\nque conseguia\ncriar sozinha.", font=display(80, "medium"), fill=hx(GRAFITE), anchor="la")
    d.text((110, 930), "— aluna da turma Exploradores, 11 anos", font=font("semibold", 26), fill=hx(CINZA), anchor="la")
    motif_mosaic(img, (110, 1080, 970, 1300), ["#0F7B5A", AZUL, AMARELO, "#C2570A"], 255)
    story_footer(img, "QUERO PARTICIPAR")
    p = out("redes-sociais", "stories", "story-depoimento.png")
    save_png(img, p)
    add(p, "Depoimento em story", "1080x1920", "Stories — prova social")


def story_tres_trilhas():
    img, d = story_base("geral", CREME, False, "3 TRILHAS")
    d.text((84, 420), "Tem uma\npara você.", font=display(96, "bold"), fill=hx(GRAFITE), anchor="la")
    y = 680
    for key in ["exploradores", "makers", "profissionais"]:
        t = TRILHAS[key]
        water = t["claro"]
        rrect(d, (84, y, 996, y + 240), 34, fill=water)
        d.text((124, y + 34), t["nome"], font=display(42, "bold"), fill=hx(t["cor"]), anchor="la")
        d.text((124, y + 96), t["rotulo"], font=font("semibold", 26), fill=hx(GRAFITE), anchor="la")
        d.text((124, y + 140), {"exploradores": "12 aulas · Scratch e site",
                                "makers": "16 aulas · Python e GitHub",
                                "profissionais": "16 aulas · automação e dados"}[key],
               font=font("regular", 24), fill=hx(CINZA), anchor="la")
        y += 274
    story_footer(img, "ESCOLHA A SUA")
    p = out("redes-sociais", "stories", "story-tres-trilhas.png")
    save_png(img, p)
    add(p, "Três trilhas em story", "1080x1920", "Stories")


def story_cta():
    img, d = story_base("geral", NOITE, True, "VAGAS LIMITADAS")
    d.text((84, 450), "Sua vaga\nestá aqui.", font=display(110, "bold"), fill=hx(BRANCO), anchor="la")
    d.text((84, 730), "20 alunos por turma.\nInscrição em 3 minutos.", font=font("regular", 30), fill=hx("#C9D8EC"), anchor="la")
    q = qr("https://marquezbertin.github.io/laboratorio-tech-social/inscricao/", 360, NOITE, BRANCO)
    img.paste(q, (84, 900))
    d.text((490, 960), "Aponte a câmera\npara o QR code", font=display(38, "semibold"), fill=hx(AMARELO), anchor="la")
    d.text((490, 1080), "ou toque no link da bio.", font=font("regular", 26), fill=hx("#C9D8EC"), anchor="la")
    story_footer(img, "INSCREVA-SE", True)
    p = out("redes-sociais", "stories", "story-cta-qrcode.png")
    save_png(img, p)
    add(p, "CTA com QR code", "1080x1920", "Stories — conversão")


# ================================================================ CARROSSÉIS
def carrossel_slide(n, total, titulo, corpo, track="geral", bg=CREME, dark=False,
                    numero_grande=None, kicker_txt=None):
    img = canvas(1080, 1350, bg)
    d = ImageDraw.Draw(img)
    # barra de progresso
    d.rectangle((0, 0, 1080, 10), fill=hx(LINHA if not dark else "#1B4A85"))
    d.rectangle((0, 0, int(1080 * n / total), 10), fill=hx(TRILHAS[track]["cor"] if track != "geral" else AMARELO))
    logo_h(img, 72, 60, 54, BRANCO if dark else AZUL, True, "#B9CBE6" if dark else CINZA)
    d.text((1008, 78), f"{n}/{total}", font=display(24, "semibold"),
           fill=hx("#B9CBE6" if dark else CINZA), anchor="ra")
    y = 250
    if kicker_txt:
        y = kicker(d, 72, y, kicker_txt, AMARELO if dark else TRILHAS[track]["cor"])
    if numero_grande:
        d.text((72, y - 40), str(numero_grande), font=display(220, "black"),
               fill=hx(AMARELO if dark else TRILHAS[track]["cor"]), anchor="la")
        y += 200
    d.text((72, y), titulo, font=display(72, "bold"), fill=hx(BRANCO if dark else GRAFITE), anchor="la")
    y += text_height(d, titulo, display(72, "bold"), 900, 1.1) + 30
    y = para(d, (72, y), corpo, font("regular", 30), "#C9D8EC" if dark else CINZA, 900, 1.45)
    return img, d, y


def carrossel_como_funciona():
    slides = [
        ("Como funciona\no curso", "5 coisas para saber antes de se inscrever.", "EM 1 MINUTO", None, CREME, False),
        ("É de graça,\nde verdade.", "Sem mensalidade, sem taxa de material e sem venda de curso no fim. As ferramentas são gratuitas e rodam no navegador.", "GRATUITO", "0", AMARELO, False),
        ("É ao vivo,\ntoda semana.", "Um encontro por semana, no mesmo horário, com turma de até 20 alunos. Você não assiste sozinho: a gente faz junto.", "AO VIVO", None, NOITE, True),
        ("Você sai com\num projeto.", "Não é só assistir. Desde a primeira semana você constrói algo seu — e apresenta na mostra final.", "MÃO NA MASSA", None, CREME, False),
        ("Como entrar.", "Inscrição em 3 minutos. 120 vagas gratuitas, 3 trilhas e certificado ao final. Terça, 19h, online.", "INSCREVA-SE", None, "#DCE8F7", False),
    ]
    for i, (ti, co, ki, num, bg, dark) in enumerate(slides, 1):
        img, d, y = carrossel_slide(i, 5, ti, co, "geral", bg, dark, num, ki)
        if i == 1:
            motif_mosaic(img, (72, 860, 1008, 1110), [AZUL, "#0F7B5A", "#C2570A", "#5B3FA8", AMARELO], 255)
        elif i == 3:
            icon(img, "play", 760, 980, 180, AMARELO)
        elif i == 4:
            motif_code(img, (600, 980, 1008, 1220), AMARELO, "#123E70")
        elif i == 5:
            icon(img, "arrow", 72, 1150, 60, AZUL)
            d.text((150, 1158), "Link na bio", font=display(34, "semibold"), fill=hx(AZUL), anchor="la")
        if i == 1:
            d.text((72, 1150), "Arraste para o lado", font=font("medium", 26), fill=hx(CINZA), anchor="la")
            icon(img, "arrow", 300, 1146, 40, AZUL)
        p = out("redes-sociais", "carrossel", f"carrossel-como-funciona-{i}.png")
        save_png(img, p)
        add(p, f"Carrossel Como funciona — slide {i}", "1080x1350", "Instagram carrossel")


def carrossel_trilhas():
    rows = [
        ("exploradores", "8 a 13 anos", "Pensamento computacional, Scratch, primeiro site.\nProjeto: Inventário Digital do Meu Bairro.", "12 aulas de 60 min"),
        ("makers", "14 a 18 anos", "Python, web, banco de dados, Git, QA e IA.\nProjeto: Impacto Local em Open Source.", "16 aulas de 90 min"),
        ("profissionais", "18+", "Automação, dados, Git, LGPD e IA no trabalho.\nProjeto: Automação Real da Minha Rotina.", "16 aulas de 90 min"),
    ]
    img, d, y = carrossel_slide(1, 5, "Três trilhas.\nUm mesmo método.", "Toda aula segue o mesmo ciclo: apresentar, explorar, fazer, projetar e mostrar.", "geral", CREME, False, None, "ESCOLHA A SUA")
    motif_mosaic(img, (72, 950, 1008, 1200), ["#0F7B5A", "#C2570A", "#5B3FA8", AZUL, AMARELO], 240)
    p = out("redes-sociais", "carrossel", "carrossel-trilhas-1.png")
    save_png(img, p)
    add(p, "Carrossel Três trilhas — capa", "1080x1350", "Instagram carrossel")

    for i, (key, idade, desc, carga) in enumerate(rows, 2):
        t = TRILHAS[key]
        img, d, y = carrossel_slide(i, 5, f"{t['nome']}\n{idade}", desc, key, t["claro"], False, None, f"TRILHA {i-1} DE 3")
        d.text((72, y + 20), carga, font=display(34, "semibold"), fill=hx(t["cor"]), anchor="la")
        box = (600, 900, 1008, 1170)
        if key == "exploradores":
            motif_blocks(img, box, t["cor"], 255)
            icon(img, "star4", 690, 830, 90, AMARELO)
        elif key == "makers":
            motif_code(img, box, AMARELO, NOITE)
        else:
            motif_terminal(img, box, AMARELO)
        p = out("redes-sociais", "carrossel", f"carrossel-trilhas-{i}.png")
        save_png(img, p)
        add(p, f"Carrossel Três trilhas — {t['nome']}", "1080x1350", "Instagram carrossel")

    img, d, y = carrossel_slide(5, 5, "Qual é a sua?", "Inscrições gratuitas, 20 vagas por turma.\nTerça, 19h, online, com certificado.", "geral", NOITE, True, None, "INSCREVA-SE")
    icon(img, "arrow", 72, 1000, 70, AMARELO)
    d.text((170, 1010), "Link na bio", font=display(40, "semibold"), fill=hx(AMARELO), anchor="la")
    motif_circuit(img, (500, 960, 1008, 1240), BRANCO, 50)
    p = out("redes-sociais", "carrossel", "carrossel-trilhas-5.png")
    save_png(img, p)
    add(p, "Carrossel Três trilhas — CTA", "1080x1350", "Instagram carrossel")


def carrossel_numeros():
    items = [
        ("3", "trilhas por idade", "8 a 13, 14 a 18 e 18+. Cada uma com projeto final."),
        ("12–16", "aulas ao vivo", "Uma por semana, no mesmo horário, com turma pequena."),
        ("20", "alunos por turma", "Gente suficiente para fazer comunidade, pouca para ninguém sumir."),
        ("0", "reais para a família", "Sem mensalidade, taxa ou material pago."),
        ("1", "projeto seu no final", "Apresentado na mostra, com certificado e portfólio."),
    ]
    for i, (n, t, s) in enumerate(items, 1):
        dark = i in (2, 4)
        img, d, y = carrossel_slide(i, 5, t, s, "geral", NOITE if dark else CREME, dark, n, "O CURSO EM NÚMEROS")
        if i == 5:
            icon(img, "cert", 760, 980, 200, AMARELO)
        p = out("redes-sociais", "carrossel", f"carrossel-numeros-{i}.png")
        save_png(img, p)
        add(p, f"Carrossel Números — {t}", "1080x1350", "Instagram carrossel")


# ================================================================ REELS / DESTAQUES
def reels_capa(nome, titulo, sub, track, bg, dark=False):
    img = canvas(1080, 1920, bg)
    d = ImageDraw.Draw(img)
    logo_h(img, 84, 170, 62, BRANCO if dark else AZUL, True, "#B9CBE6" if dark else CINZA)
    d.text((84, 900), titulo, font=display(120, "black"), fill=hx(BRANCO if dark else GRAFITE), anchor="la")
    title_bottom = 900 + len(titulo.split("\n")) * 146
    sub_y = max(1180, title_bottom + 40)
    d.text((84, sub_y), sub, font=font("medium", 34), fill=hx("#C9D8EC" if dark else CINZA), anchor="la")
    box_y = max(1300, sub_y + 70)
    box = (84, box_y, 996, box_y + 300)
    if track == "makers":
        motif_code(img, (84, box_y, 996, box_y + 300), AMARELO, "#061C3A")
    elif track == "exploradores":
        motif_blocks(img, (84, box_y, 700, box_y + 300), AMARELO, 255)
    else:
        motif_terminal(img, (84, box_y, 996, box_y + 300), AMARELO)
    p = out("redes-sociais", "reels", f"reels-{nome}.png")
    save_png(img, p)
    add(p, f"Capa de Reels — {titulo}", "1080x1920", "Capa de vídeo vertical")


def destaques():
    itens = [("Aulas", "play", AZUL), ("Projetos", "code", "#C2570A"),
             ("Mostra", "star4", "#5B3FA8"), ("Dúvidas", "cert", "#0F7B5A"),
             ("Inscrição", "arrow", NOITE)]
    for nome, ic, cor in itens:
        img = canvas(1080, 1920, CREME)
        d = ImageDraw.Draw(img)
        d.ellipse((240, 560, 840, 1160), fill=hx(cor))
        icon(img, ic, 400, 720, 280, BRANCO)
        d.text((540, 1240), nome.upper(), font=display(64, "bold"), fill=hx(GRAFITE), anchor="ma")
        p = out("redes-sociais", "destaques", f"destaque-{nome.lower()}.png")
        save_png(img, p)
        add(p, f"Capa de destaque — {nome}", "1080x1920", "Instagram destaques")


# ================================================================ IMPRESSOS
def poster(track="geral", W=3508, H=4961):
    t = TRILHAS[track]
    img = canvas(W, H, CREME)
    d = ImageDraw.Draw(img)
    m = 236
    pattern_grid(img, 118, NOITE, 10)
    logo_h(img, m, 200, 230, AZUL, True, CINZA)
    # selo grátis
    d.ellipse((W - m - 560, 160, W - m, 720), fill=hx(AMARELO))
    d.text((W - m - 280, 360), "GRÁTIS", font=display(110, "black"), fill=hx(NOITE), anchor="mm")
    d.text((W - m - 280, 470), "de verdade", font=font("semibold", 44), fill=hx(NOITE), anchor="mm")
    y = 900
    d.text((m, y), "APRENDA", font=display(300, "black"), fill=hx(NOITE), anchor="la")
    d.text((m, y + 320), "TECNOLOGIA", font=display(300, "black"), fill=hx(AZUL), anchor="la")
    d.text((m, y + 640), "FAZENDO.", font=display(300, "black"), fill=hx(NOITE), anchor="la")
    d.text((m, y + 1060), "Curso gratuito, ao vivo, uma aula por semana,\npara crianças, jovens e adultos de São Pedro/SP.",
           font=font("medium", 72), fill=hx(GRAFITE), anchor="la", spacing=20)
    # trilhas
    yy = 2500
    for key in ["exploradores", "makers", "profissionais"]:
        tt = TRILHAS[key]
        rrect(d, (m, yy, W - m, yy + 300), 44, fill=tt["claro"])
        d.rectangle((m, yy, m + 28, yy + 300), fill=hx(tt["cor"]))
        d.text((m + 70, yy + 50), tt["nome"], font=display(80, "bold"), fill=hx(tt["cor"]), anchor="la")
        d.text((m + 70, yy + 160), tt["rotulo"], font=font("semibold", 54), fill=hx(GRAFITE), anchor="la")
        d.text((W - m - 60, yy + 170), {"exploradores": "12 aulas", "makers": "16 aulas", "profissionais": "16 aulas"}[key],
               font=font("medium", 48), fill=hx(CINZA), anchor="ra")
        yy += 340
    d.text((m, yy + 40), "Terça-feira, 19h  ·  100% online  ·  Certificado ao final", font=display(58, "semibold"),
           fill=hx(NOITE), anchor="la")
    # QR
    q = qr("https://marquezbertin.github.io/laboratorio-tech-social/inscricao/", 420, NOITE, CREME)
    img.paste(q, (m, H - 900))
    d.text((m + 470, H - 860), "INSCREVA-SE", font=display(80, "black"), fill=hx(AZUL), anchor="la")
    d.text((m + 470, H - 760), "Aponte a câmera do celular\nou procure a secretaria da sua escola.", font=font("regular", 46), fill=hx(CINZA), anchor="la", spacing=14)
    d.text((m + 470, H - 590), SITE, font=font("medium", 34, mono=True), fill=hx(AZUL), anchor="la")
    # rodapé
    d.rectangle((0, H - 220, W, H), fill=hx(NOITE))
    logo_h(img, m, H - 170, 120, BRANCO, False)
    d.text((W - m, H - 110), "Realização: Laboratório Tech Social", font=font("medium", 36), fill=hx("#B9CBE6"), anchor="ra")
    p = out("impressos", f"cartaz-a3-{track}.png")
    save_png(img, p)
    save_pdf(img, out("impressos", f"cartaz-a3-{track}.pdf"), 300)
    add(p, f"Cartaz A3 — {t['nome']}", "A3 297x420mm 300dpi", "Escola, comércio, CRAS")
    save_jpg(img, out("impressos", f"cartaz-a3-{track}.jpg"), 90)


def flyer():
    W, H = 1748, 2480
    # frente
    img = canvas(W, H, AZUL)
    d = ImageDraw.Draw(img)
    pattern_dots(img, 64, BRANCO, 18)
    logo_v(img, W // 2, 180, 300, BRANCO, True, "#B9CBE6")
    d.text((W // 2, 700), "CURSO GRATUITO", font=display(86, "black"), fill=hx(AMARELO), anchor="ma")
    d.text((W // 2, 820), "DE TECNOLOGIA", font=display(110, "black"), fill=hx(BRANCO), anchor="ma")
    d.text((W // 2, 990), "São Pedro/SP", font=font("semibold", 56), fill=hx("#B9CBE6"), anchor="ma")
    d.text((W // 2, 1180), "8 a 13", font=display(140, "black"), fill=hx(BRANCO), anchor="ma")
    d.text((W // 2, 1330), "14 a 18", font=display(140, "black"), fill=hx(BRANCO), anchor="ma")
    d.text((W // 2, 1480), "18+", font=display(140, "black"), fill=hx(BRANCO), anchor="ma")
    d.text((W // 2, 1740), "1 aula ao vivo por semana", font=font("medium", 52), fill=hx(BRANCO), anchor="ma")
    d.text((W // 2, 1820), "Terça, 19h · Certificado", font=font("medium", 52), fill=hx(BRANCO), anchor="ma")
    q = qr("https://marquezbertin.github.io/laboratorio-tech-social/inscricao/", 400, NOITE, BRANCO)
    img.paste(q, ((W - 400) // 2, 1960))
    d.text((W // 2, 2390), "Inscreva-se · vagas limitadas", font=font("semibold", 40), fill=hx(AMARELO), anchor="ma")
    p = out("impressos", "flyer-a5-frente.png")
    save_png(img, p, 0.5)
    save_pdf(img, out("impressos", "flyer-a5-frente.pdf"), 300)
    add(p, "Flyer A5 — frente", "A5 148x210mm 300dpi", "Mão a mão, reunião")

    # verso
    img = canvas(W, H, CREME)
    d = ImageDraw.Draw(img)
    logo_h(img, 130, 140, 130, AZUL)
    d.text((130, 360), "O que você vai fazer", font=display(78, "bold"), fill=hx(GRAFITE), anchor="la")
    rows = [("exploradores", "Exploradores · 8 a 13", "Pensamento computacional, Scratch, Office, primeiro site e robótica simulada."),
            ("makers", "Makers/Devs · 14 a 18", "Python, web, SQL, Git/GitHub, QA, IA e projeto open source publicado."),
            ("profissionais", "Profissionais · 18+", "Linha de comando, Python, dados, LGPD e automação real da rotina.")]
    y = 520
    for key, ti, co in rows:
        t = TRILHAS[key]
        rrect(d, (130, y, W - 130, y + 380), 30, fill=t["claro"])
        d.rectangle((130, y, 158, y + 380), fill=hx(t["cor"]))
        d.text((200, y + 40), ti, font=display(52, "bold"), fill=hx(t["cor"]), anchor="la")
        para(d, (200, y + 120), co, font("regular", 38), GRAFITE, W - 380, 1.35)
        y += 400
    d.text((130, y + 10), "Como funciona", font=display(64, "bold"), fill=hx(GRAFITE), anchor="la")
    steps = ["Inscreva-se pelo QR code ou na escola.", "Receba o link da aula no WhatsApp.",
             "Faça junto, em turma pequena.", "Apresente seu projeto e receba o certificado."]
    yy = y + 100
    for i, s in enumerate(steps, 1):
        d.ellipse((130, yy, 210, yy + 80), fill=hx(AZUL))
        d.text((170, yy + 40), str(i), font=display(36, "bold"), fill=hx(BRANCO), anchor="mm")
        d.text((240, yy + 14), s, font=font("medium", 40), fill=hx(GRAFITE), anchor="la")
        yy += 90
    d.rectangle((0, H - 260, W, H), fill=hx(NOITE))
    d.text((130, H - 200), "Tecnologia na Prática", font=display(54, "bold"), fill=hx(BRANCO), anchor="la")
    d.text((130, H - 130), SITE, font=font("medium", 30, mono=True), fill=hx("#B9CBE6"), anchor="la")
    p = out("impressos", "flyer-a5-verso.png")
    save_png(img, p, 0.5)
    save_pdf(img, out("impressos", "flyer-a5-verso.pdf"), 300)
    add(p, "Flyer A5 — verso", "A5 148x210mm 300dpi", "Mão a mão, reunião")


def faixa():
    W, H = 8504, 2268
    img = canvas(W, H, NOITE)
    d = ImageDraw.Draw(img)
    pattern_dots(img, 90, BRANCO, 14)
    logo_h(img, 220, 180, 400, BRANCO, True, "#B9CBE6")
    d.text((220, 760), "CURSO GRATUITO", font=display(340, "black"), fill=hx(AMARELO), anchor="la")
    d.text((220, 1120), "DE TECNOLOGIA", font=display(340, "black"), fill=hx(BRANCO), anchor="la")
    d.text((220, 1520), "São Pedro/SP · terça, 19h · online", font=display(170, "semibold"), fill=hx("#C9D8EC"), anchor="la")
    d.text((220, 1760), "8 a 13  ·  14 a 18  ·  18+", font=display(150, "semibold"), fill=hx(AMARELO), anchor="la")
    q = qr("https://marquezbertin.github.io/laboratorio-tech-social/inscricao/", 900, NOITE, BRANCO)
    img.paste(q, (W - 1200, 620))
    d.text((W - 750, 1600), "INSCREVA-SE", font=display(140, "black"), fill=hx(AMARELO), anchor="ma")
    p = out("impressos", "faixa-3x08m.png")
    save_png(img, p)
    save_pdf(img, out("impressos", "faixa-3x08m.pdf"), 72)
    add(p, "Faixa 3 x 0,80 m", "8504x2268 px (72dpi)", "Fachada de escola, praça")


def cracha():
    W, H = 1063, 709
    for lado in ("frente", "verso"):
        img = canvas(W, H, CREME if lado == "frente" else NOITE)
        d = ImageDraw.Draw(img)
        if lado == "frente":
            d.rectangle((0, 0, W, 26), fill=hx(AZUL))
            logo_h(img, 60, 55, 120, AZUL, False)
            d.text((60, 230), "NOME DO VOLUNTÁRIO", font=display(56, "bold"), fill=hx(GRAFITE), anchor="la")
            d.text((60, 320), "FUNÇÃO · TRILHA", font=font("semibold", 32), fill=hx(CINZA), anchor="la")
            rrect(d, (60, 420, 500, 520), 50, fill=AMARELO)
            d.text((280, 470), "EQUIPE", font=display(34, "black"), fill=hx(NOITE), anchor="mm")
            d.text((60, 590), "Válido no semestre 2027/1", font=font("regular", 24), fill=hx(CINZA), anchor="la")
        else:
            d.text((60, 70), "Regras de ouro", font=display(52, "bold"), fill=hx(AMARELO), anchor="la")
            regras = ["Sempre dois adultos na sala.", "Nunca conversa privada com aluno.",
                      "Nunca gravar sem consentimento.", "Escutar, registrar e acionar."]
            y = 180
            for r in regras:
                icon(img, "check", 60, y, 34, AMARELO)
                d.text((112, y + 6), r, font=font("medium", 30), fill=hx(BRANCO), anchor="la")
                y += 76
            d.text((60, 560), "Coordenação: (14) 00000-0000", font=font("regular", 24), fill=hx("#B9CBE6"), anchor="la")
        p = out("impressos", f"cracha-{lado}.png")
        save_png(img, p)
        save_pdf(img, out("impressos", f"cracha-{lado}.pdf"), 300)
        add(p, f"Crachá — {lado}", "90x60mm 300dpi", "Mostra e visita a escola")


def adesivo():
    for nome, txt, cor in [("gratis", "GRÁTIS", AMARELO), ("eu-faco", "EU FAÇO\nTECNOLOGIA", AZUL)]:
        S = 945
        img = canvas(S, S, CREME)
        d = ImageDraw.Draw(img)
        d.ellipse((40, 40, S - 40, S - 40), fill=hx(cor))
        draw_mark(img, S // 2 - 110, 190, 220, BRANCO if cor == AZUL else NOITE)
        f = display(110, "black")
        lines = txt.split("\n")
        y = 520
        for ln in lines:
            d.text((S // 2, y), ln, font=f, fill=hx(BRANCO if cor == AZUL else NOITE), anchor="ma")
            y += 120
        d.text((S // 2, 800), "TECNOLOGIA NA PRÁTICA", font=font("semibold", 30), fill=hx(BRANCO if cor == AZUL else NOITE), anchor="ma")
        p = out("impressos", f"adesivo-{nome}.png")
        save_png(img, p)
        add(p, f"Adesivo — {nome}", "80x80mm 300dpi", "Kit do aluno e da equipe")


# ================================================================ WEB / WHATSAPP
def banner_web():
    W, H = 1200, 630
    img = canvas(W, H, NOITE)
    d = ImageDraw.Draw(img)
    motif_circuit(img, (620, 0, 1200, 630), BRANCO, 40)
    logo_h(img, 72, 60, 76, BRANCO, True, "#B9CBE6")
    d.text((72, 200), "Curso gratuito\nde tecnologia", font=display(74, "bold"), fill=hx(BRANCO), anchor="la")
    d.text((72, 380), "Ao vivo, toda semana. 8–13 · 14–18 · 18+", font=font("medium", 28), fill=hx(AMARELO), anchor="la")
    rrect(d, (72, 460, 390, 550), 45, fill=AMARELO)
    d.text((231, 505), "INSCREVA-SE", font=display(28, "bold"), fill=hx(NOITE), anchor="mm")
    p = out("web", "link-preview-1200x630.png")
    save_png(img, p)
    add(p, "Link preview / OG image", "1200x630", "WhatsApp, redes, site")

    # hero
    W, H = 1920, 1080
    img = canvas(W, H, CREME)
    d = ImageDraw.Draw(img)
    pattern_dots(img, 64, NOITE, 14)
    logo_h(img, 120, 90, 100, AZUL)
    d.text((120, 320), "Aprender tecnologia", font=display(120, "black"), fill=hx(NOITE), anchor="la")
    d.text((120, 470), "fazendo.", font=display(120, "black"), fill=hx(AZUL), anchor="la")
    d.text((120, 650), "Curso gratuito, ao vivo, uma aula por semana,\npara crianças, jovens e adultos de São Pedro/SP.",
           font=font("regular", 38), fill=hx(CINZA), anchor="la", spacing=12)
    rrect(d, (120, 810, 470, 920), 55, fill=hx(AZUL))
    d.text((295, 865), "QUERO PARTICIPAR", font=display(28, "bold"), fill=hx(BRANCO), anchor="mm")
    motif_mosaic(img, (1060, 260, 1800, 860), [AZUL, "#0F7B5A", "#C2570A", "#5B3FA8", AMARELO], 255)
    p = out("web", "hero-1920x1080.png")
    save_png(img, p)
    add(p, "Hero do site", "1920x1080", "Página de inscrição")


def whatsapp_card(tipo):
    img = canvas(1080, 1080, CREME)
    d = header(img, "geral")
    if tipo == "aula-hoje":
        d.text((72, 300), "AULA\nHOJE", font=display(170, "black"), fill=hx(AZUL), anchor="la")
        d.text((72, 700), "19h · link no grupo", font=display(52, "semibold"), fill=hx(GRAFITE), anchor="la")
        d.text((72, 790), "Traga papel e caneta.", font=font("regular", 30), fill=hx(CINZA), anchor="la")
        icon(img, "play", 780, 700, 180, AMARELO)
    elif tipo == "obrigado":
        d.text((72, 300), "OBRIGADO!", font=display(120, "black"), fill=hx(AZUL), anchor="la")
        d.text((72, 460), "Sua inscrição foi\nrecebida.", font=display(72, "semibold"), fill=hx(GRAFITE), anchor="la")
        d.text((72, 700), "Em até 5 dias úteis confirmamos sua vaga.\nQualquer dúvida, responda esta mensagem.", font=font("regular", 28), fill=hx(CINZA), anchor="la")
        icon(img, "check", 780, 300, 160, "#0F7B5A")
    else:
        d.text((72, 300), "COMECE\nTERÇA.", font=display(150, "black"), fill=hx(AZUL), anchor="la")
        d.text((72, 700), "1 aula por semana.\n1 projeto no final.", font=display(52, "semibold"), fill=hx(GRAFITE), anchor="la")
        icon(img, "arrow", 780, 740, 150, AMARELO)
    footer(img, "FALAR COM A EQUIPE")
    p = out("whatsapp", f"whatsapp-{tipo}.png")
    save_png(img, p)
    add(p, f"WhatsApp — {tipo}", "1080x1080", "Mensagem com imagem")


# ================================================================ SLIDES
def slide_capa(track):
    t = TRILHAS[track]
    img = canvas(1920, 1080, CREME)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 120, 1080), fill=hx(t["cor"]))
    logo_h(img, 200, 110, 90, AZUL)
    d.text((200, 380), t["nome"], font=display(110, "black"), fill=hx(t["cor"]), anchor="la")
    d.text((200, 520), t["rotulo"], font=display(64, "semibold"), fill=hx(GRAFITE), anchor="la")
    d.text((200, 640), {"geral": "Curso gratuito · ao vivo · 1 aula por semana",
                        "exploradores": "12 aulas de 60 min · projeto final",
                        "makers": "16 aulas de 90 min · projeto no GitHub",
                        "profissionais": "16 aulas de 90 min · automação real"}[track],
           font=font("regular", 36), fill=hx(CINZA), anchor="la")
    if track == "exploradores":
        motif_blocks(img, (1150, 340, 1750, 800), t["cor"], 255)
    elif track == "makers":
        motif_code(img, (1100, 380, 1800, 760), AMARELO, NOITE)
    else:
        motif_terminal(img, (1100, 380, 1800, 760), AMARELO)
    d.text((200, 930), "Tecnologia na Prática · São Pedro/SP", font=font("medium", 24), fill=hx(CINZA), anchor="la")
    p = out("slides", f"slide-capa-{track}.png")
    save_png(img, p)
    add(p, f"Capa de slide — {t['nome']}", "1920x1080", "Google Slides / PowerPoint")


def slide_template():
    img = canvas(1920, 1080, CREME)
    d = ImageDraw.Draw(img)
    logo_h(img, 120, 70, 60, AZUL)
    d.text((120, 230), "Título da aula em duas linhas", font=display(72, "bold"), fill=hx(GRAFITE), anchor="la")
    d.text((120, 420), "Uma ideia por slide. No máximo 6 linhas.", font=font("regular", 38), fill=hx(CINZA), anchor="la")
    rrect(d, (120, 540, 1100, 860), 26, fill=NOITE)
    for i, (a, b) in enumerate([(0.06, 0.40), (0.12, 0.58), (0.12, 0.72)]):
        d.rectangle((120 + 1100 * a, 540 + 320 * b, 120 + 1100 * (b + 0.06), 540 + 320 * b + 18),
                    fill=hx(AMARELO if i == 0 else "#4C86C8"))
    d.text((1240, 560), "Apoio visual", font=font("semibold", 30), fill=hx(CINZA), anchor="la")
    icon(img, "star4", 1300, 640, 180, AMARELO)
    d.text((120, 980), "Aula 1 · 2027", font=font("medium", 24), fill=hx(CINZA), anchor="la")
    d.text((1800, 980), "Tecnologia na Prática", font=font("medium", 24), fill=hx(CINZA), anchor="ra")
    p = out("slides", "slide-template.png")
    save_png(img, p)
    add(p, "Template de slide", "1920x1080", "Base editável para todas as aulas")


# ================================================================ CERTIFICADOS
def certificado(track):
    t = TRILHAS[track]
    W, H = 3508, 2480
    img = canvas(W, H, BRANCO)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 70), fill=hx(t["cor"]))
    d.rectangle((0, H - 70, W, H), fill=hx(t["cor"]))
    rrect(d, (90, 150, W - 90, H - 150), 20, outline=t["cor"], width=8)
    logo_h(img, 220, 230, 190, AZUL)
    d.text((W // 2, 560), "CERTIFICADO", font=display(170, "black"), fill=hx(t["cor"]), anchor="ma")
    d.text((W // 2, 760), "Certificamos que", font=font("regular", 58), fill=hx(CINZA), anchor="ma")
    d.text((W // 2, 900), "NOME COMPLETO DO ALUNO", font=display(110, "bold"), fill=hx(GRAFITE), anchor="ma")
    d.line([(600, 1060), (W - 600, 1060)], fill=hx(LINHA), width=3)
    txt = (f"concluiu o curso Tecnologia na Prática — Trilha {t['nome'].title()}, "
           f"com carga horária de {12 if track == 'exploradores' else 24} horas, "
           f"no período de ____/____/______ a ____/____/______.")
    para(d, (W // 2, 1160), txt, font("regular", 58), GRAFITE, 2600, 1.4, "ma")
    d.text((W // 2, 1400), "Projeto final: ______________________________________________", font=font("regular", 52), fill=hx(CINZA), anchor="ma")
    d.line([(650, 1900), (1450, 1900)], fill=hx(GRAFITE), width=3)
    d.text((1050, 1940), "Coordenação Pedagógica", font=font("medium", 40), fill=hx(CINZA), anchor="ma")
    d.line([(2050, 1900), (2850, 1900)], fill=hx(GRAFITE), width=3)
    d.text((2450, 1940), "Professor(a)", font=font("medium", 40), fill=hx(CINZA), anchor="ma")
    d.text((W // 2, 2140), "Código de verificação: SPT-2027-______", font=font("regular", 36, mono=True), fill=hx(CINZA), anchor="ma")
    d.text((W // 2, 2210), f"Verifique em {SITE}", font=font("regular", 32), fill=hx(CINZA), anchor="ma")
    p = out("certificados", f"certificado-{track}.png")
    save_png(img, p, 0.5)
    save_pdf(img, out("certificados", f"certificado-{track}.pdf"), 300)
    add(p, f"Certificado — {t['nome']}", "A4 paisagem 300dpi", "Entrega ao aluno")


# ================================================================ SELOS / PADRÕES
def selos():
    itens = [("gratis", "GRÁTIS", AMARELO, NOITE), ("ao-vivo", "AO VIVO", VERMELHO, BRANCO),
             ("certificado", "CERTIFICADO", AZUL, BRANCO), ("online", "100% ONLINE", "#0F7B5A", BRANCO),
             ("sao-pedro", "FEITO EM\nSÃO PEDRO", NOITE, AMARELO),
             ("vagas", "20 VAGAS", "#5B3FA8", BRANCO)]
    for nome, txt, bg, fg in itens:
        S = 600
        img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.ellipse((10, 10, S - 10, S - 10), fill=hx(bg))
        d.ellipse((34, 34, S - 34, S - 34), outline=hx(fg, 120), width=4)
        lines = txt.split("\n")
        f = display(96 if len(txt) <= 9 else 68, "black")
        y = S / 2 - (len(lines) - 1) * 46
        for ln in lines:
            d.text((S // 2, y), ln, font=f, fill=hx(fg), anchor="mm")
            y += 92
        p = out("selos", f"selo-{nome}.png")
        save_png(img, p)
        add(p, f"Selo — {txt.replace(chr(10), ' ')}", "600x600 transparente", "Aplicar sobre fotos e peças")


def padroes():
    combos = [("padrao-grade-creme", CREME, "grade"), ("padrao-pontos-noite", NOITE, "pontos"),
              ("padrao-circuito", "#DCE8F7", "circuito"), ("padrao-mosaico", CREME, "mosaico")]
    for nome, bg, tipo in combos:
        S = 1080
        img = canvas(S, S, bg)
        if tipo == "grade":
            pattern_grid(img, 54, NOITE, 16)
        elif tipo == "pontos":
            pattern_dots(img, 54, BRANCO, 26)
        elif tipo == "circuito":
            motif_circuit(img, (0, 0, S, S), AZUL, 45)
        else:
            motif_mosaic(img, (60, 60, S - 60, S - 60), [AZUL, "#0F7B5A", "#C2570A", "#5B3FA8", AMARELO], 60)
        p = out("padroes", f"{nome}.png")
        save_png(img, p)
        add(p, f"Padrão — {nome}", "1080x1080", "Fundo para stories e posts")


# ================================================================ LOGOS SVG
def logos_svg():
    svg_icon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">
  <rect x="6" y="6" width="228" height="228" rx="46" fill="none" stroke="#1657A8" stroke-width="16"/>
  <path d="M65 74 L175 74 L120 181 Z" fill="none" stroke="#1657A8" stroke-width="14" stroke-linejoin="round"/>
  <circle cx="65" cy="74" r="14" fill="#1657A8"/>
  <circle cx="175" cy="74" r="14" fill="#1657A8"/>
  <circle cx="120" cy="181" r="14" fill="#1657A8"/>
  <path d="M106 106 L106 140 L136 123 Z" fill="#1657A8"/>
</svg>'''
    branco = svg_icon.replace("#1657A8", "#FFFFFF")
    noite = svg_icon.replace("#1657A8", "#0A2E5C")
    for nome, conteudo in [("logo-icone.svg", svg_icon), ("logo-icone-branco.svg", branco),
                           ("logo-icone-preto.svg", noite)]:
        p = out("logos", nome)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(conteudo)
        add(p, f"Logotipo — {nome.replace('logo-', '').replace('.svg', '')}", "SVG vetorial", "Avatar, favicon, marca d'água")

    # versões PNG
    for nome, cor, bg, size, sub in [("logo-horizontal", AZUL, CREME, 72, True),
                                     ("logo-horizontal-branco", BRANCO, None, 72, True),
                                     ("logo-vertical", AZUL, CREME, 220, True),
                                     ("logo-vertical-branco", BRANCO, None, 220, True)]:
        W, H = (1800, 500) if "horizontal" in nome else (1200, 900)
        img = Image.new("RGBA", (W, H), hx(bg) if bg else (0, 0, 0, 0))
        if "horizontal" in nome:
            logo_h(img, 60, 120, 260, cor, sub, CINZA if cor == AZUL else "#B9CBE6")
        else:
            logo_v(img, W // 2, 120, 420, cor, sub, CINZA if cor == AZUL else "#B9CBE6")
        p = out("logos", f"{nome}.png")
        save_png(img, p)
        add(p, f"Logotipo — {nome}", "PNG alta resolução", "Peças digitais")

    # etiquetas de trilha
    for key, t in TRILHAS.items():
        if key == "geral":
            continue
        W, H = 1200, 320
        img = canvas(W, H, t["cor"])
        d = ImageDraw.Draw(img)
        draw_mark(img, 60, 70, 180, BRANCO)
        d.text((280, 90), t["nome"], font=display(76, "black"), fill=hx(BRANCO), anchor="la")
        d.text((280, 190), t["rotulo"], font=font("semibold", 44), fill=hx(BRANCO, 230), anchor="la")
        p = out("logos", f"etiqueta-{key}.png")
        save_png(img, p)
        add(p, f"Etiqueta de trilha — {t['nome']}", "1200x320", "Sobreposição em fotos e peças")


# ================================================================ PREVIEW
def preview():
    grupos = {}
    for m in MANIFEST:
        g = m["arquivo"].split("/")[1] if "/" in m["arquivo"] else "outros"
        grupos.setdefault(g, []).append(m)
    cards = []
    for g, items in grupos.items():
        cards.append(f'<h2>{g.replace("-", " ").title()} <span>{len(items)}</span></h2><div class="grid">')
        for m in items:
            cards.append(
                f'<a class="card" href="../{m["arquivo"]}" target="_blank">'
                f'<img loading="lazy" src="../{m["arquivo"]}" alt="{m["titulo"]}">'
                f'<div class="meta"><strong>{m["titulo"]}</strong>'
                f'<span>{m["formato"]} · {m["uso"]}</span></div></a>')
        cards.append("</div>")
    html = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kit de Divulgação — Tecnologia na Prática</title>
<style>
:root{{--azul:#1657A8;--noite:#0A2E5C;--creme:#FFF8EC;--grafite:#1F2933;--cinza:#5B6770;--amarelo:#FFC53D}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--creme);color:var(--grafite);
font-family:Inter,system-ui,Segoe UI,Arial,sans-serif}}
header{{background:var(--noite);color:#fff;padding:40px 6vw}}
header h1{{margin:0 0 6px;font-size:clamp(24px,3vw,40px);letter-spacing:-.02em}}
header p{{margin:0;color:#B9CBE6}}
nav{{position:sticky;top:0;background:#fff;border-bottom:1px solid #D6DBE0;padding:10px 6vw;z-index:9;
display:flex;gap:14px;overflow:auto}}
nav a{{color:var(--azul);text-decoration:none;font-size:14px;white-space:nowrap}}
main{{padding:24px 6vw 80px}}
h2{{font-size:15px;text-transform:uppercase;letter-spacing:.12em;color:var(--cinza);
margin:38px 0 12px;border-bottom:2px solid #D6DBE0;padding-bottom:8px}}
h2 span{{background:var(--azul);color:#fff;border-radius:20px;padding:2px 9px;font-size:12px;margin-left:6px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px}}
.card{{background:#fff;border-radius:14px;overflow:hidden;text-decoration:none;color:inherit;
box-shadow:0 1px 3px rgba(10,46,92,.10);transition:transform .15s,box-shadow .15s}}
.card:hover{{transform:translateY(-3px);box-shadow:0 8px 24px rgba(10,46,92,.16)}}
.card img{{display:block;width:100%;height:240px;object-fit:cover;background:#eee}}
.meta{{padding:10px 12px 14px;display:flex;flex-direction:column;gap:3px;font-size:13px}}
.meta span{{color:var(--cinza);font-size:11px}}
footer{{padding:30px 6vw;color:var(--cinza);font-size:12px;border-top:1px solid #D6DBE0}}
</style></head><body>
<header><h1>Kit de Divulgação — Tecnologia na Prática</h1>
<p>São Pedro/SP · {len(MANIFEST)} peças · pronto para publicar</p></header>
<nav><a href="#redes-sociais">Redes sociais</a><a href="#impressos">Impressos</a>
<a href="#whatsapp">WhatsApp</a><a href="#web">Web</a><a href="#slides">Slides</a>
<a href="#certificados">Certificados</a><a href="#selos">Selos</a><a href="#padroes">Padrões</a>
<a href="#logos">Logos</a></nav>
<main>{''.join(cards)}</main>
<footer>Clique em qualquer peça para abrir em tamanho real. Os arquivos estão nas subpastas deste kit.
Texto e roteiros: veja <code>../textos/</code>.</footer>
</body></html>'''
    p = out("preview", "index.html")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    add(p, "Galeria de pré-visualização", "HTML", "Abrir no navegador para revisar tudo")


# ================================================================ main
def main():
    for track in ["geral", "exploradores", "makers", "profissionais"]:
        feed_convite(track)
    feed_gratis()
    feed_prova()
    feed_trilhas()
    feed_como_funciona()
    feed_sem_computador()
    feed_inscricoes()
    feed_ultima_chamada()
    feed_mostra()
    feed_certificado()
    feed_projeto()
    feed_local()
    feed_faq()

    for n in (7, 3, 1):
        story_contagem(n)
    story_hoje()
    story_inscricoes()
    story_enquete()
    story_bastidor()
    story_mostra()
    story_depoimento()
    story_tres_trilhas()
    story_cta()

    carrossel_como_funciona()
    carrossel_trilhas()
    carrossel_numeros()

    reels_capa("seu-primeiro-projeto", "SEU PRIMEIRO\nPROJETO", "Do zero ao GitHub em 16 semanas.", "makers", NOITE, True)
    reels_capa("aprender-fazendo", "APRENDER\nFAZENDO", "Uma aula por semana. Um projeto no final.", "exploradores", "#0F7B5A", True)
    reels_capa("automacao-real", "AUTOMAÇÃO\nREAL", "Menos tarefa repetida. Mais tempo para você.", "profissionais", "#5B3FA8", True)
    reels_capa("tres-perguntas", "3 PERGUNTAS\nANTES DE\nSE INSCREVER", "Precisa de computador? É grátis? Tem certificado?", "geral", CREME, False)

    destaques()

    for track in ["geral", "exploradores", "profissionais"]:
        poster(track)
    flyer()
    faixa()
    cracha()
    adesivo()

    banner_web()
    for tipo in ("convite-curto", "aula-hoje", "obrigado"):
        whatsapp_card(tipo)

    for track in ["geral", "exploradores", "makers", "profissionais"]:
        slide_capa(track)
    slide_template()

    for track in ["exploradores", "makers", "profissionais"]:
        certificado(track)

    selos()
    padroes()
    logos_svg()
    preview()

    with open(out("manifest.json"), "w", encoding="utf-8") as f:
        json.dump(MANIFEST, f, ensure_ascii=False, indent=2)
    print(f"{len(MANIFEST)} peças geradas.")


if __name__ == "__main__":
    main()
