from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)  # Eğer sayfa GET ile açılmışsa form değeri herhangi bir form bilgisi almayacak içine ve formu boş şekilde kullanıcıya 
                                               # gösterecek. Eğer form doldurulmuşsa ve POST bilgisiyle submit edildiyse, form objesi bu bilgilerle doldurulacak.
    
    if form.is_valid(): #Kullanıcı adı-şifre bilgilerinin ve şifrenin eşleşip eşleşmediği kontrol ediliyor.
        
        username = form.cleaned_data.get("username")  #Formdan gelen kullanıcı adı ve şifreyi tutuyoruz.
        password = form.cleaned_data.get("password")
        
        newUser=User(username = username)
        newUser.set_password(password)                #Yeni kullanıcıyı veritabanına kaydediyoruz.
        newUser.save()

        login(request,newUser)
        messages.info(request,"Başarıyla Kayıt Oldunuz!")
        return redirect("index")      #Kullanıcıyı otomatik login yapmış şekilde anasayfaya yönlendiriyoruz.
    
    context ={"form":form}
    return render(request,"register.html",context)   #Eğer register sayfası GET komutuyla açıldıysa veya kullanıcı-şifre bilgilerinde problem varsa tekrardan register sayfasına yönlendiriliyor.


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {"form":form}

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)   #Authenticate fonksiyonu ile login işlemi sırasında girilen kullanıcı adı ve şifresinin veritabanında olup olmadığını kontrol ediyoruz.
                                                                   #Eğer veritabanında kullanıcı yoksa None dönecek.

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı!")
            return render(request,"login.html",context)
        
        else: #Eğer kullanıcı adı ve şifre veritabanında varsa
            messages.success(request,"Başarıyla Giriş Yaptınız")
            login(request,user)
            return redirect("index")
    
    
    else:  #Eğer login sayfası GET komutuyla açılmışsa veya girilen form valid değilse tekrardan login.html sayfası açılacak
        return render(request,"login.html",context)



def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış Yapıldı")
    return redirect("index")


