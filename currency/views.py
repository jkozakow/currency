from django.http import HttpResponse
from django.template import loader
from lxml import html
import requests


def index(request):
    url = 'http://www.bankier.pl/waluty/kursy-walut/forex'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    # // *[ @ id = "EUR_USD-b-pip"]


    timestamp = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[1]/td[6]/text()')[0]
    eur_usd_bid = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[5]/td[2]/text()')[0]
    eur_usd_ask = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[5]/td[4]/text()')[0]
    eur_pln_bid = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[1]/td[2]/text()')[0]
    eur_pln_ask = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[2]/td[4]/text()')[0]
    usd_pln_bid = tree.xpath('// *[ @ id = "boxCurrency"] / div[2] / table[1] / tbody / tr[2] / td[2]/text()')[0]
    usd_pln_ask = tree.xpath('// *[ @ id = "boxCurrency"] / div[2] / table[1] / tbody / tr[2] / td[4]/text()')[0]
    chf_pln_bid = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[3]/td[2]/text()')[0]
    chf_pln_ask = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[3]/td[4]/text()')[0]
    gbp_pln_bid = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[4]/td[2]/text()')[0]
    gbp_pln_ask = tree.xpath('//*[@id="boxCurrency"]/div[2]/table[1]/tbody/tr[4]/td[4]/text()')[0]
    template = loader.get_template('currency/index.html')
    context = {
        'timestamp': timestamp,
        'eur_usd_bid': eur_usd_bid,
        'eur_usd_ask': eur_usd_ask,
        'eur_pln_bid': eur_pln_bid,
        'eur_pln_ask': eur_pln_ask,
        'usd_pln_bid': usd_pln_bid,
        'usd_pln_ask': usd_pln_ask,
        'chf_pln_bid': chf_pln_bid,
        'chf_pln_ask': chf_pln_ask,
        'gbp_pln_bid': gbp_pln_bid,
        'gbp_pln_ask': gbp_pln_ask
    }
    return HttpResponse(template.render(context, request))

