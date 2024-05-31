# Brief Documentation Outlining the Approach


## Objective

The objective of this project is to create a Django-based web page that allows users to upload an Excel/CSV file. The uploaded file is processed to generate a summary report that groups the data by state and DPD (Days Past Due). The summary report is then displayed on the web page.

## Project Structure

### Forms

#### UploadFileForm: 
A Django form to handle file uploads.

### Utilities

#### process_file: 
A utility function to read and process the uploaded file, generate the summary report, and return it as an HTML table.

- Reading the uploaded file (either Excel or CSV format).
- Grouping the data by 'Cust State' and 'DPD', and counting the occurrences.
- Returning the summary as an HTML table

### Views

#### upload_file:
A Django view to handle the file upload and display the summary report.

- On a POST request, it processes the uploaded file using the process_file function and renders the summary report.
- On a GET request, it displays the file upload form

### Templates

#### upload.html: 
A template to render the file upload form.

#### upload_success.html: 
A template to display the summary report after successful file upload.
