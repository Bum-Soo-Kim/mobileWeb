from django.contrib import admin
from main.models import SocialAccount, UserInfo, ProductInfo, UseInfo,CleanImage, CleanInfo, ProductImage

# Register your models here.
admin.site.register(SocialAccount)
admin.site.register(UserInfo)
admin.site.register(ProductInfo)
admin.site.register(CleanImage)
admin.site.register(CleanInfo)