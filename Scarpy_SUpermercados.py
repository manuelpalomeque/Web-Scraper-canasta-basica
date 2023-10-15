# Para este proyecto, busco extraer los datos del producto y del precio del mismo de la pagina web de Hiper Libertad:
# https://www.hiperlibertad.com.ar/

# 01 - Importo librerias necesarias:
import scrapy
from datetime import datetime

# 02-  Configuro el la fecha actual:
hora = datetime.now().time()
fecha = datetime.now().today()

#03- Formato correcto para la fecha y hora:
fHoraMinuto = "%H:%M"
fDiaMesAño = "%d-%m-%Y"

horaActual = hora.strftime(fHoraMinuto)
fechaActual = fecha.strftime(fDiaMesAño)

# prueba de resultado:
# print(f'''
# La fecha actual es: {fechaActual}
# La hora actual es: {horaActual}''')

# 04 - Configuro la araña:

class ProductosSpider(scrapy.Spider):
    name = 'Canasta'
    start_urls = [
        # las paginas deben estar en comillas dobles, ya que sino da error 404
        "https://www.hiperlibertad.com.ar/pan-frances-x-500-g/p",
        # "https://www.hiperlibertad.com.ar/galleta-la-providencia-crackers-505-gr/p",
        # "https://www.hiperlibertad.com.ar/galletas-terrabusi-variedad-mix-x-170-gr-2/p",
        # "https://www.hiperlibertad.com.ar/arroz-parboil-gallo-oro-x-500-gr/p",
        # "https://www.hiperlibertad.com.ar/harina-de-trigo-morixe-000-1-kg/p",
        # "https://www.hiperlibertad.com.ar/fideos-tallarines-lucchetti-500-gr/p",
        # "https://www.hiperlibertad.com.ar/papa-cepillada-x-1-kg/p",
        # "https://www.hiperlibertad.com.ar/batata-x-500-g/p",
        # "https://www.hiperlibertad.com.ar/azucar-azucel-1-kilo/p",
        # "https://www.hiperlibertad.com.ar/mermelada-dulcor-durazno-frasco-454-gr/p",
        # "https://www.hiperlibertad.com.ar/lentejas-taeq-200gr/p",
        # "https://www.hiperlibertad.com.ar/arvejas-inca-lata-x-350-gr/p",
        # "https://www.hiperlibertad.com.ar/paquete-de-acelga-x-un/p",
        # "https://www.hiperlibertad.com.ar/cebolla-x-500-g/p",
        # "https://www.hiperlibertad.com.ar/lechuga-mantecosa-x-500-g/p",
        # "https://www.hiperlibertad.com.ar/tomate-perita-x-500g/p",
        # "https://www.hiperlibertad.com.ar/calabacin-anquito-fraccionado-x-700gr-1-2-calabacin/p",
        # "https://www.hiperlibertad.com.ar/mandarina-x-1kg/p",
        # "https://www.hiperlibertad.com.ar/naranja-p-jugo-x-1kg/p",
        # "https://www.hiperlibertad.com.ar/banana-x-kg-ecomm/p",
        # "https://www.hiperlibertad.com.ar/pollo-fresco-x-un-aprox-2-5kg/p",
        # "https://www.hiperlibertad.com.ar/pulpa-de-jamon-de-cerdo-x-500-g/p",
        # "https://www.hiperlibertad.com.ar/milanesa-de-bola-de-lomo-de-novillito-x-500-g/p",
        # "https://www.hiperlibertad.com.ar/huevo-color-carnave-carton-x-12-unidades/p",
        # "https://www.hiperlibertad.com.ar/leche-entera-c-calcio-la-lacteo-larga-vida-1-l/p",
        # "https://www.hiperlibertad.com.ar/manteca-tonadita-200gr/p",
        # "https://www.hiperlibertad.com.ar/aceite-pureza-girasol-900-cc/p",
        # "https://www.hiperlibertad.com.ar/brahma-chopp-can-4x6-473cc/p",
        # "https://www.hiperlibertad.com.ar/sal-fina-dos-anclas-500-gr-2/p",
        # "https://www.hiperlibertad.com.ar/mayonesa-hellmanns-clasica-x-475-gr/p",
        # "https://www.hiperlibertad.com.ar/cafe-molido-bonafide-sensaciones-torrado-suave-500-gr/p",
        #"https://www.hiperlibertad.com.ar/yerba-playadito-suave-bcp-1kg/p",
    ]

    def parse(self, response):
        for span in response.css("div.pr0 items-stretch vtex-flex-layout-0-x-stretchChildrenWidth flex"):
            yield {
                "fecha": fechaActual,
                "hora": horaActual,
                "pagina": response.css("li.next a::attr(href)").get(),
                "Producto": span.css("span.vtex-store-components-3-x-productBrand vtex-store-components-3-x-productBrand--pdp-product-name::text").get(),
            }

# Extrer los datos:
# scrapy runspider Scarpy_SUpermercados.py -o productos.csv