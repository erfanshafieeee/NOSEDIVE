from django.urls import path

from main.views import UserListView, RateView, UploadProfileView

urlpatterns = [
    path('rate', RateView.as_view(), name='rate'),
    path('upload_file/', UploadProfileView.as_view(), name='uploadFile'),
    path('', UserListView.as_view(), name='index'),
]
