from PyPDF2 import PdfWriter

merge = PdfWriter()
pdfs = []
n = int(input("How many PDF's do you really want to merge?\n"))

for i in range(0,n):
    name = input(f"Enter the name of PDF{i + 1}:")
    pdfs.append(name)

for pdf in pdfs:
    merge.append(pdf)

merge.write("merged-pdf.pdf")
merge.close()