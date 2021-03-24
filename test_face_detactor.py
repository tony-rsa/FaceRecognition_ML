import unittest
import os
import cv2
from fac_handler.face_detactor import *

class TestDetactFace(unittest.TestCase):

    def __init__(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        input_image = cv2.imread(ROOT_DIR+
                        "/test_data/testImages/0/p1.jpeg")
        self.image = cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)


    def test_detect(self):
        result = detect(self.image)
        self.assertTrue(len(result) == 2)
        self.assertTrue(len(result[0]) == 4)
        self.assertEquals(type(result[1]), None)


    def test_draw_rect_around_face(self):
        detection_result = detect_face(self.image)
        result = draw_rect_around_face(detection_result[1],
                                        detection_result[0])
        self.assertEquals(type(result), None)

    
    def write_text_onface(self):
        result = write_text_onface(self.image,"Hello World",10,10)
        self.assertTrue(result[0])
        self.assertTrue(result[1] != self.image)


    def test_get_arry_of_faces(self)
        result  = get_arry_of_faces(self)
        self.assertTrue(len(result) > 0)
        self.assertEquals(type(result[]), "")