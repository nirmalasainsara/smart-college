from django import forms

from .models import Paper, Notes_file, Video_url

class PaperForm(forms.ModelForm):

    class Meta:
        model = Paper
        fields = ('upload_paper', 'degree', 'year', 'subject',)

class NotesForm(forms.ModelForm):

    class Meta:
        model = Notes_file
        fields = ('subject_paper', 'degree', 'year', 'subject',)

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video_url
        fields = ('video', 'degree', 'year', 'subject',)

