
# 01 - Importo librerias necesarias:
import scrapy
from scrapy.cmdline import execute
from datetime import datetime
import pytz


# 02-  Configuro el la fecha actual:
zona_arg = pytz.timezone('America/Argentina/Buenos_Aires')

hora = datetime.now(zona_arg).time()
fecha = datetime.now().today()

#03- Formato correcto para la fecha y hora:
fHoraMinuto = "%H:%M"
fDiaMesAño = "%d-%m-%Y"

horaActual = hora.strftime(fHoraMinuto)
fechaActual = fecha.strftime(fDiaMesAño)

# prueba de resultado:
#print(f'''
#La fecha actual es: {fechaActual}
#La hora actual es: {horaActual}''')

# 04 - Configuro la araña:
class ProductosSpider(scrapy.Spider):
    name = 'Canasta'
    start_urls = [
        "https://www.hiperlibertad.com.ar/pan-frances-x-500-g/p",
        "https://www.hiperlibertad.com.ar/galletita-cracker-la-providencia-clasica-x303g/p",
        "https://www.hiperlibertad.com.ar/galletas-terrabusi-variedad-dorada-x-300-gr/p",
        "https://www.hiperlibertad.com.ar/arroz-parboil-taeq-240gr/p",
        "https://www.hiperlibertad.com.ar/harina-de-trigo-morixe-000-1-kg/p",
        "https://www.hiperlibertad.com.ar/fideos-tallarines-n7-matarazzo-x-500-gr/p",
        "https://www.hiperlibertad.com.ar/papa-cepillada-x-1-kg/p",
        "https://www.hiperlibertad.com.ar/batata-x-500-g/p",
        "https://www.hiperlibertad.com.ar/azucar-azucel-1-kilo/p",
        "https://www.hiperlibertad.com.ar/mermelada-dulcor-durazno-frasco-454-gr/p",
        "https://www.hiperlibertad.com.ar/lentejas-taeq-200gr/p",
        "https://www.hiperlibertad.com.ar/arvejas-montenevi-x-340-gr/p",
        "https://www.hiperlibertad.com.ar/acelga-congelada-green-life-500-g/p",
        "https://www.hiperlibertad.com.ar/cebolla-x-500-g/p",
        "https://www.hiperlibertad.com.ar/bandeja-lechuga-mantecosa-lavada-sue-o-verde-x-200-gr/p",
        "https://www.hiperlibertad.com.ar/tomate-perita-x-500g/p",
        "https://www.hiperlibertad.com.ar/calabacin-anquito-fraccionado-x-700gr-1-2-calabacin/p",
        "https://www.hiperlibertad.com.ar/mandarina-x-1kg/p",
        "https://www.hiperlibertad.com.ar/naranja-p-jugo-x-1kg/p",
        "https://www.hiperlibertad.com.ar/banana-x-kg-ecomm/p",
        "https://www.hiperlibertad.com.ar/pollo-fresco-x-un-aprox-2-5kg/p",
        "https://www.hiperlibertad.com.ar/pulpa-de-jamon-de-cerdo-x-500-g/p",
        "https://www.hiperlibertad.com.ar/milanesa-de-bola-de-lomo-de-novillito-x-500-g/p",
        "https://www.hiperlibertad.com.ar/huevo-blanco-carnave-carton-x-12-unidades/p",
        "https://www.hiperlibertad.com.ar/leche-entera-c-calcio-la-lacteo-larga-vida-1-l/p",
        "https://www.hiperlibertad.com.ar/manteca-tonadita-200gr/p",
        "https://www.hiperlibertad.com.ar/aceite-de-girasol-alsamar-x-900-ml/p",
        "https://www.hiperlibertad.com.ar/brahma-chopp-can-4x6-473cc/p",
        "https://www.hiperlibertad.com.ar/sal-fina-dos-anclas-250-gr/p",
        "https://www.hiperlibertad.com.ar/mayonesa-hellmanns-clasica-x-475-gr/p",
        "https://www.hiperlibertad.com.ar/cafe-molido-bonafide-sensaciones-torrado-intenso-500-gr/p",
        "https://www.hiperlibertad.com.ar/yerba-playadito-suave-bcp-1kg/p",
    ]

# 05 - Configuro la funcion Parse:

    def parse(self, response):
            nombre_producto = response.css('span.vtex-store-components-3-x-productBrand::text').get()

            # El precio esta dividido en 2 span diferentes (enteros y decimales)
            precio_entero = response.css("span.vtex-product-price-1-x-currencyInteger::text").getall()
            precio_decimales =  response.css("span.vtex-product-price-1-x-currencyFraction::text").get()

            if precio_entero: # Si tiene un precio configurado
              if len(precio_entero) == 1:  # Tiene solamente un preciosin ofertas
                precio = f'{precio_entero[0]}, {precio_decimales}'
              elif len(precio_entero[0])> 1: # cuando el producto tiene un precio anterior, enfatizando una oferta
                precio = f'{precio_entero[1]}, {precio_decimales[1]}'  # Se toma el segundo valor, que es el precio real sin promocion.
              else:
                precio = f'{precio_entero[0]}.{precio_entero[1]}, {precio_decimales}' # cuando tiene entero y decimales
            else: # Si no tiene un precion configurado
              precio = "No disponible"

            yield {
                "fecha": fechaActual,
                "hora": horaActual,
                "Nombre Producto": nombre_producto,
                "Precio": precio,
                "URL": response.url
            }
