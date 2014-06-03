from django.db import models
from django.contrib import admin
from django.db.models import permalink

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    
    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return self.name
    
    
class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)
    
    class Meta:
        ordering = ['title']
        
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absoulte_url(self):
        return ('photo_detail', None, {'object_id':self.id})
    
class PhotoInline(admin.StackedInline):
    model = Photo
    
class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    
admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
    