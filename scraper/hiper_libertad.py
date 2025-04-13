
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
        "https://www.hiperlibertad.com.ar/pan-baguete-x-unidad-2/p",
        "https://www.hiperlibertad.com.ar/galletitas-sandwich-mediatarde-x3-107-g/p",
        "https://www.hiperlibertad.com.ar/galletitas-surtido-diversi-n-en-bolsa-400-g/p",
        "https://www.hiperlibertad.com.ar/arroz-blanco-largo-fino-molinos-ala-1-kg/p",
        "https://www.hiperlibertad.com.ar/harina-000-favorita-con-vitaminas-x-1-kg/p",
        "https://www.hiperlibertad.com.ar/papa-cepillada-x-1-kg/p",
        "https://www.hiperlibertad.com.ar/batata-x-500-g/p",
        "https://www.hiperlibertad.com.ar/azucar-ledesma-clasica-1-kg/p",
        "https://www.hiperlibertad.com.ar/dulce-de-leche-clasico-ilolay-400-gr/p",
        "https://www.hiperlibertad.com.ar/cebolla-x-500-g/p",
        "https://www.hiperlibertad.com.ar/manzana-roja-fraccionada-x-1kg/p",
        "https://www.hiperlibertad.com.ar/pollo-fresco-x-un-aprox-2-5kg/p",
        "https://www.hiperlibertad.com.ar/salame-milan-lario-feteado-150g/p",
        "https://www.hiperlibertad.com.ar/huevo-blanco-mediterranea-x6u/p",
        "https://www.hiperlibertad.com.ar/leche-entera-la-seren-sima-mult-vit-3-sachet-x-1-lt/p",
        "https://www.hiperlibertad.com.ar/queso-crema-cl-sico-casancrem-290gr-3/p",
        "https://www.hiperlibertad.com.ar/yogur-bebible-vainilla-la-seren-sima-cl-sico-900gr-2/p",
        "https://www.hiperlibertad.com.ar/manteca-primer-premio-100gr/p",
        "https://www.hiperlibertad.com.ar/aceite-de-girasol-natura-1-5-lt/p",
        "https://www.hiperlibertad.com.ar/sal-final-celusal-paquete-500-gr/p",
        "https://www.hiperlibertad.com.ar/vinagre-vino-alcazar-x-500ml/p",
        "https://www.hiperlibertad.com.ar/caf-cabrales-al-grano-torrado-molido-x-500-gr/p",
        "https://www.hiperlibertad.com.ar/yerba-chamigo-sin-tacc-x-1-kg/p",
        "https://www.hiperlibertad.com.ar/mayonesa-natura-250-cc/p"
    ]

# 05 - Configuro la funcion Parse:

    def parse(self, response):
            nombre_producto = response.css('span.vtex-store-components-3-x-productBrand::text').get()

            # El precio esta dividido en 2 span diferentes (enteros y decimales)
            precio_normal_oferta_entero = response.css("span.vtex-product-price-1-x-currencyInteger::text").getall()
            precio_normal_oferta_decimales =  response.css("span.vtex-product-price-1-x-currencyFraction::text").get()

            # Extraer precio desde el tag meta
            precio_normal = response.css('meta[property="product:price:amount"]::attr(content)').get()

            # Seleccionar el precio normal en caso de oferta, si no el precio  del tag meta

            if precio_normal_oferta_entero:
              precio = f'{ precio_normal_oferta_entero[0]}{precio_normal_oferta_entero[1]}, {precio_normal_oferta_decimales[1]}'
            elif precio_normal:
              precio = precio_normal.replace(".",",")
            else:
              precio = "No disponible"

            yield {
                "fecha": fechaActual,
                "hora": horaActual,
                "Nombre Producto": nombre_producto,
                "Precio": precio,
                "URL": response.url
            }
