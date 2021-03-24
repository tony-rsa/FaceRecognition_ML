import unittest
import os
from ImportHandler.ImportImages import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class TestImportHandler(unittest.TestCase):

    def test_invalid_path(self):
        try:
            ImportImages('invalid/path/to/images')
            self.assertTrue(False, "Class did not raise exception.")
        except ValueError:
            self.assertTrue(True, "Class Must raises exception.")


    def test_getImagesGrayAndResized(self):
        result = ImportImages(ROOT_DIR+"/TestData/testImages").getGrayScaleResized()
        self.assertTrue("0" in result.keys(), "Must have Image id")
        self.assertEqual(len(result["0"]),22, "Result must have images with clear face.")
        self.assertTrue("1" in result.keys(), "Must have Image id")
        self.assertEqual(len(result["1"]),10, "Result must have images with clear face.")

