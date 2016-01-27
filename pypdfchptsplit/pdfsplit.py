import os
from bisect import bisect_right
import PyPDF2


def pdf_split(filename, pages, offset=0):
    """Splits the given file into chapters at the given pages"""
    # Load the PDF file
    with open(filename, 'rb') as pdf_file_obj:
        pdf = PyPDF2.PdfFileReader(pdf_file_obj)

        # Clean pages iterable; make sure no dupes, sorted, and in valid range
        clean_pages = sorted(map(lambda x: (x-1+offset), set(pages)))
        if clean_pages[-1] >= pdf.numPages or clean_pages[0] < 0:
            raise ValueError('Pages outside of vaild range for the given PDF.')

        # Create a PdfFileWriter for each chapter
        chapters = {
            (chpt+1): PyPDF2.PdfFileWriter() for chpt in range(len(clean_pages))
        }

        # Check each page for its chapter and add it to the corresponding writer
        for pg_num in range(pdf.numPages):
            # Get the chapter for the given page
            chpt_num = bisect_right(clean_pages, pg_num)

            if chpt_num in chapters:
                chapters[chpt_num].addPage(pdf.getPage(pg_num))

        # Path manipulations to set up output directory and files
        base_name = os.path.splitext(os.path.basename(filename))[0]
        in_dir = os.path.dirname(filename)
        out_dir = os.path.join(in_dir, '{}_chapters'.format(base_name))
        # Make output directory if necessary
        os.makedirs(out_dir, exist_ok=True)

        # Write all writers to new PDF files
        for chpt_num, writer_obj in chapters.items():
            chpt_filename = '{} (Ch {}).pdf'.format(base_name, chpt_num)
            chpt_filepath = os.path.join(out_dir, chpt_filename)
            with open(chpt_filepath, 'wb') as file_obj:
                writer_obj.write(file_obj)
