from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
# Create your views here.

def upload_pdf(request):
    if request.method == 'POST' and request.FILES['pdf_resume']:
        pdf_resume = request.FILES['pdf_resume']
        # Determine the directory where you want to save the uploaded PDF
        upload_dir = os.path.join(settings.BASE_DIR, 'recommendation/uploads/')
        
        # Ensure the directory exists
        os.makedirs(upload_dir, exist_ok=True)

        # Construct the full path for the uploaded file
        file_path = os.path.join(upload_dir, 'uploaded.pdf')

        # Save the uploaded file
        with open(file_path, 'wb') as destination:
            for chunk in pdf_resume.chunks():
                destination.write(chunk)
        # Need to develop later:
        #return render(request, <h1>succuss</h1>)
    #return render(request, <h1>uploaded</h1>)
    # Until here.
        success_html = "<h1>Upload Successful</h1>"
        upload_html = "<h1>Uploaded</h1>"
        return HttpResponse(success_html)

    return HttpResponse(upload_html)  # Add a message for GET requests