#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador del index.html del Tema 26 (ETRIVIUM IAM) desde los .md.

Build COMPLETO (no quirúrgico): ensambla el documento autosuficiente entero a
partir de los .md fuente. Reutiliza el CSS de la serie técnica (`_build_css.txt`)
y el motor de test/JS de T11/T15/T18/T19/T21. Incluye desde el inicio la pestaña
ÍNDICE y un conversor md->HTML que respeta las listas anidadas.

Pestañas: Inicio · Contenido · Índice · Diagramas · Test · Casos · Validación · Fuentes.
Idempotente: re-ejecutar regenera index.html desde los .md.
"""
import re, html, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
VERSION = "v1.0"
FECHA = "2026-08-20"
NN = "26"


def read(name):
    with open(os.path.join(BASE, name), encoding="utf-8") as f:
        return f.read()


# ---------- Inline ----------
def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)  # admite énfasis anidado
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    return t


CALLOUTS = {
    "DATO CLAVE EXAMEN": "dato",
    "EJERCICIO RESUELTO": "ejercicio",
    "EJEMPLO AYTO MADRID": "ayto",
    "REFERENCIA CRUZADA": "ref",
}


# ---------- Listas anidadas ----------
def build_list(items, i, indent, tag):
    out = f"<{tag}>"
    while i < len(items) and items[i][0] >= indent:
        ind, txt = items[i]
        if ind > indent:
            break
        out += "<li>" + inline(txt)
        i += 1
        if i < len(items) and items[i][0] > indent:
            child, i = build_list(items, i, items[i][0], tag)
            out += child
        out += "</li>"
    out += f"</{tag}>"
    return out, i


def _indent_of(line):
    return len(line) - len(line.lstrip(" "))


# ---------- Conversor Markdown -> HTML ----------
def md_to_html(md, skip_h1=True, drop_header_blockquote=True, raw_svg=False):
    lines = md.split("\n")
    out = []
    i, n = 0, len(lines)
    header_bq_dropped = False
    while i < n:
        line = lines[i]
        s = line.strip()
        # bloque de código ``` (con info string)
        if s.startswith("```"):
            info = s[3:].strip().lower()
            i += 1
            buf = []
            while i < n and lines[i].strip() != "```":
                buf.append(lines[i])
                i += 1
            i += 1  # cierre ```
            body = "\n".join(buf)
            if raw_svg and info == "svg":
                out.append(body)  # SVG inline, sin escapar
            else:
                out.append(f"<pre><code>{html.escape(body)}</code></pre>")
            continue
        if s == "---":
            out.append("<hr>")
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            level = len(m.group(1))
            if level == 1 and skip_h1:
                i += 1
                continue
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in header)
            trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue
        if s.startswith(">"):
            bq = []
            while i < n and lines[i].strip().startswith(">"):
                bq.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            text = " ".join(x.strip() for x in bq if x.strip())
            if drop_header_blockquote and not header_bq_dropped and ("Título oficial" in text or "Título" in text or "Versión" in text):
                header_bq_dropped = True
                continue
            cm = re.match(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$", text)
            if cm and cm.group(1) in CALLOUTS:
                cls = CALLOUTS[cm.group(1)]
                kicker = cm.group(1)
                out.append(f'<div class="callout {cls}"><span class="kicker">{kicker}</span>{inline(cm.group(2))}</div>')
            else:
                out.append(f"<blockquote>{inline(text)}</blockquote>")
            continue
        if re.match(r"^\s*-\s+", line):
            items = []
            while i < n and re.match(r"^\s*-\s+", lines[i]):
                items.append((_indent_of(lines[i]), re.sub(r"^\s*-\s+", "", lines[i]).strip()))
                i += 1
            base = min(it[0] for it in items)
            h, _ = build_list(items, 0, base, "ul")
            out.append(h)
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append((_indent_of(lines[i]), re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip()))
                i += 1
            base = min(it[0] for it in items)
            h, _ = build_list(items, 0, base, "ol")
            out.append(h)
            continue
        if s == "":
            i += 1
            continue
        para = [s]
        i += 1
        while i < n:
            nx = lines[i].strip()
            if nx == "" or nx.startswith(("#", "|", ">", "-", "---", "```")) or re.match(r"^\d+\.\s", nx):
                break
            para.append(nx)
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


# ---------- Índice (esquema jerárquico N / N.M / N.M.O) ----------
def build_outline(entries, i, level):
    out = '<ol style="list-style:none">'
    while i < len(entries) and entries[i][0] >= level:
        lvl, txt = entries[i]
        if lvl > level:
            break
        out += "<li>" + txt
        i += 1
        if i < len(entries) and entries[i][0] > level:
            child, i = build_outline(entries, i, entries[i][0])
            out += child
        out += "</li>"
    out += "</ol>"
    return out, i


def indice_html(md):
    lines = md.split("\n")
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if s == "---" or s == "":
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            if lvl == 1:
                i += 1
                continue
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        if s.startswith(">"):
            while i < n and lines[i].strip().startswith(">"):
                i += 1
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in header)
            trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue
        is_outline = (re.match(r"^\d+\.\s+\*\*", line) or re.match(r"^\s+\d+\.\d+", line))
        if is_outline:
            entries = []
            while i < n:
                ln = lines[i]
                t = ln.strip()
                mt = re.match(r"^(\d+)\.\s+\*\*(.+?)\*\*\s*$", t)
                m3 = re.match(r"^(\d+)\.(\d+)\.(\d+)\.\s+(.*)$", t)
                m2 = re.match(r"^(\d+)\.(\d+)\.\s+(.*)$", t)
                if mt:
                    entries.append((1, f"<strong>{mt.group(1)}. {inline(mt.group(2))}</strong>"))
                elif m3:
                    entries.append((3, inline(f"{m3.group(1)}.{m3.group(2)}.{m3.group(3)}. {m3.group(4)}")))
                elif m2:
                    entries.append((2, inline(f"{m2.group(1)}.{m2.group(2)}. {m2.group(3)}")))
                elif t == "":
                    if i + 1 < n and (re.match(r"^\d+\.\s+\*\*", lines[i + 1]) or re.match(r"^\s+\d+\.\d+", lines[i + 1])):
                        i += 1
                        continue
                    break
                else:
                    break
                i += 1
            h, _ = build_outline(entries, 0, 1)
            out.append(f'<div class="indice-outline">{h}</div>')
            continue
        out.append(f"<p>{inline(s)}</p>")
        i += 1
    return "\n".join(out)


# ---------- Test ----------
def parse_test(md):
    questions = []
    blocks = re.split(r"^### Pregunta \d+\s*$", md, flags=re.M)[1:]
    for b in blocks:
        # enunciado: primer **...**
        qm = re.search(r"\*\*(.+?)\*\*", b, flags=re.S)
        q = qm.group(1).strip() if qm else ""
        opts = re.findall(r"^([ABC])\)\s+(.*)$", b, flags=re.M)
        opts = [o[1].strip() for o in opts[:3]]
        cm = re.search(r"\*\*Correcta:\s*([ABC])\)\s*(.*?)\*\*\s*(.*?)\s*\*Referencia:\s*(.+?)\*", b, flags=re.S)
        if not cm or len(opts) != 3:
            raise SystemExit(f"Pregunta mal formada:\n{b[:200]}")
        correct = "ABC".index(cm.group(1))
        expl = cm.group(3).strip().replace("\n", " ")
        ref = cm.group(4).strip()
        questions.append({
            "q": inline(q),
            "opts": [inline(o) for o in opts],
            "correct": correct,
            "ref": ref,
            "expl": inline(expl),
        })
    return questions


# ---------- Build ----------
def build():
    css = read("_build_css.txt")
    contenido = md_to_html(read(f"tema-{NN}-contenido.md"))
    indice = indice_html(read(f"tema-{NN}-indice.md"))
    diagramas = md_to_html(read(f"tema-{NN}-diagramas.md"), raw_svg=True)
    casos = md_to_html(read(f"tema-{NN}-caso-practico.md"))
    validacion = md_to_html(read(f"tema-{NN}-validacion.md"))
    fuentes = md_to_html(read(f"tema-{NN}-fuentes.md"))
    questions = parse_test(read(f"tema-{NN}-test.md"))

    qjson = json.dumps(questions, ensure_ascii=False, indent=0)

    inicio = f"""<div class="hero">
  <span class="vbadge">{VERSION}</span>
  <h1>Tema {NN} — Almacenamiento, virtualización y copias de seguridad</h1>
  <div class="sub">DAS, SAN, NAS y objetos · RAID y optimización · SDS e hiperconvergencia · RTO/RPO y regla 3-2-1 · Backup de sistemas físicos y virtuales · ENS y RGPD</div>
  <div class="banner"><strong>Parte II — Técnico · C1 Ayuntamiento de Madrid</strong> · Piloto {VERSION} · {FECHA} · Pendiente de validación</div>
</div>
<h2>Qué incluye este tema</h2>
<table><thead><tr><th>Entregable</th><th>Cantidad</th></tr></thead><tbody>
<tr><td>Contenido teórico</td><td>5 secciones · 32 epígrafes · ~17.600 palabras (el más extenso de la serie técnica)</td></tr>
<tr><td>Diagramas SVG inline</td><td>14 diagramas autosuficientes</td></tr>
<tr><td>Banco de preguntas tipo test</td><td>60 preguntas A/B/C (balanceadas 20/20/20) con corrección y penalización 1/3</td></tr>
<tr><td>Casos prácticos Ayto Madrid</td><td>3 casos (diseño del almacenamiento del CPD municipal; política de copias con RTO/RPO y ventana de respaldo; recuperación ante un incidente de ransomware)</td></tr>
<tr><td>Fuentes Tier 1</td><td>23 referencias canónicas (SNIA, INCITS T10/T11, NVM Express, IETF, ISO/IEC, NIST…)</td></tr>
</tbody></table>
<div class="callout ref"><span class="kicker">Cómo estudiar</span>Lee el <strong>Contenido</strong>, usa el <strong>Índice</strong> para navegar, apóyate en los <strong>Diagramas</strong>, autoevalúate en el <strong>Test</strong> y practica con los <strong>Casos</strong>. Las cajas naranjas (DATO CLAVE) marcan lo más memorizable.</div>"""

    nav = (
        '<nav class="tabs">'
        f"<button class=\"tab-btn active\" data-tab=\"inicio\">Inicio <span class='version-badge'>{VERSION}</span></button>"
        '<button class="tab-btn" data-tab="contenido">Contenido</button>'
        '<button class="tab-btn" data-tab="indice">Índice</button>'
        '<button class="tab-btn" data-tab="diagramas">Diagramas</button>'
        '<button class="tab-btn" data-tab="test">Test</button>'
        '<button class="tab-btn" data-tab="casos">Casos</button>'
        '<button class="tab-btn" data-tab="validacion">Validación</button>'
        '<button class="tab-btn" data-tab="fuentes">Fuentes</button>'
        "</nav>"
    )

    test_section = """<div class="test-bar">
  <div class="kpi">Respondidas<b id="s-resp">0</b></div>
  <div class="kpi">Aciertos<b id="s-correct">0</b></div>
  <div class="kpi">Fallos<b id="s-wrong">0</b></div>
  <div class="kpi">Nota (−1/3)<b id="s-score">0.00</b></div>
  <button class="btn-c" onclick="correctAll()">Corregir todo</button>
  <button class="btn-r" onclick="resetTest()">Reiniciar</button>
</div>
<div id="test-container"></div>"""

    js = ("""const questions = %s;
function renderQuestions(){
  const c=document.getElementById('test-container');
  c.innerHTML=questions.map((q,i)=>`
    <div class="question" data-q="${i}">
      <div class="q-num">Pregunta ${i+1}</div>
      <div class="q-text">${q.q}</div>
      <div class="q-options">${q.opts.map((o,j)=>`<div class="q-opt" data-opt="${j}" onclick="selectOption(${i},${j})"><div class="q-letter">${String.fromCharCode(65+j)}</div><div>${o}</div></div>`).join('')}</div>
      <div class="q-answer"><strong>Correcta: ${String.fromCharCode(65+q.correct)}) ${q.opts[q.correct]}</strong><br>${q.expl}<div class="q-ref">Referencia: tema-%s-contenido.md ${q.ref}</div></div>
    </div>`).join('');
}
const answers={};
function selectOption(qi,oi){answers[qi]=oi;const q=document.querySelector(`[data-q="${qi}"]`);q.querySelectorAll('.q-opt').forEach(e=>e.classList.remove('selected'));q.querySelector(`[data-opt="${oi}"]`).classList.add('selected');updateScore();}
function correctAll(){questions.forEach((q,i)=>{const el=document.querySelector(`[data-q="${i}"]`);el.querySelectorAll('.q-opt').forEach((e,j)=>{e.classList.remove('selected','correct','wrong');if(j===q.correct)e.classList.add('correct');else if(answers[i]===j)e.classList.add('wrong');});el.querySelector('.q-answer').classList.add('show');});}
function resetTest(){Object.keys(answers).forEach(k=>delete answers[k]);document.querySelectorAll('.q-opt').forEach(e=>e.classList.remove('selected','correct','wrong'));document.querySelectorAll('.q-answer').forEach(e=>e.classList.remove('show'));updateScore();}
function updateScore(){const r=Object.keys(answers).length;const ok=Object.entries(answers).filter(([i,v])=>questions[i].correct===v).length;const w=r-ok;document.getElementById('s-resp').textContent=r;document.getElementById('s-correct').textContent=ok;document.getElementById('s-wrong').textContent=w;document.getElementById('s-score').textContent=Math.max(0,ok-w/3).toFixed(2);}
function showTab(name,btn){document.querySelectorAll('.tab-content').forEach(e=>e.classList.remove('active'));document.querySelectorAll('.tab-btn').forEach(e=>e.classList.remove('active'));const t=document.getElementById('tab-'+name);if(t)t.classList.add('active');if(btn)btn.classList.add('active');try{window.scrollTo(0,0);}catch(e){}}
function initTabs(){document.querySelectorAll('.tab-btn[data-tab]').forEach(b=>b.addEventListener('click',function(){showTab(this.dataset.tab,this);}));try{renderQuestions();}catch(e){console.error(e);}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initTabs);else initTabs();""" % (qjson, NN))

    doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tema {NN} {VERSION} — ETRIVIUM IAM</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{css}
.indice-outline ol{{margin:6px 0 6px 18px}}
.hero h1{{padding-right:96px}}
</style>
</head>
<body>
<div class="wrap">
{nav}
<section id="tab-inicio" class="tab-content active">{inicio}</section>
<section id="tab-contenido" class="tab-content"><hr>
{contenido}</section>
<section id="tab-indice" class="tab-content"><hr>
{indice}</section>
<section id="tab-diagramas" class="tab-content"><hr>
{diagramas}</section>
<section id="tab-test" class="tab-content">
{test_section}</section>
<section id="tab-casos" class="tab-content"><hr>
{casos}</section>
<section id="tab-validacion" class="tab-content"><hr>
{validacion}</section>
<section id="tab-fuentes" class="tab-content"><hr>
{fuentes}</section>
<div class="footer">Tema {NN} · {VERSION} · {FECHA} · ETRIVIUM — IAM Ayuntamiento de Madrid · Generado desde los .md (sincronizado)</div>
</div>
<script>
{js}
</script>
</body>
</html>"""

    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)

    svg_count = doc.count("<svg")
    nested = len(re.findall(r"[^>]<ul><li>", contenido)) + len(re.findall(r"[^>]<ol><li>", contenido))
    print(f"index.html generado: {len(doc)} bytes")
    print(f"  · Preguntas test: {len(questions)}")
    dist = {0: 0, 1: 0, 2: 0}
    for q in questions:
        dist[q["correct"]] += 1
    print(f"  · Distribución A/B/C: {dist[0]}/{dist[1]}/{dist[2]}")
    print(f"  · Diagramas SVG: {svg_count}")
    print(f"  · Listas anidadas reales en Contenido: {nested}")
    print(f"  · Pestaña Índice: {'data-tab=\"indice\"' in doc}")


if __name__ == "__main__":
    build()
