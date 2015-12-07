#Python programming project
#Christian Mills

#importing the GUI
from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style
import webbrowser


#defining the class
class Example(Frame):
      
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    #setting up the GUI    
    def initUI(self):
        #sets the title of the window  
        self.parent.title("Do you dare to Zlatan?")
        self.style = Style()
        self.style.theme_use("alt")
        #creates an object for the window
        self.pack(fill=BOTH, expand=1)
        #makes buttons
        quitButton = Button(self, text="No, Zlatan sucks",
            command=self.quit)
        quitButton.place(x=30, y=50)

        webbutton = Button(self, text="Yes, #DaretoZlatan", command=self.OpenUrl)
        webbutton.place(x=130, y=50)
    #defines what the buttons do    
    def quit(self):
        self.parent.destroy()

    def OpenUrl(self):
        webbrowser.open_new('https://www.youtube.com/watch?v=ia-zi5oLa_0')




#the code that runs when the program starts
def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
