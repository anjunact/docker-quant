from django.core.management.base import BaseCommand, CommandError
from stock.models import Stock as Stock
from stock.management.commands.gpys import run
class Command(BaseCommand):
    help = 'get gpys data'

    def handle(self, *args, **options):
        run()
