from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.

def index(request):
    """学习笔记的主页。"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """显示所有主题。"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request,topic_id):
    """显示单个主题及其所有条目。"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户。
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    """添加新主题。"""
    if request.method != 'POST':   # 确定请求方法是GET还是POST，再按需返回一个空列表
        # 未提交数据：创建一个新表单。
        form = TopicForm()   # 创建一个实例，将其赋给form
    else:
        # POST提交的数据：对数据进行处理
        form = TopicForm(data=request.POST)  # 如果是post请求。就将用户输入的数据（存储在request.POST）里的数据进行处理，创建一个TopicForm实例，这样对象form将包含用户提交的信息。
        if form.is_valid():  # 要将提交的信息保存到数据库，必须先通过检查确定他们是否有效，方法is_valid核实用户填写了所有必不可少的字段（秒单字段默认都是必不可少的），且输入的数据与要求的字段类型一致。
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics') # 保存数据后，就可以离开这个页面了。为此，使用redirect() 将用户的浏览器重新定向到topic
        
    # 显示空表单或指出表单数据无效。
    context = {'form':form}  # 通过上下文将表单发送给模板。由于实例化是没有指定任何实参，django将创建一个空表单，供用户填写
    return render(request,'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """在特定主题中添加新条目。"""
    topic = Topic.objects.get(id=topic_id) # 使用topic来获得正确的主题
    if request.method != 'POST':  # 检查请求方法是post还是get
        # 未移交数据时，创建一个空表单。
        form = EntryForm()  # 如果是get 就创建一个空的enrtyForm 实例
    else:  # 如果是post 就对数据进行处理
        # POST提交的数据，对数据进行处理。
        form = EntryForm(data=request.POST)  # 创建一个entryform实例，使用request 对象中的Post数据来填充它
        if form.is_valid(): # 然后检查表单是否有效
            new_entry = form.save(commit=False) # 调用save()时， 传递实参commit=false，让django创建一个新的条目对象，将其赋给new_enrty的属性topic
            new_entry.topic = topic  # 再调用save（）且不制定任何实参。这将把条目存储到数据库
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)  # 调用redirect()，它要求提供两个是惨：
        
    # 显示空列表指出表单数据无效。
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有条目。"""
    try:
        entry = Entry.objects.get(id=entry_id) 
        topic = entry.topic
        if topic.owner != request.user:
            raise Http404

        if request.method != 'POST':
            form = EntryForm(instance=entry)
        else:
            form = EntryForm(instance=entry, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('learning_logs:topic',topic_id=topic.id)
        
        context = {'entry':entry, 'topic':topic, 'form':form}
        return render(request, 'learning_logs/edit_entry.html', context)
    
    except Exception as e:
        # 添加详细错误日志
        print(f"Error in edit_entry: {str(e)}")
        raise  # 重新抛出异常




