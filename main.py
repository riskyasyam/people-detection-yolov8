import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *

model = YOLO('yolov8s.pt')

area1 = [(int(156 * 2), int(194 * 2)), (int(144 * 2), int(195 * 2)), 
         (int(237 * 2), int(234 * 2)), (int(248 * 2), int(231 * 2))]
area2 = [(int(140 * 2), int(196 * 2)), (int(125 * 2), int(198 * 2)), 
         (int(211 * 2), int(238 * 2)), (int(227 * 2), int(234 * 2))]

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Atur lebar frame lebih besar
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Atur tinggi frame lebih besar

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")

count = 0

tracker = Tracker()

people_entering = {}
people_exiting = {}
entering = set()
exiting = set()

while True:    
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 2 != 0:
        continue
    frame = cv2.resize(frame, (650, 480))  # Sesuaikan resolusi dengan ESP32-CAM
    frame = cv2.flip(frame, 1) # Flip Video

    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    list = []

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        if 'person' in c:
            list.append([x1, y1, x2, y2])

    bbox_id = tracker.update(list)

    for bbox in bbox_id:
        x3, y3, x4, y4, id = bbox

        # Deteksi orang yang menyentuh area2
        results = cv2.pointPolygonTest(np.array(area2, np.int32), (x4, y4), False)
        if results >= 0:
            people_entering[id] = (x4, y4)
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)

        # Deteksi orang yang berpindah ke area1
        if id in people_entering:  
            results1 = cv2.pointPolygonTest(np.array(area1, np.int32), (x4, y4), False)
            if results1 >= 0:
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 0), 2)
                cv2.circle(frame, (x4, y4), 4, (255, 0, 255), -1)
                cv2.putText(frame, str(id), (x3, y3), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                entering.add(id)

        # Deteksi orang yang menyentuh area1
        results2 = cv2.pointPolygonTest(np.array(area1, np.int32), (x4, y4), False)
        if results2 >= 0:
            people_exiting[id] = (x4, y4)
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 0), 2)

        # Deteksi orang yang keluar dari area2
        if id in people_exiting:  
            results3 = cv2.pointPolygonTest(np.array(area2, np.int32), (x4, y4), False)
            if results3 >= 0:
                cv2.rectangle(frame, (x3, y3), (x4, y4), (255, 0, 255), 2)
                cv2.circle(frame, (x4, y4), 5, (255, 0, 255), -1)
                cv2.putText(frame, str(id), (x3, y3), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                exiting.add(id)

        # Deteksi orang yang tidak menyentuh area1 atau area2
        if results < 0 and results2 < 0:
            cv2.rectangle(frame, (x3, y3), (x4, y4), (128, 0, 128), 2)  # Warna ungu untuk deteksi

    # Gambarkan area poligon
    cv2.polylines(frame, [np.array(area1, np.int32)], True, (255, 0, 0), 2)
    cv2.putText(frame, str('1'), (504, 471), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    cv2.polylines(frame, [np.array(area2, np.int32)], True, (255, 0, 0), 2)
    cv2.putText(frame, str('2'), (466, 485), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

    # Tampilkan jumlah pengunjung
    i = len(entering)
    o = len(exiting)
    inside = i - o

    cv2.putText(frame, f"Pengunjung Masuk = {i}", (60, 80), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, f"Pengunjung Keluar = {o}", (60, 140), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 255), 2)
    cv2.putText(frame, f"Pengunjung di Dalam = {inside}", (60, 200), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
