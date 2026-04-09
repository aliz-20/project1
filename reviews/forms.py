from django import forms
from .models import Review, Reply
from .utils import contains_blocked_words


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'description', 'stars', 'image', 'video']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if contains_blocked_words(title):
            raise forms.ValidationError("Your title contains inappropriate language.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if contains_blocked_words(description):
            raise forms.ValidationError("Your review contains inappropriate language.")
        return description


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your reply...'
            })
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if contains_blocked_words(message):
            raise forms.ValidationError("Your reply contains inappropriate language.")
        return message