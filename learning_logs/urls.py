"""定义learning_logs 的 URL 模式"""  # 为了指出当前位于那个urls.py文件中，在该文件开头添加一个文档字符串

from django.urls import path   # 导入了函数path 因为要使用它将url映射到视图
from django.contrib.auth import views as auth_views
from . import views  # 导入模块views 其中的句点让Python从当前这个urls.py文件同项目内其他的应用程序中的同名文件区分开来

app_name = 'learning_logs'  # 变量app_name 能让django将这个urls.py文件同项目的其他应用程序中的同名文件区分开来
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新追加的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path ('new_entry/<int:topic_id>/', views.new_entry,
          name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry,name='edit_entry'),
    
]
