import cv2 as cv
from BOUNDARIES import ROIs
from observer import *


font = cv.FONT_HERSHEY_PLAIN


def click_event(event, x, y, _, _2):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x*2, y*2)


def end_wait(key: int=27):
    while True:
        if cv.waitKey(0) == key:
            break


if __name__ == "__main__":
    img = cv.imread("C:/Users/morga/PycharmProjects/ValSpectate/Images/val1.jpeg")

    # main = img[ROIs['main'][0][1]: ROIs['main'][1][1], ROIs['main'][0][0]: ROIs['main'][1][0]]
    # sidearm = img[ROIs['sidearm'][0][1]: ROIs['sidearm'][1][1], ROIs['sidearm'][0][0]: ROIs['sidearm'][1][0]]
    # cv.imwrite("Images/Sidearm/Pistol.jpeg", sidearm)
    # cv.imwrite("Images/Main/AK.jpeg", main)

    MainMonitor = ImageMonitor(ROIs['main'], "Images/Main/")
    print(MainMonitor.find_item(img))
    SidearmMonitor = ImageMonitor(ROIs['sidearm'], "Images/Sidearm/")
    print(SidearmMonitor.find_item(img))

    for item in ROIs.items():
        cv.rectangle(img, item[1][0], item[1][1], (0, 255, 0), 2)
        cv.putText(img, item[0], item[1][0], font, 2, (0, 255, 0), 2)

    img = cv.resize(img, (1920 // 2, 1080 // 2))
    cv.imshow("preview", img)
    cv.setMouseCallback("preview", click_event)

    end_wait()

    cv.destroyAllWindows()


