from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index.as_view(), name='index'),
    path('', views.home, name='home'),

    path('notices/', views.NoticeListView.as_view(), name='notice_list' ),
    path('notices/create/', views.NoticeCreateView.as_view(), name='notice_create'),
    path('notices/<int:pk>/', views.NoticeDetailView.as_view(), name='notice'),
    path('notices/<int:pk>/update', views.NoticeUpdateView.as_view(), name='notice_update'),
    path('notices/<int:pk>/delete', views.NoticeDeleteView.as_view(), name='notice_delete'),
]