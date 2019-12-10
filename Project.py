import cv2
import numpy as np
IMAGE_FILE = "test_sample6.jpg"

img = cv2.imread(IMAGE_FILE, cv2.IMREAD_GRAYSCALE)
img1 = cv2.medianBlur(img, 13)
img2= cv2.medianBlur(img, 5)
correctCircles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT, 1, 20, param1=40, param2=30, minRadius=10, maxRadius=30)
allCircles = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, 1, 20, param1=40, param2=30, minRadius=10, maxRadius=30)
# np.ndarray.sort(correctCircles,1,"quicksort")
# np.ndarray.sort(allCircles,1,"quicksort")
correctCircles=np.uint16(np.around(correctCircles))
allCircles=np.uint16(np.around(allCircles))

img1 = cv2.resize(img1, (600, 800))
img2 = cv2.resize(img2, (600, 800))
cv2.imshow("Gray: Correct", img1)
cv2.imshow("Gray: All", img2)

ci=1
ai=1
img1 = cv2.imread(IMAGE_FILE, cv2.IMREAD_COLOR)
img2= cv2.imread(IMAGE_FILE, cv2.IMREAD_COLOR)
for (x, y, r) in correctCircles[0, :]:
    cv2.putText(img1, ""+str(ci), (int(x-50), int(y+9)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    print(""+str(ci)+"= X: "+str(x) +" Y:"+str(y))
    ci+=1

for (x1, y1, r1) in allCircles[0, :]:
    cv2.putText(img2, ""+str(ai), (int(x1-50), int(y1+9)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    print(""+str(ai)+"= X: "+str(x1) +" Y:"+str(y1))
    ai+=1

img1 = cv2.resize(img1, (600, 800))
img2 = cv2.resize(img2, (600, 800))
cv2.imshow("Correct", img1)
cv2.imshow("All", img2)

def checkGender():
    for (x,y,r) in correctCircles[0, :]:
        if (y==294 or y==292 or y==293 or y==295 or y==296):
            if(x==1258 or x==1259 or x==1260 or x==1257 or x==1256):
                return "Male"
            else:
                return "Female"

def checkSemester():
    for(x,y,r) in correctCircles[0, :]:
        if(y==376 or y==375 or y==374 or y== 377 or y==378):
            if(x==556 or x==557 or x==558 or x==555 or x==554):
                return "Fall"
            elif(x in range(818,822)):
                return "Spring"
            else:
                return"Summer"
def checkProgram():
    for(x,y,r) in correctCircles[0, :]:
        if(y==454 or y== 455 or y==456 or y==457 or y==458 or y==459 or y==460):
            if(x in range(456, 460)):
                return "MCTA"
            elif(x in range(588, 592)):
                return "ENVR"
            elif(x in range(720, 724)):
                return "BLDG"
            elif(x in range(856, 860)):
                return "CESS"
            elif(x in range(986, 992)):
                return "ERGY"
            elif(x in range(1122,1126)):
                return "COMM"
            elif(x in range(1256, 1260)):
                return "MANF"
        elif(y in range(494, 500)):
            if(x in range(454, 458)):
                return "LAAR"
            elif(x in range(588, 592)):
                return "MATL"
            elif(x in range(722, 726)):
                return "CISE"
            elif(x in range(856, 860)):
                return "HAUD"
    return "NONE"
def check19Option():
    for(x,y,r) in correctCircles[0, :]:
        if(y in range(974, 980)): #1.1
            v11="NONE"
            if(x in range(1120, 1128)):
                v11="Strongly Agree"
            elif(x in range(1218, 1226)):
                v11="Agree"
            elif(x in range(1322, 1330)):
                v11="Neutral"
            elif(x in range(1420, 1428)):
                v11="Disagree"
            elif(x in range(1520, 1528)):
                v11="Strongly Disagree"
        elif(y in range(1014, 1020)): #1.2
            v12="NONE"
            if(x in range(1120, 1128)):
                v12="Strongly Agree"
            elif(x in range(1218, 1226)):
                v12="Agree"
            elif(x in range(1322, 1330)):
                v12="Neutral"
            elif(x in range(1420, 1428)):
                v12="Disagree"
            elif(x in range(1520, 1528)):
                v12="Strongly Disagree"
        elif(y in range(1054, 1062)): #1.3
            v13="NONE"
            if(x in range(1120, 1128)):
                v13="Strongly Agree"
            elif(x in range(1218, 1226)):
                v13="Agree"
            elif(x in range(1322, 1330)):
                v13="Neutral"
            elif(x in range(1420, 1428)):
                v13="Disagree"
            elif(x in range(1520, 1528)):
                v13="Strongly Disagree"
        elif(y in range(1094, 1102)): #1.4
            v14="NONE"
            if(x in range(1120, 1128)):
                v14="Strongly Agree"
            elif(x in range(1218, 1226)):
                v14="Agree"
            elif(x in range(1322, 1330)):
                v14="Neutral"
            elif(x in range(1420, 1428)):
                v14="Disagree"
            elif(x in range(1520, 1528)):
                v14="Strongly Disagree"
        elif(y in range(1132, 1142)): #1.5
            v15="NONE"
            if(x in range(1120, 1128)):
                v15="Strongly Agree"
            elif(x in range(1218, 1226)):
                v15="Agree"
            elif(x in range(1322, 1330)):
                v15="Neutral"
            elif(x in range(1420, 1428)):
                v15="Disagree"
            elif(x in range(1520, 1528)):
                v15="Strongly Disagree"
        elif(y in range(1250, 1266)): #2.1
            v21="NONE"
            if(x in range(1120, 1128)):
                v21="Strongly Agree"
            elif(x in range(1218, 1226)):
                v21="Agree"
            elif(x in range(1322, 1330)):
                v21="Neutral"
            elif(x in range(1420, 1428)):
                v21="Disagree"
            elif(x in range(1520, 1528)):
                v21="Strongly Disagree"
        elif(y in range(1290, 1306)): #2.2
            v22="NONE"
            if(x in range(1120, 1128)):
                v22="Strongly Agree"
            elif(x in range(1218, 1226)):
                v22="Agree"
            elif(x in range(1322, 1330)):
                v22="Neutral"
            elif(x in range(1420, 1428)):
                v22="Disagree"
            elif(x in range(1520, 1528)):
                v22="Strongly Disagree"
        elif(y in range(1328, 1348)): #2.3
            v23="NONE"
            if(x in range(1120, 1128)):
                v23="Strongly Agree"
            elif(x in range(1218, 1226)):
                v23="Agree"
            elif(x in range(1322, 1330)):
                v23="Neutral"
            elif(x in range(1420, 1428)):
                v23="Disagree"
            elif(x in range(1520, 1528)):
                v23="Strongly Disagree"
        elif(y in range(1370, 1386)): #2.4
            v24="NONE"
            if(x in range(1120, 1128)):
                v24="Strongly Agree"
            elif(x in range(1218, 1226)):
                v24="Agree"
            elif(x in range(1322, 1330)):
                v24="Neutral"
            elif(x in range(1420, 1428)):
                v24="Disagree"
            elif(x in range(1520, 1528)):
                v24="Strongly Disagree"
        elif(y in range(1408, 1422)): #2.5
            v25="NONE"
            if(x in range(1120, 1128)):
                v25="Strongly Agree"
            elif(x in range(1218, 1226)):
                v25="Agree"
            elif(x in range(1322, 1330)):
                v25="Neutral"
            elif(x in range(1420, 1428)):
                v25="Disagree"
            elif(x in range(1520, 1528)):
                v25="Strongly Disagree"
        elif(y in range(1446, 1466)): #2.6
            v26="NONE"
            if(x in range(1120, 1128)):
                v26="Strongly Agree"
            elif(x in range(1218, 1226)):
                v26="Agree"
            elif(x in range(1322, 1330)):
                v26="Neutral"
            elif(x in range(1420, 1428)):
                v26="Disagree"
            elif(x in range(1520, 1528)):
                v26="Strongly Disagree"
        elif(y in range(1564, 1584)): #3.1
            v31="NONE"
            if(x in range(1120, 1128)):
                v31="Strongly Agree"
            elif(x in range(1218, 1226)):
                v31="Agree"
            elif(x in range(1322, 1330)):
                v31="Neutral"
            elif(x in range(1420, 1428)):
                v31="Disagree"
            elif(x in range(1520, 1528)):
                v31="Strongly Disagree"
        elif(y in range(1604, 1624)): #3.2
            v32="NONE"
            if(x in range(1120, 1128)):
                v32="Strongly Agree"
            elif(x in range(1218, 1226)):
                v32="Agree"
            elif(x in range(1322, 1330)):
                v32="Neutral"
            elif(x in range(1420, 1428)):
                v32="Disagree"
            elif(x in range(1520, 1528)):
                v32="Strongly Disagree"
        elif(y in range(1644, 1664)): #3.3
            v33="NONE"
            if(x in range(1120, 1128)):
                v33="Strongly Agree"
            elif(x in range(1218, 1226)):
                v33="Agree"
            elif(x in range(1322, 1330)):
                v33="Neutral"
            elif(x in range(1420, 1428)):
                v33="Disagree"
            elif(x in range(1520, 1528)):
                v33="Strongly Disagree"
        elif(y in range(1768, 1788)): #4.1
            v41="NONE"
            if(x in range(1120, 1128)):
                v41="Strongly Agree"
            elif(x in range(1218, 1226)):
                v41="Agree"
            elif(x in range(1322, 1330)):
                v41="Neutral"
            elif(x in range(1420, 1428)):
                v41="Disagree"
            elif(x in range(1520, 1528)):
                v41="Strongly Disagree"
        elif(y in range(1808, 1828)): #4.2
            v42="NONE"
            if(x in range(1120, 1128)):
                v42="Strongly Agree"
            elif(x in range(1218, 1226)):
                v42="Agree"
            elif(x in range(1322, 1330)):
                v42="Neutral"
            elif(x in range(1420, 1428)):
                v42="Disagree"
            elif(x in range(1520, 1528)):
                v42="Strongly Disagree"
        elif(y in range(1886, 1906)): #4.3
            v43="NONE"
            if(x in range(1120, 1128)):
                v43="Strongly Agree"
            elif(x in range(1218, 1226)):
                v43="Agree"
            elif(x in range(1322, 1330)):
                v43="Neutral"
            elif(x in range(1420, 1428)):
                v43="Disagree"
            elif(x in range(1520, 1528)):
                v43="Strongly Disagree"
        elif(y in range(2004, 2024)): #5.1
            v51="NONE"
            if(x in range(1120, 1128)):
                v51="Strongly Agree"
            elif(x in range(1218, 1226)):
                v51="Agree"
            elif(x in range(1322, 1330)):
                v51="Neutral"
            elif(x in range(1420, 1428)):
                v51="Disagree"
            elif(x in range(1520, 1528)):
                v51="Strongly Disagree"
        elif(y in range(2046, 2066)): #5.2
            v52="NONE"
            if(x in range(1120, 1128)):
                v52="Strongly Agree"
            elif(x in range(1218, 1226)):
                v52="Agree"
            elif(x in range(1322, 1330)):
                v52="Neutral"
            elif(x in range(1420, 1428)):
                v52="Disagree"
            elif(x in range(1520, 1528)):
                v52="Strongly Disagree"
    print("1.1 Is" + v11 + "\n 1.2 Is "+v12 +"\n1.3 Is " +v13+"\n1.4 is"+v14+ "\n1.5 is "+v15 +"\n2.1 is"+v21+"\n2.2 is"+v22 +"\n2.3 is"+v23)
    print("2.4 is"+v24+"\n2.5 is"+v25+"\n2.6 is"+v26 + "\n3.1 is "+v31 +"\n3.2 is"+v32 + "\n3.3 is "+v33+"\n4.1 is"+v41+"\n4.2 is"+v42+"\n5.1 is "+v51+"\n5.2 is"+v52)

print("Identified Gender is:"+ checkGender())
print("Identified Semester is:"+checkSemester())
print("Identified Credit Hours Program is:"+ checkProgram())

cv2.waitKey()
cv2.destroyAllWindows()
