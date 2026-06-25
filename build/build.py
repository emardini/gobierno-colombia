#!/usr/bin/env python3
"""
Build del proyecto. Une los archivos de docs/ (segun build/manifest.txt) en un
unico markdown y, si pandoc esta disponible, genera el Word.

Fuente de verdad: los archivos de docs/. Este script NO los edita; solo deriva
los entregables. Uso:  python3 build/build.py
"""
import os, re, sys, shutil, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "build", "manifest.txt")
OUT_MD = os.path.join(ROOT, "programa-completo.md")
OUT_DOCX = os.path.join(ROOT, "dist", "estado-en-el-territorio.docx")

TITLE = "PROGRAMA DE GOBIERNO: ESTADO EN EL TERRITORIO"
SUBTITLE = "Empleo de calidad, instituciones honestas y carga justa"
DATE = "Version reorganizada e integrada"

FRONT_MATTER = f"""---
title: "{TITLE}"
subtitle: "{SUBTITLE}"
date: "{DATE}"
lang: es
---
"""

GENERATED_NOTE = (
    "<!-- ARCHIVO GENERADO POR build/build.py. NO LO EDITES A MANO. "
    "Edita los archivos de docs/ y vuelve a correr el build. -->\n"
)

BANNER_PREFIXES = ("> **NÚCLEO", "> **EJECUCIÓN", "> **MIXTO", "> **META")


def read_manifest():
    files = []
    with open(MANIFEST, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            files.append(s)
    return files


def all_doc_files():
    found = []
    for dirpath, _, names in os.walk(os.path.join(ROOT, "docs")):
        for n in names:
            if n.endswith(".md"):
                rel = os.path.relpath(os.path.join(dirpath, n), ROOT)
                found.append(rel.replace("\\", "/"))
    return set(found)


def strip_banner(text):
    """Quita el banner de capa (NUCLEO/EJECUCION/MIXTO/META) del inicio del archivo."""
    lines = text.split("\n")
    # saltar lineas en blanco iniciales
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and lines[i].lstrip().startswith(BANNER_PREFIXES):
        i += 1
        # saltar la linea en blanco que sigue al banner
        while i < len(lines) and lines[i].strip() == "":
            i += 1
    return "\n".join(lines[i:]).rstrip()


def validate(manifest, found):
    errs, warns = [], []
    for rel in manifest:
        if not os.path.exists(os.path.join(ROOT, rel)):
            errs.append(f"El manifiesto referencia un archivo que no existe: {rel}")
    in_manifest = set(manifest)
    for rel in sorted(found - in_manifest):
        warns.append(f"Archivo en docs/ que NO esta en el manifiesto (no se incluira): {rel}")
    return errs, warns


def main():
    manifest = read_manifest()
    found = all_doc_files()
    errs, warns = validate(manifest, found)
    for w in warns:
        print("AVISO:", w)
    if errs:
        for e in errs:
            print("ERROR:", e)
        sys.exit(1)

    partes = []
    for rel in manifest:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            partes.append(strip_banner(f.read()))
    cuerpo = "\n\n".join(partes).strip() + "\n"

    os.makedirs(os.path.dirname(OUT_DOCX), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(FRONT_MATTER + GENERATED_NOTE + "\n" + cuerpo)
    print(f"OK markdown: {os.path.relpath(OUT_MD, ROOT)}  ({len(manifest)} secciones)")

    # Word con pandoc si esta disponible
    if shutil.which("pandoc"):
        cmd = [
            "pandoc", OUT_MD, "-o", OUT_DOCX,
            "--toc", "--toc-depth=2",
            "--metadata", f"title={TITLE}",
        ]
        try:
            subprocess.run(cmd, check=True)
            print(f"OK Word:     {os.path.relpath(OUT_DOCX, ROOT)}")
        except subprocess.CalledProcessError as e:
            print("ERROR al generar el Word con pandoc:", e)
            sys.exit(1)
    else:
        print("AVISO: pandoc no esta instalado; se genero solo el markdown.")
        print("       Instala pandoc para producir el Word, o usa el flujo de GitHub Actions.")


if __name__ == "__main__":
    main()
