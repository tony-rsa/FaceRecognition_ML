import os
from cv2 import *

class FaceRecognizer:

    def __init__(self):
        """
            This Class uses LBP histograms, and encodes image to numpy arry. 
        """
        self.LBRHrec = None


        binary_histograms = face.LBPHFaceRecognizer_create()

        self.LBRHrec = binary_histograms.train(faces,np.array(faceID))
        return binary_histograms
    