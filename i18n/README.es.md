<p align="center">
  <img src="../assets/Capp_Zeus.png" width="260" alt="ZeusDeveloper Logo">
</p>

<h1 align="center">ZeusDeveloper</h1>

<p align="center">
  <em>Código mínimo. Biblioteca estándar nativa. Límites de seguridad reforzados.</em>
</p>

<p align="center">
  <a href="../README.md">English</a> &middot;
  <a href="README.it.md">Italiano</a> &middot;
  <a href="README.es.md"><strong>Español</strong></a> &middot;
  <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/release-v1.2.0-111827?style=flat-square" alt="Versión">
  <img src="https://img.shields.io/badge/works%20with-20%2B%20agents-111827?style=flat-square" alt="Compatible con más de 20 agentes">
  <img src="https://img.shields.io/badge/license-MIT-111827?style=flat-square" alt="Licencia">
</p>

---

## Resultados de Benchmark

<p align="center">
  <img src="../assets/chart-overview.svg" width="880" alt="Resumen de Benchmark de ZeusDeveloper">
</p>

<p align="center">
  <img src="../assets/chart-tests.svg" width="880" alt="Confiabilidad y Pruebas de ZeusDeveloper">
</p>

<p align="center">
  <img src="../assets/chart-tiers.svg" width="880" alt="Ahorro de Tokens por Nivel Operativo">
</p>

---

## Caso de Estudio: Antes y Después

<p align="center">
  <img src="../assets/chart-before-after.svg" width="880" alt="Caso de estudio Antes y Después">
</p>

Los asistentes de código con IA suelen generar complejidad innecesaria:
- Pides un limitador de tasa y agregan paquetes externos con múltiples archivos de configuración.
- Pides corregir un error e introducen clases intermedias e interfaces no solicitadas.
- Gastan tokens en saludos, disculpas y resúmenes antes de mostrar el código.

ZeusDeveloper mantiene cambios mínimos garantizando módulos limpios, uso de APIs nativas y validación estricta de entradas.

---

## Pautas Principales

1. **El cambio mínimo y robusto**: Resuelve el requisito modificando lo mínimo necesario. Evita parámetros hipotéticos o utilidades innecesarias.
2. **Biblioteca estándar primero**: Utiliza funciones integradas en el entorno antes de incorporar dependencias externas.
3. **Defensa de los límites de confianza**: Valida siempre las entradas externas, propaga errores y asegura autenticación y permisos.
4. **Respuestas directas**: Muestra la solución concreta (`[Destino] [Acción] [Motivo]`) seguida del diff. Sin cortesías innecesarias.
5. **Separación de responsabilidades**: Mantén la lógica de negocio separada del transporte de red y almacenamiento.
6. **Verificación determinista**: Añade pruebas unitarias o aserciones de invariantes para toda lógica crítica.

---

## Niveles Operativos

| Nivel | Comando | Uso |
| :--- | :--- | :--- |
| **Hermes** | `/zeus hermes` | Correcciones rápidas y directas con mínima fricción. Señala deuda técnica en una línea. |
| **Zeus** | `/zeus` | Modo predeterminado. Cambios mínimos, librerías nativas y validaciones de seguridad. |
| **Titan** | `/zeus titan` | Cuestiona requisitos sobredimensionados antes de escribir código. |
| **Oracle** | `/zeus oracle` | Respuestas de alta densidad. Elimina explicaciones no esenciales (-78% de tokens). |

---

## Panel de Monitoreo Local

Inicia el panel interactivo en tu navegador:

```bash
python board.py
```

Abre una interfaz en `http://localhost:3000` con el resumen de sesiones y métricas de ahorro.

---

## Instalación

### Configuración Universal
Descarga [`AGENTS.md`](../AGENTS.md) en la raíz de tu proyecto:
```bash
curl -o AGENTS.md https://raw.githubusercontent.com/24Capp/ZeusDeveloper/main/AGENTS.md
```

### Antigravity & Gemini CLI
```bash
agy plugin install https://github.com/24Capp/ZeusDeveloper
```

### Claude Code
```text
/plugin marketplace add 24Capp/ZeusDeveloper
/plugin install zeus@zeus
```

---

## Licencia
MIT © 2026 Luca Quagliozzi (24Capp)
