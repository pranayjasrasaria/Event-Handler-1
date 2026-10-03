from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("100x100")

def handler_keypress(event):
    """Print the character associated to the keypressed"""
    print(event.char)   
    
window.bind('<Key>', handler_keypress)
def handler_click(event):
    print("The button was clicked")

button=Button(text="Click Me")
button.bind('<Button-1>', handler_click)
button.pack()
window.mainloop()