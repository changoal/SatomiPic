# -*- coding: utf-8 -*-
BOT_NAME = 'satomi_pic'

SPIDER_MODULES = ['satomi_pic.spiders']
NEWSPIDER_MODULE = 'satomi_pic.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    # 'Referer':
    #     'https://movie.douban.com/',
    # 'Host':
    #     'movie.douban.com'
}

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}

IMAGES_STORE = 'path_to_your_dir'
