# 🛒 Evolución de la Canasta Básica en Córdoba, Argentina durante el 2025
---

## 🧑 Autor
* Jonathan Manuel Palomeque
* Estudiante de Ciencia de Datos e Inteligencia Artificial
* LinkedIn: [jonathan-palomeque](https://www.linkedin.com/in/jonathan-palomeque/)
* GitHub: [manuelpalomeque](https://github.com/manuelpalomeque)
---

## Descripción

Este proyecto analiza la evolución de precios de productos de la [canasta básica](https://www.indec.gob.ar/ftp/cuadros/sociedad/preguntas_frecuentes_cba_cbt.pdf) relevados directamente de sitios web de supermercados de Córdoba (Argentina) durante el 2025, mediante técnicas de web scraping.

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
│   ├── hiper_libertad.py
│   └── disco.py
├── data/
│   ├── relevamiento_precios_hiper_libertad.csv
│   ├── relevamiento_precios_disco.csv
│   └── precios_limpios/
├── notebooks/
│   ├── hiper_libertad.ipynb
|   |── disco.ipynb 
│   ├── 01_eda.ipynb
│   └── 02_modelo_tendencias.ipynb
├── visualizaciones/
│   └── dashboard_precios.pdf
├── Canasta Básica Alimentaria.png
├── Relevamiento de productos- Enlaces.pdf
├── requirements.txt
└── README.md
```

---

## 🧰 Tecnologías utilizadas
Lenguaje: Python 3.10

* Scraping: requests, BeautifulSoup, Selenium
* Procesamiento de datos: pandas, numpy
* Visualización: matplotlib, seaborn, plotly, Power BI
* Automatización (a futuro): cron, Airflow o Prefect
* Versionado de código: Git

---

## 📤 Fuentes de datos
Los datos fueron extraídos de las siguientes cadenas de supermercados:

* Hiper Libertad – https://www.hiperlibertad.com.ar/
* Disco – https://www.disco.com.ar/

⚠️ Importante: Este proyecto tiene fines educativos y no persigue fines comerciales. Se respetan los términos de uso de cada sitio web.

---

## ⚙️ Instrucciones para ejecutar el scraper
1. Clonar el repositorio:

``` bash
git clone https://github.com/tu_usuario/canasta-basica-cba.git
cd canasta-basica-cba
```
2. Instalar dependencias:

``` bash
pip install -r requirements.txt
```
3. Ejecutar el scraper para una cadena específica:

``` bash
python scraper/carrefour.py
```

---

## 📊 Análisis y visualizaciones
Los notebooks dentro de /notebooks contienen el análisis exploratorio y los modelos predictivos de tendencia de precios.

Se incluyen visualizaciones de:

* Evolución de precios por producto y categoría.
* Comparación entre cadenas de supermercados.
* Productos con mayor aumento o baja en el período.

📁 Ver carpeta visualizaciones/ para resultados gráficos y dashboards.

---

## 🧠 Hallazgos clave
* Los productos de limpieza y lácteos presentan mayor volatilidad de precios.
* Algunos supermercados aplican aumentos similares a intervalos regulares.
* Se detectaron diferencias de hasta un 40% en productos equivalentes entre cadenas.

---

## 📝 Contribuciones y mejoras
Este proyecto está en desarrollo. Se planea:

* Incorporar nuevos supermercados.
* Mejorar la automatización con pipelines programados.
* Publicar un dashboard online en Power BI o Streamlit.
* 
Contribuciones son bienvenidas. Podés abrir un issue o hacer un pull request.

---

## 📄 Licencia
Este proyecto está bajo la Licencia MIT.
