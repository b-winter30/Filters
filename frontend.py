from matplotlib import image
from torch._C import Value
from filters import non_local_means_filter
from tkinter import *
from filters import median_filter, bilateral_filter
from PIL import ImageTk, Image, ImageEnhance
from tkinter import filedialog
  
# Function for opening the
# file explorer window
image_file = ""
file_tuple = []

def browseFiles(label_file_explorer):
    filenames = filedialog.askopenfilenames(initialdir = "/",
                                          title = "Select an image or files",
                                          filetypes = (("Image files",
                                                        ".png"),
                                                       ("Image files",
                                                        ".jpg"),
                                                        ("Image files",
                                                        ".jpeg"),("all files",
                                                        ".*")))
      
    # Change label contents
    label_file_explorer.configure(text="File/s loaded")
    global image_file
    global file_tuple
    file_tuple = filenames
    image_file = filenames[0]
    return None

def resize__and_convert_to_photo_images(img):
    basewidth = 28
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

def new_window(image_url):
    canvas = Canvas(root, height=1200, width=1200)
    canvas.pack()
    # img = ImageEnhance.Sharpness(Image.open(image_url).convert('RGB'))
    img = resize__and_convert_to_photo_images(Image.open(image_url))
    img1 = resize__and_convert_to_photo_images(median_filter(image_url, 5))
    img2 = resize__and_convert_to_photo_images(bilateral_filter(image_url))
    img3 = resize__and_convert_to_photo_images(non_local_means_filter(image_url))

    norm_label = Label(canvas, text='Unfiltered image', fg='white', bg='gray')
    norm_label.pack()
    median_label = Label(canvas, text='Median filter size = 5', fg='white', bg='gray')
    median_label.pack()
    bilat_label = Label(canvas, text='Bi-lateral filter ' + '\u03C3' + ' = 5' + '\u03C3' +' = 15', fg='white', bg='gray')
    bilat_label.pack()
    nlmeans_label = Label(canvas, text='Non-local means filter ', fg='white', bg='gray')
    nlmeans_label.pack()
    #The coordinates here need to be changed to be dynamic
    canvas.create_window(50, 10, window=norm_label)
    canvas.create_window(400, 10, window=median_label)
    canvas.create_window(800, 10, window=bilat_label)
    canvas.create_window(50, 490, window=nlmeans_label)
    canvas.create_image(0, 20, image=img, anchor=NW)
    canvas.create_image(400, 20, image=img1, anchor=NW)
    canvas.create_image(800, 20, image=img2, anchor=NW)
    canvas.create_image(0, 500, image=img3, anchor=NW)
    mainloop()
    return None

def new_window(image_urls):
    canvas = Canvas(root, height=1200, width=1200)
    canvas.pack()
    # img = ImageEnhance.Sharpness(Image.open(image_url).convert('RGB'))
    img = resize__and_convert_to_photo_images(Image.open(image_url))

    norm_label = Label(canvas, text='Unfiltered image', fg='white', bg='gray')
    norm_label.pack()
    #The coordinates here need to be changed to be dynamic
    canvas.create_window(1000, 600, window=norm_label)
    canvas.create_image(1000, 600, image=img, anchor=NW)
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
    global file_tuple
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