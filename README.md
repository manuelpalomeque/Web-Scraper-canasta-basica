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
- Unificar y limpiar los datos para facilitar el análisis.
- Visualizar las variaciones de precios por producto y supermercado.
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
│   └── datos_limpios.xlsx
├── notebooks/
│   ├── hiper_libertad.ipynb
|   |── disco.ipynb 
│   ├── 01_EDA_WS.ipynb
│   └── 02_modelo_tendencias.ipynb
├── Canasta Básica Alimentaria.png
├── Relevamiento de productos- Enlaces usados.pdf
├── requirements.txt
└── README.md
```

---

## 🧰 Tecnologías utilizadas
* Lenguaje: Python 3.10
* Notebook: Colab

* Scraping: Scrapy y datetime 
* Procesamiento de datos: Pandas
* Visualización: Matplotlib  y Seaborn

---

## 📤 Fuentes de datos
Los datos fueron extraídos de las siguientes cadenas de supermercados:

* [Hiper Libertad](https://www.hiperlibertad.com.ar/)
* [Disco](https://www.disco.com.ar/)

⚠️ Importante: Este proyecto tiene fines educativos y no persigue fines comerciales. Se respetan los términos de uso de cada sitio web.

---

## 📊 Análisis Exploratorio de Datos -EDA
Los notebooks dentro de [/notebooks](https://github.com/manuelpalomeque/Web-Scraper-canasta-basica/tree/main/notebooks) contienen el análisis exploratorio y los modelos predictivos de tendencia de precios.

Se incluyen visualizaciones de:
* Evolución de precios por producto y categoría.
* Comparación entre cadenas de supermercados.
* Productos con mayor aumento o baja en el período.

📁 [Ver Análisis Exploratorio de Datos -EDA](https://github.com/manuelpalomeque/Web-Scraper-canasta-basica/blob/main/notebooks/01_EDA_WS.ipynb)


📉 [Ver Modelo de Tendencias](https://github.com/manuelpalomeque/Web-Scraper-canasta-basica/blob/main/notebooks/02_modelo_tendencias_WS.ipynb)



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
