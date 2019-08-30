from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:folio_id>/', views.foliodetail, name="folio-detail"),
]