from pathlib import Path
import scrapy

class CitasSpider(scrapy.Spider):
    name = 'citas'
    # el nombre identifica la Araña. Debe ser único dentro de un proyecto, es decir, no se puede establecer
    # el mismo nombre para diferentes Spiders

    def iniciarSolicitudes(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f"Citas-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f'Archivo guardado {filename}')
