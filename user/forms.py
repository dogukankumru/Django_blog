from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form): #Login işlemi için o sayfada görünecek olan form
    username=forms.CharField(label="Kullanıcı Adı")
    password=forms.CharField(label="Parola",widget=PasswordInput)




class RegisterForm(forms.Form):  #Kayıt Olma ekranındaki formda görünecek bilgiler ve bilgilerin doğrulanması!

    username = forms.CharField(max_length=20,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Şifre",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parolayı Doğrula",widget=PasswordInput)

    def clean(self):  #Girilen parolanın ve confirm parola kısmının eşleşip eşleşmediğini kontrol edecek. import edilen forms'daki clean fonksiyonunu override ediyoruz.

        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password!=confirm:    #Eğer parola ve parolayı doğrula bilgileri girilmişse fakat eşleşmiyorlarsa..
            
            raise forms.ValidationError("Parola Eşleşmiyor")
        
        values ={"username":username,
                 "password":password
                }
        
        return values

