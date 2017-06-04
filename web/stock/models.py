from django.db import models

class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    gpys = models.OneToOneField('GPYS', blank=True, null=True)
    def __str__(self):
        return str(self.id)+',' +self.code+','+self.name
class GPYS(models.Model):
    grade = models.CharField(max_length=5)
    ggzs = models.DecimalField(max_digits=3, decimal_places=1)
    bkzs = models.DecimalField(max_digits=3, decimal_places=1)
    hybj = models.DecimalField(max_digits=3, decimal_places=1)
    jgdx = models.DecimalField(max_digits=3, decimal_places=1)
    xypc = models.DecimalField(max_digits=3, decimal_places=1)
    gsyy = models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):
        return str(self.id)+':'+ str(self.grade)+','+str(self.ggzs) +','+str(self.bkzs)+','+str(self.hybj)+','+str(self.xypc) \
               +','+ str(self.gsyy)



