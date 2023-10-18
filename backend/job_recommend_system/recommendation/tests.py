from django.test import TestCase
import os
# Create your tests here.
from django.urls import reverse

class YourViewTestCase(TestCase):
    def test_submit_function(self):
        url = reverse('upload_pdf')  # Replace 'upload_pdf' with your actual URL name
        # Get the directory of the test file
        test_dir = os.path.dirname(__file__)
        # Construct the full path to resume.pdf
        pdf_path = os.path.join(test_dir, 'resume.pdf')
        with open(pdf_path, 'rb') as pdf_file:
            response = self.client.post(url, {'pdf_resume': pdf_file})
        
        # Perform assertions based on your view's response
        self.assertEqual(response.status_code, 200)  # Assuming a successful submission returns a 200 status code
        # Add more assertions as needed