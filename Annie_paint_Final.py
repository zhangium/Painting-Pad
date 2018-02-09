"""
Annie Zhang
January 26th 2015
ICS3U
Painting Pad
Paint Project based on Breaking Bad
"""

from pygame import *
from random import randint
import os
from math import hypot
from math import sqrt
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

#=====================================START============================================
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,20'
screen = display.set_mode((1200,750)) #600/800 = 3/4

display.set_caption("Painting Pad")
displayIcon=image.load("displayIcon.png")
display.set_icon(displayIcon)

bg=image.load("periodicTableBG_crop.png")
bg=transform.scale(bg,(1300,800)) #transformed
screen.blit(bg,(-50,-50))

colour_pic = image.load("colourPalette.png")
colour_pic = transform.scale(colour_pic,(250,140))
colour_rect = Rect(140,575,250,140)
screen.blit(colour_pic,(140,575))

canvas_length = 940
canvas_height = 475
canvas_rect = Rect(145,60,canvas_length,canvas_height)
draw.rect(screen,(255,255,255),canvas_rect)
canvas = screen.subsurface(canvas_rect)

#=================================LEFT SIDE COLUMN====================================
pen_b=Rect(15,20,50,70)
pen_pic = image.load("pencil.png")
pen_hover = image.load("pencil_hover.png")

erase_b = Rect(10,95,50,70)
eraser_pic = image.load("hydrofluoric.png")
eraser_pic = transform.scale(eraser_pic,(50,55))
eraser_hover = image.load("hydrofluoric_hover.png")
eraser_hover = transform.scale(eraser_hover,(50,55))

brush_b = Rect(10,185,50,70)
brush_pic = image.load("brush.png")
brush_pic = transform.scale(brush_pic,(30,50))
brush_hover = image.load("brush_hover.png")
brush_hover = transform.scale(brush_hover,(30,50))

spray_b=Rect(10,245,50,70)
spray_pic = image.load("spray.png")
spray_pic = transform.scale(spray_pic,(30,45))
spray_hover = image.load("spray_hover.png")
spray_hover = transform.scale(spray_hover,(30,45))

fill_b = Rect(10,330,50,70)
fill_pic = image.load("beaker.png")
fill_hover = image.load("beaker_hover.png")

text_b = Rect(15,400,50,70)
text_pic = image.load("text.png")
text_pic = transform.scale(text_pic,(45,45))
text_hover = image.load("text_hover.png")
text_hover = transform.scale(text_hover,(45,45))

dropper_b = Rect(20,470,50,70)
dropper_pic = image.load("eyedropper.png")
dropper_pic = transform.scale(dropper_pic,(45,45))
dropper_hover = image.load("eyedropper_hover.png")
dropper_hover = transform.scale(dropper_hover,(45,45))

#==================================2ND LEFT COLUMN=======================================
line_b=Rect(75,105,50,80)
draw.line(screen,(0,0,0),(80,120),(110,160),2)

rectangle_b = Rect(75,175,50,70)
draw.rect(screen,(0,0,0),(85,190,35,45),2)

ellipse_b = Rect(75,245,60,70)
draw.ellipse(screen,(0,0,0),(80,265,50,40),2)

fillRect_b = Rect(75,315,50,80)
draw.rect(screen,(0,0,0),(85,335,35,45))

fillElip_b = Rect(75,390,60,70)
draw.ellipse(screen,(0,0,0),(80,400,50,40))

poly_pic = image.load("polygon.png")
poly_pic = transform.scale(poly_pic,(45,45))
poly_b = Rect(75,465,70,70)
poly_hover = image.load("polygon_hover.png")
poly_hover = transform.scale(poly_hover,(45,45))

#=============================RIGHT SIDE COLUMN===============================
undo_b = Rect(1100,25,50,70)
undo_pic = image.load("undo.png")
undo_pic = transform.scale(undo_pic,(30,40))
undo_hover = image.load("undo_hover.png")
undo_hover = transform.scale(undo_hover,(30,40))

redo_b = Rect(1100,105,50,70)
redo_pic = image.load("undo.png")
redo_pic = transform.scale(redo_pic,(30,40))
redo_pic = transform.flip(redo_pic,True,False)
redo_hover = transform.flip(undo_hover,True,False)

open_b = Rect(1100,170,50,70)
open_pic = image.load("file.png")
open_pic = transform.scale(open_pic,(40,50))
open_hover = image.load("file_hover.png")
open_hover = transform.scale(open_hover,(40,50))

new_b = Rect(1090,240,50,70)
new_pic = image.load("new.png")
new_pic = transform.scale(new_pic,(55,55))
new_hover = image.load("new_hover.png")
new_hover = transform.scale(new_hover,(55,55))

save_b = Rect(1100,320,50,70)
save_pic = image.load("save.png")
save_pic = transform.scale(save_pic,(40,40))
save_hover = image.load("save_hover.png")
save_hover = transform.scale(save_hover,(40,40))

help_b = Rect(1090,390,50,70)
help_pic = image.load("help.png")
help_pic = transform.scale(help_pic,(55,55))
help_hover = image.load("help_hover.png")
help_hover = transform.scale(help_hover,(55,55))
help_paintPic = image.load("help_paintPic.png")

#============================ON BOTTOM================================
#STICKERS
moth_b = Rect(390,580,50,70)
moth_pic = image.load("moth.png")
moth_pic = transform.scale(moth_pic,(55,50))
moth_hover = image.load("moth_hover.png")
moth_hover = transform.scale(moth_hover,(55,50))

bear_b = Rect(390,650,50,70)
bear_pic = image.load("bear.png")
bear_pic = transform.scale(bear_pic,(55,50))
bear_hover = image.load("bear_hover.png")
bear_hover = transform.scale(bear_hover,(55,50))

heisen_b = Rect(440,580,50,70)
heisen_pic = image.load("heisenberg.png")
heisen_pic = transform.scale(heisen_pic,(55,65))
heisen_hover = image.load("heisenberg_hover.png")
heisen_hover = transform.scale(heisen_hover,(55,65))

rv_b = Rect(440,650,50,70)
rv_pic = image.load("rv.png")
rv_pic = transform.scale(rv_pic,(50,50))
rv_hover = image.load("rv_hover.png")
rv_hover = transform.scale(rv_hover,(50,50))

pollos_b = Rect(500,580,50,70)
pollos_pic = image.load("pollos.png")
pollos_pic = transform.scale(pollos_pic,(55,60))
pollos_hover = image.load("pollos_hover.png")
pollos_hover = transform.scale(pollos_hover,(55,60))

a1_b = Rect(500,660,50,70)
a1_pic = image.load("a1.png")
a1_pic = transform.scale(a1_pic,(55,55))
a1_hover = image.load("a1_hover.png")
a1_hover = transform.scale(a1_hover,(55,55))

saul_b = Rect(560,580,50,70)
saul_pic = image.load("callSaul.png")
saul_pic = transform.scale(saul_pic,(55,50))
saul_hover = image.load("callSaul_hover.png")
saul_hover = transform.scale(saul_hover,(55,50))

cook_b = Rect(560,650,50,70)
cook_pic = image.load("wecancook.png")
cook_pic = transform.scale(cook_pic,(55,55))
cook_hover = image.load("wecancook_hover.png")
cook_hover = transform.scale(cook_hover,(55,55))

#FILTERS
norm_pic = image.load('filter.png')
norm_pic = transform.scale(norm_pic,(40,55))

grayscale_b = Rect(630,590,50,70)
grayscale_pic = image.load("filter_grayscale.png")
grayscale_pic = transform.scale(grayscale_pic,(40,55))

neg_b = Rect(630,660,50,70)
neg_pic = image.load("filter_negative.png")
neg_pic = transform.scale(neg_pic,(40,55))

sepia_b = Rect(700,590,50,70)
sepia_pic = image.load("filter_sepia.png")
sepia_pic = transform.scale(sepia_pic,(40,55))

red_b = Rect(700,660,50,70)
red_pic = image.load("filter_red.png")
red_pic = transform.scale(red_pic,(40,55))

green_b = Rect(770,590,50,70)
green_pic = image.load("filter_green.png")
green_pic = transform.scale(green_pic,(40,55))

blue_b = Rect(770,660,50,70)
blue_pic = image.load("filter_blue.png")
blue_pic = transform.scale(blue_pic,(40,55))

#SPECIAL TOOLS
marker_b = Rect(830,590,50,70)
marker_pic = image.load("particles.png")
marker_pic = transform.scale(marker_pic,(40,55))
marker_hover = image.load("particles_hover.png")
marker_hover = transform.scale(marker_hover,(40,55))

random_b = Rect(830,660,50,70)
random_pic = image.load("randomLines.png")
random_pic = transform.scale(random_pic,(40,55))
random_hover = image.load("randomLines_hover.png")
random_hover = transform.scale(random_hover,(40,55))

#CANVASES (6 in total)
canvas_bList = [Rect(875,580,50,70),Rect(940,580,50,70),Rect(1000,580,50,70),
              Rect(875,650,50,70),Rect(940,650,50,70),Rect(1000,650,50,70)]
cvs = [screen.subsurface(canvas_rect).copy() for i in range(6)]
numCvs = ["1","2","3","4","5","6"]
currentCvs = 0  #set index
 
#===============================FUNCTIONS==================================
def brush(screen,col,pos,brush_size):
    distance = hypot(pos[0]-oldx,pos[1]-oldy)
    distance = max(distance,1)
    x = int(oldx)
    y = int(oldy)
    ix = (pos[0]-oldx)/distance
    iy = (pos[1]-oldy)/distance
    for i in range(int(distance)):
        draw.circle(screen,col,(int(x),int(y)),brush_size)
        x += ix
        y += iy
    draw.circle(screen,col,(mx,my),brush_size)
    
def marker(screen,col,pos,brush_size):
    markerHead = Surface((80,80),SRCALPHA)
    draw.circle(markerHead,(col[0],col[1],col[2],40),(40,40),brush_size)
    screen.blit(markerHead,(mx-40,my-40))

def fill(x,y,oldcol,newcol):
    if oldcol != newcol:
        points = [(x,y)]
        oldc = screen.get_at((x,y))
        while len(points) > 0:
          nx,ny = points.pop(0)
          if screen.get_at((nx,ny)) == oldc:
            screen.set_at((nx,ny),newcol)
            points += [(nx+1,ny),(nx-1,ny),(nx,ny+1),(nx,ny-1)]

def grayscale(canvas):
    for xp in range(canvas_length):
        for yp in range(canvas_height):
            currentCol = canvas.get_at((xp,yp))
            grayCol = (currentCol[0]+currentCol[1]+currentCol[2])//3
            canvas.set_at((xp,yp),(grayCol,grayCol,grayCol))
        
def negative(canvas):
    for xp in range(canvas_length):
        for yp in range(canvas_height):
            currentCol = canvas.get_at((xp,yp))
            negRed = max(1,255 - currentCol[0])
            negGreen = max(1,255 - currentCol[1])
            negBlue = max(1,255 - currentCol[2])
            canvas.set_at((xp,yp),(negRed,negGreen,negBlue))

def sepia(canvas):
    for xp in range(canvas_length):
        for yp in range(canvas_height):
            currentCol = canvas.get_at((xp,yp))
            red = currentCol[0]
            green = currentCol[1]
            blue = currentCol[2]
            outputRed = min(255,int((red * .393) + (green *.769) + (blue * .189)))
            outputGreen = min(255,int((red * .349) + (green *.686) + (blue * .168)))
            outputBlue = min(255,int((red * .272) + (green *.534) + (blue * .131)))
            canvas.set_at((xp,yp), (outputRed,outputGreen,outputBlue))

def red(canvas):
    for xp in range(canvas_length):
        for yp in range(495):
            currentCol = canvas.get_at((xp,yp))
            avg = min(255,((currentCol[0] + currentCol[1] + currentCol[2])//3))
            canvas.set_at((xp,yp), (avg,0,0))

def green(canvas):
    for xp in range(canvas_length):
        for yp in range(canvas_height):
            currentCol = canvas.get_at((xp,yp))
            avg = min(255,((currentCol[0] + currentCol[1] + currentCol[2])//3))
            canvas.set_at((xp,yp), (0,avg,0))

def blue(canvas):
    for xp in range(canvas_length):
        for yp in range(canvas_height):
            currentCol = canvas.get_at((xp,yp))
            avg = min(255,((currentCol[0] + currentCol[1] + currentCol[2])//3))
            canvas.set_at((xp,yp), (0,0,avg))

#===================================DESCRIPTIONS===================================
font.init()
times = font.SysFont("Times New Roman", 18)
timesBIG = font.SysFont("Times New Roman", 24)
descr = ["Pencil: Draw with pencil. Key right/left for size.",
         "Hydrofluoric acid: Lets you erase mistakes. Key up/down for size.",
         "Brush: Draw with brush. Key up/down for size.",
         "Spray: Draw with tiny dots. Key up/down for size.",
         "Beaker: Fills closed areas with chemical colour of choice.",
         "Text: Start typing and click to desired place.",
         "Eyedropper: Click to retrieve chemical composition of colour.",
         "Line: Draw line by clicking and dragging. Key right/left for size.",
         "Rectangle: Self-explanatory. Key right/left for size.",
         "Ellipse: Same as rectangle. Key right/left for size.",
         "Filled Rectangle: Refer to Rectangle, but filled.",
         "Filled Ellipse: Refer to Ellipse, but filled.",
         "Chemical Bonder: Draw polygons. Right click to connect.",
         "Sticker: Click and drag to desired place.",
         "Filter: Click on canvas to apply.",
         "Particles: Draws translucent atoms.",
         "Random Lines: Does as title suggests."]

#===================================PRESET THINGS=======================================
col = (0,0,0)
showcol = (0,0,0)
eraserCol = (255,255,255)

txtPic = times.render(descr[0], True, (255,255,255))
draw.rect(screen,(0,85,80),(300,10,600,40))
screen.blit(txtPic,(400,20))

root = Tk() 
root.withdraw()

size = 2
brush_size = 6 #also eraser size
spray_size = 20
stickerSize = 100
currentSize = size

word = ""   #text tool
tool = "pencil"
click = False
running = True
helpRunning = False
drawing = False

start = 0,0
mx,my = 0,0

copy = screen.copy()
past = [[screen.subsurface(canvas_rect).copy()] for i in range(6)]
future = [[] for i in range(6)]
list_poly = []      #for polygon
points = []         #for fill

#====================================LOOP STARTS=====================================
while running:
    
    oldx,oldy = mx,my
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    click = False
    button_up = False
    closed = False
    colAtPos = screen.get_at((mx,my)) #for fill

    for e in event.get():
        mb = mouse.get_pressed()

        if e.type  ==  QUIT:
            running = False

        if e.type  ==  MOUSEBUTTONDOWN:
            click = True
            if e.button  ==  1:
                start = e.pos
            if canvas_rect.collidepoint((mx,my)):
                drawing = True
                
        if e.type  ==  MOUSEBUTTONUP:
            button_up = True
            if not helpRunning:
                copy = screen.copy()
            if drawing or canvas_rect.collidepoint((mx,my)):
                #different canvases different undo/redo
                past[currentCvs].append(screen.subsurface(canvas_rect).copy())
            if tool == "text" and canvas_rect.collidepoint((mx,my)):
                screen.set_clip(canvas_rect)
                enterText = times.render(word, True, col)
                screen.blit(enterText, (mx, my))
                word = ""
            drawing = False
            
        if e.type  ==  KEYDOWN:
            if tool == "text":
                if e.key  ==  K_BACKSPACE and word != "":
                    word = word[:-1]
                else:
                    word += e.unicode
            if e.key == K_RIGHT and size<=6:  #size for everything else
                size += 1
            if e.key == K_LEFT and size>=2:
                size -= 1
            if e.key == K_UP :
                if tool == "brush" and brush_size<=40:
                    brush_size += 2
                if tool == "eraser" and brush_size<=40:
                    brush_size += 2
                elif tool == "spray" and spray_size<=40:
                    spray_size += 5
            if e.key == K_DOWN :
                if tool == "brush" and brush_size>5:
                    brush_size -= 2
                if tool == "eraser" and brush_size>5:
                    brush_size -= 2
                elif tool == "spray" and spray_size>10:
                    spray_size -= 5

    #Canvas numbers
    for i in range(len(canvas_bList)):
        if i==currentCvs:
            cvsTxt = times.render(numCvs[i], True, (255,255,255))
            screen.blit(cvsTxt,(canvas_bList[i][0]+30,canvas_bList[i][1]+30))
        else:
            cvsTxt = times.render(numCvs[i], True, (50,50,50))
            cvsTxt2 = times.render(numCvs[i], True, (100,100,100))
            if canvas_bList[i].collidepoint((mx,my)):
                screen.blit(cvsTxt2,(canvas_bList[i][0]+30,canvas_bList[i][1]+30))
            screen.blit(cvsTxt,(canvas_bList[i][0]+30,canvas_bList[i][1]+30))

    if not helpRunning:     #doesn't show when user selects help screen

        #SHOWS SELECTED TOOL AND COLOUR
        draw.rect(screen,(255,255,255),(25,620,90,90))  #covers up
        draw.circle(screen,col,(70,670),currentSize)
        draw.rect(screen,showcol,colour_rect,2)

        #ICONS
        screen.blit(pen_pic,(15,20))
        screen.blit(eraser_pic,(10,110))
        screen.blit(brush_pic,(20,180))
        screen.blit(spray_pic,(20,255))
        screen.blit(fill_pic,(15,325))
        screen.blit(text_pic,(15,400))
        screen.blit(dropper_pic,(20,470))
        screen.blit(poly_pic,(85,470))

        draw.line(screen,(0,0,0),(80,120),(110,160),2)
        draw.rect(screen,(0,0,0),(85,190,35,45),2)
        draw.ellipse(screen,(0,0,0),(80,265,50,40),2)
        draw.rect(screen,(0,0,0),(85,335,35,45))
        draw.ellipse(screen,(0,0,0),(80,400,50,40))

        screen.blit(undo_pic,(1100,40))
        screen.blit(redo_pic,(1100,115))
        screen.blit(open_pic,(1100,170))
        screen.blit(new_pic,(1090,245))
        screen.blit(save_pic,(1100,325))
        screen.blit(help_pic,(1090,390))

        screen.blit(moth_pic,(390,590))
        screen.blit(bear_pic,(390,660))
        screen.blit(heisen_pic,(455,580))
        screen.blit(rv_pic,(455,670))
        screen.blit(pollos_pic,(510,580))
        screen.blit(a1_pic,(510,660))
        screen.blit(saul_pic,(570,585))
        screen.blit(cook_pic,(570,660))

        screen.blit(grayscale_pic,(640,590))
        screen.blit(neg_pic,(640,660))
        screen.blit(sepia_pic,(700,590))
        screen.blit(red_pic,(700,660))
        screen.blit(green_pic,(770,590))
        screen.blit(blue_pic,(770,660))

        screen.blit(marker_pic,(830,590))
        screen.blit(random_pic,(830,665))

        #HOVERING ICONS <==== blit only when collidepoint((mx,my))
        if pen_b.collidepoint((mx,my)):
            screen.blit(pen_hover,(15,20))
        if erase_b.collidepoint((mx,my)):
            screen.blit(eraser_hover,(10,110))
        if brush_b.collidepoint((mx,my)):
            screen.blit(brush_hover,(20,180))
        if spray_b.collidepoint((mx,my)):
            screen.blit(spray_hover,(20,255))
        if fill_b.collidepoint((mx,my)):
            screen.blit(fill_hover,(15,325))
        if text_b.collidepoint((mx,my)):
            screen.blit(text_hover,(15,400))
        if dropper_b.collidepoint((mx,my)):
            screen.blit(dropper_hover,(20,470))
            
        if line_b.collidepoint((mx,my)):
            draw.line(screen,(50,50,50),(80,120),(110,160),2)
        if rectangle_b.collidepoint((mx,my)):
            draw.rect(screen,(50,50,50),(85,190,35,45),2)
        if ellipse_b.collidepoint((mx,my)):
            draw.ellipse(screen,(50,50,50),(80,265,50,40),2)
        if fillRect_b.collidepoint((mx,my)):
            draw.rect(screen,(50,50,50),(85,335,35,45))
        if fillElip_b.collidepoint((mx,my)):
            draw.ellipse(screen,(50,50,50),(80,400,50,40))
        if poly_b.collidepoint((mx,my)):
            screen.blit(poly_hover,(85,470))

        if undo_b.collidepoint((mx,my)):
            screen.blit(undo_hover,(1100,40))
        if redo_b.collidepoint((mx,my)):
            screen.blit(redo_hover,(1100,115))
        if open_b.collidepoint((mx,my)):
            screen.blit(open_hover,(1100,170))
        if new_b.collidepoint((mx,my)):
            screen.blit(new_hover,(1090,245))
        if save_b.collidepoint((mx,my)):
            screen.blit(save_hover,(1100,325))
        if help_b.collidepoint((mx,my)):
            screen.blit(help_hover,(1090,390))

        if moth_b.collidepoint((mx,my)):
            screen.blit(moth_hover,(390,590))
        if bear_b.collidepoint((mx,my)):
            screen.blit(bear_hover,(390,660))
        if heisen_b.collidepoint((mx,my)):
            screen.blit(heisen_hover,(455,580))
        if rv_b.collidepoint((mx,my)):
            screen.blit(rv_hover,(455,670))
        if pollos_b.collidepoint((mx,my)):
            screen.blit(pollos_hover,(510,580))
        if a1_b.collidepoint((mx,my)):
            screen.blit(a1_hover,(510,660))
        if saul_b.collidepoint((mx,my)):
            screen.blit(saul_hover,(570,585))
        if cook_b.collidepoint((mx,my)):
            screen.blit(cook_hover,(570,660))

        if grayscale_b.collidepoint((mx,my)):
            screen.blit(norm_pic,(640,590))    
        if neg_b.collidepoint((mx,my)):
            screen.blit(norm_pic,(640,660))
        if sepia_b.collidepoint((mx,my)):
            screen.blit(norm_pic,(700,590))
        if red_b.collidepoint((mx,my)):
            screen.blit(norm_pic,(700,660))
        if green_b.collidepoint((mx,my)):
            screen.blit(norm_pic,(770,590))
        if blue_b.collidepoint((mx,my)):
            screen.blit(norm_pic,(770,660))
        
        if marker_b.collidepoint((mx,my)):
            screen.blit(marker_hover,(830,590))
        if random_b.collidepoint((mx,my)):
            screen.blit(random_hover,(830,665))
        if colour_rect.collidepoint((mx,my)):   #updates colour immediately
            showcol = screen.get_at((mx,my))
        
    if click:
        #SELECT CANVASES
        for i in range(len(canvas_bList)):
            if canvas_bList[i].collidepoint(mx,my):
                cvs[currentCvs] = screen.subsurface(canvas_rect).copy()
                screen.set_clip(canvas_rect)
                screen.blit(cvs[i],(145,60))
                currentCvs = i
                break
        #SELECT COLOUR
        if colour_rect.collidepoint((mx,my)):
            col = screen.get_at((mx,my))
        #SELECT TOOLS
        if pen_b.collidepoint((mx,my)):
            tool = "pencil"
            currentSize = size
            txtPic = times.render(descr[0], True, (255,255,255))
        if erase_b.collidepoint((mx,my)):
            tool = "eraser"
            currentSize = brush_size
            txtPic = times.render(descr[1], True, (255,255,255))
        if brush_b.collidepoint((mx,my)):
            tool = "brush"
            currentSize = brush_size
            txtPic = times.render(descr[2], True, (255,255,255))
        if spray_b.collidepoint((mx,my)):
            tool = "spray"
            currentSize = spray_size
            txtPic = times.render(descr[3], True, (255,255,255))
        if fill_b.collidepoint((mx,my)):
            tool = "fill"
            txtPic = times.render(descr[4], True, (255,255,255))
        if text_b.collidepoint((mx,my)):
            tool = "text"
            txtPic = times.render(descr[5], True, (255,255,255))
        if dropper_b.collidepoint((mx,my)):
            tool = "dropper"
            txtPic = times.render(descr[6], True, (255,255,255))
        if line_b.collidepoint((mx,my)):
            tool = "line"
            txtPic = times.render(descr[7], True, (255,255,255))
        if rectangle_b.collidepoint((mx,my)):
            tool = "rectangle"
            currentSize = size
            txtPic = times.render(descr[8], True, (255,255,255))
        if ellipse_b.collidepoint((mx,my)):
            tool = "ellipse"
            currentSize = size
            txtPic = times.render(descr[9], True, (255,255,255))
        if fillRect_b.collidepoint((mx,my)):
            tool = "fillRect"
            txtPic = times.render(descr[10], True, (255,255,255))
        if fillElip_b.collidepoint((mx,my)):
            tool = "fillElip"
            txtPic = times.render(descr[11], True, (255,255,255))
        if poly_b.collidepoint((mx,my)):
            tool = "poly"
            currentSize = size
            txtPic = times.render(descr[12], True, (255,255,255))
        #SELECT STICKERS
        if moth_b.collidepoint((mx,my)):
            tool = "moth"
            txtPic = times.render(descr[13], True, (255,255,255))
        if bear_b.collidepoint((mx,my)):
            tool = "bear"
            txtPic = times.render(descr[13], True, (255,255,255))
        if heisen_b.collidepoint((mx,my)):
            tool = "heisen"
            txtPic = times.render(descr[13], True, (255,255,255))
        if rv_b.collidepoint((mx,my)):
            tool = "rv"
            txtPic = times.render(descr[13], True, (255,255,255))
        if pollos_b.collidepoint((mx,my)):
            tool = "pollos"
            txtPic = times.render(descr[13], True, (255,255,255))
        if a1_b.collidepoint((mx,my)):
            tool = "a1"
            txtPic = times.render(descr[13], True, (255,255,255))
        if saul_b.collidepoint((mx,my)):
            tool = "saul"
            txtPic = times.render(descr[13], True, (255,255,255))
        if cook_b.collidepoint((mx,my)):
            tool = "cook"
            txtPic = times.render(descr[13], True, (255,255,255))
        #SELECT FILTERS
        if grayscale_b.collidepoint((mx,my)):
            tool = "grayscale"
            txtPic = times.render(descr[14], True, (255,255,255))
        if neg_b.collidepoint((mx,my)):
            tool = "negative"
            txtPic = times.render(descr[14], True, (255,255,255))
        if sepia_b.collidepoint((mx,my)):
            tool = "sepia"
            txtPic = times.render(descr[14], True, (255,255,255))
        if red_b.collidepoint((mx,my)):
            tool = "red"
            txtPic = times.render(descr[14], True, (255,255,255))
        if green_b.collidepoint((mx,my)):
            tool = "green"
            txtPic = times.render(descr[14], True, (255,255,255))
        if blue_b.collidepoint((mx,my)):
            tool = "blue"
            txtPic = times.render(descr[14], True, (255,255,255))
        if marker_b.collidepoint((mx,my)):
            tool = "marker"
            txtPic = times.render(descr[15], True, (255,255,255))
        if random_b.collidepoint((mx,my)):
            tool = "randomlines"
            txtPic = times.render(descr[16], True, (255,255,255))
        #show user tool selected + brief description
        draw.rect(screen,(0,85,80),(300,10,600,35))
        screen.blit(txtPic,(400,20))
        
        if undo_b.collidepoint((mx,my)) and len(past[currentCvs])>=2:
            future[currentCvs].append(past[currentCvs][-1])
            del past[currentCvs][-1]
            screen.blit(past[currentCvs][-1],(145,60))
            if len(list_poly)>1:
                del list_poly[-1]
        if redo_b.collidepoint((mx,my)) and len(future[currentCvs])>=1:
            screen.blit(future[currentCvs][-1],(145,60))
            past[currentCvs].append(future[currentCvs][-1])
            del future[currentCvs][-1]
        if new_b.collidepoint((mx,my)):
            screen.set_clip(canvas_rect)
            screen.fill((255,255,255))
            past[currentCvs].append(screen.subsurface(canvas_rect).copy())
            list_poly=[]
        if help_b.collidepoint((mx,my)):
            helpRunning = True

    #HELP?!?           
    if helpRunning:
        infoTxt = times.render("Paint project by Annie Zhang.2014.", True, (255,255,255))
        infoTxt1 = times.render("Based off of AMC's Breaking Bad.", True, (255,255,255))
        infoTxt2 = times.render("Vince Gilligan is the one who knocks.", True, (255,255,255))
        infoTxt3 = times.render("savewalterwhite.com",True,(255,255,255))
        draw.rect(screen,(0,0,0),(0,0,1200,800))        #cover up paint in back
        screen.blit(help_paintPic,(0,0))
        screen.blit(infoTxt,(900,100))
        screen.blit(infoTxt1,(900,150))
        screen.blit(infoTxt2,(900,200))
        screen.blit(infoTxt3,(900,250))
        exitBox = Rect(1100,0,100,50)
        draw.rect(screen,(255,0,0),exitBox)
        draw.line(screen,(0,0,0),(1100,0),(1200,50))
        draw.line(screen,(0,0,0),(1100,50),(1200,0))
        if exitBox.collidepoint((mx,my)) and mb[0] == 1:    #to exit
            helpRunning = False
            screen.blit(copy,(0,0))
    
    #OPEN//SAVE
    if button_up:   #opens window in front of paint window
        if open_b.collidepoint((mx,my)):
            fileName = askopenfilename(parent=root,title="Open Image:")
            if fileName:
                pic = image.load("%s"%(fileName))
                pic = transform.scale(pic,(975,495))    #fit to canvas
                screen.blit(pic,(145,70))
                copy=screen.copy()
        if save_b.collidepoint((mx,my)):
            fileName = asksaveasfilename(parent=root,title="Save the image as...")
            if fileName: #if user enters name, else don't save
                image.save(screen.subsurface(canvas_rect),("%s.png"%fileName))

    #tools that need to show user size/colour
    if tool == "pencil":
        currentSize = size
        #collidepoint((oldx,oldy)) <==== pencil will still draw if user frantically goes about
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)) or mb[0] == 1 and canvas_rect.collidepoint((oldx,oldy)):
            screen.set_clip(canvas_rect)
            draw.line(screen,col,(oldx,oldy),(mx,my),size)
    if tool == "eraser":
        currentSize = brush_size
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)):
            screen.set_clip(canvas_rect)
            brush(screen,eraserCol,(mx,my),brush_size)
    if tool == "brush":
        currentSize = brush_size
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)):
            screen.set_clip(canvas_rect)
            brush(screen,col,(mx,my),brush_size)
    if tool == "spray":
        currentSize = spray_size
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)):
            screen.set_clip(canvas_rect)
            for i in range(10):
                randx=randint(-spray_size,spray_size)
                randy=randint(-int(sqrt(spray_size**2-randx**2)),int(sqrt(spray_size**2-randx**2)))
                draw.line(screen,col,(mx+randx,my+randy),(mx+randx,my+randy),size)
    if tool == "line":
        currentSize = size
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)) and not helpRunning:
            screen.set_clip(canvas_rect)
            screen.blit(copy,(0,0))
            draw.line(screen,col,start,(mx,my),size)  
    if tool == "rectangle":
        currentSize = size
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)) and not helpRunning:
            screen.set_clip(canvas_rect)
            screen.blit(copy,(0,0))
            rectangle=Rect(start[0],start[1],mx-start[0],my-start[1])
            draw.rect(screen,col,rectangle,size)
    if tool == "ellipse":
        currentSize = size
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)) and not helpRunning:
            screen.set_clip(canvas_rect)
            screen.blit(copy,(0,0))
            rectangle=Rect(start[0],start[1],mx-start[0],my-start[1])
            rectangle.normalize()
            if rectangle.width < size*2 or rectangle.height < size*2:
                draw.ellipse(screen,col,rectangle,0)
            else:
                draw.ellipse(screen,col,rectangle,size)
    #POLYGON
    if tool == "poly":  #different mb functions for POLYGON
        currentSize = size
        if click and canvas_rect.collidepoint((mx,my)) and not helpRunning: 
            screen.set_clip(canvas_rect)
            if mb[0] == 1:
                list_poly.append(start)
            if mb[2] == 1:
                closed=True
            if len(list_poly)>1:
                draw.lines(screen,col,closed,list_poly,size)
                if closed:
                    list_poly=[]
    #SPECIAL TOOLS
    if tool == "marker":
        currentSize = brush_size
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)):
            screen.set_clip(canvas_rect)
            if mx!=oldx or my!=oldy:
                brushHead = Surface((brush_size,brush_size),SRCALPHA)
                marker(screen,col,(mx,my),brush_size)
    if tool == "randomlines":
        currentSize = 30
        if mb[0] == 1 and canvas_rect.collidepoint((mx,my)):
            screen.set_clip(canvas_rect)
            rx = randint(mx-30,mx+30)
            ry = randint(my-30,my+30)
            rcol = (randint(0,255),randint(0,255),randint(0,255))
            draw.line(screen,rcol,(mx,my),(rx,ry),1)
    #TEXT
    if tool != "text":
        word = ""       #don't blit anything
    if tool == "text" and canvas_rect.collidepoint((mx,my)) and not helpRunning:  #needs to be outside click loop
        screen.set_clip(canvas_rect)
        screen.blit(copy,(0,0))
        enterText =  times.render(word,True,col)
        screen.blit(enterText,(mx, my))

    if mb[0] == 1 and canvas_rect.collidepoint((mx,my)):    #all for left click
        screen.set_clip(canvas_rect)                        #DON'T need to show size AND col
        if tool == "fill":
            fill(mx,my,colAtPos,col)
        if tool == "dropper":
            col = screen.get_at((e.pos))
        if tool == "fillRect" and not helpRunning: 
            screen.blit(copy,(0,0))
            rectangle=Rect(start[0],start[1],mx-start[0],my-start[1])
            draw.rect(screen,col,rectangle)
        if tool == "fillElip" and not helpRunning:
            screen.blit(copy,(0,0))
            rectangle=Rect(start[0],start[1],mx-start[0],my-start[1])
            rectangle.normalize()
            draw.ellipse(screen,col,rectangle)
        
        #STICKERS
        if tool == "moth":
            screen.blit(copy,(0,0))
            moth_stick = image.load("moth.png")
            moth_stick = transform.scale(moth_stick,(stickerSize,stickerSize))
            screen.blit(moth_stick,(mx-stickerSize//2,my-stickerSize//2))
        if tool == "bear":
            screen.blit(copy,(0,0))
            bear_stick = image.load("bear.png")
            bear_stick = transform.scale(bear_stick,(stickerSize,stickerSize))
            screen.blit(bear_stick,(mx-stickerSize//2,my-stickerSize//2))
        if tool == "heisen":
            screen.blit(copy,(0,0))
            heisen_stick = image.load("heisenberg.png")
            heisen_stick = transform.scale(heisen_stick,(stickerSize,stickerSize))
            screen.blit(heisen_stick,(mx-stickerSize//2,my-stickerSize//2))
        if tool == "rv":
            screen.blit(copy,(0,0))
            rv_stick = image.load("rv.png")
            rv_stick = transform.scale(rv_stick,(stickerSize,stickerSize))
            screen.blit(rv_stick,(mx-stickerSize//2,my-stickerSize//2))
        if tool == "pollos":
            screen.blit(copy,(0,0))
            pollos_stick = image.load("pollos.png")
            pollos_stick = transform.scale(pollos_stick,(stickerSize,stickerSize))
            screen.blit(pollos_stick,(mx-stickerSize//2,my-stickerSize//2))
        if tool == "a1":
            screen.blit(copy,(0,0))
            a1_stick = image.load("a1.png")
            a1_stick = transform.scale(a1_stick,(stickerSize,stickerSize))
            screen.blit(a1_stick,(mx-stickerSize//2,my-stickerSize//2))
        if tool == "saul":
            screen.blit(copy,(0,0))
            saul_stick = image.load("callSaul.png")
            saul_stick = transform.scale(saul_stick,(stickerSize,stickerSize))
            screen.blit(saul_stick,(mx-stickerSize//2,my-stickerSize//2))
        if tool == "cook":
            screen.blit(copy,(0,0))
            cook_stick = image.load("wecancook.png")
            cook_stick = transform.scale(cook_stick,(stickerSize,stickerSize))
            screen.blit(cook_stick,(mx-stickerSize//2,my-stickerSize//2))

        #FILTERS
        if tool == "grayscale":
            grayscale(screen.subsurface(canvas_rect))
        if tool == "negative":
            negative(screen.subsurface(canvas_rect))
        if tool == "sepia":
            sepia(screen.subsurface(canvas_rect))
        if tool == "red":
            red(screen.subsurface(canvas_rect))
        if tool == "green":
            green(screen.subsurface(canvas_rect))
        if tool == "blue":
            blue(screen.subsurface(canvas_rect))

    screen.set_clip(None)
    display.flip()
quit()
