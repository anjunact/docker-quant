
from django.core.management.base import BaseCommand, CommandError
from stock.models import Stock as Stock
import tushare as ts
import csv

class Command(BaseCommand):
    help = 'get A 股数据'

    def handle(self, *args, **options):
        df = ts.get_stock_basics()
        df.to_csv('a.csv', encoding='utf-8',columns=['name'])
        with open('a.csv') as f:
            reader = csv.reader(f)
            for i,row in enumerate(reader):
                if i==0:
                    continue
                _,created=Stock.objects.get_or_create(
                    code=row[0],
                    name=row[1],
                )
