from django import forms
from .models import Comment

class pushCommentForms(forms.ModelForm):
    # product = forms.CharField(widget=forms.HiddenInput())
    # owner_comment = forms.CharField(widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        self.owner_comment = kwargs.pop('owner_comment', None)
        self.product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.owner_comment = self.owner_comment
        comment.product = self.product
        comment.save()

    class Meta:
        model = Comment
        fields = ('content', )