import cv2 as cv
from os import listdir


class Monitor:
    def __init__(self, roi):
        self.roi = roi

    def apply_roi(self, image):
        return image[self.roi[0][1]: self.roi[1][1], self.roi[0][0]: self.roi[1][0]]


class ImageMonitor(Monitor):
    def __init__(self, roi, path):
        super().__init__(roi)
        self.path = path

    def find_item(self, img):
        highestS = 0
        itemName = ""
        img = self.apply_roi(img)

        for item in listdir(self.path):
            sim = round(1-self.get_similarity(img, cv.imread(f'{self.path}/{item}')), 3)
            print(sim)
            if sim >= highestS:
                highestS = sim
                itemName = item.split('.')[0]

        return itemName

    def get_similarity(self, img, item):
        img_mask = self._get_mask(img)
        item_mask = self._get_mask(item)
        item_mask = cv.bitwise_not(item_mask)

        result = cv.bitwise_and(img_mask, item_mask)
        return (result.sum() / 255) / ((self.roi[1][0] - self.roi[0][0])*(self.roi[1][1] - self.roi[0][1]))

    def _get_mask(self, img):
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.GaussianBlur(img, (3, 3), 0.5)
        _, thresh = cv.threshold(img, 60, 255, cv.THRESH_BINARY)

        return thresh
