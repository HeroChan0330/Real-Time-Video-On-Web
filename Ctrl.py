#coding:utf8


btnState=[False,False,False,False]
dir2Index={
    "forward":0,
    "downward":1,
    "left":2,
    "right":3
}

#设置电机速度，Motor为0 1分别为左右 speed为速度 从-10~10共21档
def setMotor(motor,speed):
    pass

def dirBtnPress(dir):
    global dir2Index,btnState
    if dir not in dir2Index:
        return False
    btnState[dir2Index[dir]]=True
    stateUpdate()

def dirBtnRelease(dir):
    global dir2Index,btnState
    if dir not in dir2Index:
        return False
    btnState[dir2Index[dir]]=False
    stateUpdate()

def stateUpdate():
    global dir2Index,btnState
    print(btnState)
    if btnState[0] and not (btnState[2] or btnState[3]):
        setMotor(0,10)
        setMotor(1,10)
    elif btnState[0] and btnState[2]:
        setMotor(0,5)
        setMotor(1,10)
    elif btnState[0] and btnState[3]:
        setMotor(0,10)
        setMotor(1,5)
    elif btnState[1] and not (btnState[2] or btnState[3]):
        setMotor(0,-10)
        setMotor(1,-10)
    elif btnState[1] and btnState[2]:
        setMotor(0,-5)
        setMotor(1,-10)
    elif btnState[1] and btnState[3]:
        setMotor(0,-10)
        setMotor(1,-5)
    elif btnState[2]:
        setMotor(0,-5)
        setMotor(1,5)
    elif btnState[3]:
        setMotor(0,5)
        setMotor(1,-5)
    else:
        setMotor(0,0)
        setMotor(1,0)