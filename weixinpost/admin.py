from django.contrib import admin

# Register your models here.

# 引用我们建立的模型
from weixinpost.models import *


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ('senderName', 'fromAddress', 'phoneNumber', 'submitTime', 'status')

admin.site.register(OrderInfo, OrderInfoAdmin)
