from django.contrib.comments.models import Comment

from forms import LightCommentForm

def get_model():
    return Comment

def get_form():
    return LightCommentForm