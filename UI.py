import tkinter as tk
from secondScreen import *
from properties import *
import FileOperations
import time
class FirstScreen():
    global wpm
    wpmLabel = 0
    def incWpm(self):
        global wpm
        wpm += 5
        self.wpmLabel.config(text="WPM : "+str(wpm))
    def decWpm(self):
        global wpm
        wpm -= 5
        self.wpmLabel.config(text="WPM : "+str(wpm))
    def loadText(self,root,parentFrame,inputTextBox):
        #root.withdraw()
        global words
        contents=inputTextBox.get('1.0','end')
        fileOp = FileOperations.FileOp()
        fileOp.writeFile(contents)
        secondScreen = SecondScreen(root,parentFrame)
        parentFrame.pack_forget()
        
    def __init__(self,root):
        global wpm
        parentFrame = tk.Frame(root)
        parentFrame.pack(fill='both',expand=True)
        
        inputLabel = tk.Label(parentFrame,text="Input text here : ")
        inputLabel.pack(fill='x')
        
        inputTextBox = tk.Text(parentFrame)
        inputTextBox.pack(fill='x')
        
        self.wpmLabel = tk.Label(parentFrame)
        self.wpmLabel.pack(fill='x')
        self.wpmLabel.config(text="WPM : "+str(wpm))
        
        buttonFrame = tk.Frame(parentFrame)
        buttonFrame.pack()
        slowButton = tk.Button(buttonFrame,text='Slower',command=self.decWpm)
        slowButton.pack(side='left')
        fastButton = tk.Button(buttonFrame,text='Faster',command=self.incWpm)
        fastButton.pack(side='right')
        loadButton = tk.Button(buttonFrame,text='Load Text',command=lambda: self.loadText(root,parentFrame,inputTextBox))
        loadButton.pack(anchor='center',fill='x')
        #startButton = tk.Button(buttonFrame,text='Start',command=lambda: self.startRead(root,parentFrame))
        #startButton.pack(anchor='center')

class MainView():
    def __init__(self,root):
        global wpm
        firstScreen = FirstScreen(root)
        #secondScreen = SecondScreen(root)

        

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Speed Reader")
    window.state("zoomed")
    main = MainView(window)
    window.mainloop()

