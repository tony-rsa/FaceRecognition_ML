import os
import cv2


class FaceDetactor:

    def __init__(self, gray_images):
        """
            Class is used as an instance to detect faces in an array
            of gray images.
                :param gray_image: This is a list with of gray_images 
                                   represented by arrays with pixel 
                                   values of each.
        """
        self.gray_images = gray_images
        self.face_coordinates = []
        self.cropped_faces = []


    def __findFaceCoordinates(self):
        """
            Method looks for faceses in a gray image, raises an exception if no faces where found.
                :returns list_of_faces: list with cropped faces.
        """
        haar_classifier = cv2.CascadeClassifier(ROOT_DIR+
                          "/Assets/haarcascade_frontalface_default.xml")
        found_faces = haar_classifier.detectMultiScale(self.gray_images,
                                      scaleFactor=1.7, minNeighbors=5)
        if len(found_faces) > 0:
            self.face_coordinates = found_faces
        else:
            raise Exception("No faces found.")

    
    def getFaceCoordinates(self):
        """
            Method returns a list with coordinates of faces.
            :return self.face_coordinates: returns list like [[x,y,w,h]]
        """
        if not len(self.face_coordinates) > 0:
            self.__findFaceCoordinates()
        return self.face_coordinates

    
    def getCroppedFaces(self):
        """
            Method crops a link of 
        """
        if not len(self.cropped_faces) > 0:
            for x,y,w,h in self.getFaceCoordinates():
                self.cropped_faces.append(self.gray_images[y:y+h,x:x+w])
        return self.cropped_faces


ROOT_DIR = os.path.dirname(os.path.abspath(__name__))
























    #     if not len(self.face_coordinates) > 0:
    #         self.__findFaceCoordinates()
    #     return self.face_coordinates

    
    # def getCroppedFaces(self):
    #     """
    #         Method clops a link of 
    #     """
    #     if not len(self.cropped_faces) > 0:
    #         for x,y,w,h in self.getFaceCoordinates():
    #             self.cropped_faces.append(self.gray_images[y:y+h,x:x+w])
    #     return self.cropped_faces















#



        # if len(found_faces) > 0:

        #     print("-> Classifier found {} face(s).".format(len(found_faces)))
        #     for x, y, w, h in found_faces:
        #         list_of_faces.append(self.gray_image[y:y+h,x:x+w])
        # else:
        #     raise Exception("-> No faces found, Try again!")
        # return list_of_faces


        
        # if self.imageIsValid(img_path):
        #     self.gray_image = self.loadImageGrayScale(img_path)
        # else:
        #     raise Exception(msgErrorImgInvalid+img_path+"'.")



    # def loadImageGrayScale(self, img_path):
    #     """
    #         Method reads and converts an image to gray scale.
    #             :param img_path: verifyed path to image.
    #             :returns: converted image.
    #     """
    #     loaded_image = cv2.imread(img_path)
    #     gray_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
    #     return gray_image


# msgErrorImgInvalid = "The provided path dose not contain a supported file or is invalid. I cannot use '"