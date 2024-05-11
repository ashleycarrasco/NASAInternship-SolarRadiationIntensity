#Ashley Carrasco -- NASA STEM Internship
#Mentor: Professor Kevin Squires
#Advisors: Professors Ana Teodorescu and Karina Ochs

#main screen (planet selection)
import tkinter as tk
import planetInfo as pli
from PIL import Image, ImageTk

primaryWindow = tk.Tk()
primaryWindow.title("The Solar System: Calculating the Solar Irradiance")
primaryWindow.geometry('1400x800')

#planet events
def mercuryClicked(e):
    print("mercury cliked")
    pli.planetInfo("mercury", 88, primaryWindow)

def venusClicked(e):
    print("venus cliked")
    pli.planetInfo("venus", 224,primaryWindow)

#def earthClicked(e):
    #print("earth clicked")
    #pw.planetInfo("earth", 366,window)

def marsClicked(e):
    print("mars cliked")
    pli.planetInfo("mars", 687, primaryWindow)

def jupiterClicked(e):
    print("jupiter cliked")
    pli.planetInfo("jupiter", 366,primaryWindow)

def saturnClicked(e):
    print("saturn cliked")
    pli.planetInfo("saturn", 366,primaryWindow)

def uranusClicked(e):
    print("uranus cliked")
    pli.planetInfo("uranus", 366,primaryWindow)

def neptuneClicked(e):
    print("neptune cliked")
    pli.planetInfo("neptune", 366,primaryWindow)


#background
imageBg = Image.open("images/background.jpeg")
imageBg = imageBg.resize((1400,800))
bgPhoto = ImageTk.PhotoImage(imageBg)

canvas = tk.Canvas(primaryWindow, width=1400, height=800)
canvas.pack()
canvas.create_image(0,0,anchor=tk.NW, image=bgPhoto)

#planet images
imageSun = Image.open("images/sun.png")
imageMercury = Image.open("images/mercury.png")
imageVenus = Image.open("images/venus.png")
imageEarth = Image.open("images/earth.png")
imageMars = Image.open("images/mars.png")
imageJupiter = Image.open("images/jupiter.png")
imageSaturn = Image.open("images/saturn.png")
imageUranus = Image.open("images/uranus.png")
imageNeptune = Image.open("images/neptune.png")

resize_Sun = imageSun.resize((285,285))
resize_Mercury = imageMercury.resize((46,46))
resize_Venus = imageVenus.resize((67,67))
resize_Earth = imageEarth.resize((72,72))
resize_Mars = imageMars.resize((69,69))
resize_Jupiter = imageJupiter.resize((190,190))
resize_Saturn = imageSaturn.resize((280,175))
resize_Uranus = imageUranus.resize((90,90))
resize_Neptune = imageNeptune.resize((90,90))

imageSun = ImageTk.PhotoImage(resize_Sun)
imageMercury = ImageTk.PhotoImage(resize_Mercury)
imageVenus = ImageTk.PhotoImage(resize_Venus)
imageEarth = ImageTk.PhotoImage(resize_Earth)
imageMars = ImageTk.PhotoImage(resize_Mars)
imageJupiter = ImageTk.PhotoImage(resize_Jupiter)
imageSaturn = ImageTk.PhotoImage(resize_Saturn)
imageUranus = ImageTk.PhotoImage(resize_Uranus)
imageNeptune = ImageTk.PhotoImage(resize_Neptune)

imgSun = canvas.create_image(140, 350, anchor=tk.CENTER, image=imageSun)
imgMercury = canvas.create_image(300, 350, anchor=tk.CENTER, image=imageMercury)
imgVenus = canvas.create_image(375, 350, anchor=tk.CENTER, image=imageVenus)
imgEarth = canvas.create_image(465, 350, anchor=tk.CENTER, image=imageEarth)
imgMars = canvas.create_image(568, 350, anchor=tk.CENTER, image=imageMars)
imgJupiter = canvas.create_image(740, 350, anchor=tk.CENTER, image=imageJupiter)
imgSaturn = canvas.create_image(960, 350, anchor=tk.CENTER, image=imageSaturn)
imgUranus = canvas.create_image(1160, 350, anchor=tk.CENTER, image=imageUranus)
imgNeptune = canvas.create_image(1275, 350, anchor=tk.CENTER, image=imageNeptune)

#action from event
canvas.tag_bind(imgMercury, "<Button-1>", mercuryClicked)
canvas.tag_bind(imgVenus, "<Button-1>", venusClicked)
#canvas.tag_bind(imgEarth, "<Button-1>", earthClicked)
canvas.tag_bind(imgMars, "<Button-1>", marsClicked)
canvas.tag_bind(imgJupiter, "<Button-1>", jupiterClicked)
canvas.tag_bind(imgSaturn, "<Button-1>", saturnClicked)
canvas.tag_bind(imgUranus, "<Button-1>", uranusClicked)
canvas.tag_bind(imgNeptune, "<Button-1>", neptuneClicked)

#event loop
primaryWindow.mainloop()