from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Make the home view the default view for the root URL
    path('authors_page/', views.authors_page, name='authors_page'),
    path('<int:lecturer_id>/', views.lecturer_detail, name='lecturer_detail'),
    # Add the search view URL pattern
    path('search/', views.search_lecturer, name='search_lecturer'),
]
