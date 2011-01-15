'''
Author: Martin Stolle
Description: Simulation of Quadruped Robot using ODE and VPython

PyOde: http://pyode.sourceforge.net
VPython: http://www.vpython.org
VPyOde: http://www.missioncognition.net/visualpyode/

CGKit(Rendering): http://cgkit.sourceforge.net/
Pixie: http://www.renderpixie.com/

Definition Quadruped:
1. noun: an animal especially a mammal having four limbs specialized for walking
2. adjective: having four feet
'''

# Standard Python Library
import sys
from random import gauss
# Physics Engine
import ode
# 3D Engine
import visual
import visual.controls
import visual.graph
# Merged Lib between pyODE and VPython
import vpyode
# Rendering
import cgkit.cgtypes
import cgkit.riutil
# GUI
import Tkinter
import thread

from WorldPhysics import myWorld
from Robot import Robot
from Controls import ControlWindow, tkWindow
import Constants as const
import Grid
from Simu import Simulation
                
def setupWindow(scene):
    scene.title = 'Quadruped Simulation'
    scene.height = const.windowHeight
    scene.width = const.windowWidth
    scene.autoscale = 0
    scene.forward = (-5,-5,-5)
    scene.background = (0.2,0.2,0.2)
    
    createFloor()
    createArrows()
    
def createFloor():
    Grid.grid(500)

def createArrows():
    ''' Create arrow coordinates '''
    visual.arrow(pos=(0,0,0), axis=(1,0,0), radius=1, color=(0,0,1), length=3)
    visual.arrow(pos=(0,0,0), axis=(0,1,0), radius=1, color=(1,0,0), length=3)
    visual.arrow(pos=(0,0,0), axis=(0,0,1), radius=1, color=(0,1,0), length=3)
    
    visual.controls.label(pos = (3,0,0), text='x',box=False, opacity=0.0)
    visual.controls.label(pos = (0,3,0), text='y',box=False, opacity=0.0)
    visual.controls.label(pos = (0,0,3), text='z',box=False, opacity=0.0)
    
def createUI(scene):
    '''Setup window and controls'''
    setupWindow(scene)
    
def normalMode():
    '''Uses VPython to visualize, manipulate and simulate the Quadruped live.'''
    cWorld = myWorld()
    createUI(cWorld.world._getScene())
    
    cRobot = Robot(cWorld.world, vpyode._bigSpace, 50)
    cCtrl = ControlWindow(cWorld.world._getScene(), cRobot, cWorld)
    
    cRobot.dropRobot()
    
    dt = 1.0/const.framerate
    refresh = 0
    
    while(1):
        visual.rate(const.framerate) # Frame rate
        
        # check for events, drive actions; must be executed repeatedly in a loop
        cCtrl.ctrls.interact()

        # do multiple simulation steps per frame to prevent jittering due to
        # 'small' collisions
        n = 10
        
        for i in range(n):           
            # Simulation step
            cWorld.world.step(dt/n)
            
            if cRobot.bodyExists():
                cRobot.refreshRobot(cCtrl.lBody)
            
                if (cCtrl.centerRobot):
                    cWorld.world._getScene().center = cRobot.center
                
                for leg in cRobot.tibia:
                    leg.UpdateDisplay()
                    
                for leg in cRobot.femur:
                    leg.UpdateDisplay()


def GUImode():
	root = Tkinter.Tk()
	root.geometry('200x730+1050+0')
	sim = Simulation()
	thread.start_new_thread(sim.startLoop,())
	app = tkWindow(root, sim)
	root.mainloop()

            
def usage():
    '''Prints the usage of this program.'''
    print 'Right-Click Rotate, Mid-Click Move'
    
def usageRender():
    '''Prints rendering how-to.'''
    print 'usageRender'

def main(argv):
    if '--help' in argv:
        usage()
        usageRender()
    elif '--render' in argv:
        if len(argv) < 2:
            usageRender()
        else:
            renderMode(argv[-1])
    else:
        GUImode()
        
if __name__ == "__main__":
    main(sys.argv[1:])