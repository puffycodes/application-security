#!/usr/bin/env python3

import sys
import argparse
from markdown_pdf import MarkdownPdf, Section

def markdown_to_pdf(markdown_files, pdf_file, verbose=False):
    pdf = MarkdownPdf(toc_level=2, optimize=True)
    count = 1
    for file in markdown_files:
        if verbose:
            print(f'input file #{count}: {file}', file=sys.stderr)
        with open(file, 'r') as fd:
            text = fd.read()
            pdf.add_section(Section(text))
        count += 1
    if verbose:
        print(f'output file: {pdf_file}', file=sys.stderr)
    pdf.save(pdf_file)
    return

def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown Files to PDF File'
    )
    parser.add_argument('file', nargs='+')
    parser.add_argument('-o', '--output_file', required=True)
    args = parser.parse_args()

    markdown_to_pdf(args.file, args.output_file)

    return

if __name__ == '__main__':
    main()

# --- end of file --- #
