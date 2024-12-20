from django.urls import path
from .views import UploadFileView, FileDetailsView, FileListView, DeleteFileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
     # Paths API, JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/upload/', UploadFileView.as_view(), name='file_upload'),
    path('api/files/<int:pk>/', FileDetailsView.as_view(), name='file_details'),
    # Paths django
    path('', FileListView.as_view(), name='file_list'),
    path('delete/<int:pk>/', DeleteFileView.as_view(), name='file_delete'),
]
