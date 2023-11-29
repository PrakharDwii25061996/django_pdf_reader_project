import PyPDF2

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import File
from .forms import FileUploadForm


def index(request):
    return render(request, 'core/index.html', {})


def file_upload(request):
    if request.method == 'POST':
        file_upload_form  = FileUploadForm(request.POST, request.FILES)
        file_upload_form.save()
        return redirect('file_list')

    file_upload_form  = FileUploadForm()
    return render(request, 'core/file_upload.html', {'form': file_upload_form})


def file_list(request):
    files = File.objects.all()
    return render(request, 'core/file_list.html', {'file_list': files})


def page_reader(request, id, page_number=1):

    file = get_object_or_404(File, pk=id)
    if request.method == 'GET':
        pdf_file = open(f'{file.file.path}', 'rb')
        pdfReader = PyPDF2.PdfReader(pdf_file)
        page = pdfReader.pages[page_number]
        page_content = page.extract_text()

    return render(request, 'core/page_render.html', {
            'file': file,
            'current_page_number': page_number,
            'next_page_number': page_number + 1,
            'prev_page_number': page_number - 1,
            'page_content': page_content
        }
    )
