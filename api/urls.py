from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.drink_list),
    path("<int:pk>/", views.drink_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
