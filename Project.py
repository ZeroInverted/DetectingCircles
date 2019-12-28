#Always outnumbered. NEVER outcoded.

import cv2
import numpy as np
import math
from scipy import ndimage
v11=v12=v13=v14=v15=v21=v22=v23=v24=v25=v26=v31=v32=v33=v41=v42=v43=v51=v52="NONE" #Chosen parameters
IMAGE_FILE = "test_sample8.jpg"
def checkGender():
    for (x,y,r) in correctCircles[0, :]:
        if (y in range(280, 300)):
            if(x in range(1240,1280)):
                return "Male"
            elif(x in range(1350, 1420)):
                return "Female"
    return "NONE"
def checkSemester():
    for(x,y,r) in correctCircles[0, :]:
        if(y in range(360, 390)):
            if(x in range(540, 570)):
                return "Fall"
            elif(x in range(800,840)):
                return "Spring"
            elif(x in range(1020,1120)):
                return"Summer"
    return "NONE"
def checkProgram():
    for(x,y,r) in correctCircles[0, :]:
        if(y in range(440, 480)):
            if(x in range(440, 470)):
                return "MCTA"
            elif(x in range(570, 600)):
                return "ENVR"
            elif(x in range(710, 740)):
                return "BLDG"
            elif(x in range(840, 870)):
                return "CESS"
            elif(x in range(980, 1010)):
                return "ERGY"
            elif(x in range(1110,1140)):
                return "COMM"
            elif(x in range(1240, 1270)):
                return "MANF"
        elif(y in range(480, 520)):
            if(x in range(440, 470)):
                return "LAAR"
            elif(x in range(570, 600)):
                return "MATL"
            elif(x in range(710, 740)):
                return "CISE"
            elif(x in range(840, 870)):
                return "HAUD"
    return "NONE"
def check19Option():
    for(x,y,r) in correctCircles[0, :]:
        if(y in range(960, 990)): #1.1
            global v11
            if(x in range(1110, 1140)):
                v11="Strongly Agree"
            elif(x in range(1210, 1240)):
                v11="Agree"
            elif(x in range(1320, 1350)):
                v11="Neutral"
            elif(x in range(1410, 1440)):
                v11="Disagree"
            elif(x in range(1510, 1540)):
                v11="Strongly Disagree"
        elif(y in range(1000, 1030)): #1.2
            global v12
            if(x in range(1110, 1140)):
                v12="Strongly Agree"
            elif(x in range(1210, 1240)):
                v12="Agree"
            elif(x in range(1320, 1350)):
                v12="Neutral"
            elif(x in range(1410, 1440)):
                v12="Disagree"
            elif(x in range(1510, 1540)):
                v12="Strongly Disagree"
        elif(y in range(1040, 1070)): #1.3
            global v13
            if(x in range(1110, 1140)):
                v13="Strongly Agree"
            elif(x in range(1210, 1240)):
                v13="Agree"
            elif(x in range(1320, 1350)):
                v13="Neutral"
            elif(x in range(1410, 1440)):
                v13="Disagree"
            elif(x in range(1510, 1540)):
                v13="Strongly Disagree"
        elif(y in range(1080, 1110)): #1.4
            global v14
            if(x in range(1110, 1140)):
                v14="Strongly Agree"
            elif(x in range(1210, 1240)):
                v14="Agree"
            elif(x in range(1320, 1350)):
                v14="Neutral"
            elif(x in range(1410, 1440)):
                v14="Disagree"
            elif(x in range(1510, 1540)):
                v14="Strongly Disagree"
        elif(y in range(1120, 1150)): #1.5
            global v15
            if (x in range(1110, 1140)):
                v15 = "Strongly Agree"
            elif (x in range(1210, 1240)):
                v15 = "Agree"
            elif (x in range(1320, 1350)):
                v15 = "Neutral"
            elif (x in range(1410, 1440)):
                v15 = "Disagree"
            elif (x in range(1510, 1540)):
                v15 = "Strongly Disagree"
        elif(y in range(1240, 1280)): #2.1
            global v21
            if(x in range(1110, 1140)):
                v21="Strongly Agree"
            elif(x in range(1210, 1240)):
                v21="Agree"
            elif(x in range(1320, 1350)):
                v21="Neutral"
            elif(x in range(1410, 1440)):
                v21="Disagree"
            elif(x in range(1510, 1540)):
                v21="Strongly Disagree"
        elif(y in range(1290, 1320)): #2.2
            global v22
            if(x in range(1110, 1140)):
                v22="Strongly Agree"
            elif(x in range(1210, 1240)):
                v22="Agree"
            elif(x in range(1320, 1350)):
                v22="Neutral"
            elif(x in range(1410, 1440)):
                v22="Disagree"
            elif(x in range(1510, 1540)):
                v22="Strongly Disagree"
        elif(y in range(1321, 1350)): #2.3
            global v23
            if(x in range(1110, 1140)):
                v23="Strongly Agree"
            elif(x in range(1210, 1240)):
                v23="Agree"
            elif(x in range(1320, 1350)):
                v23="Neutral"
            elif(x in range(1410, 1440)):
                v23="Disagree"
            elif(x in range(1510, 1540)):
                v23="Strongly Disagree"
        elif(y in range(1360, 1390)): #2.4
            global v24
            if(x in range(1110, 1140)):
                v24="Strongly Agree"
            elif(x in range(1210, 1240)):
                v24="Agree"
            elif(x in range(1320, 1350)):
                v24="Neutral"
            elif(x in range(1410, 1440)):
                v24="Disagree"
            elif(x in range(1510, 1540)):
                v24="Strongly Disagree"
        elif(y in range(1400, 1430)): #2.5
            global v25
            if(x in range(1110, 1140)):
                v25="Strongly Agree"
            elif(x in range(1210, 1240)):
                v25="Agree"
            elif(x in range(1320, 1350)):
                v25="Neutral"
            elif(x in range(1410, 1440)):
                v25="Disagree"
            elif(x in range(1510, 1540)):
                v25="Strongly Disagree"
        elif(y in range(1440, 1470)): #2.6
            global v26
            if(x in range(1110, 1140)):
                v26="Strongly Agree"
            elif(x in range(1210, 1240)):
                v26="Agree"
            elif(x in range(1320, 1350)):
                v26="Neutral"
            elif(x in range(1410, 1440)):
                v26="Disagree"
            elif(x in range(1510, 1540)):
                v26="Strongly Disagree"
        elif(y in range(1540, 1590)): #3.1
            global v31
            if(x in range(1110, 1140)):
                v31="Strongly Agree"
            elif(x in range(1210, 1240)):
                v31="Agree"
            elif(x in range(1320, 1350)):
                v31="Neutral"
            elif(x in range(1410, 1440)):
                v31="Disagree"
            elif(x in range(1510, 1540)):
                v31="Strongly Disagree"
        elif(y in range(1600, 1630)): #3.2
            global v32
            if(x in range(1110, 1140)):
                v32="Strongly Agree"
            elif(x in range(1210, 1240)):
                v32="Agree"
            elif(x in range(1320, 1350)):
                v32="Neutral"
            elif(x in range(1410, 1440)):
                v32="Disagree"
            elif(x in range(1510, 1540)):
                v32="Strongly Disagree"
        elif(y in range(1640, 1670)): #3.3
            global v33
            if(x in range(1110, 1140)):
                v33="Strongly Agree"
            elif(x in range(1210, 1240)):
                v33="Agree"
            elif(x in range(1320, 1350)):
                v33="Neutral"
            elif(x in range(1410, 1440)):
                v33="Disagree"
            elif(x in range(1510, 1540)):
                v33="Strongly Disagree"
        elif(y in range(1740, 1790)): #4.1
            global v41
            if(x in range(1110, 1140)):
                v41="Strongly Agree"
            elif(x in range(1210, 1240)):
                v41="Agree"
            elif(x in range(1320, 1350)):
                v41="Neutral"
            elif(x in range(1410, 1440)):
                v41="Disagree"
            elif(x in range(1510, 1540)):
                v41="Strongly Disagree"
        elif(y in range(1800, 1840)): #4.2
            global v42
            if(x in range(1110, 1140)):
                v42="Strongly Agree"
            elif(x in range(1210, 1240)):
                v42="Agree"
            elif(x in range(1320, 1350)):
                v42="Neutral"
            elif(x in range(1410, 1440)):
                v42="Disagree"
            elif(x in range(1510, 1540)):
                v42="Strongly Disagree"
        elif(y in range(1870, 1920)): #4.3
            global v43
            if(x in range(1110, 1140)):
                v43="Strongly Agree"
            elif(x in range(1210, 1240)):
                v43="Agree"
            elif(x in range(1320, 1350)):
                v43="Neutral"
            elif(x in range(1410, 1440)):
                v43="Disagree"
            elif(x in range(1510, 1540)):
                v43="Strongly Disagree"
        elif(y in range(1990, 2030)): #5.1
            global v51
            if(x in range(1110, 1140)):
                v51="Strongly Agree"
            elif(x in range(1210, 1240)):
                v51="Agree"
            elif(x in range(1320, 1350)):
                v51="Neutral"
            elif(x in range(1410, 1440)):
                v51="Disagree"
            elif(x in range(1510, 1540)):
                v51="Strongly Disagree"
        elif(y in range(2040, 2080)): #5.2
            global v52
            if(x in range(1110, 1140)):
                v52="Strongly Agree"
            elif(x in range(1210, 1240)):
                v52="Agree"
            elif(x in range(1320, 1350)):
                v52="Neutral"
            elif(x in range(1410, 1440)):
                v52="Disagree"
            elif(x in range(1510, 1540)):
                v52="Strongly Disagree"
def checkForShift(angle, img1, img2 ,im2):
    if (angle!=0):
        #Detecting shift values
        allCirc = cv2.HoughCircles(im2, cv2.HOUGH_GRADIENT, 1, 20, param1=40, param2=30, minRadius=10, maxRadius=30)
        maleXCoord = 100000
        maleYCoord = 100000
        for (x, y, r) in allCirc[0, :]: #Getting minimum Y coordinate
            if (maleYCoord > y ):
                maleYCoord = y
                maleXCoord = x
        maleYCoord=np.uint16(np.around(maleYCoord))
        maleXCoord=np.uint16(np.around(maleXCoord))
        for(x, y, r) in allCirc[0, :]: #Getting minimum X coordinate that has the minimum coordinate. (Male Gender circle.)
            minRange=int(y)-8
            maxRange=int(y)+8
            if (int(maleYCoord) in range(minRange, maxRange)):
                if (maleXCoord > x):
                    maleYCoord = y
                    maleXCoord = x
        maleYCoord=math.ceil(maleYCoord)
        maleXCoord=math.ceil(maleXCoord)
        maleYCoord=int(maleYCoord)
        maleXCoord=int(maleXCoord)
        # X Axis Shift
        shift = int(math.fabs(maleXCoord-1258))
        for i in range(img1.shape[1] - 1, img1.shape[1] - shift, -1):
            img1 = np.roll(img1, -1, axis=1)
            img1[:, -1] = 0
        for i in range(img2.shape[1] - 1, img2.shape[1] - shift, -1):
            img2 = np.roll(img2, -1, axis=1)
            img2[:, -1] = 0
        # Y Axis Shift
        shift = int(math.fabs(maleYCoord-294))
        for i in range(img1.shape[0] - 1, img1.shape[0] - shift, -1):
            img1 = np.roll(img1, -1, axis=0)
            img1[-1, :] = 0
        for i in range(img2.shape[0] - 1, img2.shape[0] - shift, -1):
            img2 = np.roll(img2, -1, axis=0)
            img2[-1, :] = 0
    return img1, img2
def checkForRotation(imgOG, imgGray):
    img_edges = cv2.Canny(imgGray, 100, 100, apertureSize=3)
    lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5) #Detect Lines
    angles = [] #Store the angle of each line in an  array
    for x1, y1, x2, y2 in lines[0]:
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1)) #calculate line angle
        angles.append(angle) #Insert the calculated value into the array
    median_angle = np.median(angles) #Get Median Angle
    imgOG= ndimage.rotate(imgOG, median_angle) #Rotate the original image with the median angle of line inclination
    return imgOG, angle
img = cv2.imread(IMAGE_FILE, cv2.IMREAD_GRAYSCALE)
img, angle=checkForRotation(img, img)
img1 = cv2.medianBlur(img, 13) #Blur aggressively until only the filled circles remain
img2= cv2.medianBlur(img, 5) #Blur a little in order to smooth out the circles for detection
im2=img2
img1, img2=checkForShift(angle, img1, img2, im2)
#Detection
correctCircles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT, 1, 20, param1=40, param2=30, minRadius=10, maxRadius=30)
allCircles = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, 1, 20, param1=40, param2=30, minRadius=10, maxRadius=30)
#Round the results
correctCircles=np.uint16(np.around(correctCircles))
allCircles=np.uint16(np.around(allCircles))
#Resize the image to a suitable size
img1 = cv2.resize(img1, (600, 800))
img2 = cv2.resize(img2, (600, 800))

check19Option()
with open(IMAGE_FILE+"_outut.txt","w") as text_file:
    print("Gender: {}".format(checkGender()), file=text_file)
    print("Semester: {}".format(checkSemester()), file=text_file)
    print("Credit Hours Program: {}".format(checkProgram()), file=text_file)
    print("1.1: {}".format(v11)+"\n1.2: {}".format(v12)+"\n1.3: {}".format(v13)+"\n1.4: {}".format(v14), file=text_file)
    print("1.5: {}".format(v15)+"\n2.1: {}".format(v21)+"\n2.2: {}".format(v22)+"\n2.3: {}".format(v23), file=text_file)
    print("2.4: {}".format(v24)+"\n2.5: {}".format(v25)+"\n2.6: {}".format(v26)+"\n3.1: {}".format(v31), file=text_file)
    print("3.2: {}".format(v32)+"\n3.3: {}".format(v33)+"\n4.1: {}".format(v41)+"\n4.2: {}".format(v42), file=text_file)
    print("4.3: {}".format(v43)+"\n5.1: {}".format(v51)+"\n5.2: {}".format(v52), file=text_file)
cv2.waitKey()
cv2.destroyAllWindows()