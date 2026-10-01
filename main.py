from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk,ImageDraw,ImageFont

opeing=''

def save_image():
    opeing.save("watermark.jpg")

def open_image():
    global opeing
    
    open_image=filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if open_image:
        opeing=Image.open(open_image)
        set_size(400,400)
        show()
        
def set_size(x,y):
    global opeing
    opeing=opeing.resize((x,y))
    show()
    
def show():
    showing=ImageTk.PhotoImage(opeing)
    label_image.config(image=showing)
    label_image.image=showing
    
def water_add():
    edit=ImageDraw.Draw(opeing)
    font = ImageFont.truetype("arial.ttf", 20)
    edit.text((10,10),input.get(),fill=theme.get(),font=font)
    show()
    
def value_change(a):
    data=a.split(",")
    x=int(data[0])
    y=int(data[1])
    set_size(x,y)
    
window=Tk()
window.title("Image Resizer & Watermark Tool")
window.config(padx=100,pady=20)

button=Button(text="Upload Image",width=25,font=("Arial",15,'bold'),command=open_image)
button.grid(column=0,row=1,pady=10,columnspan=2)

show_px=Label(text="Image Size in Pixels (Example: 200,200) (1cm → 78.74 px)",font=("Arial",15,'bold'),fg='red')
show_px.grid(column=0,row=2,pady=5,columnspan=2)

size=Entry(width=30,font=("Arial",15,'bold'))
size.grid(column=1,row=3,sticky='w')
size.insert(0,'400,400')

size_button=Button(text="Set",font=("Arial",12,'bold'),command=lambda: value_change(size.get()))
size_button.grid(column=0,row=3,sticky='e',padx=10)

theme=StringVar(value='Watermark Color')
OptionMenu(window,theme,'white','black').grid(column=0,row=4,pady=10,padx=10,sticky='e')

input=Entry(width=30,font=("Arial",15,'bold'))
input.grid(column=1,row=4,pady=10,sticky='w')
input.insert(0,"watermark")

label_image=Label(window)
label_image.grid(column=0,row=7,columnspan=2)

add_watermark=Button(text="Add Watermark",width=20,font=("Arial",15,'bold'),fg='blue',command=water_add)
add_watermark.grid(column=0,row=5,pady=10,columnspan=2)

save_image=Button(text="Save Image",width=20,font=("Arial",15,'bold'),fg='red',command=save_image)
save_image.grid(column=0,row=6,pady=10,columnspan=2)

window.mainloop()
