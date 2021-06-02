from django import forms
from blog.models import Comment 
class EmailSendForm(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    To = forms.EmailField()
    Comments = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment 
        fields=('name','email','body')