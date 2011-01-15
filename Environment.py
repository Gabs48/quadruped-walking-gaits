import visual
import ode
import random
from math import pi
import vpyode

   
# create_box
def create_box(world, density, lx, ly, lz):
    """Create a box body and its corresponding geom."""
    
    # Create body
    body = vpyode.GDMFrameBody(world)
    element = vpyode.GDMElement()
    element.DefineBox(density, lx, ly, lz)
    element.GetDisplayObject().color = (random.uniform(0,1),random.uniform(0,1), random.uniform(0,1))
    body.AddGDMElement('Box', element)
    
    return body
    
# drop_objec
def drop_object(world):
    """Drop an object into the scene."""
    random.seed()
    
    body = create_box(world, random.uniform(100,500), random.uniform(0.5,6),random.uniform(0.1,0.6),random.uniform(0.5,6))
    body.setPosition( (random.uniform(-30,0),random.uniform(6,20),random.uniform(-10,10)) )
        
    # Rotate by a random angle about all three axes
    theta = random.uniform(0,2*pi)
    body.RotateOrientation(theta, (1,0,0))
    theta = random.uniform(0,2*pi)
    body.RotateOrientation(theta, (0,1,0))
    theta = random.uniform(0,2*pi)
    body.RotateOrientation(theta, (0,0,1))
        
    return body