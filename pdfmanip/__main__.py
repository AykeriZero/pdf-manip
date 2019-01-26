"""Rotate a pdf from the command line"""

import click        # command line argument processing
import PyPDF2       # pdf processing

# process command line arguments
# TODO: add option to rotate left or right
@click.command()
@click.argument('input_pdf')
def main(input_pdf):
    """Top Level Command Line Interface"""

    print('Hello World!')

if __name__ == "__main__":
    main()


