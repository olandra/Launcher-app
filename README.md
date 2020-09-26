# Launcher-app
Python app for launching apps, files and web pages

Requires python 3.6+ and tkinter

## Currently implemented features
- Ability to add apps and files
- Ability to remove items from the list
- Automatic generation of the save.txt file
- If the list of items is empty, save.txt is automatically added to the list
- The list is saved upon closing the app, not when it's altered. Run time list is kept only in RAM

## To-Do
- Add URLs
- Add config file to save preferred web browser and wether or not the user wants new tab or window
- Switch to indexed referrals to avoid removing the first occurrance of an item if duplicates exist
- Add separators
- Comments and cleaning up the code
- Add saving save.txt into add and remove functions

## Considered additions
- Ability to choose which configured browser opens a URL
- Automatically opening config file if it doesn't exist or hasn't been set up

## What probably won't be added
- Ability to alter the list by drag-n-drop (format of the file is simple, so manual editing is good enough for now)