from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('neuro', views.neuro, name='neuro'),
    path('graphs', views.graphs, name='graphs'),
    path('view_pdf', views.view_pdf, name='view_pdf')
]
