from tkinter import *
from tkinter import filedialog,messagebox
import subprocess
from turtle import undo
path=''

def font_inc(event=None):
    global font_size
    font_size+=1
    textarea.config(font=('arial',font_size,'bold'))

def font_dec(event=None):
    global font_size
    font_size-=1
    textarea.config(font=('arial',font_size,'bold'))



def run_code():
    if path=='':
        messagebox.showerror('Error','Please save the file before running')
    else:
        command=f'python {path}'
        run_file=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        output,error=run_file.communicate()
        outputarea.delete(1.0,END)
        outputarea.insert(1.0,output)
        outputarea.insert(1.0,error)



def saveas(event=None):
    global path
    path=filedialog.asksaveasfilename(filetypes=[('Python Files','*.py')],defaultextension=('.py'))
    if path!='':
        file=open(path,'w')
        file.write(textarea.get(1.0,END))
        file.close()

def openfile(event=None):
    global path
    path=filedialog.askopenfilename(filetypes=[('Python Files','*.py')],defaultextension=('.py'))
    print(path)
    if path != '':
        file=open(path,'r')
        data=file.read()
        textarea.delete(1.0,END)
        textarea.insert(1.0,data)
        file.close()

def save(event=None):
    if path=='':
        saveas()
    else:
        file=open(path,'w')
        file.write(textarea.get(1.0,END))
        file.close()

def new(event=None):
    global path
    path=''
    textarea.delete(1.0,END)
    outputarea.delete(1.0,END)

def exit(event=None):
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        hulk.destroy()
    else:
        pass

def theme():
    if check.get()=='light':
        textarea.config(bg='white',fg='black')
        outputarea.config(bg='white',fg='black')

    if check.get()=='dark':
        textarea.config(bg='gray20', fg='white')
        outputarea.config(bg='gray20', fg='white')


def clear():
    textarea.delete(1.0,END)
    outputarea.delete(1.0,END)

font_size=18

hulk=Tk()
hulk.geometry('1200x600')
hulk.title('Hulk-Py Editor')

check=StringVar()
check.set('light')
myMenu=Menu()
filemenu=Menu(myMenu,tearoff=False)
filemenu.add_command(label='New File',accelerator='Ctrl+N',command=new)
filemenu.add_command(label='Open File',accelerator='Ctrl+O',command=openfile)
filemenu.add_command(label='Save',accelerator='Ctrl+S',command=save)
filemenu.add_command(label='Save as',accelerator='Ctrl+G',command=saveas)
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',command=exit)
myMenu.add_cascade(label='File',menu=filemenu)

thememenu=Menu(myMenu,tearoff=False)
thememenu.add_radiobutton(label='Light',variable=check,value='light',command=theme)
thememenu.add_radiobutton(label='Dark',variable=check,value='dark',command=theme)

myMenu.add_cascade(label='Themes',menu=thememenu)

myMenu.add_command(label='Clear',command=clear)

myMenu.add_command(label='Run',command=run_code)

editFrame=Frame(hulk,bg='white')
editFrame.place(x=0,y=0,height=500,relwidth=1)

scrollbar=Scrollbar(editFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(editFrame,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
textarea.pack(fill=BOTH)
scrollbar.config(command=textarea.yview)

outputFrame=LabelFrame(hulk,text='Output',font=('arial',10,'bold'))
outputFrame.place(x=0,y=450,relwidth=6,height=300)

scrollbar1=Scrollbar(outputFrame,orient=VERTICAL)
scrollbar1.pack(side=RIGHT,fill=Y)
outputarea=Text(outputFrame,font=('arial',10,'bold'),yscrollcommand=scrollbar1.set)
outputarea.pack(fill=BOTH)
scrollbar1.config(command=textarea.yview)

hulk.config(menu=myMenu)

hulk.bind('<Control-n>',new)
hulk.bind('<Control-o>',openfile)
hulk.bind('<Control-s>',save)
hulk.bind('<Control-g>',saveas)
hulk.bind('<Control-q>',exit)
hulk.bind('<Control-p>',font_inc)
hulk.bind('<Control-m>',font_dec)

hulk.mainloop()