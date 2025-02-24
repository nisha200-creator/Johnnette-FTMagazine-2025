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




