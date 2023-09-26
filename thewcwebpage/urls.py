from django.urls import path
from . import views

urlpatterns = [
    path('', views.WritingListView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('my_writings/', views.MyWritingsListView.as_view(), name='my_writings'),
    path('new_writing/', views.NewWritingView.as_view(), name='new_writing'),
    path('update_writing/<slug:slug>/', views.UpdateWritingView.as_view(), name='update_writing'),
    path('delete_writing/<slug:slug>/', views.DeleteWritingView.as_view(), name='delete_writing'),
    path('approve_comment/<int:pk>/', views.ApproveCommentView.as_view(), name='approve_comment'),
    path('select_comment/<int:pk>/', views.SelectCommentView.as_view(), name='select_comment'),
    path('<slug:slug>/', views.WritingDetailView.as_view(), name='writing_detail'),
    path('like/<slug:slug>', views.WritingLike.as_view(), name='writing_like'),
]