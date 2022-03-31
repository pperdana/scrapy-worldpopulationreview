import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = [
        'https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//tbody/tr")
        for item in rows:
            country = item.xpath(".//td/a/text()").get()
            ratio = item.xpath(".//td[2]/text()").get()

            yield {
                "country ": country,
                "gdp_debt ": ratio
            }
