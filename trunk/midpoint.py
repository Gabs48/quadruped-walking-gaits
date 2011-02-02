# code adapted from http://bocoup.com/processing-js/docs/index.php?page=Plasma%20Fractals
# original from http://www.ic.sunysb.edu/Stu/jseyster/plasma/ (Justin Seyster)
import random
import visual
from time import sleep

def plasma(x, y, width, height, c1, c2, c3, c4):
    newWidth = width / 2
    newHeight = height / 2

    if (width > gridSize or height > gridSize):
        #Randomly displace the midpoint!
        midPoint = (c1 + c2 + c3 + c4) / 4 + Displace(newWidth + newHeight)

        #Calculate the edges by averaging the two corners of each edge.
        edge1 = (c1 + c2) / 2
        edge2 = (c2 + c3) / 2
        edge3 = (c3 + c4) / 2
        edge4 = (c4 + c1) / 2

        x1 = x + newWidth
        y1 = y + newHeight
        
        #Do the operation over again for each of the four new grids.
        plasma(x,            y,             newWidth,   newHeight, c1,        edge1,    midPoint, edge4)
        plasma(x + newWidth, y,             newWidth,   newHeight, edge1,     c2,       edge2,    midPoint)
        plasma(x + newWidth, y + newHeight, newWidth,   newHeight, midPoint,  edge2,    c3,       edge3)
        plasma(x,            y + newHeight, newWidth,   newHeight, edge4,     midPoint, edge3,    c4)     
    else:
        #This is the "base case," where each grid piece is less than the size of a pixel.    
        c = (c1 + c2 + c3 + c4) / 4;

        #if c < 0:
        #    c = 0.01

        hw = (w/2)
        hh = (h/2)
        ch = c/2
        cc = c/maxHeight
        '''
        if c/maxHeight > 0.4 and c/maxHeight < 1:
            visual.box(frame=f,pos=[(x-hw), ch, (y-hh)],
                       color=(0,cc,0),
                       shape="square",
                       length=gridSize, height=c, width=gridSize)
        elif c/maxHeight > 1:
            visual.box(frame=f,pos=[(x-hw), ch, (y-hh)],
                       color=(cc,cc,0),
                       shape="square",
                       length=gridSize, height=c, width=gridSize)            
        else:
            visual.box(frame=f,pos=[x-hw, ch, y-hh],
                      color=(0,0,cc+0.5),
                      shape="square",
                      length=gridSize, height=c, width=gridSize)
        '''
        points.append([x-hw,c,y-hh])

        if len(points) > 3:
            mid = (points[0][1] + points[1][1] + points[2][1] + points[3][1])/4

            x1 = ((float(points[0][0]) + float(points[2][0]))/2)
            y1 = ((float(points[0][2]) + float(points[2][2]))/2)
            visual.convex(frame=f, pos=[points[0],points[1],points[2],points[3]])
            '''visual.box(frame=f,pos=[x1, c/2, y1],
                      color=(cc,0,0),
                      shape="square",
                      length=gridSize, height=c, width=gridSize)'''
            points[:] = []
            
def Displace(num):
    rand = (random.uniform(1, maxHeight) - noise)
    return rand


global gridSize, gamma, points, maxHeight, points, w, h, f
random.seed('Albert Einstein was a German theoretical physicist.')
f = visual.frame()
points=[]
width, w = 1000, 1000
noise = random.uniform(1,27) # less noise = higher map
height, h = 1000, 1000
gridSize = 10 # size between pixels
maxHeight = random.uniform(1,20)
#points.append([width-100,0,height-100])
#points.append([0-100,0,height-100])
#points.append([width-100,0,0-100])
#points.append([0-100,0,0-100])

lamp = visual.local_light(pos=(0,70,0), color=visual.color.gray(0.8))
#visual.convex(frame=f, pos=[(w/2,0,h/2),(w/2,0,-h/2),(-w/2,0,h/2),(-w/2,0,-h/2)])
plasma(0,0, width, height, random.uniform(1, maxHeight), random.uniform(1, maxHeight), random.uniform(1, maxHeight), random.uniform(1, maxHeight))

r = 0.01

while 1:
    visual.rate(25)
    if r < 1:
        f.rotate(angle=-0.0439822971503,axis=(r,1,0))
        r += 0.01
    else:
        f.rotate(angle=-0.0439822971503,axis=(r,1,0))
        r -= 0.01


