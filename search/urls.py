from django.urls import path
from search import views

app_name = "bible-search"
urlpatterns = [
    path('', views.SearchView.as_view(), name="main"),
    path('chapter/<int:pk>', views.ChapterView.as_view(), name="chapter")
]