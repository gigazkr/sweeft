from django.urls import path

from shortener import views

urlpatterns = [
    path('', views.URLShortener.as_view()),
    path('custom/', views.CustomURLShortener.as_view()),
    path('<str:short>/', views.redirect_url),
]
