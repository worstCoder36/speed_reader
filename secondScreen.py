import tkinter as tk
from properties import *
import FileOperations
import time
class SecondScreen():
    words = []
    wordLabel = ""
    def startSpeedRead(self,root):
        for word in self.words:
            self.wordLabel.config(text=word)
            root.update_idletasks()
            time.sleep(1)
    def goBack(self,secondFrame,oldFrame):
        secondFrame.pack_forget()
        oldFrame.pack(fill='both',expand=True)
        
    def __init__(self,root,oldFrame):
        global words
        secondFrame = tk.Frame(root)
        secondFrame.pack(fill='both',expand=True)
        fileOp = FileOperations.FileOp()
        contents = fileOp.readFile()
        self.words = contents.split(' ')
        self.wordLabel = tk.Label(secondFrame,text=self.words[0])
        self.wordLabel.pack(fill='both',expand=True,anchor='center')
        
        buttonFrame = tk.Frame(secondFrame)
        buttonFrame.pack(fill='x')
        
        backButton = tk.Button(buttonFrame,text='Back',command=lambda:self.goBack(secondFrame,oldFrame))
        backButton.pack(side='left')
        
        readButton = tk.Button(buttonFrame,text='Start',command=lambda:self.startSpeedRead(root))
        readButton.pack(anchor='center')
