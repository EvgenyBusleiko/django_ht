from django import forms

class Author(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    lastname = forms.CharField(max_length=100)
    biography = forms.CharField(widget=forms.Textarea)
    data_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeField(auto_now_add=True)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    is_published = forms.BooleanField()
    views = forms.IntegerField(default=0)
