from django.contrib import admin

from .models import Topic, Entry
# Register your models here.

from django.contrib import admin

from .models import Topic  # 首先导入要注册的模型Topic。Models 前面的句点让Djang在admin.py所在的目录中查找models.py

admin.site.register(Topic)  # admin.site.register() 让Django通过管理网站管理模型 
admin.site.register(Entry)