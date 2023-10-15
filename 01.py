# EXTRAER CITAS FAMOSAS DE UNA PAGINA WEB
#
# Se extraeran citas de la  siguiente pagina: https://quotes.toscrape.com/

# 1 - Importar libreria Scrapy
import scrapy

#2- Crear la clase para exrtraer los datos
class CitasSpider(scrapy.Spider):
    name = "quotes" # name debe estar en ingles
    # defino las urls donde quiere trabajar:
    start_urls  = [ #start_urls  debe estar en ingles
        "https://quotes.toscrape.com/tag/humor/",
    ]
    # Funcion Parse para  obtener la respuesta como argumento:
    def parse(self, response):
        for quote in response.css("div.quote"):
            # Se define el formato con el cual se va a mostrar el texto en el archivo de salida:
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# Ejecutar desde cmd, usando el runspider comando:
# scrapy runspider 01.py -o citas.json
# se guarda un json con los datos extraidos
# Se intento guardar como .txt pero no funciona
# Sis e puede fuardar como .csv