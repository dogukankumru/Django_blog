from django.contrib import admin
from .models import Article,Comment   #Admin panelinde Makale tablosunu görebilmek için buraya import ediyoruz.

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author"]          #Artık admin panelinde sadece article başlığı değil  hem article başlığı hem de yazarı gözükecek.
    list_display_links=["title","author"]    #Yazarın üstüne tıklandığında da makalenin içeriği açılacak.
    search_fields=["title"]                  #Admin panelinde arama çubuğu oluşturduk ve makale başlıklarına göre makaleyi bulmamızı sağlayacak.
    list_filter=["created_date"]             #Son 7 günde veya bu ay oluşturulan makaleleri görmemizi sağlayacak.

    class Meta:
        model=Article             #Bunun amacı django frameworkünde ArticleAdmin ile Article classlarını birbirlerine bağlamayı sağlıyor.

admin.site.register(Comment)