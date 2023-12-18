from django import forms


from todos.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите описание'}),
        }
        labels = {
        'title': 'Заголовок',
        'description': 'Описание',
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'complited']
        labels = {
        'title': 'Заголовок',
        'description': 'Описание',
        'complited': 'Завершено',
        }

class SearchForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    complited = forms.BooleanField(required=False)