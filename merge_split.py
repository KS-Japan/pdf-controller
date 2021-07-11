import os
import PyPDF2
import glob

def merge(pdfdir , outdir):
    merger = PyPDF2.PdfFileMerger()
    for filepath in glob.glob(pdfdir + '*.pdf'):
        merger.append(filepath)
    merger.write(outdir + 'merge.pdf')
    merger.close()

def split(filename, outpath):
    reader = PyPDF2.PdfFileReader(filename)
    page_n = reader.getNumPages()

    for page in range(page_n):
        split_page = PyPDF2.PdfFileWriter()
        split_page.addPage(reader.getPage(page))
        savepath = outpath + str(page) + '.pdf'
        with open(savepath, 'wb') as f:
            split_page.write(f)

if __name__ == "__main__":
    filename = './data/sample.pdf'
    splitpath = './split_out/'
    os.makedirs(splitpath, exist_ok=True)
    split(filename,splitpath)
    mergepath = './merge_out/'
    os.makedirs(mergepath, exist_ok=True)
    merge(splitpath, mergepath)
