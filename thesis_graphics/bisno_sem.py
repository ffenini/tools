'''This code creates a grid on the image of 10 lines, it is able to draw a
ruler on the image in order to determine the positions   

Use: open the created file (croppimm) file with Windows Photo viewer

-circle drawing with size bar and notation 
-image crop
-image save

 
'''
file='C:/M_drive_docs/Thesis/graphics/bisnoSEM/bisno_6.png'
imm=Image.open(file)
imm=imm.convert("RGBA")
size = ImageDraw.Draw(imm)   ####image object 
ximm=imm.size[0] ##size of the image
yimm=imm.size[1] ##
white=(255,255,255)
black=(0,0,0)
blue=(40,125,244)
red=(224,41,20)
yellow=(246,242,39)
###grid
grid=False
if grid:
    rng=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.99999]
    for i in rng:
        ximm=ximm
        yimm=yimm
        size.line([ximm*i,yimm*0,ximm*i,yimm*1], fill=white, width=0)###Horiz lines
        size.line([ximm*0,yimm*i,ximm*1,yimm*i], fill=white, width=1)###Vert lines
        font = ImageFont.truetype("arial.ttf", int(ximm*0.02))  ### font type and font size relative to figure size
        size.text((ximm*0.05, yimm*i-yimm*0.03),str(i) ,font=font, fill=white) ### x position
        size.text((ximm*i-ximm*0.03, yimm*0.05),str(i) ,font=font, fill=white) ### y position
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

###ellipses
x_cir=0.43 #### x coordinate of the center of the circle
y_cir=0.39 #### y coordinate of the center of the circle
diam=0### diameter of the circle
thickness=0.000000951*ximm
meas='1 µm'###text to display below the bar
if diam!=0:
    r=ximm/yimm*1 ###ratio between x and y dimension of the image
    for i in linspace(diam-thickness,diam+thickness,100):
        size.ellipse([ximm*(x_cir-i/2-rotation),yimm*(y_cir-i*r/2-rotation),ximm*(rotation+x_cir+i/2),yimm*(rotation+y_cir+i*r/2)], fill=None, outline=yellow)
    ##increase the thickness by mult circles    #size.ellipse([ximm*(x_cir*1.01-diam/2),yimm*(y_cir*1.01-diam*r/2),ximm*(x_cir*1.01+diam/2),yimm*(y_cir*1.01+diam*r/2)], fill=None, outline=900)
    ### maesuring bar
    meas_bar=False
    if meas_bar:
        size.line([ximm*(x_cir-diam/2),yimm*(y_cir+diam*0.75*r),ximm*(x_cir+diam/2),yimm*(y_cir+diam*0.75*r)], fill=yellow, width=2)
        size.line([ximm*(x_cir-diam/2),yimm*(y_cir+(diam*0.75*r-0.005)),ximm*(x_cir-diam/2),yimm*(y_cir+(diam*0.75*r+0.005))], fill=yellow, width=2) 
        size.line([ximm*(x_cir+diam/2),yimm*(y_cir+(diam*0.75*r-0.005)),ximm*(x_cir+diam/2),yimm*(y_cir+(diam*0.75*r+0.005))], fill=yellow, width=2) 
        font = ImageFont.truetype("arial.ttf", int(ximm*0.03))  ### font type and font size
        size.text((ximm*(x_cir-diam/6), yimm*(y_cir+diam)),meas ,font=font, fill=300) ###position


#####scale bar

bar_x1,bar_y1,bar_x2,bar_y2,color_bar=0.8,0.83,0.9,0.83,True
size.line([ximm*bar_x1,yimm*bar_y1,ximm*bar_x2,yimm*bar_y2],fill=white, width=int(ximm*0.008)) #main scale bar
if color_bar:
    size.line([ximm*bar_x1,yimm*(bar_y1+0.005),ximm*bar_x2,yimm*(bar_y2+0.005)],fill=red, width=int(ximm*0.003)) #colored scale bar
font = ImageFont.truetype("arial.ttf", int(ximm*0.04))  ### font type and font size
font2 = ImageFont.truetype("arial.ttf", int(ximm*0.06))
nm,um='500 nm','1 µm'
size.text((ximm*0.805, yimm*0.76), um ,font=font, fill=white) ###position
size.text((ximm*0.05, yimm*0.05),'(f)' ,font=font2, fill=white) ###position
###Cropping
croppimm=imm.crop((0, 0, ximm*1, 0.9*yimm))
croppimm.save(file[:-4]+'_MOD'+file[-4:])

del size




display(croppimm)
