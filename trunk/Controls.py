'''
Author: Martin Stolle

Description: Window containing the controls
'''

import visual.controls
import Constants as const
from visual import pi
import Tkinter as tk

class tkWindow:
    def __init__(self, master, sim):
        frame = tk.Frame(master)
        frame.pack()

        self.sim = sim
        
        frameWindow = tk.LabelFrame(master, text='Window')
        frameWindow.pack(fill='both', expand='yes')
        
        frameWorld = tk.LabelFrame(master, text='World')
        frameWorld.pack(fill='both', expand='yes')

        frameRobot = tk.LabelFrame(master, text='Robot')
        frameRobot.pack(fill='both', expand='yes')
        
        frameMotion = tk.LabelFrame(master, text='Motion')
        frameMotion.pack(fill='both', expand='yes')

        self.setupWindowProps(frameWindow)
        self.setupWorldProps(frameWorld)
        self.setupRobotProps(frameRobot)
        #self.setupMotionProps(frameMotion)
    
    def setupMotionProps(self, root):
        mainFrame = tk.Frame(root)
        mainFrame.pack()
 
        topFrame = tk.Frame(mainFrame)
        topFrame.pack(side=tk.TOP)

        bottomFrame = tk.Frame(mainFrame)
        bottomFrame.pack(side=tk.BOTTOM)
        
        buttonPush = tk.Button(topFrame, text='Push',
                               command=self.sim.cRobot.pushRobot,
                               width=const.toCtrlWidth)       
        buttonPull = tk.Button(topFrame, text='Pull',
                               command=self.sim.cRobot.pushRobot,
                               width=const.toCtrlWidth)
        buttonDrop = tk.Button(topFrame, text='Re-Drop',
                               command=self.sim.cRobot.dropAgain,
                               width=const.toCtrlWidth) 
 
        buttonPush.pack(side=tk.LEFT)
        buttonPull.pack(side=tk.LEFT)
        buttonDrop.pack(side=tk.LEFT)
        
        self.motionVal = tk.StringVar()
        self.motionVal.set('Forward') # initial value
        dropMotion = tk.OptionMenu(bottomFrame, self.motionVal, 'Forward', 'm2', 'm3', 'm4', 'm5', 'm6')
        labelMotion = tk.Label(bottomFrame, text='Motion: ')
        buttonMotion = tk.Button(bottomFrame, text='Go', command=self.setMotion)
        
        labelMotion.pack(side=tk.LEFT)
        dropMotion.pack(side=tk.LEFT)
        buttonMotion.pack(side=tk.LEFT)
        
    
    def setupRobotProps(self, root):
        mainFrame = tk.Frame(root)
        mainFrame.pack()
 
        topFrame = tk.Frame(mainFrame)
        topFrame.pack(side=tk.TOP)

        bottomFrame = tk.Frame(mainFrame)
        bottomFrame.pack(side=tk.BOTTOM)
        
        centerFrame = tk.Frame(mainFrame)
        centerFrame.pack(side=tk.BOTTOM)
        
        self.densityVal = tk.StringVar()
        self.densityVal.set('Maple') # initial value
        dropDensity = tk.OptionMenu(topFrame, self.densityVal, 'Iron', 'Maple', 'Plastic', 'Carbon', 'Gold', 'Bamboo')
        labelDensity = tk.Label(topFrame, text='Density: ')
        buttonDensity = tk.Button(topFrame, text='Set', command=self.setDensity)
        
        labelDensity.pack(side=tk.LEFT)
        dropDensity.pack(side=tk.LEFT)
        buttonDensity.pack(side=tk.LEFT)
        
        labelCoverage = tk.Label(centerFrame, text='Bodyshare(%): ')
        sliderCoverage = tk.Scale(centerFrame, orient=tk.HORIZONTAL,
                               from_=0.01, to=1.0, resolution=0.01,
                               command=self.sim.cRobot.setBodyCoverage,
                               length=const.tkCtrlLength, showvalue=0 )
        
        labelCoverage.pack(side=tk.LEFT)
        sliderCoverage.pack(side=tk.LEFT)
        sliderCoverage.set(1.0)
        
        labelTorque = tk.Label(bottomFrame, text='Joint-Torque: ')
        sliderTorque = tk.Scale(bottomFrame, orient=tk.HORIZONTAL,
                               from_=0.0, to=10000.0, resolution=1.0,
                               command=self.sim.cRobot.setFMax,
                               length=const.tkCtrlLength, showvalue=0 )
        sliderTorque.set(10000)
        
        labelTorque.pack(side=tk.LEFT)
        sliderTorque.pack(side=tk.LEFT)        
    
    def setupWorldProps(self, root):
        mainFrame = tk.Frame(root)
        mainFrame.pack()
        
        topFrame = tk.Frame(mainFrame)
        topFrame.pack(side=tk.TOP)
        
        bottomFrame = tk.Frame(mainFrame)
        bottomFrame.pack(side=tk.BOTTOM)        
        
        self.gravityVal = tk.StringVar()
        self.gravityVal.set('Earth') # initial value
        dropGravity = tk.OptionMenu(topFrame, self.gravityVal, 'Earth', 'Moon', 'Venus', 'Jupiter', 'Mars')
        labelGravity = tk.Label(topFrame, text='Gravity: ')
        buttonGravity = tk.Button(topFrame, text='Set', command=self.setGravity)
        
        labelGravity.pack(side=tk.LEFT)
        dropGravity.pack(side=tk.LEFT)
        buttonGravity.pack(side=tk.LEFT)
        
        labelExplain = tk.Label(bottomFrame, text='Icy <---------------> Rough')
        labelGround = tk.Label(bottomFrame, text='Ground: ')
        sliderGround = tk.Scale(bottomFrame, orient=tk.HORIZONTAL,
                               from_=0.1, to=5000.0, resolution=0.1,
                               command=self.sim.cWorld.setFloorGrip,
                               length=const.tkCtrlLength, showvalue=0 )
        sliderGround.set(5000)
        
        labelExplain.pack(side=tk.TOP)
        labelGround.pack(side=tk.LEFT)
        sliderGround.pack(side=tk.RIGHT)        
    
    def setupWindowProps(self, root):
        mainFrame = tk.Frame(root)
        mainFrame.pack()
        
        topFrame = tk.Frame(mainFrame)
        topFrame.pack(side=tk.TOP)
        
        bottomFrame = tk.Frame(mainFrame)
        bottomFrame.pack(side=tk.BOTTOM)
        
        labelColor = tk.Label(topFrame, text='Color: ')
        sliderColor = tk.Scale(topFrame, orient=tk.HORIZONTAL,
                               from_=0.0, to=1.0, resolution=0.1,
                               command=self.setBackgroundColor,
                               showvalue=0, length=const.tkCtrlLength)
    
        labelColor.pack(side=tk.LEFT)
        sliderColor.pack(side=tk.RIGHT)
        
        self.camVar = tk.IntVar()
        self.labelVar = tk.IntVar()
        checkCamera = tk.Checkbutton(bottomFrame, text='Robot Cam',
                                     command=self.onCheckCamera,
                                     variable=self.camVar)
        checkLabels = tk.Checkbutton(bottomFrame, text='Labels',
                                     command=self.onCheckLabels,
                                     variable=self.labelVar)

        checkCamera.pack(side=tk.LEFT)
        checkLabels.pack(side=tk.LEFT)
        checkCamera.select()
        checkLabels.select()
        
        
    def setBackgroundColor(self, val):
        color = (float(val), float(val), float(val))
        self.sim.cWorld.world._getScene().background = color
        
    
    def setGravity(self):
        if self.gravityVal.get() == 'Earth':
            self.sim.cWorld.setGravity(-9.81)
        elif self.gravityVal.get() == 'Moon':
            self.sim.cWorld.setGravity(-1.62)
        elif self.gravityVal.get() == 'Venus':
            self.sim.cWorld.setGravity(-8.87)
        elif self.gravityVal.get() == 'Jupiter':
            self.sim.cWorld.setGravity(-23.12)
        elif self.gravityVal.get() == 'Mars':
            self.cWorld.setGravity(-3.71)
        
        
    def setDensity(self):
        print "value is", self.densityVal.get()        
    
    
    def setMotion(self):
        print "value is", self.motionVal.get()
        
        
    def onCheckCamera(self):
        if self.camVar.get() == 0:
            self.sim.cRobot.centerRobot = False
        else:
            self.sim.cRobot.centerRobot = True
            
            
    def onCheckLabels(self):
        if self.labelVar.get() == 0:
            self.sim.showLabel(True)
        else:
            self.sim.showLabel(False)
            
        
class ControlWindow:
    def __init__(self, scene, cRobot, world):
        self.robot = cRobot
        self.world = world
        self.scene = scene
        self.centerRobot = True
        self.ctrls = visual.controls.controls(title='Controls', x=scene.width+10,
                                              y=0, width=220, height=scene.height/2,
                                              range=100)
        self.setupButtons()
        #self.setupSliders()
        #self.setupDropbox()
        self.setupLabels()
        #self.setupToggle()
        self.setupCtrlActions(cRobot)
        
        
    def setupButtons(self):
        self.bPush = visual.controls.button(pos=(0,0,0), width=const.ctrlsWidth,
                               height=24, text='Push', action=None )
        self.bRestart = visual.controls.button(pos=(0,25,0), width=const.ctrlsWidth,
                               height=24, text='Restart', action=None )
        
        self.bBack = visual.controls.button(pos=(0,-50,0), width=const.ctrlsWidth-60,
                                   height=24, text='B', action=lambda: self.robot.moveBackward() )
        self.bForward = visual.controls.button(pos=(0,-25,0), width=const.ctrlsWidth-60,
                                   height=24, text='F', action=lambda: self.robot.moveForward() )
        self.bLeft = visual.controls.button(pos=(-30,-25,0), width=const.ctrlsWidth-60,
                                   height=24, text='L', action=lambda: self.robot.turnLeft() )
        self.bRight = visual.controls.button(pos=(30,-25,0), width=const.ctrlsWidth-60,
                                   height=24, text='R', action=lambda: self.robot.turnRight() )
        
        
    def setupToggle(self):
        self.tLabels = visual.controls.toggle(pos=(40,180,0), width=10, height=10,
                                              text0='Labels On', text1='Labels Off',
                                              action=lambda: self.toggleLabels())
        
        self.tCenter = visual.controls.toggle(pos=(-40,180,0), width=10, height=10,
                                              text0='RobotCam On', text1='RobotCam Off',
                                              action=lambda: self.toggleCenterCamera())
        
        
    def toggleLabels(self):
        if self.tLabels.value:
            self.robot.showLabels = False
            self.lBody.visible = False
        else:
            self.robot.showLabels = True
            self.lBody.visible = True
            
            
    def toggleCenterCamera(self):
        if self.tCenter.value:
            self.centerRobot = False
        else:
            self.centerRobot = True
            
        
    def setupSliders(self):      
        self.sColor = visual.controls.slider(pos=(-40,-100), width=const.sliderWidth,
                               length=const.ctrlsWidth, axis=(1,0,0), min= 0.0, max= 1.0,
                               action=lambda: self.setBackgroundColor(self.sColor.value))
        
        self.sColor.value = self.scene.background[0]
        
        self.sFMax = visual.controls.slider(pos=(-40,100), width=const.sliderWidth,
                               length=const.ctrlsWidth, axis=(1,0,0), min= 0.0, max= 10000.0,
                               action=lambda: self.robot.setFMax(self.sFMax.value))
        
        self.sFMax.value = self.robot.FMax
        
        self.sCoverage = visual.controls.slider(pos=(-40,90), width=const.sliderWidth,
                               length=const.ctrlsWidth, axis=(1,0,0), min= 0.01, max= 1.0,
                               action=lambda: self.robot.setBodyCoverage(self.sCoverage.value))
        
        self.sCoverage.value = self.robot.bodyCoverage
        
        self.sFloor = visual.controls.slider(pos=(-40,80), width=const.sliderWidth,
                               length=const.ctrlsWidth, axis=(1,0,0), min= 0.01, max= 5000.0,
                               action=lambda: self.world.setFloorGrip(self.sFloor.value))
        
        self.sFloor.value = self.world.returnMu()
        
        
    def setBackgroundColor(self, val):
        color = (val, val, val)
        self.scene.background = color
        
        
    def setupDropbox(self):
        self.mGravity = visual.controls.menu(pos=(-30,-125,0), height=10,
                                    width=const.ctrlsWidth-30, text='Gravity')
        
        self.mGravity.items.append(('Earth', lambda: self.world.setGravity(-9.81)))
        self.mGravity.items.append(('Moon',lambda: self.world.setGravity(-1.62)))
        self.mGravity.items.append(('Venus',lambda: self.world.setGravity(-8.87))) 
        self.mGravity.items.append(('Jupiter',lambda: self.world.setGravity(-23.12))) 
        self.mGravity.items.append(('Mars',lambda: self.world.setGravity(-3.71))) 
    
        self.mDensity = visual.controls.menu(pos=(30,-125,0), height=10, range=50,
                                        width=const.ctrlsWidth-30, text='Density')
    
        self.mDensity.items.append(('Iron',lambda: self.robot.setDensity(7874))) 
        self.mDensity.items.append(('Maple',lambda: self.robot.setDensity(755))) 
        self.mDensity.items.append(('Plastic',lambda: self.robot.setDensity(1350)))
        self.mDensity.items.append(('Carbon',lambda: self.robot.setDensity(2260)))
        self.mDensity.items.append(('Gold',lambda: self.robot.setDensity(19300))) 
        self.mDensity.items.append(('Bamboo',lambda: self.robot.setDensity(400))) 
        
                
    def setupLabels(self):
        self.lBody = visual.controls.label(text="Body", space=0.2, pos=(1,0),
                                  opacity=0.5, xoffset=20, yoffset=20)

        
    def setupCtrlActions(self, cRobot):
        # After to assign the actions after the robot instance has been created
        self.bPush.action = lambda: cRobot.pushRobot()
        self.bRestart.action = lambda: cRobot.dropAgain()