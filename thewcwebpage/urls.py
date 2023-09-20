from django.urls import path
from . import views

urlpatterns = [
    path('', views.WritingListView.as_view(), name='home'),
    path('new_writing/', views.NewWritingView.as_view(), name='new_writing'),
    path('update_writing/<slug:slug>/', views.UpdateWritingView.as_view(), name='update_writing'),
    path('delete_writing/<slug:slug>/', views.DeleteWritingView.as_view(), name='delete_writing'),
    path('<slug:slug>/', views.WritingDetailView.as_view(), name='writing_detail'),
    path('like/<slug:slug>', views.WritingLike.as_view(), name='writing_like'),
]