#IMPORT TKINTER MODULES FOR BUILDING UI
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

#PROVIDE FUNCTIONS TO BE USED IN UI 

def selectImage(): 
    global canvas
    canvas = Canvas(root, width = 300, height=300)
    canvas.grid(row=0, column=1, columnspan=3, padx='150px', pady='10px')
    filename=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])  
    img = Image.open(filename) 
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(20, 20, anchor=NW, image=img)
    canvas.image = img

def analyzeImage():
    result_output["text"] = "Benign"

def clearImage():
    global canvas
    canvas.delete('all')
    canvas.destroy()
    del canvas

#PROVIDE UI WIDGETS
root = Tk()
root.title("BREAST CANCER DETECTOR")
root.geometry("765x550")
#root.resizable(width = True, height = True)

#root.rowconfigure(1, minsize=400, weight=1)
#root.columnconfigure(0, minsize=400, weight=1)

#IMAGE LABEL
img_lbl = Label(root, bg='#8e2de2', width=42, height=22, image='', fg='white', padx='10px', pady='10px')
img_lbl.grid(row=0, column=1, columnspan=3, padx='150px', pady='10px')

#IMAGE CANVAS
canvas = Canvas(root, width = 300, height=300)
canvas.grid(row=0, column=1, columnspan=3, padx='150px', pady='10px')

#CHOOSE IMAGE BUTTON
choose_btn = Button(root, bg='#4a00e0', fg='white', padx='5px', pady='5px', 
text='Choose image', command=selectImage, font=('bold', 12))
choose_btn.grid(row=1, column=1, padx='0px', pady='10px')

#ANALYZE IMAGE BUTTON
analyze_btn = Button(root, bg='#4a00e0', fg='white', padx='5px', pady='5px', 
text='Analyze image', font=('bold', 12), command=analyzeImage )
analyze_btn.grid(row=1, column=2, padx='0px', pady='10px')

#CLEAR IMAGE BUTTON
clear_btn = Button(root, bg='#4a00e0', fg='white', text='Clear image', padx='5px', 
pady='5px', command=clearImage, font=('bold', 12))
clear_btn.grid(row=1, column=3, padx='0px', pady='10px')

#SHOW RESULT OF ANALYSIS
result_label = Label(root, text='Result', bg='#f80759', fg='white', padx='5px', pady='5px', font=('bold', 12))
result_output = Label(root, text='Malignant', bg='white', fg='black', padx='5px', pady='5px', font=('bold', 12))
result_label.grid(row=4, column=1, sticky=E, padx='0px', pady='20px')
result_output.grid(row=4, column=2, sticky=W, padx='0px', pady='20px')

root.mainloop()