import cv2
import os
from matplotlib import pyplot as plt

async def analyzeVideo(file):
    contents = await file.read()

    cap = cv2.VideoCapture()
    if not cap.isOpened():
        print("file is not opened")
        return

    rpm = 0
    speedMPH = 0
    distanceYards = 0

    return {
        "rpm" : rpm,
        "speed" : speedMPH,
        "distance" : distanceYards
    }