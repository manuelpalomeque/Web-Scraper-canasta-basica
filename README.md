# 🛒 Evolución de la Canasta Básica en Córdoba, Argentina

Este proyecto analiza la evolución de precios de productos de la canasta básica relevados directamente de sitios web de supermercados de Córdoba (Argentina) mediante técnicas de web scraping.

El objetivo es generar una herramienta automatizada que permita observar y visualizar variaciones de precios entre cadenas, categorías de productos y momentos del tiempo, contribuyendo a una mayor transparencia y análisis económico-social.

---

## 📌 Objetivos del proyecto

- Extraer datos de precios desde diferentes supermercados cordobeses.
- Automatizar la recolección periódica para analizar la evolución en el tiempo.
- Unificar y limpiar los datos para facilitar el análisis.
- Visualizar las variaciones de precios por producto, categoría y supermercado.
- Identificar patrones de inflación, estabilidad o anomalías.

---

## 🧱 Arquitectura del Proyecto

```bash
📁 canasta-basica-cba/
├── scraper/
│   ├── carrefour.py
│   ├── disco.py
│   └── supermercados_utils.py
├── data/
│   ├── precios_crudos/
│   └── precios_limpios/
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_modelo_tendencias.ipynb
├── visualizaciones/
│   └── dashboard_precios.pdf
├── requirements.txt
└── README.md
