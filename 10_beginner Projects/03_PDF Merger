from pypdf import PdfWriter

# 1. Initialize the writer
merger = PdfWriter()

# 2. Append your PDF files in order
n=int(input("Enter the number of PDF files to merge: "))
pdfs = []

for i in range(n):
    name=input(f"Enter the name of PDF: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

# 3. Write out the combined PDF and close the file
merger.write("merged_output.pdf")
merger.close()
