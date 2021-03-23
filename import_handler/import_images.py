import os
import cv2

class ImportImages:
    
    def __init__(self, path):
        if os.path.exists(path):
            self.path_dir = path
        else:
            raise ValueError("Invalid path. No images found.")


    def __isImage(self, path):
        valid_path = (".jpg", ".jpeg", ".png")
        if path.endswith(valid_path):
                return True
        return False


    def __downloadResizeGrayScale(self, path):
        image = cv2.imread(path)
        if len(image) < 0:
            return None
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray_image, (100,100))
        return resized_image


    def getGrayScaleResized(self):
        image_dict = {}
        for root, image_ids, filenames in os.walk(self.path_dir):
            id = ""
            list_of_images = []
            for filename in filenames:
                if self.__isImage(filename):
                    id = os.path.basename(root)
                    resized_image = self.__downloadResizeGrayScale(
                                    self.path_dir+"/"+id+"/"+filename)
                    list_of_images.append(resized_image)
            image_dict[id] = list_of_images
        return image_dict