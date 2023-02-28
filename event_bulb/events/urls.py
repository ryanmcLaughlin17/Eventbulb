from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name="events_list"),
    # path('past', views.list_past, name="events_list_past"),
    path('<int:id>/', views.details, name="events_details"),
]
