from django.urls import path
from . import views

urlpatterns = [
    path('', views.CinemaViews.as_view()),
    path('<slug:slug>/', views.CinemaDetailView.as_view(), name='cinema_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
]