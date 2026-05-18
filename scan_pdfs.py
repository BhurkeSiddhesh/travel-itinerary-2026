import os
import fitz  # PyMuPDF
import sys

# Set standard output encoding to utf-8 in case it's not set
sys.stdout.reconfigure(encoding='utf-8')

def scan_pdf(filepath):
    print("=" * 60)
    print(f"File: {os.path.basename(filepath)}")
    print("=" * 60)
    try:
        doc = fitz.open(filepath)
        print(f"Pages: {len(doc)}")
        text = ""
        for i, page in enumerate(doc):
            text += f"--- Page {i+1} ---\n"
            text += page.get_text()
        # Print with encoding safe characters
        print(text[:2000])
        if len(text) > 2000:
            print("... [TRUNCATED] ...")
    except Exception as e:
        print(f"Error scanning: {e}")
    print("\n")

pdf_dir = "tickets-bookings"
for f in os.listdir(pdf_dir):
    if f.endswith(".pdf"):
        scan_pdf(os.path.join(pdf_dir, f))
