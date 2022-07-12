from django.urls import path
from . import views

urlpatterns = [
    path('', views.generated),
    path('<int:amount>', views.generated)
]
