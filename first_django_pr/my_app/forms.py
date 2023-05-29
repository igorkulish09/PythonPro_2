from django import forms
from django.core.exceptions import ValidationError
from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(min_length=5, max_length=10)

    class Meta:
        model = Note
        fields = ['msg', 'assignee', 'email']

    def clean_assignee(self):
        assignee = self.cleaned_data.get('assignee')
        if assignee and len(assignee.split()) < 2:
            raise forms.ValidationError("Assignee should contain at least two words.")
        return assignee

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@ithillel.ua'):
            raise forms.ValidationError("Email should be associated with ithillel.ua.")
        return email

    def clean_title(self):
        data = self.cleaned_data['title']
        if len(data.split(' ')) < 2:
            raise ValidationError("Please create Title with at least two words")
        return data

    def clean(self):
        cleaned_data = super().clean()
        # NOTE: Everything work with the exchange of the cleaned_data[key] to cleaned_data.get(key)
        title = cleaned_data.get('title')
        msg = cleaned_data.get('msg')

        if title and msg and (title not in msg):
            # raise ValidationError("Please start your note from the Title")
            self.add_error('msg', "Please start your note from the Title")

# class NoteForm(forms.Form):
#     title = forms.CharField(min_length=5, max_length=10)
#     msg = forms.CharField(min_length=10, max_length=200)
#
#     def clean_title(self):
#         data = self.cleaned_data['title']
#         if len(data.split(' ')) < 2:
#             raise ValidationError("Please create Title with at least two words")
#         return data
#
#     def clean(self):
#         cleaned_data = super().clean()
#         # NOTE: Everything work with the exchange of the cleaned_data[key] to cleaned_data.get(key)
#         title = cleaned_data.get('title')
#         msg = cleaned_data.get('msg')
#
#         if title and msg and (title not in msg):
#             raise ValidationError("Please start your note from the Title")