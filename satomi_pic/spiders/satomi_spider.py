from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Rule, CrawlSpider

from satomi_pic.items import SatomiPicItem


class SatomiSpider(CrawlSpider):
    name = "satomi_pic_spider"

    download_delay = 1

    allowed_domains = []

    start_urls = [
        'https://movie.douban.com/celebrity/1016930/photo/1253599819/'
    ]

    rules = (Rule(
        LinkExtractor(
            allow=r'https://movie.douban.com/celebrity/1016930/photo/\d+'),
        callback='parse_item',
        follow=True),)

    def parse_item(self, response):

        sel = Selector(response)

        item = SatomiPicItem()

        item['image_urls'] = sel.xpath(
            '//div[@class="photo-show"]/div[@class="photo-wp"]/a/img/@src'
        ).extract()

        yield item
