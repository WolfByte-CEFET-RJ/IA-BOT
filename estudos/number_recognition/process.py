import cv2 
import os 

path = os.path.abspath('./dataset')

def process(path, dimX = 28, dimY = 28): 
    files = os.listdir()
    