import av
import cv2
import dlib
import numpy as np


class VideoProcessor:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
        self.margin = 5

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        ret, pupil_coords = self.__detect_eyes(img)

        if ret is False:
            return frame

        for coord in pupil_coords:
            if coord is None:
                continue
            cv2.drawMarker(img, coord, (0, 0, 255), cv2.MARKER_CROSS, markerSize=10, thickness=2)
        return av.VideoFrame.from_ndarray(img, format="bgr24")

    def on_ended(self):
        pass

    def __detect_eyes(self, img):
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.detector(img_g)
        if len(faces) == 0:
            return False, None

        for face in faces:
            landmarks = self.predictor(img_g, face)

        # 右目：[36, 37, 39, 40] 左目：[42, 43, 45, 46]
        eyes_idx = [[36, 37, 39, 40], [42, 43, 45, 46]]
        pupil_coords = []
        for idx in eyes_idx:
            ref_point, eye_img = self.__get_eye_img(img, landmarks, idx)
            coord = self.__get_pupil_coord(ref_point, eye_img)
            pupil_coords.append(coord)
        return True, pupil_coords

    def __get_eye_img(self, img, landmarks, idx):
        xmin = landmarks.part(idx[0]).x
        ymin = landmarks.part(idx[1]).y
        xmax = landmarks.part(idx[2]).x
        ymax = landmarks.part(idx[3]).y
        return (xmin, ymin), img[ymin - self.margin:ymax + self.margin, xmin:xmax]

    def __get_pupil_coord(self, ref_point, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        Hl, Sl, Vl = 0, 0, 11
        Hu, Su, Vu = 179, 255, 77
        lower = np.array([Hl, Sl, Vl])
        upper = np.array([Hu, Su, Vu])
        mask = cv2.inRange(hsv, lower, upper)
        cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) == 0:
            return None
        cnt = max(cnts, key=lambda x: cv2.contourArea(x))

        x, y, w, h = cv2.boundingRect(cnt)
        x, y, w, h = x + ref_point[0], y + ref_point[1], w, h
        return (int(x + w / 2), int(y + h / 2))
