from django import forms
from django.forms.widgets import SelectDateWidget

from .models import BlogPost, Comment


class BlogPostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    publish_date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = BlogPost
        fields = ["title", "image", "content", "draft", "publish_date"]

    def clean_title(self, *arg, **kwargs):
        title = self.cleaned_data.get("title")
        instance = self.instance
        print(instance)
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)  # id = instance.id
        if qs.exists():
            raise forms.ValidationError(
                "This title has already been used, Please enter another title."
            )
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
