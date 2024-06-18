# urls.py (in the 'gallery' app)

from django.urls import path
from . import views



urlpatterns = [
    path('image_gallery/', views.image_gallery, name='image_gallery'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('upload_delete_images/', views.upload_delete_images, name='upload_delete_images'),
    path('upload_delete_images/<int:image_id>/', views.upload_delete_images, name='delete_image'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    # path('upload-delete-videos/', views.upload_delete_videos, name='upload_delete_videos'),
    # path('display-videos/', views.display_videos, name='display_videos'),
    # path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('photo_video_editing/', views.photo_video_editing, name='photo_video_editing'),
]
