import os
from readline import append_history_file
from typing import List
from PyPDF2 import PdfFileMerger

def merge_pdf(filepath: List[str]):
    pdf_merger = PdfFileMerger()

    for fp in filepath:
        pdf_merger.append(fp)
    return pdf_merger

def print_help():
    print('-----\n' \
          'PDF Merger\n' \
          'Enter your pdfs files names in the order you want them to be merged\n'\
          'press Q to finish\n' \
          '-----'
        )

if __name__ == '__main__':
    path_list = []

    print_help()
    while True:
        cmd = input('> ')
        if cmd == 'Q':
            break
        if cmd:
            path = os.path.join('.', cmd)
            path_list.append(path)

    if len(path_list) == 0:
        print('No file to merge')
    else:
        try:
            mergerd_pdf = merge_pdf(path_list)
            output_filename = input('output file name: ')
            with open(f'{output_filename}.pdf', "wb") as file:
                mergerd_pdf.write(file)
        except Exception as error:
            print(f'Fail to merge pdf: {error}')
