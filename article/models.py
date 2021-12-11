from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):   #Bizim sql veritabanında kullanılacak olan makalelerimizi koyacağımız article tablosu

                                                                                                              #Bu makalenin yazar ismini veritabanında oluşturulan kullanıcı adından alacak, bunu yapabilmek için foreignkey modülüyle oluşturuyoruz
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name = "Yazar")                  #ve auth.User ile kayıtlı olan kullanıcılara ulaşıyoruz. Bununla beraber on_delete fonksiyonu ile eğer kullanıcı hesabını silersek, otomatik olarak o kullanıcının oluşturduğu makaleler de silinecek
    title = models.CharField(max_length=40,verbose_name = "Başlık")
    content = RichTextField(verbose_name="İçerik")                                         #Verbose_name ile content isminin admin panelinde İçerik ismiyle gözükmesini sağlıyoruz
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")  #Makalenin oluşturulduğu tarihe göre otomatik tarih değeri alacak.
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin")

    def __str__(self):
        return self.title    #Artık article objesini print(Article) işlemi yapıldığında veya admin panelinde Article object ile bakıldığı zaman bize makalenin başlığı gözükecek. 


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE,verbose_name="Makale")
    comment_author = models.CharField(max_length=20,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)