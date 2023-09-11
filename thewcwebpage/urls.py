from django.urls import path
from . import views

urlpatterns = [
    path('', views.WritingListView.as_view(), name='home'),
    path('<slug:slug>/', views.WritingDetailView.as_view(), name='writing_detail'),
]