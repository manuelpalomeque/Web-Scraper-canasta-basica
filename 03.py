import scrapy

#  1-  extraer fecha y hora actual:
from datetime import datetime
# instalar la libreria datetime, para extraer la fecha y hora actual para el reporte

fecha = datetime.now().today()
hora = datetime.now().time()

# darle formato que necesito a la fecha y hora:
fHorasMinutos = "%H:%M"
horaActual = hora.strftime(fHorasMinutos)

fDiaMesAño = "%d-%m-%Y"
fechaActual = fecha.strftime(fDiaMesAño)

# 2-  Cnfigurar el spider para la extraccion de datos:

#A - Defino la araña, con su nombre unico y las paginas donde buscara:
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        #"https://quotes.toscrape.com/page/2/",  ACA defino puntualmente una pagina
    ]

#B - establesco la funcion parse para que extraiga los datos que necesito, basandome en las etiquetas de html de la web
    def parse(self, response):
        for quote in response.css("div.quote"): # quote es la clase presente en el html de la pagina
            yield { # palabra reservada de python para la devolucion de datos
                "fecha": fechaActual,
                "hora": horaActual,
                "pagina": response.css("li.next a::attr(href)").get(),
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
        # Extraer datos de las paginas siguientes:
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page) # se crea el enlace de la pagina siguiente y la solucitud
            yield scrapy.Request(next_page, callback=self.parse)


# Extrer los datos:  scrapy runspider 03.py -o citas3.csv
