from Tkinter import * 
import tkFileDialog
#-----------------
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

#------------------------------
import sys
import os
if sys.version_info[0] < 3:
   import Tkinter as Tk
else:
   import tkinter as Tk

#------------------------------------

def browse_file():
    fname = tkFileDialog.askopenfilename(filetypes = (("pdf files", "pdf"), ("All files", "*")))

    fp = open(fname, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    ls=[]
    for page in pages:
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                print(x,y,text)
                #after you knew what are the values of the wanted X's and Y's
                #copy and paste the values bellow then comment the first print and
                #uncomment the second one to have a clear view of the resulat
                if x==9.6681 and y==74.58526499999999:
                    #print(text)
                   #it will be stored here 
                    ls.append(text)
    print fname

    #to write the list to txt tile  
    with open('your_file.txt', 'w') as f:
       for item in ls:
          print >> f, item
root=Tk.Tk()
root.wm_title("Browser")
broButton = Tk.Button(master = root, text = 'Browse', width = 10, fg='red',command=browse_file)
broButton.pack(side=Tk.BOTTOM, padx = 2, pady=2)
root.mainloop()
