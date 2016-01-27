import argparse
import pypdfchptsplit.pdfsplit as pdfsplit


def parse_arguments():
    """Parses commands line options"""
    parser = argparse.ArgumentParser(
        description='Program to split PDF book into chapters'
    )
    parser.add_argument(
        'file', type=str,
        help='Path to the PDF file to be split'
    )
    parser.add_argument(
        'pages', nargs='+', type=int,
        help='Space delimited list of the fist page of each chapter'
    )
    return parser.parse_args()


def process_commands():
    """Parses and processes command line options"""
    # Parse and handle each different command
    args = parse_arguments()

    pdfsplit.pdf_split(args.file, args.pages)
