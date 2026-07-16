#!/usr/bin/env python3
"""
Consolida todos los archivos markdown en un documento único.
Se ejecuta automáticamente en GitHub Actions y commitea a rama 'docs'.
"""

import os
from pathlib import Path
from datetime import datetime

def read_file(path):
    """Lee un archivo."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️  No encontrado: {path}")
        return None

def build_markdown():
    """Construye documento consolidado."""

    print("🔨 Consolidando archivos markdown...")

    # Archivos a incluir (en orden lógico)
    files_to_include = [
        ('docs/05-columna-vertebral.md', 'Columna Vertebral: Estado en el Territorio'),
        ('docs/frentes/frente-01-formalidad.md', 'Frente I: Formalidad y Empleo'),
        ('docs/frentes/frente-02-reforma-agraria.md', 'Frente II: Reforma Agraria'),
        ('docs/frentes/frente-03-seguridad.md', 'Frente III: Seguridad'),
        ('docs/frentes/frente-04-salud.md', 'Frente IV: Salud'),
        ('docs/frentes/frente-05-finanzas.md', 'Frente V: Finanzas Públicas'),
        ('docs/frentes/frente-06-gasto-social.md', 'Frente VI: Gasto Social'),
        ('docs/frentes/frente-07-educacion.md', 'Frente VII: Educación y Capacidad Humana'),
        ('docs/frentes/frente-08-capacidad-estatal.md', 'Frente VIII: Capacidad Operativa'),
        ('docs/frentes/frente-09-innovacion.md', 'Frente IX: Innovación Digital'),
        ('docs/frentes/frente-10-productividad.md', 'Frente X: Productividad Rural'),
        ('docs/frentes/frente-11-servicios-basicos.md', 'Frente XI: Servicios Básicos'),
        ('docs/frentes/frente-12-ciudades.md', 'Frente XII: Ciudades Inclusivas'),
        ('docs/frentes/frente-13-integridad-mecanismos.md', 'Frente XIII: Integridad Estructural'),
        ('docs/transversal/fundamentos-investigacion.md', 'Fundamentos en Investigación Reciente'),
        ('docs/transversal/dimension-deliberativa.md', 'Dimensión Deliberativa'),
        ('docs/transversal/viabilidad-juridica.md', 'Viabilidad Jurídica'),
        ('docs/transversal/plataforma-trazabilidad.md', 'Plataforma de Trazabilidad'),
        ('docs/transversal/desmantelamiento-economias-ilegales.md', 'Desmantelamiento de Economías Ilegales'),
    ]

    # Construir documento
    doc = []

    # Portada
    doc.append("# Estado en el Territorio")
    doc.append("")
    doc.append("## Plan de Gobierno Integral 2026-2030")
    doc.append("")
    doc.append(f"**Generado:** {datetime.now().strftime('%d de %B de %Y')}")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Tabla de contenidos
    doc.append("## Contenido")
    doc.append("")
    for i, (_, section_name) in enumerate(files_to_include, 1):
        doc.append(f"{i}. {section_name}")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Procesa cada archivo
    valid_files = 0
    for file_path, section_name in files_to_include:
        if os.path.exists(file_path):
            print(f"  ✓ {section_name}")
            content = read_file(file_path)
            if content:
                # Salta línea de comentario inicial si existe
                lines = content.split('\n')
                start_idx = 0

                # Si la primera línea es un comentario markdown, saltarla
                if lines and lines[0].startswith('> **'):
                    start_idx = 1

                processed_lines = lines[start_idx:]

                # Agrega contenido
                doc.append('\n'.join(processed_lines))
                doc.append("")
                doc.append("---")
                doc.append("")
                valid_files += 1
        else:
            print(f"  ⊘ {section_name} (no encontrado)")

    if valid_files == 0:
        print("❌ No se encontraron archivos")
        return False

    # Pie de página
    doc.append("## Notas")
    doc.append("")
    doc.append("Este documento es versionado y abierto.")
    doc.append("")
    doc.append("- Si encuentras errores, abre un issue")
    doc.append("- Cambios de principio requieren justificación técnica")
    doc.append("- Parámetros se discuten con evidencia")
    doc.append("")
    doc.append(f"**Última actualización:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Guarda el documento
    output_path = 'DOCUMENTO-COMPLETO.md'
    content = '\n'.join(doc)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"\n✅ Documento consolidado exitosamente")
    print(f"   📄 {output_path}")
    print(f"   📊 {file_size_kb:.1f} KB")
    print(f"   📅 {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    return True

if __name__ == '__main__':
    try:
        success = build_markdown()
        exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Error:")
        print(f"   {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)
