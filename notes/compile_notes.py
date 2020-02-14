import os
import subprocess

import PyPDF2
import contextlib


CHAPTERS_PATH = "chapters/"
PDF_DIR = "pdf_out/"
BOOK_OUTPUT = "./book.pdf"

def get_chapters():
    return os.listdir(CHAPTERS_PATH)

def get_pdfs():
    return os.listdir(PDF_DIR)

def chapters_to_pdf():
    # TODO add bit about emptying out the pdf_out dir
    chapters = get_chapters()
    for chapter in chapters:
        curr_path = os.path.join(CHAPTERS_PATH, chapter)
        if os.path.isdir(curr_path):
            files_in_chapter = os.listdir(curr_path)
            for file_ in files_in_chapter:
                if file_.endswith(".md"):
                    print(subprocess.check_output(["mdpdf", os.path.join(curr_path, file_)]))
                    pre,_ = os.path.splitext(file_)
                    os.rename(os.path.join(curr_path, pre + ".pdf"), os.path.join(PDF_DIR, chapter[:2] + pre + ".pdf"))

def pdfs_to_book():
    with contextlib.ExitStack() as stack:
        pdfMerger = PyPDF2.PdfFileMerger()
        pdfs = get_pdfs()
        sorted_pdfs = [os.path.join(PDF_DIR, pdf) for pdf in pdfs]
        sorted_pdfs.sort()

        files = [stack.enter_context(open(pdf, 'rb')) for pdf in sorted_pdfs]
        for f in files:
            pdfMerger.append(f)
        with open(BOOK_OUTPUT, 'wb') as f:
            pdfMerger.write(f)

if __name__ == "__main__":
    chapters_to_pdf()
    pdfs_to_book()
