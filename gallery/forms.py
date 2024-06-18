from django import forms
from .models import Image
# from .models import Video

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image', 'category', 'description']

class DeleteImageForm(forms.Form):
    image_id = forms.IntegerField(widget=forms.HiddenInput())




        
# class VideoForm(forms.ModelForm):
#     class Meta:
#         model = Video
#         fields = ['title', 'video_file', 'poster_image', 'description']

# class VideoDeleteForm(forms.Form):
#     video_ids = forms.ModelMultipleChoiceField(
#         queryset=Video.objects.all(), 
#         widget=forms.CheckboxSelectMultiple
#     )
    