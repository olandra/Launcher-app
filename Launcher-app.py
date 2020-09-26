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
    pass

def removeApp(app):
    apps.remove(app)

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
        menu.add_command(label='Add URL', command=addURL)
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