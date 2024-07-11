import PyPDF2 
import os
import re

def extract_invoice_info(pdf_file_path):

    #Open the PDF file
    with open(pdf_file_path,'rb') as file:
        #create a pdf reader object
        pdf_reader = PyPDF2.PdfReader(file)
        #Extract text from each page
        text= ''

        for page_num in range(len(pdf_reader.pages)):
            page=pdf_reader.pages[page_num]
            text+= page.extract_text()
       
        # Regular expressions
        invoice_number_pattern = r'INVOICE\s*#\s*(\d+)'
        bill_to_pattern = r'Bills\s*To\s*:\s*(.*)'
        items_pattern = r'(.*?)\s*(\d+)\s*(€\d+\.\d{2})\s*(€\d+\.\d{2})'
        notes_terms_pattern = r'Notes\s*:\s*(.*?)\s*Terms\s*:\s*(.*)'

        #Extract information using Regular expressions
        invoice_number_match = re.search(invoice_number_pattern, text)
        bill_to_match = re.search(bill_to_pattern, text)
        items_matches = re.search(items_pattern, text)
        notes_terms_match = re.search(notes_terms_pattern, text)
        discount_tax_pattern = r'Discount\s*\((\d+)%\)[\s\s]*?Tax\s*\((\d+)%\)'

        #Extrated information
        invoice_number = invoice_number_match.group(1) if invoice_number_match else None
        bill_to = bill_to_match.group(1) if bill_to_match else None
        items = items_matches
        notes, terms = notes_terms_match.group() if notes_terms_match else (None, None)
        match =re.search(discount_tax_pattern, text)
        discount_percentage = match.group(1) 
        tax_percentage = match.group(2) 

        i=0
        subtotal=0
        total=0

        for item in items:
            if len(items)-1 != i:
                subtotal = subtotal + float(item[3].replace('€',''))
                i=i+1

        total_discount = subtotal - (subtotal*int(discount_percentage)/100)
        total= total_discount + (total_discount*int(tax_percentage)/100)

        return invoice_number, bill_to, subtotal, total, discount_percentage, tax_percentage, notes, terms
    

        print(f'Invoice Number: {invoice_number}')
        print(f'Bill To: {bill_to}')
        print(f'items: ')
        for item in items:
            print(f' - {item[0]}: {item[1]}: units x {item[2]} = {item[3]}')
        print(f'Notes: {notes}')
        print(f'Terms: {terms}')
        print(f'Discount Percentage: {discount_percentage}')
        print(f'Tax Percentage: {tax_percentage}')
        #print(text)


extract_invoice_info("invoice/invoice.pdf")