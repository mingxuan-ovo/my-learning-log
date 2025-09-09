from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):  # 继承了forms.ModeForm
    class Meta: # 让Django根据那个模型创建表单以及在表单中包含那些字段

        model = Topic # 根据Topic创建表单
        fields = ['text'] # 其中只包含字段text
        labels = {'text': ''}  # 让django不要为字段text生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}  # 这里给字段‘text'指定了标签'Entry:'
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # 定义了属性widgets。 小部件（widget)
        # 是一个HTML表单元素，如单行文本框，多行文本框或下拉文本框。通过设置属性widgets, 可覆盖Django选择的默认小部件
        # 通过让Django使用forms.Textarea, 我们定制了字段‘text'的输入小部件，将文本区域的宽度设置为80列，而不是默认的40列