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
print("Identified Gender is:"+ checkGender())
print("Identified Semester is:"+checkSemester())
print("Identified Credit Hours Program is:"+ checkProgram())

cv2.waitKey()
cv2.destroyAllWindows()
