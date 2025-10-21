import scrapy

class Sp500Spider(scrapy.Spider):
    name = "sp500"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        rows = response.css('table.table tbody tr')
        # Only ptake the top 20 companies
        for row in rows[:20]:
            number = row.css('td:nth-child(1)::text').get()
            company = row.css('td:nth-child(2) a::text').get()
            symbol = row.css('td:nth-child(3) a::text').get()
            ytd_return = row.css('td:nth-child(4)::text').get()
            
            yield {
                'number': number.strip() if number else None,
                'company': company.strip() if company else None,
                'symbol': symbol.strip() if symbol else None,
                'ytd_return': ytd_return.strip() if ytd_return else None
            }