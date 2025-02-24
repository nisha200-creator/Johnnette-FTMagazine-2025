
from django.contrib import admin
from Megazine.models import HomeArticle

class HomeArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


admin.site.register(HomeArticle, HomeArticleAdmin)  


# Register your models here.
