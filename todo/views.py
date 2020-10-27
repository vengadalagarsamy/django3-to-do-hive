from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'todo/home.html')

@login_required
def current(request):

    return render(request, 'todo/current.html', {'todos':todos})

# @login_required
# def complete(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
#     if request.method == 'POST':
#         todo.datecompleted = timezone.now()
#         todo.save()
#         return redirect('current')


#CRUD
class CreateToDo(generic.CreateView):
    model = Todo
    fields = ['title', 'memo', 'important']
    template_name = 'todo/create.html'
    success_url = reverse_lazy('current')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateToDo, self).form_valid(form)
        return redirect('current')

#class viewtodo(generic.DetailView):
#model = Todo
#template_name = 'todo/viewtodo.html'

class updatetodo(generic.UpdateView):
    model = Todo
    template_name = 'todo/updatetodo.html'
    fields = ['title', 'memo', 'important']
    success_url = reverse_lazy('current')

class deletetodo(generic.DeleteView):
    model = Todo
    template_name = 'todo/deletetodo.html'
    success_url = reverse_lazy('current')


#Authentication situation ebolation
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('create')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
