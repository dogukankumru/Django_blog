from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):               #Eğer bizim elimizde Article modeli var ve bu form Article modeline göre oluşturulacak.
    class Meta:
        model = Article                           #Burdaki formumuzla Article modelini bağlantılı hale getirdik.
        fields =["title","content","article_image"]               #Article ekleme formumuzda sadece title ve content değerlerini alacağımızı belirttik.