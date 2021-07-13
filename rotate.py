import os
from pdfrw import PdfReader, PdfWriter

def Rotate(inpfn, rotate, savepath):
    rotate = int(rotate)
    assert rotate % 90 == 0

    outfn = savepath + os.path.basename(inpfn)
    trailer = PdfReader(inpfn)
    pages = trailer.pages
    ranges = [[i] for i in range(1, len(pages)+1)]

    for onerange in ranges:
        onerange = (onerange + onerange[-1:])[:2]
        for pagenum in range(onerange[0]-1, onerange[1]):
            pages[pagenum].Rotate = (int(pages[pagenum].inheritable.Rotate or
                                         0) + rotate) %360
            outdata = PdfWriter(outfn)
            outdata.trailer = trailer
            outdata.write()


if __name__ == "__main__":
    pdfpath = './data/sample.pdf'
    rotate = 270
    savepath = './out/'
    os.makedirs(savepath, exist_ok=True)
    Rotate(pdfpath, rotate, savepath)
