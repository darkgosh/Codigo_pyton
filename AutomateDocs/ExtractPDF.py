import PyPDF2
import os

def extract_invoice_info(pdf_file_path):

    #Open the PDF file
    with open(pdf_file_path,'rb') as file:
        #create a pdf reader object
        pdf_reader = PyPDF2.PdfReader(file)
        #Extract text from each page
        text= ''

        for page_num in range(len(pdf_reader.pages)):
            page=pdf_reader.page[page_num]
            text+= page.extract_text()
        
        print(text)

extract_invoice_info("invoice/invoice.pdf")