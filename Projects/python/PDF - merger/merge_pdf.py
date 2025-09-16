from PyPDF2 import PdfMerger

pdf_files = [ "pdf1.pdf","pdf2.pdf" ]

merger = PdfMerger()

for pdf in pdf_files:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()

print("PDFs merged successfully!")
