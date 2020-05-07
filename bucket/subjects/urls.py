from django.urls import path
from .  import views


urlpatterns = [
    
    path('', views.home, name = 'blog-home'),
    path('<slug:slug>/',views.detail_view, name = 'subject_detail')
    
]