import cv2  

def contours(path, x, y, w, h):
    img = cv2.imread(path)
    result_img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
    
    cv2.imshow("result_img", result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()