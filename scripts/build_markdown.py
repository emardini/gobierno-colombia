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
        ('docs/00-nota-de-version.md', 'Nota de esta versión'),
        ('docs/01-vision-2042.md', 'Visión Colombia 2042'),
        ('docs/02-modelo-de-pais.md', '0. El Modelo de País: La Brújula'),
        ('docs/03-diagnostico.md', '1. Diagnóstico: Dos Raíces, No Veinte Problemas'),
        ('docs/04-principios.md', '2. Principios Rectores'),
        ('docs/05-columna-vertebral.md', '3. La Columna Vertebral: Estado en el Territorio'),
        ('docs/06-rendimiento-compuesto.md', 'El Rendimiento Compuesto del Modelo de Nodos'),
        ('docs/frentes/frente-01-empleo.md', 'Frente I: Empleo de Calidad y Desarrollo de la Periferia'),
        ('docs/frentes/frente-02-reforma-agraria.md', 'Frente II: Reforma Agraria Integral'),
        ('docs/frentes/frente-03-seguridad.md', 'Frente III: Seguridad, Soberanía e Inteligencia'),
        ('docs/frentes/frente-04-anticorrupcion.md', 'Frente IV: Anticorrupción'),
        ('docs/frentes/frente-05-fiscal.md', 'Frente V: Sostenibilidad Fiscal'),
        ('docs/frentes/frente-06-salud.md', 'Frente VI: Salud'),
        ('docs/frentes/frente-07-educacion.md', 'Frente VII: Educación'),
        ('docs/frentes/frente-08-capacidad-estatal.md', 'Frente VIII: Capacidad Operativa del Estado'),
        ('docs/frentes/frente-09-infraestructura.md', 'Frente IX: Infraestructura Estratégica'),
        ('docs/frentes/frente-10-industria.md', 'Frente X: Industria Avanzada y Capacidad Tecnológica'),
        ('docs/frentes/frente-11-servicios-basicos.md', 'Frente XI: Piso Universal de Servicios Básicos'),
        ('docs/frentes/frente-12-ciudades-turismo.md', 'Frente XII: Ciudades, Turismo y Productividad Urbana'),
        ('docs/frentes/frente-13-integridad-mecanismos.md', 'Frente XIII: Integridad Estructural y Diseño de Mecanismos'),
        ('docs/frentes/frente-14-servicio-nacional.md', 'Frente XIV: Servicio Nacional de Vida'),
        ('docs/frentes/frente-15-medio-ambiente.md', 'Frente XV: Medio Ambiente, Agua y Uso de los Recursos Naturales'),
        ('docs/transversal/fundamentos-investigacion.md', 'Fundamentos en Investigación Reciente'),
        ('docs/transversal/dimension-deliberativa.md', 'La Dimensión Deliberativa'),
        ('docs/transversal/viabilidad-juridica.md', 'Viabilidad Jurídica de los Mecanismos'),
        ('docs/transversal/plataforma-trazabilidad.md', 'Plataforma de Trazabilidad del Gasto Público'),
        ('docs/transversal/desmantelamiento-economias-ilegales.md', 'Desmantelamiento de Economías Ilegales'),
        ('docs/transversal/cuadro-fiscal.md', 'Cuadro Fiscal de Dos Escenarios'),
        ('docs/transversal/comunicacion-publica.md', 'Comunicación Pública y Derecho a la Información'),
        ('docs/transversal/politica-exterior.md', 'Política Exterior: Interés Nacional, Autonomía y Principios'),
        ('docs/transversal/productividad-competitividad.md', 'Productividad y Competitividad Nacional'),
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
