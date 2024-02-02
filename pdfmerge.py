import os
import argparse
from pypdf import PdfMerger

def create_directory(file_name: str):
    
    if '/' in file_name: # check if the file name contains directory information
        directory = os.path.dirname(file_name) # extract directory path
        if not os.path.exists(directory): # check if the directory exists
            os.makedirs(directory) 
            print(f"Directory '{directory}' created.")
        else:
            print(f"Directory '{directory}' already exists.")
            
def merge_pdfs(lst, name):    
    merger = PdfMerger()
    for file in lst:
        merger.append(file)
    print(f"Saving file at {name}")
    merger.write(f"{name}")
    merger.close()

def run(args):
    pdf_list = [file for file in os.listdir(args.folder_name) if file.endswith('.pdf')] # create a list of pdf from folder 
    file_name = args.file_name+'.pdf' if not args.file_name.endswith('.pdf') else args.file_name # adds .pdf to outputfile name
    print('Merging :', pdf_list)
    create_directory(file_name) # check for directory
    merge_pdfs([f'{args.folder_name}/{file}' for file in pdf_list], file_name) # merge files 
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(
        prog='Merge PDFs',
        description='This tool reads .pdf file in the folder and outputs a single merged pdf',
        epilog='Dev@RB'
    )
    parser.add_argument('folder_name')
    parser.add_argument('file_name')
    args = parser.parse_args()
    run(args)
    
    