import PyPDF2


def pdf_split(filename, pages):
    """Splits the given file into chapters at the given pages"""
    # Load the PDF file
    with open(filename, 'rb') as pdf_file_obj:
        pdf = PyPDF2.PdfFileReader(pdf_file_obj)

        # Clean pages iterable; make sure no dupes, sorted, and in valid range
        clean_pages = sorted(set(pages))
        if max(clean_pages) > pdf.numPages:
            raise ValueError('Pages outside of vaild range for the given PDF.')

        chapter_number = 1
        chapter_writer = PyPDF2.PdfFileWriter()
        for pg_num in range(pdf.numPages):
            try:
                if (pg_num >= clean_pages[chapter_number-1] and
                        pg_num < clean_pages[chapter_number]):
                    page = pdf.getPage(pg_num)
                else:

            except IndexError:
                # We have reached the last chapter, just keep writing to the last reader
                page = pdf.getPage(pg_num)
