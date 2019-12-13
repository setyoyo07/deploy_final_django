from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explore',views.explore, name='explore'),
    path('explore/animation',views.animation, name='animation'),
    path('explore/branding',views.branding, name='branding'),
    path('explore/ilustration',views.ilustration, name='ilustration'),
    path('ourdesigner', views.ourdesigner, name='ourdesigner'),
    path('account', views.account, name='account'),
    path('addpost', views.addpost, name='addpost'),
    path('daftar', views.daftar, name='daftar'),
    path('inputpost', views.inputpost, name="inputpost")
]