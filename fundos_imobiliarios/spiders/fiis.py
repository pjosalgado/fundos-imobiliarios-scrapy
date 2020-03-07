# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime

class FiisSpider(scrapy.Spider):

    name = 'fiis'
    
    start_urls = [
        'https://fiis.com.br/mfii11', 
        'https://fiis.com.br/bbpo11'
    ]
    
    def parse(self, response): 

        self.log('Visited: {}'.format(response.url))

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        fund_ticker = response.css('#fund-ticker::text').get().strip()
        fund_name = response.css('#fund-name::text').get().strip()

        for item in response.css('tbody > tr'): 

            columns = item.css('td::text')

            data_base = columns[0].get().strip()
            data_pagamento = columns[1].get().strip()
            cotacao_base = columns[2].get().strip()
            dy = columns[3].get().strip()
            rendimento = columns[4].get().strip()
            
            yield {
                'timestamp': timestamp, 
                'url': response.url, 
                'fund_ticker': fund_ticker, 
                'fund_name': fund_name, 
                'data_base': data_base, 
                'data_pagamento': data_pagamento, 
                'cotacao_base': cotacao_base, 
                'dy': dy, 
                'rendimento': rendimento
            }
