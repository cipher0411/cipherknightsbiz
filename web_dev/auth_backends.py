# # web_dev/auth_backends.py

# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User

# class EmailOrUsernameModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         if username is None:
#             username = kwargs.get(User.USERNAME_FIELD)
#         if username is None or password is None:
#             return
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             try:
#                 user = User.objects.get(email=username)
#             except User.DoesNotExist:
#                 User().set_password(password)
#                 return
#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user
