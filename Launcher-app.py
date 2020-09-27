import tkinter as tk
from tkinter import filedialog, Text
import os
from functools import partial

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
else:
    apps.append(os.getcwd() + '/save.txt')
    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')

def addApp():
    filename = filedialog.askopenfile(initialdir='/', title='Select File', filetypes=(('all files', '*.*'),))
    if filename:
        apps.append(filename.name)
    
    for widget in root.winfo_children():
        widget.destroy()

    for app in apps:
        button = tk.Button(root, text=app, bg='gray', command=partial(runApp, app))
        button.bind('<Button-3>', partial(openMenu, app=app))
        button.pack(fill='x')

def runApps():
    for app in apps:
        os.startfile(app)

def runApp(app):
    os.startfile(app)

def addURL():
    url = textBox.get()
    if url:
        apps.append(url)

    for widget in root.winfo_children():
        widget.destroy()

    for app in apps:
        button = tk.Button(root, text=app, bg='gray', command=partial(runApp, app))
        button.bind('<Button-3>', partial(openMenu, app=app))
        button.pack(fill='x')

def addURLMenu():
    top = tk.Toplevel()
    top.title('Enter URL')
    label = tk.Label(top, text='Enter URL')
    label.grid(row=0, column=0)
    global textBox
    textBox = tk.Entry(top, width=40)
    textBox.grid(row=0, column=1)
    buttonSave = tk.Button(top, text='Save', command=addURL)
    buttonSave.grid(row=1, column=0)
    # buttonCancel = tk.Button(top, text='Cancel')
    # buttonCancel.grid(row=1, column=1)

def removeApp(app):
    apps.remove(app)

    if len(apps) == 0:
        apps.append(os.getcwd() + '/save.txt')

    for widget in root.winfo_children():
        widget.destroy()

    for app in apps:
        button = tk.Button(root, text=app, bg='gray', command=partial(runApp, app))
        button.bind('<Button-3>', partial(openMenu, app=app))
        button.pack(fill='x')

def openMenu(event, app):
    try:
        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label='Add File', command=addApp)
        menu.add_command(label='Add URL', command=addURLMenu)
        menu.add_command(label='Remove', command=partial(removeApp, app=app))

        menu.tk_popup(event.x_root, event.y_root, 0)
    finally:
        menu.grab_release()

for app in apps:
    # button = tk.Button(root, text=app, bg='gray', command=lambda x=apps.index(app): runApp(apps[x]))
    button = tk.Button(root, text=app, bg='gray', command=partial(runApp, app))
    button.bind('<Button-3>', partial(openMenu, app=app))
    button.pack(fill='x')

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')