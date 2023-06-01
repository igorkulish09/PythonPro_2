from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    title = forms.CharField(min_length=5, max_length=100)
    assignee = forms.CharField(min_length=5, max_length=100)
    email = forms.EmailField()

    class Meta:
        model = Note
        fields = ["msg", "assignee", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = True

    def clean_assignee(self):
        Assignee = self.cleaned_data.get("assignee")
        if Assignee and len(Assignee.split()) < 2:
            raise forms.ValidationError("Assignee should contain at least two words.")
        return Assignee

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and not email.endswith("@ithillel.ua"):
            raise forms.ValidationError("Email should be associated with ithillel.ua.")
        return email

    def clean_title(self):
        data = self.cleaned_data["title"]
        if len(data.split(" ")) < 2:
            raise forms.ValidationError("Please create Title with at least two words")
        return data

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        msg = cleaned_data.get("msg")

        if title and msg and (title not in msg):
            raise forms.ValidationError("Please start your note from the Title")

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


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
