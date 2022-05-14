from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    model = Comment
    fields = ('body')
