from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib import admin


class Games(models.Model):
    name = models.CharField(max_length=155)
    category = models.CharField(max_length=155)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="images/game_image/") 
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, db_index=True)

    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Oyun"
        verbose_name_plural = "Oyunlar"
        ordering = ["id"]  

class Gamers(models.Model):    
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="gamer")
    age = models.IntegerField(blank= True, null=True)
    profile_image = models.ImageField(upload_to="images/gamers_image/" )
    best_game = models.ForeignKey('Games', on_delete=models.CASCADE, related_name='best_players', null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, db_index=True)
    games_played=models.ManyToManyField(Games,  blank=True, )
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.username} - {self.age}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Gamer"
        verbose_name_plural = "Gamers"
        ordering = ["id"]
                

class Contact(models.Model):
    isim = models.CharField(max_length=100, verbose_name='isim')
    email = models.EmailField(max_length=100, verbose_name='email')
    konu = models.CharField(max_length=100, verbose_name='konu')
    mesaj = models.TextField(max_length=255 , verbose_name='mesaj')

    def __str__(self):
        return f"{self.isim} - {self.konu}"               


# class ContactAdmin(admin.ModelAdmin):
#     list_display=('isim','email','konu','mesaj') #Paneldeki kolonları gösterir.
#     list_display_links=('isim','email')        #gösterilen parametreleri link haline getirir
#     list_filter=('mesaj',) #filtreleme işlemleri ekler girilen paramtetreye göre
#     list_editable=('mesaj',) #editable checkbox sutunu koyar. Defultda false hoca true yaptı
#     search_fields=('isim','mesaj') #Üste arama searchBox'i koyar. girilen parametrelere göre arama yapılır contain ile çalışır.
#     list_per_page=20    #Her sayfada kaç tane ürün olduğunu belirler ve ona göre sayfaları böler.      