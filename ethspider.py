import scrapy


class EthspiderSpider(scrapy.Spider):
    name = "ethspider"
    allowed_domains = ["keys.lol"]
    start_urls = ["https://keys.lol/ethereum/1"]

    def parse(self, response):
        wallets = response.xpath("//div[@class = 'wallet loading flex flex-col lg:flex-row font-mono text-sm pl-2 py-1 lg:py-0']")
        for wallet in wallets :
            amount = wallet.xpath("descendant::strong/text()").get()
            if amount.split(' ')[0] != '0':
                yield {
                        'amount' : amount,
                        'private_key' : wallet.xpath("descendant::span[@class ='text-xs sm:text-sm break-words']/text()").get(),
                        'publick_key' : wallet.xpath("descendant::span[@class ='inline-block']/a[@class = 'break-words text-xs sm:text-sm']/@href").get()
                    }
        next_page_url = response.xpath("//a[@title = 'Next page']/@href").get()
        