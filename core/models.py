from django.db import models
import PyPDF2


class File(models.Model):
	name = models.CharField(max_length=55, null=False)
	number_of_pages = models.IntegerField(null=True)
	author = models.CharField(max_length=55)
	file = models.FileField(upload_to='file')

	def __str__(self):
		return f'{self.name}'

	def save(self, *args, **kwargs):
		super().save()

		if not self.number_of_pages:
			file = open(f'{self.file.path}', 'rb')
			pdf_reader = PyPDF2.PdfReader(file)
			self.number_of_pages = len(pdf_reader.pages)
			self.save()
