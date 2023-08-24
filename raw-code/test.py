import PyPDF2

# Open the PDF file
with open("E:\hackathon\Resume(19-07-23).pdf", "rb") as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
 
    num_pages = len(pdf_reader.pages)
    print("Number of pages:", num_pages)
    
    # Iterate over all the pages
    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()
        print(f"Page {page_number + 1}:\n{page_text}\n")
    
    # Read all the text into one string
    all_text = "\n\n".join([page.extract_text() for page in pdf_reader.pages])
    print("All text:\n", all_text)
