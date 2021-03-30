import cv2

path = './dataset/train'

def datasets(path, dimX=28, dimY=28):
    for img_name in path: 
        img = cv2.imread(path + "/" + img_name)
        img = cv2.resize(img, (dimX, dimY)/255)
    
