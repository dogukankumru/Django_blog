from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):  #Fonksiyonların içine http requestlerini(get-post gibi) koymak için requesti her zaman koymamız gerekiyor.
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def articles(request):

    keyword = request.GET.get("keyword")                #Eğer arama çubuğuna kelime yazıldıysa ona uygun makale olup olmadığına bakıyor.
    if keyword :
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})


    articles=Article.objects.all()       #Veritabanındaki tüm makaleleri articles'ın içine attık liste halinde
    return render(request,"articles.html",{"articles":articles})




@login_required(login_url = "user:login")  #Eğer kullanıcı girişi yapılmadan bu siteye girilmeye çalışılırsa kullanıcı giriş ekranına yönlendirilecek
def dashboard(request):
    articles = Article.objects.filter(author=request.user)  #Hesapta bulunan kullanıcının yazdığı makaleleri aldık
    context={"articles":articles}
    return render(request,"dashboard.html",context)





#Makale Ekleme işlemi
@login_required(login_url = "user:login")  #Eğer kullanıcı girişi yapılmadan bu siteye girilmeye çalışılırsa kullanıcı giriş ekranına yönlendirilecek
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False)   #Biz title ve content bilgilerini addarticle sitesinden aldık fakat user bilgisine sahip değiliz bu yüzden veritabanına kaydetmeden önce user'ı biz içine koyup kaydedicez.
        article.author= request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu!")
        return redirect("index")

    return render(request,"addarticle.html",{"form":form})

@login_required(login_url = "user:login")  #Eğer kullanıcı girişi yapılmadan bu siteye girilmeye çalışılırsa kullanıcı giriş ekranına yönlendirilecek
def updateArticle(request,id):  #Makale Güncelleme İşlemi

    article = get_object_or_404(Article,id=id) #Bize girilen id'deki makalenin bilgilerinin article içine koy fakat eğer belirtilen id'de makale yoksa ve kullanıcı websitede bu sayfayı açmaya çalışırsa 404 hatasını ver.

    form = ArticleForm(request.POST or None,request.FILES or None, instance = article)  #Id'sini belirttiğimiz makalenin bilgilerini formun içine koyduk

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi!")

        return redirect("article:dashboard")
    
    else:
        return render(request,"update.html",{"form":form})


@login_required(login_url = "user:login")  #Eğer kullanıcı girişi yapılmadan bu siteye girilmeye çalışılırsa kullanıcı giriş ekranına yönlendirilecek
def deleteArticle(request,id):

    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("article:dashboard")




def details(request,id):   #Makalelerin detay sayfası
    article=get_object_or_404(Article,id=id)  #Bize girilen id'deki makalenin bilgilerinin article içine koy fakat eğer belirtilen id'de makale yoksa ve kullanıcı websitede bu sayfayı açmaya çalışırsa 404 hatasını ver.
    return render(request,"details.html",{"article":article})

