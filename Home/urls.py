from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('save-word/', views.saving_view, name='save'),
    path('saved/', views.saved_view, name='saved')
]
