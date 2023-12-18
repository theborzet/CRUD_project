from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.db.models import Q


from functools import reduce
from operator import and_


from todos.models import Todo
from todos.forms import TodoForm, TodoUpdateForm, SearchForm

class ModelView(ListView):
    context_object_name = 'tasks'
    template_name = 'todos/index.html'
    model = Todo


class TodoCreateView(SuccessMessageMixin, CreateView):
    model = Todo
    template_name = 'todos/create.html' 
    form_class = TodoForm  
    success_url = reverse_lazy('index')  
    success_message = 'Задача добавлена!'


def delete_task(request, task_id):
    model = Todo
    
    task = get_object_or_404(model, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('index'))

    return redirect('index')


class TodoUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'todos/update.html'
    model = Todo
    form_class = TodoUpdateForm
    success_message = 'Запись обновлена!'
    success_url = reverse_lazy('index')


class SearchView(View):
    template_name = 'todos/search.html'
    results_template_name = 'todos/search_result.html'

    def get(self, request):
        form = SearchForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)

        if form.is_valid():
            q_filters = []

            if form.cleaned_data['title']:
                q_filters.append(Q(title__icontains=form.cleaned_data['title']))

            if form.cleaned_data['description']:
                q_filters.append(Q(description__icontains=form.cleaned_data['description']))

            if form.cleaned_data['complited'] is not None:
                q_filters.append(Q(complited__icontains=form.cleaned_data['complited']))
            search_results = Todo.objects.filter(reduce(and_, q_filters))

            return render(request, self.results_template_name, {'results': search_results})
        
        return render(request, self.template_name, {'form': form})


    
