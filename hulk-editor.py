import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkcode import CodeEditor

logo = '''
    _  _ _  _ _    _  _    ____ ___  _ ___ ____ ____ 
    |__| |  | |    |_/     |___ |  \ |  |  |  | |__/ 
    |  | |__| |___ | \_    |___ |__/ |  |  |__| |  \     
              
              coded by R3DHULK                                                               
'''
print(logo)
code=input("Enter file name : ")

hulk = tk.Tk()
hulk.title("Hulk Editor")
hulk.option_add("*tearOff", 0)


notebook = ttk.Notebook(hulk)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text=code+input('write extension : '))
notebook.pack(fill="both", expand=True)

code_editor = CodeEditor(
    tab_1,
    width=99,
    height=30,
    language="python",
    background="black",
    highlighter="dracula",
    font="Consolas",
    autofocus=True,
    blockcursor=True,
    insertofftime=0,
    padx=10,
    pady=10,
    
)
code_editor.pack(fill="both", expand=True)
code_editor.content = input("write here : ")
hulk.update()
hulk.minsize(hulk.winfo_width(), hulk.winfo_height())
hulk.mainloop()