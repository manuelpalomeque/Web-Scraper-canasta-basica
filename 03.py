import scrapy

#  1-  extraer fecha y hora actual:
from datetime import datetime
# instalar la libreria datetime, para extraer la fecha y hora actual para el reporte

fecha = datetime.now().today()
hora = datetime.now().time()
# darle formato correcto:
fHorasMinutos = "%H:%M"
horaActual = hora.strftime(fHorasMinutos)

fDiaMesAño = "%d-%m-%Y"
fechaActual = fecha.strftime(fDiaMesAño)

# 2-  Cnfigurar el spider para la extraccion de datos:
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"): # quote es la clase presente en el html de la pagina
            yield { # palabra reservada de python para la devolucion de datos
                "fecha": fechaActual,
                "hora": horaActual,
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

# Extrer los datos:  scrapy runspider 03.py -o citas3.csv
