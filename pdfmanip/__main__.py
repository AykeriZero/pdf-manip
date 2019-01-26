"""Rotate a pdf from the command line"""

import click        # command line argument processing
import PyPDF2       # pdf processing

# process command line arguments
# TODO: add option to rotate left or right
@click.command()
@click.argument('input_pdf')
def main(input_pdf):
    """Top Level Command Line Interface"""

    with open(input_pdf, 'rb') as pdf_in:
        pdf_reader = PyPDF2.PdfFileReader(pdf_in)
        pdf_writer = PyPDF2.PdfFileWriter()

        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            page.rotateClockwise(-90)
            pdf_writer.addPage(page)

        # input_pdf needs to be open?
        with open('rotated.pdf', 'wb') as pdf_out:
            pdf_writer.write(pdf_out)

    print('Hello World!')

if __name__ == "__main__":
    main()


