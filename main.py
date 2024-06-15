from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring

from claptone import *
window = Tk()


#Colors#################
elementColor = "#8a32db"
textColor = "white"
mainColor = "#222222"
lighterMainColor = "#333333"
SecondColor = "#444444"
#Colors#################



instruments = [
    "Acoustic Grand Piano", "Bright Acoustic Piano", "Electric Grand Piano", "Honky-tonk Piano",
    "Rhodes Piano", "Chorused Piano", "Harpsichord", "Clavinet", "Celesta", "Glockenspiel",
    "Music box", "Vibraphone", "Marimba", "Xylophone", "Tubular Bells", "Dulcimer",
    "Hammond Organ", "Percussive Organ", "Rock Organ", "Church Organ", "Reed Organ", "Accordion",
    "Harmonica", "Tango Accordion", "Acoustic Guitar (nylon)", "Acoustic Guitar (steel)",
    "Electric Guitar (jazz)", "Electric Guitar (clean)", "Electric Guitar (muted)", "Overdriven Guitar",
    "Distortion Guitar", "Guitar Harmonics", "Acoustic Bass", "Electric Bass (finger)",
    "Electric Bass (pick)", "Fretless Bass", "Slap Bass 1", "Slap Bass 2", "Synth Bass 1", "Synth Bass 2",
    "Violin", "Viola", "Cello", "Contrabass", "Tremolo Strings", "Pizzicato Strings", "Orchestral Harp",
    "Timpani", "String Ensemble 1", "String Ensemble 2", "Synth Strings 1", "Synth Strings 2",
    "Choir Aahs", "Voice Oohs", "Synth Voice", "Orchestra Hit", "Trumpet", "Trombone", "Tuba",
    "Muted Trumpet", "French Horn", "Brass Section", "Synth Brass 1", "Synth Brass 2", "Soprano Sax",
    "Alto Sax", "Tenor Sax", "Baritone Sax", "Oboe", "English Horn", "Bassoon", "Clarinet", "Piccolo",
    "Flute", "Recorder", "Pan Flute", "Bottle Blow", "Shakuhachi", "Whistle", "Ocarina",
    "Lead 1 (square)", "Lead 2 (sawtooth)", "Lead 3 (calliope lead)", "Lead 4 (chiffer lead)",
    "Lead 5 (charang)", "Lead 6 (voice)", "Lead 7 (fifths)", "Lead 8 (brass + lead)", "Pad 1 (new age)",
    "Pad 2 (warm)", "Pad 3 (polysynth)", "Pad 4 (choir)", "Pad 5 (bowed)", "Pad 6 (metallic)", "Pad 7 (halo)",
    "Pad 8 (sweep)", "FX 1 (rain)", "FX 2 (soundtrack)", "FX 3 (crystal)", "FX 4 (atmosphere)", "FX 5 (brightness)",
    "FX 6 (goblins)", "FX 7 (echoes)", "FX 8 (sci-fi)", "Sitar", "Banjo", "Shamisen", "Koto", "Kalimba",
    "Bagpipe", "Fiddle", "Shana", "Tinkle Bell", "Agogo", "Steel Drums", "Woodblock", "Taiko Drum",
    "Melodic Tom", "Synth Drum", "Reverse Cymbal", "Guitar Fret Noise", "Breath Noise", "Seashore",
    "Bird Tweet", "Telephone Ring", "Helicopter", "Applause", "Gunshot"
]

isThereTab = False
tabControl = NONE
instrumentName = StringVar()
style = ttk.Style()
inputLenght = None
style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] ,"background": lighterMainColor,"title_color":"blue", "selected_title_color":"red"} },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": SecondColor,"foreground":elementColor },
            "map":       {"background": [("selected", mainColor)],
                          "expand": [("selected", [1, 1, 1, 0])]} } } )

style.theme_use("yummy")

def createMusic():
    e_text=inputLenght.get()
    if(not e_text.isnumeric() ):
        messagebox.showerror("Error!", "Lenght has to be a Integer")
        return
    e_text = int(e_text)
    print(e_text)
    if(e_text<=0 ):
        messagebox.showerror("Error!", "Lenght has to be a positive number")
        return
    if(e_text>100 ):
        messagebox.showerror("Error!", "Lenght can't be above 100s")
        return
    if(instrumentName.get()=="" ):
        messagebox.showerror("Error!", "Please select an instrument")
        return
    print(instrumentName.get())
    notes_to_midi(generated_notes,"w.mid",instrumentName.get())

def createOptionsSection(frame):
    global inputLenght
    l1 = Label(frame,text="Enter Paremeters",width=20,fg=elementColor,bg=mainColor, font =
               ('calibri', 35, 'bold','underline'))
    lenghtOfFile = 30
    # l1 = Label(frame,textvariable=v,width=10,fg=elementColor)
    l1.place(relx=0.5, rely=0.1, anchor=CENTER)
    l2 = Label(frame,text="Whats the lenght of the music peice?",width=30,fg=textColor,bg=mainColor, font =
            ('calibri', 30))
    l2.place(relx=0.5, rely=0.2, anchor=CENTER)
    
    
    inputLenght = Entry(window,textvariable = lenghtOfFile, font=('calibre',15,'normal'),bg=mainColor,fg=textColor,width=10)
    inputLenght.config(highlightbackground=elementColor)
    inputLenght.place(relx=0.5, rely=0.27, anchor=CENTER)

    l2 = Label(frame,text="Whats instrument do you want to play",width=40,fg=textColor,bg=mainColor, font =
            ('calibri', 30))
    l2.place(relx=0.5, rely=0.32, anchor=CENTER)
    combo = ttk.Combobox(
        state="readonly",
        values=instruments,
        textvariable = instrumentName
    )
    combo.place(relx=0.5, rely=0.38, anchor=CENTER)

    createBtn = Button(text="Create",width=20,fg=elementColor,bg=mainColor,command=createMusic, font =
               ('calibri', 20, 'bold'))
    createBtn.place(relx=0.5, rely=0.45, anchor=CENTER)
def createTab():
    name = askstring("New Project","What is the Name of the project?")
    if name == "": return
    if not isinstance(name, str): return
    global isThereTab
    global tabControl
    if not isThereTab:
        tabControl = ttk.Notebook(window)
        tabControl.place(width=1600, height=900)
        isThereTab = True

    tab1 = Frame(tabControl, bg= mainColor)
    tabControl.add(tab1, text=name)
    
    createOptionsSection(tab1)

def firstTab():
    createTab()



window.title("Claptone")
# window.resizable(False, False)
canvas1 = Frame(window, width=1600, height=900,bg="#222222")
canvas1.pack()
window.config(bg='#222222')
commadMenu =  Menu(window)
window.configure(menu=commadMenu)
filemenue = Menu(commadMenu, tearoff=0)
filemenue.add_command(label="Create another music peice",command=createTab)
filemenue.add_command(label="Train",command=createTab)
filemenue.add_command(label="Locate Dataset",command=createTab)
commadMenu.add_cascade(label="File", menu=filemenue)

B = Button(canvas1, text ="Create your\n first sound!",fg=textColor,bg=elementColor, font =
               ('calibri', 20, 'bold') ,command = firstTab ,borderwidth = 0,width=15,height=3)

B2 = Button(canvas1, text ="Train the model",fg=textColor,bg=elementColor, font =
               ('calibri', 20, 'bold') ,command = None ,borderwidth = 0,width=15,height=3)

B3 = Button(canvas1, text ="Locate Data",fg=textColor,bg=elementColor, font =
               ('calibri', 20, 'bold') ,command = None ,borderwidth = 0,width=15,height=3)

B.place(relx=0.3, rely=0.5, anchor=CENTER)
B2.place(relx=0.7, rely=0.5, anchor=CENTER)
B3.place(relx=0.5, rely=0.5, anchor=CENTER)

window.wm_attributes('-transparentcolor','black')


def showError():
    messagebox.showerror("Error!", "There is an error in your input")

mainloop()