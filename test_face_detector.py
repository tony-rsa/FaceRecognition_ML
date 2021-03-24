import unittest
import os
import cv2
from face_handler.face_detector import *

class TestDetectFace(unittest.TestCase):
    global image0, input_image0
    global image1, input_image1

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    #invalid Image with no face.
    input_image0 = cv2.imread(ROOT_DIR+
                    "/test_data/unittest/0.jpg")
    image0 = cv2.cvtColor(input_image0,cv2.COLOR_BGR2GRAY)

    #valid Image with 2 faces.
    input_image1 = cv2.imread(ROOT_DIR+
                    "/test_data/unittest/1.png")
    image1 = cv2.cvtColor(input_image1,cv2.COLOR_BGR2GRAY)


    def test_detect(self):
        result = face_detector().detect_face(image1)
        self.assertTrue(len(result) == 2)
        self.assertEqual(len(result[0][0]), 4)
        self.assertTrue(len(result[1])> 0)


    def test_draw_rect_invalid(self):
        try:
            detection_result = face_detector().detect_face(image0)
            result = face_detector.draw_rect_around_face(detection_result[1],
                                            detection_result[0])
            self.assertTrue(False)
        except:
            self.assertTrue(True)


    def test_draw_rect_valid(self):
        try:
            detection_result = face_detector().detect_face(image1)
            result = face_detector.draw_rect_around_face(input_image1,detection_result[0])
            while True:
                cv2.imshow("DETECTED.. press 'x' to close.", cv2.resize(result, (800, 500)))
                if cv2.waitKey(10) == ord('x'):#wait until 'q' key is pressed
                    break
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    
    def test_write_text_img(self):
        result = face_detector.write_text_on_img(input_image1,
                                "Test passed if you can read this. press 'x' again.",100,950)
        self.assertTrue(result[0])
        while True:
            cv2.imshow("test2 press 'x' to close.", cv2.resize(result[1], (800, 500)))
            if cv2.waitKey(10) == ord('x'):#wait until 'q' key is prexssed
                break
        self.assertTrue(True)


    def test_get_arry_of_faces(self):
        face_detector().detect_face(image1)
        result  = face_detector().get_arry_of_faces()
        self.assertTrue(len(result) > 0)
        self.assertEqual(type(result[0]), type((0,0,0,0)))