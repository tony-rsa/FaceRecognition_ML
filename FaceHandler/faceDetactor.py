import os
import cv2

ROOT_DIR = os.path.dirname(os.path.abspath(__name__))

class faceDetactor:

    def __init__(self, img_path):
        if self.imageIsValid(img_path):
            self.gray_image = self.loadImageGrayScale(img_path)
        else:
            raise Exception(msgErrorImgInvalid+img_path+"'.")


    def imageIsValid(self, img_path):
        """
            Method checks if img_path is valid.
                :param img_path: the path to the image.
                :returns: True/False, True if valid.
        """
        valid_path = [".jpg", ".jpeg", ".png"]
        for each in valid_path:
            if (img_path.find(each) > len(img_path)-len(each)-1) \
                & os.path.exists(img_path):
                return True
        return False


    def loadImageGrayScale(self, img_path):
        """
            Method reads and converts an image to gray scale.
                :param img_path: verifyed path to image.
                :returns: converted image.
        """
        loaded_image = cv2.imread(img_path)
        gray_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
        return gray_image


    def findFace(self):
        """
            Method looks for faceses in a gray image, raises an exception if no faces where found.
                :returns list_of_faces: list with cropped faces.
        """
        list_of_faces = []
        haar_classifier = cv2.CascadeClassifier(ROOT_DIR+
                          "/Assets/haarcascade_frontalface_default.xml")
        found_faces = haar_classifier.detectMultiScale(self.gray_image,
                                      scaleFactor=1.7, minNeighbors=5)
        if len(found_faces) > 0:
            print("-> Classifier found {} face(s).".format(len(found_faces)))
            for x, y, w, h in found_faces:
                list_of_faces.append(self.gray_image[y:y+h,x:x+w])
        else:
            raise Exception("-> No faces found, Try again!")
        return list_of_faces


msgErrorImgInvalid = "The provided path dose not contain a supported file or is invalid. I cannot use '"