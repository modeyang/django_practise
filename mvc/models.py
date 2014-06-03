from django.db import models
from django.utils import timezone
from datetime import  *
 
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()
    
    def was_published_recently(self):
        return self.pub_date >= date.today() - timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'public recently?'
     
    def __unicode__(self):
        return '%s %s' % (self.name, self.pub_date)    
     
class Choice(models.Model):
    book = models.ForeignKey(Book)
    choice = models.CharField(max_length=20)
    votes = models.IntegerField()
     
    def __unicode__(self):
        return self.choice
    

    
