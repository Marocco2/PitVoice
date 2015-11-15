import ac
import acsys
import subprocess
import datetime

DoOnce = 0
PitButton = "0"
DoPitOnce = 0

def acMain(ac_version):
    global appWindow,FuelSelection,label1,label2,label3,NoChange,SuperSoft
    global SoftSlick,MediumSlick,HardSlick,SuperHard,Body,Engine,Suspension
    global DoOnce,ahk,response

    if DoOnce == 0:
    	ahk = subprocess.Popen(["apps\python\PitVoice\Pitvoice.exe"])
    	DoOnce = 1
    	
    #
    appWindow = ac.newApp("PitVoice")
    ac.setSize(appWindow,350,250)
    ac.setTitle(appWindow,"")
    ac.setBackgroundOpacity(appWindow,0.5)
    ac.setBackgroundTexture(appWindow,"apps/python/PitVoice/PitMenu.png")
    #
    FuelSelection = ac.addSpinner(appWindow,"")#Fuel
    ac.setPosition(FuelSelection,87,110)
    ac.setSize(FuelSelection,175,25)
    ac.setFontColor(FuelSelection,1,1,0,1)
    ac.setFontSize(FuelSelection, 15)
    ac.setRange(FuelSelection,0,190)
    ac.setStep(FuelSelection,1)
    ac.addOnValueChangeListener(FuelSelection,FuelEvent)
    #
    NoChange = ac.addCheckBox(appWindow,"")
    ac.setPosition(NoChange,22,86)
    ac.setSize(NoChange,15,15)
    ac.addOnCheckBoxChanged(NoChange,NoChangeEvent)
    #
    SuperSoft = ac.addCheckBox(appWindow,"")
    ac.setPosition(SuperSoft,82,86)
    ac.setSize(SuperSoft,15,15)
    ac.addOnCheckBoxChanged(SuperSoft,SuperSoftEvent)
    #
    SoftSlick = ac.addCheckBox(appWindow,"")
    ac.setPosition(SoftSlick,138,86)
    ac.setSize(SoftSlick,15,15)
    ac.addOnCheckBoxChanged(SoftSlick,SoftSlickEvent)
    #
    MediumSlick = ac.addCheckBox(appWindow,"")
    ac.setPosition(MediumSlick,197,86)
    ac.setSize(MediumSlick,15,15)
    ac.addOnCheckBoxChanged(MediumSlick,MediumSlickEvent)
    #
    HardSlick = ac.addCheckBox(appWindow,"")
    ac.setPosition(HardSlick,255,86)
    ac.setSize(HardSlick,15,15)
    ac.addOnCheckBoxChanged(HardSlick,HardSlickEvent)
    #
    SuperHard = ac.addCheckBox(appWindow,"")
    ac.setPosition(SuperHard,313,86)
    ac.setSize(SuperHard,15,15)
    ac.addOnCheckBoxChanged(SuperHard,SuperHardEvent)
    #
    Body = ac.addCheckBox(appWindow,"")
    ac.setPosition(Body,59,229)
    ac.setSize(Body,15,15)
    ac.addOnCheckBoxChanged(Body,BodyEvent)
    #
    Engine = ac.addCheckBox(appWindow,"")
    ac.setPosition(Engine,169,229)
    ac.setSize(Engine,15,15)
    ac.addOnCheckBoxChanged(Engine,EngineEvent)
    #
    Suspension = ac.addCheckBox(appWindow,"")
    ac.setPosition(Suspension,276,229)
    ac.setSize(Suspension,15,15)
    ac.addOnCheckBoxChanged(Suspension,SuspensionEvent)
    #
    label1=ac.addLabel(appWindow,"Fuel +")
    ac.setPosition(label1,275,113)
    ac.setFontColor(label1,1,1,0,1)
    ac.setFontSize(label1, 15)
    #
    label2=ac.addLabel(appWindow,"Fuel -")
    ac.setPosition(label2,30,113)
    ac.setFontColor(label2,1,1,0,1)
    ac.setFontSize(label2, 15)
    #
    label3=ac.addLabel(appWindow,"0")
    ac.setPosition(label3,166,110)
    ac.setFontColor(label3,1,1,0,0)
    ac.setFontSize(label3, 15)
    # 

    ResponseWit()
    return "PitVoice"

def acUpdate(deltaT):
    global PitButton,Speed,DoPitOnce
    
    
    Speed = ac.getCarState(0,acsys.CS.SpeedMS)
    
    if Speed <= 0.060 and DoPitOnce == 0:
    	PitButton = "1"
    	DoPitOnce = 1
    	PushPitButton()
		
    if DoPitOnce == 1:
        PitButton = "0"
        PushPitButton()
    	
    if Speed > 0.060:
    	DoPitOnce = 0
    	PushPitButton()

    ResponseWit()
    ac.console("[PV]Refresh at " + datetime.now())
    ac.log("[PV]Refresh at " + datetime.now())

def acShutdown():  
    subprocess.Popen.kill(ahk)

def ResponseWit():
    global SoftSlick,MediumSlick,HardSlick,SuperHard,Body,Engine,Suspension,NoChange,SuperSoft
    global PitFileText,PitFileLines,Tires,Gas,FixBody,FixEngine,FixSuspension
    
    with open('apps/python/PitVoice/Pit.txt') as PitFileText:
        PitFileLines = [line.rstrip('\n') for line in PitFileText]
    
    Tires = PitFileLines[0]
    Gas = PitFileLines[1]
    FixBody = PitFileLines[2]
    FixEngine = PitFileLines[3]
    FixSuspension = PitFileLines[4]
    PitFileText.close()

    if Tires == "NoChange":
        ac.setValue(NoChange,1)
        ac.setValue(SoftSlick,0)
        ac.setValue(SuperSoft,0)
        ac.setValue(MediumSlick,0)
        ac.setValue(HardSlick,0)
        ac.setValue(SuperHard,0)
    if Tires == "SuperSoft":
        ac.setValue(SuperSoft,1)
        ac.setValue(NoChange,0)
        ac.setValue(SoftSlick,0)
        ac.setValue(MediumSlick,0)
        ac.setValue(HardSlick,0)
        ac.setValue(SuperHard,0)
    if Tires == "SoftSlick":
        ac.setValue(SoftSlick,1)
        ac.setValue(NoChange,0)
        ac.setValue(SuperSoft,0)
        ac.setValue(MediumSlick,0)
        ac.setValue(HardSlick,0)
        ac.setValue(SuperHard,0)
    if Tires == "MediumSlick":
        ac.setValue(MediumSlick,1)
        ac.setValue(NoChange,0)
        ac.setValue(SuperSoft,0)
        ac.setValue(SoftSlick,0)
        ac.setValue(HardSlick,0)
        ac.setValue(SuperHard,0)
    if Tires == "HardSlick":
        ac.setValue(SuperSoft,1)
        ac.setValue(NoChange,0)
        ac.setValue(SuperSoft,0)
        ac.setValue(SoftSlick,0)
        ac.setValue(MediumSlick,0)
        ac.setValue(SuperHard,0)
    if Tires == "SuperHard":
        ac.setValue(SuperHard,1)
        ac.setValue(NoChange,0)
        ac.setValue(SuperSoft,0)
        ac.setValue(SoftSlick,0)
        ac.setValue(MediumSlick,0)
        ac.setValue(HardSlick,0)

    if FixBody == "yes":
        ac.setValue(Body,1)
    else:
        ac.setValue(Body,0)
    if FixEngine == "yes":
        ac.setValue(Engine,1)
    else:
        ac.setValue(Engine,0)
    if FixSuspension == "yes":
        ac.setValue(Suspension,1)
    else:
        ac.setValue(Suspension,0)

    if Gas != "0":
        ac.setText(label3,"{}".format(round(Gas)))
    
def FuelEvent(x):
    global FuelSelection,amount,Gas

    amount = ac.getValue(FuelSelection)
    ac.setText(label3,"{}".format(round(amount)))
    Gas = ac.getText(label3)
    WriteData()

def NoChangeEvent(name, state):
    global NoChange,Tires

    Tires = "NoChange"
    ac.setValue(SoftSlick,0)
    ac.setValue(SuperSoft,0)
    ac.setValue(MediumSlick,0)
    ac.setValue(HardSlick,0)
    ac.setValue(SuperHard,0)
    WriteData()
    
def SuperSoftEvent(name, state):
    global SuperSoft,Tires

    Tires = "SuperSoft"
    ac.setValue(NoChange,0)
    ac.setValue(SoftSlick,0)
    ac.setValue(MediumSlick,0)
    ac.setValue(HardSlick,0)
    ac.setValue(SuperHard,0)
    WriteData()
    
def SoftSlickEvent(name, state):
    global SoftSlick,Tires

    Tires = "SoftSlick"
    ac.setValue(NoChange,0)
    ac.setValue(SuperSoft,0)
    ac.setValue(MediumSlick,0)
    ac.setValue(HardSlick,0)
    ac.setValue(SuperHard,0)
    WriteData()

def MediumSlickEvent(name, state):
    global MediumSlick,Tires

    Tires = "MediumSlick"
    ac.setValue(NoChange,0)
    ac.setValue(SuperSoft,0)
    ac.setValue(SoftSlick,0)
    ac.setValue(HardSlick,0)
    ac.setValue(SuperHard,0)
    WriteData()

def HardSlickEvent(name, state):
    global HardSlick,Tires

    Tires = "HardSlick"
    ac.setValue(NoChange,0)
    ac.setValue(SuperSoft,0)
    ac.setValue(SoftSlick,0)
    ac.setValue(MediumSlick,0)
    ac.setValue(SuperHard,0)
    WriteData()

def SuperHardEvent(name, state):
    global SuperHard,Tires

    Tires = "SuperHard"
    ac.setValue(NoChange,0)
    ac.setValue(SuperSoft,0)
    ac.setValue(SoftSlick,0)
    ac.setValue(MediumSlick,0)
    ac.setValue(HardSlick,0)
    WriteData()

def BodyEvent(name, state):
    global Body,FixBody

    if FixBody == "no":
        FixBody = "yes"
    else:
        FixBody = "no"
        
    WriteData()

def EngineEvent(name, state):
    global Engine,FixEngine

    if FixEngine == "no":
        FixEngine = "yes"
    else:
        FixEngine = "no"
    
    WriteData()

def SuspensionEvent(name, state):
    global Suspension,FixSuspension

    if FixSuspension == "no":
        FixSuspension = "yes"
    else:
        FixSuspension = "no"
    
    WriteData()
    
def WriteData():

    ac.console("[PV]Tires:" + Tires + ",Fuel:" + Gas + "Fix body:" + FixBody + "Fix engine:" + FixEngine + "Fix suspension:" + FixSuspension)
    ac.log("[PV]Tires:" + Tires + ",Fuel:" + Gas + "Fix body:" + FixBody + "Fix engine:" + FixEngine + "Fix suspension:" + FixSuspension)
    
    with open('apps/python/PitVoice/Pit.txt', 'w') as f:
          f.write(Tires + "\n")
          f.write(Gas + "\n")
          f.write(FixBody + "\n")
          f.write(FixEngine + "\n")
          f.write(FixSuspension)
          f.close()
	
def PushPitButton():
    with open('apps/python/PitVoice/PitButton.txt', 'w') as g:
          g.write(PitButton)
          g.close()    
   
