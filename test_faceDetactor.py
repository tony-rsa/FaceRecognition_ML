import unittest
import os
from FaceHandler.FaceDetactor import *
from ImportHandler.ImportImages import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestDetactFace(unittest.TestCase):

    def test_getFaceCoord(self):
        gray_images = ImportImages(ROOT_DIR+"/TestData/testImages").getGrayScaleResized()
        for each in gray_images.keys():
            faces = FaceDetactor(gray_images[each]).getFaceCoordinates()
            self.assertTrue(len (faces) > 0)


    def test_getCroppedImage(self):
        gray_images = ImportImages(ROOT_DIR+"/TestData/testImages").getGrayScaleResized()
        for each in gray_images.keys():
            faces = FaceDetactor(gray_images[each]).getCroppedFaces()
            self.assertTrue(len (faces) > 0)

<<<<<<< HEAD

    # def test_imageIsValid(self):
    #     result = faceDetactor.imageIsValid(None,ROOT_DIR+"/TestData/Images/noface.jpeg")
    #     self.assertTrue(result, "Path is valid.")

    #     result = faceDetactor.imageIsValid(None,"/not/a/valid/path")
    #     self.assertFalse(result, "Path is not valid.")


    # def test_not_an_image(self):
    #     img_path = ROOT_DIR+"/TestData/Images/notAnImage.txt"
    #     fail = False
    #     try:
    #         faceDetactor(img_path)
    #         fail = True
    #     except Exception:
    #         self.assertTrue(True)
    #     self.assertFalse(fail, "Must rase an exceptions.")

        
    # def test_image_noface(self):
    #     img_path = "TestData/Images/noface.jpeg"
    #     fail = False
    #     try:
    #         faceDetactor(img_path).findFace()
    #         fail = True
    #     except Exception:
    #         self.assertTrue(True)
    #     self.assertFalse(fail, "Must rase an exceptions")

    
    # def test_image_hasface(self):
    #     img_path = ROOT_DIR+"/TestData/Images/hasface.jpg"
    #     result =  faceDetactor(img_path).findFace()
    #     try:
    #         self.assertEqual(2,len(result), "number of faces incorrect.")
    #     except TypeError:
    #         self.assertTrue(False,"Returns list with the location of faces.")
=======
    def test_not_an_image(self):
        img_path = ROOT_DIR+"/TestData/Images/notAnImage.txt"
        fail = False
        try:
            faceDetactor(img_path)
            fail = True
        except Exception:
            self.assertTrue(True)
        self.assertFalse(fail, "Must raise an exceptions.")

        
    def test_image_noface(self):
        img_path = "TestData/Images/noface.jpeg"
        fail = False
        try:
            faceDetactor(img_path).findFace()
            fail = True
        except Exception:
            self.assertTrue(True)
        self.assertFalse(fail, "Must raise an exceptions")

    
    def test_image_hasface(self):
        img_path = ROOT_DIR+"/TestData/Images/hasface.jpg"
        result =  faceDetactor(img_path).findFace()
        try:
            self.assertEqual(2,len(result), "number of faces incorrect.")
        except TypeError:
            self.assertTrue(False,"Returns list with the location of faces.")

            
>>>>>>> 0f238791f148b7dc4c2605663388d779ddde9376
