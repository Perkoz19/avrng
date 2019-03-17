import cv2
import os


class VideoHandler:
    def __init__(self):
        pass

    def get_frame(self):
        cap = cv2.VideoCapture(0)
        count = 0
        path = 'C:/users/wasik/Desktop/obrazki'  # sciezka do wpisania gdzie maja byc obrazki zapisane

        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)
            cv2.imwrite(os.path.join(path, "frame%d.jpg" % count), frame)
            count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

