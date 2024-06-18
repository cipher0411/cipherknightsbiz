from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, related_name='images', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title




# class Video(models.Model):
#     user = models.CharField(max_length=150)
#     title = models.CharField(max_length=200)
#     video_file = models.FileField(upload_to='videos/')
#     poster_image = models.ImageField(upload_to='video_posters/')
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title