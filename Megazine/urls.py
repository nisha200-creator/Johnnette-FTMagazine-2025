
from django.conf import settings
from django.urls import path
from Megazine import views
from django.conf.urls.static import static
from django.contrib import admin




urlpatterns = [

    path("", views.home, name="home"),
    path("singlepage",views.singlepage,name='singlepage'),
    path("about",views.About,name='about'),
    path("articles",views.Articles,name='articles'),
    path("page",views.page,name='page'),  
    path("page2",views.page2,name='page2'), 
    path("contact",views.Contact,name='contact'),    
    path("subscribe", views.Subscribe, name='subscribe'),
    path("future_military", views.future_military, name='future_military'),
    path("AI_STARTUPS", views.AI_STARTUPS, name='AI_STARTUPS'),
    path("PARADIGM", views.PARADIGM, name='PARADIGM'),
     path("next_unicorn", views.next_unicorn, name='next_unicorn'),
  
 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)