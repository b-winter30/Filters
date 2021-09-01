from tkinter import *
from filters import median_filter
from PIL import ImageTk, Image
from tkinter import filedialog
  
# Function for opening the
# file explorer window
image_file = ""

def browseFiles(label_file_explorer):
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.png*"),
                                                       ("Image files",
                                                        "*.jpg*"),
                                                        ("Image files",
                                                        "*.jpeg*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    global image_file
    image_file = filename
    return None

def new_window(image_url):
    canvas = Canvas(root, height=500, width=500)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(image_url))
    img1 = median_filter(image_url, 5)
    canvas.create_image(50, 10, image=img, anchor=NW)
    canvas.create_image(50, 10, image=img1, anchor=NE)
    mainloop()
    return None
    

def file_explorer_canvas():
    # Set window title
    canvas = Canvas(root, height=450, width=450)
    #Set window background color
    canvas.config(background = "white")
    # Create a File Explorer label
    label_file_explorer = Label(canvas,
                                text = "File Explorer using Tkinter",
                                width = 100, height = 4,
                                fg = "blue")
    button_explore = Button(canvas,
                            text = "Browse Files",
                            command = lambda: browseFiles(label_file_explorer))
    button_exit = Button(canvas,
                        text = "Exit",
                        command = lambda: exit_callback(canvas))
    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer.grid(column = 1, row = 1)
    button_explore.grid(column = 1, row = 2)
    button_exit.grid(column = 1,row = 3)
    canvas.pack()


def exit_callback(canvas):
    global image_file
    print (image_file)
    canvas.destroy()
    new_window(image_file)
    return None 
                                                                                            
# Create the root window
root = Tk() 
root.title('File explorer')
file_explorer_canvas()

# Let the window wait for any events
root.mainloop()