from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Image, Category
from .forms import ImageForm, DeleteImageForm
# from .models import Video
# from .forms import VideoForm, VideoDeleteForm






def gallery_view(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    return render(request, 'gallery/image_gallery.html', {'categories': categories, 'images': images})

def category_view(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    images = category.images.all()
    return render(request, 'gallery/image_gallery.html', {'categories': categories, 'images': images})


def image_gallery(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    return render(request, 'gallery/image_gallery.html', {'categories': categories, 'images': images})

def upload_delete_images(request):
    if request.method == 'POST':
        # Handling Image Upload
        if 'upload' in request.POST:
            upload_form = ImageForm(request.POST, request.FILES)
            if upload_form.is_valid():
                upload_form.save()
                return redirect('upload_delete_images')
        else:
            upload_form = ImageForm()

        # Handling Image Deletion
        if 'delete' in request.POST:
            delete_form = DeleteImageForm(request.POST)
            if delete_form.is_valid():
                image_id = delete_form.cleaned_data['image_id']
                image = get_object_or_404(Image, id=image_id)
                image.delete()
                return redirect('upload_delete_images')
        else:
            delete_form = DeleteImageForm()

    else:
        upload_form = ImageForm()
        delete_form = DeleteImageForm()

    images = Image.objects.all()
    categories = Category.objects.all()
    context = {
        'upload_form': upload_form,
        'delete_form': delete_form,
        'images': images,
        'categories': categories,
    }
    return render(request, 'web_dev/upload_delete_images.html', context)







# def photo_video_editing(request):
#     return render(request, 'web_dev/photo_video_editing.html')


# def index(request):
#     videos = Video.objects.all()
#     return render(request, 'gallery/index.html', {'videos': videos})

# def upload_delete_videos(request):
#     videos = Video.objects.all()

#     if request.method == 'POST':
#         if 'upload' in request.POST:
#             form = VideoForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 return redirect('upload_delete_videos')
#         elif 'delete' in request.POST:
#             delete_form = VideoDeleteForm(request.POST)
#             if delete_form.is_valid():
#                 video_ids = delete_form.cleaned_data.get('video_ids')
#                 Video.objects.filter(id__in=video_ids).delete()
#                 return redirect('upload_delete_videos')
#     else:
#         form = VideoForm()
#         delete_form = VideoDeleteForm()

#     return render(request, 'gallery/upload_delete_videos.html', {
#         'form': form,
#         'delete_form': delete_form,
#         'videos': videos
#     })

# def gallery(request):
#     videos = Video.objects.all()
#     return render(request, 'gallery/gallery.html', {'videos': videos})



# def display_videos(request):
#     videos = Video.objects.all()
#     return render(request, 'web_dev/display_videos.html', {'videos': videos})



# def delete_video(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
    
#     if request.method == 'POST':
#         video.delete()
#         return redirect('gallery')  # Redirect to the appropriate URL after deletion
    
#     return render(request, 'gallery/confirm_delete_video.html', {'video': video})


