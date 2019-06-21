'''This code creates a grid on the image of 10 lines, it is able to draw a
ruler on the image in order to determine the positions   

Use: open the created file (croppimm) file with Windows Photo viewer

-circle drawing with size bar and notation 
-image crop
-image save

 
'''
from header import *
from PIL import Image, ImageDraw, ImageFont, ImageColor # image command from Pillow library


#import plot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import cm
import numpy as np


percorso='C:/M_drive_docs/Lab/SEM/180712_befaftMnCu_NiCr2_MT2/'
percorso='D:/M_drive_docs/Lab/SEM/Merlin/180504/'
percorso='D:/M_drive_docs/Lab/SEM/TEM3000/180221_NiCr2mill_Ti_SS_felts/'
immagine,image_label='Ti_FELT_cs0000(x250).png',' '
imm=Image.open(percorso+immagine)
imm=imm.convert("RGBA")
size = ImageDraw.Draw(imm)   ####image object 
ximm=imm.size[0] ##size of the image
yimm=imm.size[1] ##
white,black,blue,red,yellow,grey=(255,255,255),(0,0,0),(40,125,244),(224,41,20),(246,242,39),(150,150,150)

###grid
grid=False
if grid:
    rng=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.99999]
    for i in rng:
        ximm=ximm
        yimm=yimm
        size.line([ximm*i,yimm*0,ximm*i,yimm*1], fill=100, width=0)###Horiz lines
        size.line([ximm*0,yimm*i,ximm*1,yimm*i], fill=100, width=1)###Vert lines
        font = ImageFont.truetype("arial.ttf", int(ximm*0.02))  ### font type and font size relative to figure size
        size.text((ximm*0.05, yimm*i-yimm*0.03),str(i) ,font=font, fill=1000) ### x position
        size.text((ximm*0.95, yimm*i-yimm*0.03),str(i) ,font=font, fill=1000) ### x position
        size.text((ximm*i-ximm*0.03, yimm*0.05),str(i) ,font=font, fill=1000) ### y position
        size.text((ximm*i-ximm*0.03, yimm*0.95),str(i) ,font=font, fill=1000) ### y position



    
    
    
###ruler
'''Draws a ruler between x/y_st and x/y_en with 10 thicks in between'''

rulx_st=0.5
rulx_en=0.5
ruly_st=0.7
ruly_en=0.7
if  rulx_st!=rulx_en or ruly_st!=ruly_en:
    rule=np.arange(0,11,1)
    clr=1000 ####color for ruler, 1 is black more than 500 is white
    deltaX=rulx_en-rulx_st
    deltaY=ruly_en-ruly_st
    if deltaX>0:
        size.line([ximm*rulx_st,yimm*ruly_st,ximm*rulx_en,yimm*ruly_en], fill=clr, width=1)### draw horizontal line
        for e in rule: #draw a len(rule) number of thicks
            size.line([ximm*rulx_st+ximm*(deltaX/(len(rule)-1))*e,yimm*ruly_st-yimm*0.01*ruly_st,
                       ximm*rulx_st+ximm*(deltaX/(len(rule)-1))*e,yimm*ruly_en+yimm*0.01*ruly_en], fill=255, width=1)
    if deltaY>0:
        size.line([ximm*rulx_st,yimm*ruly_st,ximm*rulx_en,yimm*ruly_en], fill=300, width=1)### draw vertical line
        for e in rule: #draw a len(rule) number of thicks
            size.line([ximm*rulx_st-ximm*0.01*rulx_st,yimm*ruly_st+yimm*(deltaY/(len(rule)-1))*e,
                       ximm*rulx_en+ximm*0.01*rulx_en,yimm*ruly_st+yimm*(deltaY/(len(rule)-1))*e], fill=300, width=1)
            

            


   
   
    
    

####circle
x_cir=0.515 #### x coordinate of the center of the circle
y_cir=0.69 #### y coordinate of the center of the circle
diam=0### diameter of the circle
meas='1 µm'###text to display below the bar
if diam!=0:
    r=ximm/yimm ###ratio between x and y dimension of the image
    size.ellipse([ximm*(x_cir-diam/2),yimm*(y_cir-diam*r/2),ximm*(x_cir+diam/2),yimm*(y_cir+diam*r/2)], fill=None, outline=900)
    ##increase the thickness by mult circles    #size.ellipse([ximm*(x_cir*1.01-diam/2),yimm*(y_cir*1.01-diam*r/2),ximm*(x_cir*1.01+diam/2),yimm*(y_cir*1.01+diam*r/2)], fill=None, outline=900)
    ### maesuring bar
    size.line([ximm*(x_cir-diam/2),yimm*(y_cir+diam*0.75*r),ximm*(x_cir+diam/2),yimm*(y_cir+diam*0.75*r)], fill=300, width=2)
    size.line([ximm*(x_cir-diam/2),yimm*(y_cir+(diam*0.75*r-0.005)),ximm*(x_cir-diam/2),yimm*(y_cir+(diam*0.75*r+0.005))], fill=300, width=2) 
    size.line([ximm*(x_cir+diam/2),yimm*(y_cir+(diam*0.75*r-0.005)),ximm*(x_cir+diam/2),yimm*(y_cir+(diam*0.75*r+0.005))], fill=300, width=2) 
    font = ImageFont.truetype("arial.ttf", int(ximm*0.03))  ### font type and font size
    size.text((ximm*(x_cir-diam/6), yimm*(y_cir+diam)),meas ,font=font, fill=300) ###position

###Cropping
cropped=ximm*0.0, yimm*0.07, ximm*1, yimm*0.87
Xfinale,Yfinale=int(cropped[2]-cropped[0]),int(cropped[3]-cropped[1])
print('Final image size (px):',Xfinale,' x ',Yfinale)

print(0.17799/5)
#####scale bar
x1,x2,y=0.8,0.910,0.8 #edited position, bot rx
x1,x2,y=0.006,0.059,0.95 #scale bar measuring position, bot lx, MERLIN

x1,x2,y=0.75,0.9,0.999
size.line([Xfinale*x1,Yfinale*y,Xfinale*x2,Yfinale*y], 
          fill=white, width=int(Xfinale*0.0162)) 
print('dimensions of scale bar ( original image H size):',((x2-x1)*Xfinale)/ximm)# 0.071 = 10 um
font = ImageFont.truetype("arial.ttf", int(Xfinale*0.076))  ### font type and font size
shiftx,shifty=-0.073,-0.085
size.text((Xfinale*(x1-0.0+shiftx), Yfinale*(y-0.07+shifty)),'100 µm' ,font=font, fill=white) ###position µm
     
### figure labeling
font = ImageFont.truetype("arial.ttf", int(Xfinale*0.081))    ### font type and font size
size.text((cropped[0], cropped[1]),image_label ,font=font, fill=white) ###position

### figure labeling
#font = ImageFont.truetype("arial.ttf", int(Xfinale*0.05))    ### font type and font size
#size.text((ximm*0.55, yimm*0.7),'Pt ring' ,font=font, fill=black) ###position

#font = ImageFont.truetype("arial.ttf", int(Xfinale*0.05))    ### font type and font size
#size.text((ximm*0.2, yimm*0.1),'Casted ink on\nGC disk' ,font=font, fill=white) ###position

croppimm=imm.crop((cropped))
croppimm.save('D:/M_drive_docs/Lab/SEM/TITANATES/'+immagine)
del size



display(croppimm)

