from decimal import Decimal
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from stock.models import Stock, GPYS
def run():
    driver = webdriver.PhantomJS()
    # driver = webdriver.Chrome()
    stocks = Stock.objects.all().filter(gpys_id__isnull=True) #.filter(code='000001')
    for stock in stocks:
        # time.sleep(3)
        print(stock)
        driver.get("http://gpys.emoney.cn/tj/"+stock.code)
        html = BeautifulSoup(driver.page_source,'lxml')
        grades = html.select('.grade span')
        if len(grades)==0:
            continue
        grade = grades[0].text
        ggzs = html.select('#STech')[0].text
        bkzs = html.select('#BTechBlock')[0].text
        hybj = html.select('#SIndustry')[0].text
        jgdx = html.select('#SMajor')[0].text
        xypc = html.select('#SMsg')[0].text
        gsyy = html.select('#SBasic')[0].text
        if(stock.gpys):
            continue
            gpys= stock.gpys
        else:
            gpys = GPYS()

        gpys.grade = grade
        gpys.ggzs = Decimal(ggzs)
        gpys.bkzs = Decimal(bkzs)
        gpys.hybj = Decimal(hybj)
        gpys.jgdx = Decimal(jgdx)
        gpys.xypc = Decimal(xypc)
        gpys.gsyy = Decimal(gsyy)
        stock = Stock.objects.filter(code=stock.code).get()
        gpys.save()
        stock.gpys = gpys
        stock.save()
        print(gpys)

'''
ss = Stock.objects.filter(gpys__grade__contains='A')
ss = Stock.objects.filter(gpys__ggzs__gte=8.0)
'''



