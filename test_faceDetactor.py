import unittest
import os
from FaceHandler.faceDetactor import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestDetactFace(unittest.TestCase):

    def test_imageIsValid(self):
        result = faceDetactor.imageIsValid(None,ROOT_DIR+"/TestData/Images/noface.jpeg")
        self.assertTrue(result, "Path is valid.")

        result = faceDetactor.imageIsValid(None,"/not/a/valid/path")
        self.assertFalse(result, "Path is not valid.")


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
