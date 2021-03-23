import os
from cv2 import *

class FaceDetactor:

    def __init__(self):
        """
            This Class can detect and encapsulate faces found in an image. 
        """
        self.faces = [(,)]


    def detect(self,one_gray_image):
        """
            Method finds a face in a given gray scale image picture.
            Method uses the haar Classifier's multi Scale detector for accuracy.
            :param one_gray_image: Takes in one gray scale image with a face.
            :returns tuple: with face coord and gray_image if face found.    
        """
        classifier = CascadeClassifier(
                    'haarcascade/haarcascade_frontalface_default.xml')
        faces = classifier.detectMultiScale(one_gray_image,
                                            scaleFactor=1.32,
                                            minNeighbors=5)
        self.faces.append((faces, one_gray_image))
        return (faces,one_gray_image)


    def draw_rect_around_face(image,face):
        (x, y, w, h) = face
        rectangle(image,(x, y),(x+w, y+h),
                                (255, 0, 0),thickness=3)
        return image

    
    def write_text_onface(image,text,x,y):
        putText(image,text,(x,y), FONT_HERSHEY_DUPLEX,2,(255,0,0),4)


    def get_arry_of_faces(self){
        """
            Returns a 2D arry with detected faces and gray image used of detection.  
        """
        return self.faces
    }

ROOT_DIR = os.path.dirname(os.path.abspath(__name__))