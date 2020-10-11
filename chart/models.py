from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
    name =models.CharField(max_length=150, default='',null=True,blank=True)
    date = models.DateTimeField(default=datetime.now)
    timestamp = models.CharField(editable = False,max_length=150,blank=True,null=True)
    text = models.CharField(max_length=150, default='',null=True,blank=True)

    Colors = (
        ("#007bff","primary"),
        ("#6c757d","secondary"),
        ("#28a745","success"),
        ("#dc3545","danger"),
        ("#ffc107","warning"),
        ("#17a2b8","info"),
    )
    color = models.CharField(max_length=30,choices=Colors)
    Positions = (
        ("aboveBar", "aboveBar"),
        ("belowBar", "belowBar"),
        ("inBar", "inBar"),
    )
    position = models.CharField(max_length=30,choices=Positions)
    Shapes = (
        ("circle", "circle"),
        ("arrowUp", "arrowUp"),
        ("arrowDown", "arrowDown"),
       
    )
    shape = models.CharField(max_length=30,choices=Shapes)

    def save(self , *args , **kwargs):
        # self.timestamp = datetime.fromtimestamp(self.date)
        print('self.date=',self.date)
        print('self.date type=',type(self.date))
        ts=int(datetime.timestamp(self.date)*1000)
        print('ts =',ts)
        print('ts type=',type(ts))
        self.timestamp = ts
        # self.text = ts
        # ts=int(datetime.datetime.timestamp(self.date))
        # print('ts=',ts)
        print(self.timestamp)
        print ('SAVE!!!')

        super(Event,self).save(*args,**kwargs)
    def __str__(self):
        return self.name