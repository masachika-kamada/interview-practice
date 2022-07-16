import av
import cv2
import dlib
import numpy as np
import json


class VideoProcessor:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
        self.margin = 5
        self.thresh_diff_eyes_hor = 0.2
        self.eye_center = 0
        self.eye_left = 0
        self.eye_right = 0

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        ret, pupil_coords, eye_tracks = self.__detect_eyes(img)

        if ret is False:
            return frame

        for coord in pupil_coords:
            if coord is None:
                continue
            cv2.drawMarker(img, coord, (0, 0, 255), cv2.MARKER_CROSS, markerSize=10, thickness=2)
        eye_hor_l = 1 - eye_tracks[0][0]
        eye_hor_r = eye_tracks[1][0]
        diff_eyes_hor = eye_hor_l - eye_hor_r
        if abs(diff_eyes_hor) < self.thresh_diff_eyes_hor:
            cv2.putText(img, "Center", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            self.eye_center += 1
        elif diff_eyes_hor < 0:
            cv2.putText(img, "Left", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            self.eye_left += 1
        else:
            cv2.putText(img, "Right", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            self.eye_right += 1
        return av.VideoFrame.from_ndarray(img, format="bgr24")

    def on_ended(self):
        n_frames = self.eye_center + self.eye_left + self.eye_right
        d = {
            "eye_center_ratio": self.eye_center / n_frames,
            "eye_left_ratio": self.eye_left / n_frames,
            "eye_right_ratio": self.eye_right / n_frames
        }
        with open('results/eye_track.json', 'w') as f:
            json.dump(d, f)

    def __detect_eyes(self, img):
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.detector(img_g)
        if len(faces) == 0:
            return False, None, None

        for face in faces:
            landmarks = self.predictor(img_g, face)

        # 右目：[36, 37, 39, 40] 左目：[42, 43, 45, 46]
        eyes_idx = [[36, 37, 39, 40], [42, 43, 45, 46]]
        pupil_coords = []
        eye_track = []
        for idx in eyes_idx:
            ref_point, eye_img, w, h = self.__get_eye_img(img, landmarks, idx)
            cx, cy = self.__get_pupil_coord(eye_img)
            pupil_coords.append((int(cx + ref_point[0]), int(cy + ref_point[1])))
            eye_track.append((cx / w, cy / h))
        return True, pupil_coords, eye_track

    def __get_eye_img(self, img, landmarks, idx):
        xmin = landmarks.part(idx[0]).x
        ymin = landmarks.part(idx[1]).y - self.margin
        xmax = landmarks.part(idx[2]).x
        ymax = landmarks.part(idx[3]).y + self.margin
        return (xmin, ymin), img[ymin:ymax, xmin:xmax], xmax - xmin, ymax - ymin

    def __get_pupil_coord(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        Hl, Sl, Vl = 0, 0, 11
        Hu, Su, Vu = 179, 255, 77
        lower = np.array([Hl, Sl, Vl])
        upper = np.array([Hu, Su, Vu])
        mask = cv2.inRange(hsv, lower, upper)
        try:
            cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        except Exception as e:
            print(e)
            return None, None
        if len(cnts) == 0:
            return None, None
        cnt = max(cnts, key=lambda x: cv2.contourArea(x))

        x, y, w, h = cv2.boundingRect(cnt)
        return int(x + w / 2), int(y + h / 2)
