def setup():
    size(1000, 600)

def gradience_vertical(left_color_amount):
    gradient_color_1 = color(0, 135, 186) #light blue
    gradient_color_2 = color(255, 175, 140) #orange
    #255, 175, 140

    noStroke()
    fill(gradient_color_1)
    
    noStroke()
    fill(gradient_color_2)

    
    for lines in range(0, 1000):
        change = map(lines, 0, height, 0, left_color_amount)
        in_between_color = lerpColor(gradient_color_1, gradient_color_2, change)
        
        stroke(in_between_color)
        line(0, lines, width, lines)
    


#Cloud 1 ellipse variables
#--------
x_mover1 = -250
x_mover2 = -265
x_mover3 = -280
x_mover4 = -258
x_mover5 = -287
#--------

#Cloud 2 ellipse variables
#--------
IIx_mover1 = 1100
IIx_mover2 = 1100
IIx_mover3 = 1070
#--------

#Cloud 3 ellipse variables
#--------
IIIx_mover1 = -50
#--------

#Cloud 4 ellipse variables
#--------
IVx_mover1 = -70
#--------

#Cloud 5 ellipse variables
#--------
Vx_mover1 = 1130
Vx_mover2 = 1130
#--------



def draw():
    
    
    gradience_vertical(2.2) #Background
    
    #Cloud 3 (backround)
    #--------   
    global IIIx_mover1 

    IIIx_mover1 += 1.3
    
    noStroke
    fill(255)
    ellipse(IIIx_mover1, 300, 60, 7)
    
    if IIIx_mover1 == 150:
        IIIx_mover1 = -60
    #--------   

    
    #Cloud 2 (behind big mountains)
    #--------
    noStroke()
    global IIx_mover1 
    global IIx_mover2 
    global IIx_mover3 

    IIx_mover1 -= 1
    IIx_mover2 -= 1
    IIx_mover3 -= 1
    
    fill(255)
    ellipse(IIx_mover1, 110, 55, 10)
    ellipse(IIx_mover2, 115, 110, 15)
    ellipse(IIx_mover3, 125, 200, 15)

    if IIx_mover1 == -200:
        IIx_mover1 = 1100
        IIx_mover2 = 1100
        IIx_mover3 = 1070
    #--------     
   
   
    
    #Background mountains
    #--------   
    noStroke()
    fill(4, 98, 153)
    triangle(200, 450, 700, 450, 400, 320)
    triangle(300, 450, 1000, 450, 600, 290)
    #--------
    
    #Cloud 4 (background)
    #--------   
    global IVx_mover1 

    IVx_mover1 += 1.2
    
    noStroke
    fill(255)
    ellipse(IVx_mover1, 285, 90, 5)
    
    if IVx_mover1 == 150:
        IVx_mover1 = -60
    #--------  
    
     
     #Cloud 5 (kinda-background )
    #--------   
    global Vx_mover1 
    global Vx_mover2

    Vx_mover1 -= .5
    Vx_mover2 -= .5
    
    noStroke
    fill(255)
    ellipse(Vx_mover1, 205, 130, 15)
    ellipse(Vx_mover2, 195, 60, 7.5)
    
    if Vx_mover1 == -130:
        Vx_mover1 = 1130
        Vx_mover2 = 1130
    #--------   
    
    
    
    #Rolling hills
    #--------
    noStroke
    fill(170, 178, 134)
    ellipse(700, 415, 2000, 70) #Hill 3 (farthest)
    #-------- mountain 1 (front right, big)(sub-catergory object)
    noStroke()
    fill(78, 142, 178)
    triangle(500, 500, 1100, 500,  900, 60) #Mountain
    fill(74, 106, 124)
    triangle(1100, 500, 900, 500,  900, 60) #Shaded
    fill(255)
    triangle(840, 130, 900, 190,  900, 60) #Snow 2
    fill(255)
    triangle(820, 150, 900, 120,  900, 60) #Snow (main body)
    fill(200)
    triangle(939, 150, 900, 190,  900, 60) #Snow Shaded
    #--------
    fill(117, 165, 124)
    ellipse(700, 440, 2000, 50) #Hill 3 (far)
    #--------  #mountain 2 (front left, big)(sub-catergory object)
    noStroke()
    fill(117, 165, 124)
    ellipse(0, 440, 200, 70) #cover
    fill(78, 142, 178)
    triangle(350, 440, -50, 480, 100, 30) #Mountain 
    fill(105, 181, 224)
    triangle(335, 415, 380, 418, 100, 30) #glare of mountain 
    fill(105, 181, 224)
    triangle(350, 415, 350, 440, 100, 110) #glare of mountain 2
    fill(200)
    triangle(80, 85, 173, 150, 100, 30) #Dark snow
    fill(255)
    triangle(167, 140, 160, 100, 100, 30)
    #--------
    fill(105, 140, 110)
    ellipse(300, 620, 900, 300) #Hill 4 (2nd closest)
    fill(0, 105, 148)
    ellipse(500, 490, 1100, 104) #Shadow Lake
    fill(87, 180, 214)
    triangle(350, 440, 850, 431, 325, 540) #light lake
    fill(138, 170, 142)
    ellipse(900, 550, 520, 300) #Hill 1
    fill(105, 140, 110)
    ellipse(700, 615, 850, 300) #Hill 2 (closest)
    #--------
    
    
    #Cloud 1
    #--------
    global x_mover1 
    global x_mover2 
    global x_mover3 
    global x_mover4 
    global x_mover5 

    x_mover1 += 1.5
    x_mover2 += 1.5
    x_mover3 += 1.5
    x_mover4 += 1.5
    x_mover5 += 1.5
    
    fill(255)
    ellipse(x_mover1, 110, 500, 35)
    ellipse(x_mover2, 100, 250, 35)
    ellipse(x_mover3, 95, 130, 35)
    ellipse(x_mover4, 90, 90, 35)
    ellipse(x_mover5, 85, 90, 35)
    
    if x_mover1 == 1250:
        x_mover1 = -250
        x_mover2 = -265
        x_mover3 = -280
        x_mover4 = -258
        x_mover5 = -287
    

   

   
   

    
        



    
    
