from django import forms
from .models import File


class FileUploadForm(forms.ModelForm):

	class Meta:
		model = File
		exclude = ['number_of_pages']
