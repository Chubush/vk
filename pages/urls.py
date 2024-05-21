from django.urls import path
from pages import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [    
    path('',  views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'), 
    path("search/", views.SearchView.as_view(), name="search"),
    path("succes/",views.SuccesView.as_view(), name="succes"),
    path('gamers/<int:pk>/',views.GamerInfoDetailView.as_view(), name='gamer_info'),
    path('games/', views.GamesListView.as_view(), name='games_list'),
    path('gamers/', views.GamersListView.as_view(), name='gamers'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game-detail')
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
