from django.shortcuts import render
from Megazine.models import HomeArticle
# from appname.models import model name






# Create your views here.




def home(request):
    HomeArticledata =HomeArticle.objects.all()
    
   

    data ={
        'HomeArticledata':HomeArticledata,
    
        

    }
    


    return render(request, "home.html", data)



def Articles(request):
    return render(request, 'articles.html')

def singlepage(request):
    return render(request,'singlepage.html')

def About(request):
    return render (request,'about.html')

def page(request):
    return render (request,'page.html')

def page2(request):
    return render (request,'page2.html')

def Contact(request):
    return render(request,'contact.html')


def Subscribe(request):
    return render(request,'subscribe.html')


def future_military(request):
    return render(request,'future_military.html')


def AI_STARTUPS(request):
    return render(request,'AI_STARTUPS.html')

def PARADIGM(request):
    return render(request,'PARADIGM.html')

def next_unicorn(request):
    return render(request,'next_unicorn.html')

def news(request):
    return render(request,'news.html')


