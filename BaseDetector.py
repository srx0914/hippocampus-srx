import cv2

from tracker import update_tracker


class baseDet(object):
    def __init__(self):
        self.img_size = 640
        self.threshold = 0.3
        self.stride = 1

    def build_config(self):
        self.faceTracker = {}
        self.faceClasses = {}
        self.faceLocation1 = {}
        self.faceLocation2 = {}
        self.frameCounter = 0
        self.currentCarID = 0
        self.recorded = []

        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def feedCap(self, im):
        retDict = {"frame": None, "faces": None, "list_of_ids": None, "face_bboxes": []}
        self.frameCounter += 1

        im, faces, face_bboxes, bboxes2draw = update_tracker(self, im)

        retDict["frame"] = im
        retDict["faces"] = faces
        retDict["face_bboxes"] = face_bboxes
        retDict["bboxes2draw"] = bboxes2draw

        return retDict

    def init_model(self):
        raise EOFError("Undefined model type.")

    def preprocess(self):
        raise EOFError("Undefined model type.")

    def detect(self):
        raise EOFError("Undefined model type.")
