
# 01 importo las librerias necesarias
import scrapy 
from scrapy.cmdline import execute
from datetime import datetime
import pytz

# 02 Configuro la fecha actual
zona_arg = pytz.timezone('America/Argentina/Buenos_Aires')

hora = datetime.now(zona_arg).time()
fecha = datetime.now().today()

# 03 Formato correcto para la fecha y hora
fHoraMinuto = "%H:%M"
fDiaMesAño = "%d-%m-%Y"

horaActual = hora.strftime(fHoraMinuto)
fechaActual = fecha.strftime(fDiaMesAño)

# 04 Configuro la araña:
class ProductosSpider(scrapy.Spider):
  name = 'Canasta'
  start_urls = [
      "https://www.disco.com.ar/galletitas-de-agua-criollitas-originales-300-gr/p",
      "https://www.disco.com.ar/galletitas-surtido-bagley-400-gr-2/p",
      "https://www.disco.com.ar/arroz-grano-largo-fino-dos-hermanos-1-kg/p",
      "https://www.disco.com.ar/harina-000-vit-x-1-kg-favorita/p",
      "https://www.disco.com.ar/papa-cepillada-granel-por-kg/p",
      "https://www.disco.com.ar/batata-por-kg/p",
      "https://www.disco.com.ar/azucar-ledesma-x-1kg/p",
      "https://www.disco.com.ar/dulce-de-leche-la-serenisima-clasico-400g-2/p",
      "https://www.disco.com.ar/cebolla-superior-por-kg/p",
      "https://www.disco.com.ar/manzana-roja-por-kg-2/p",
      "https://www.disco.com.ar/pollo-fresco-con-menudos-2/p",
      "https://www.disco.com.ar/salame-milan-campo-austral-feteado-x-150-gr/p",
      "https://www.disco.com.ar/huevos-color-6-un-maxima-mp-2/p",
      "https://www.disco.com.ar/leche-entera-la-serenisima-3sachet-1lt/p",
      "https://www.disco.com.ar/queso-crema-casancrem-clasico-290-gr/p",
      "https://www.disco.com.ar/yogur-bebible-entero-la-serenisima-vainilla-900-gr/p",
      "https://www.disco.com.ar/manteca-la-serenisima-100-gr/p",
      "https://www.disco.com.ar/aceite-de-girasol-natura-1-5-l/p",
      "https://www.disco.com.ar/gaseosa-coca-cola-sabor-original-2-25-l/p",
      "https://www.disco.com.ar/cerveza-quilmes-stout-1lt/p",
      "https://www.disco.com.ar/sal-fina-celusal-500-gr/p",
      "https://www.disco.com.ar/vinagre-de-vino-cuisine-and-co-500-ml/p",
      "https://www.disco.com.ar/cafe-molido-cabrales-250-gr/p",
      "https://www.disco.com.ar/yerba-mate-sin-tacc-chamigo-1-kg/p",
      "https://www.disco.com.ar/aderezo-mayonesa-natura-237-gr/p"
  ]

# 05 Configuro la funcion Parse:
  def parse(self, response):
    nombre_producto = response.css('span.vtex-store-components-3-x-productBrand::text').get()
    precio_web = response.css('meta[property="product:price:amount"]::attr(content)').get()

    if precio_web:
      precio = precio_web
    else:
      precio = "No disponible"

    yield {
        "fecha" : fechaActual,
        "hora" : horaActual,
        "Nombre Producto": nombre_producto,
        "Precio" : precio,
        "URL" : response.url
    }
