from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import  Task
from .forms import  TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskListView(ListView):
    model=Task
    template_name='index.html'
    context_object_name='task'

class TaskDetailView(DetailView):
    model = Task
    template_name='detail.html'
    context_object_name = 'task1'

class TaskUpdateView(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name ='task'
    fields = ('t_name','t_priority','t_date')

    def get_success_url(self):
        return reverse_lazy('classdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model =Task
    template_name='delete.html'
    success_url = reverse_lazy('classlist')

def index(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=Task(t_name=name,t_priority=priority,t_date=date)
        task.save()
        return redirect('/')

    return  render(request,'index.html',{'task':task1})

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return  render(request,'delete.html')
#
#

def update(request,task_id):
    task=Task.objects.get(id=task_id)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})
