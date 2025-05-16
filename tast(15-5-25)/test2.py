from pypdf import PdfReader, PdfWriter

files = [
    r"D:\pdf1.pdf",
    r"D:\pdf2.pdf",
    r"D:\pdf3.pdf",
    r"D:\pdf4.pdf",
    r"D:\pdf5.pdf"
]

writer = PdfWriter()
for i in files:
    pdf = PdfReader(i)
    for page in pdf.pages:
        writer.add_page(page)

with open("outcome.pdf", "wb") as out:
    writer.write(out)

print("done")
