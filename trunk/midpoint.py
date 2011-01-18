# code adapted from http://bocoup.com/processing-js/docs/index.php?page=Plasma%20Fractals
# original from http://www.ic.sunysb.edu/Stu/jseyster/plasma/ (Justin Seyster)
import random
import visual

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

        #Do the operation over again for each of the four new grids.
        plasma(x, y, newWidth, newHeight, c1, edge1, midPoint, edge4)
  	plasma(x + newWidth, y, newWidth, newHeight, edge1, c2, edge2, midPoint)
  	plasma(x + newWidth, y + newHeight, newWidth, newHeight, midPoint, edge2, c3, edge3)
  	plasma(x, y + newHeight, newWidth, newHeight, edge4, midPoint, edge3, c4)		
    else:
        #This is the "base case," where each grid piece is less than the size of a pixel.    
        c = (c1 + c2 + c3 + c4) / 4;

        visual.points(pos=[x-(100),c,y-(100)], color=(c/20,c/20,c/20))

def Displace(num):
    rand = (random.uniform(1, 20) - noise)
    print rand
    return rand


global gridSize, gamma, points, width, height
random.seed('Albert Einstein was a German theoretical physicist.')

width = 200
noise = 1 # less noise = higher map
height = 200
gridSize = 10 # size between pixels

plasma(0,0, width, height, random.uniform(1, 20), random.uniform(1, 20), random.uniform(1, 20), random.uniform(1, 20))
