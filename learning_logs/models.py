from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """用户学习的主题。"""
    text = models.CharField(max_length=200) # 属性text 是一个CharField ————由字符组成的数据，即文本。
                                            # 需要存储少量字典的时候，如名称，标题或城市时，可使用它，不过定义CharFiled属性时
                                            # 必须告诉Djang该在数据库中预留多少空间 这里将max_lengh设置成了200
    
    date_added = models.DateTimeField(auto_now_add=True)  # date_added 是一个DateTimeField ———— 记录日期和时间的数据
                                                          # 我们传递了实参auto_now_add = True，每当用户创建新主题的时候，Djang都会将这个属性自动设置为当前的日期和时间
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):   # 告诉Dajang 默认使用那些属性来显示有关主题的信息。
        """返回模型的字符串表示。"""
        return self.text  # Dajang 调用方法__str__() 来显示模型的简单表示。这里编写了方法str， 它返回存储在属性text中的字符串
    

class Entry(models.Model):  # 继承了Django基类Model
    """学到的有关某个主体的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # on_delete = models.CASCADE 表示在删除主题时同时删除所有与之相关连的条目（级联删除）
    text = models.TextField() # text 是一个 textfiled()的实例。这种字段的长度不受限制，因为不想限制条目的长度
    date_added = models.DateTimeField(auto_now_add=True)  # 属性date_added让我们能够按创建顺序呈现条目，并在每个条目旁边放置时间戳

    class Meta:  # 嵌套类， Meta 存储用于管理模型的额外信息，它让我们能够设置一个特殊属性，让django在需要时使用Entries来表示多个条目
        verbose_name_plural = 'entries'
    
    def __str__(self):  # 告诉django，呈现条目时应当显示那些信息，条目包含的文本可能很长，因此让django只显示前50个字符，逗号表示并非显示整个条目
        """返回模型的字符串表示"""
        if len(self.text) > 50:
            return f"{self.text[:50]}"
        else:
            return self.text