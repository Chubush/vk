from django.shortcuts import render

from account import models
from account.models import Gamers, Games
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ContactForm  # İletişim formunu içe aktarın
from django.db.models import Q
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.db.models import Count


class IndexView(ListView):
    template_name = 'pages/index.html'
    model = Gamers

    def get_queryset(self):
        top_gamers = Gamers.objects.filter(is_active=True).order_by('-games_played')
        return top_gamers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        unique_gamers = []
        seen_gamers = set()

        for gamer in queryset:
            if gamer.username not in seen_gamers:
                unique_gamers.append(gamer)
                if len(unique_gamers) >= 3:  # Stop once we have 3 unique gamers
                    break
                seen_gamers.add(gamer.username)

        context['top_gamers'] = unique_gamers
        return context


    

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('succes')

    def form_valid(self, form):
        form.save()  # Form verilerini kaydet
        return super().form_valid(form)    
    
class SuccesView(TemplateView):
    template_name =("pages/partials/succes.html")    
    
class AboutView(ListView):
    template_name = 'pages/about.html'
    model = Gamers
    context_object_name = 'gamers'

  

class SearchView(ListView):
    model = Gamers
    template_name = 'pages/search.html'
    context_object_name = 'gamers'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            
            gamers = Gamers.objects.filter(
            Q(username__username__icontains=query)
            | Q(slug__icontains=query)
            | Q(best_game__name__icontains=query)                
            ).distinct()  
            return gamers
        else:
            
            return Gamers.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['search_query'] = query  # Arama sorgusunu şablona gönder
        return context
        
class GamerInfoDetailView(DetailView):
    model = Gamers
    template_name = 'pages/gamer-info.html'
    context_object_name = 'gamer'

class GamesListView(ListView):
    model = Games
    template_name = 'pages/games_list.html'
    context_object_name = 'games'    
    
 
class GamersListView(ListView): 
    template_name = 'pages/gamers.html'
    model = Gamers
    context_object_name = 'gamers'
    
    def get_queryset(self):
        return Gamers.objects.all()  

class GameDetailView(DetailView):
    model = Games
    template_name = 'pages/game-info.html'  # Bu template'i oluşturmanız gerekecek

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
      