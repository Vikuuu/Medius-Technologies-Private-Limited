from django.shortcuts import render
from .forms import UploadFileForm
from .utils import process_file


def home(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            summary = process_file(file)

            return render(request, "upload_file/success.html", {"summary": summary})
    else: 
        form = UploadFileForm()
    return render(request, "upload_file/upload.html", {"form": form})
