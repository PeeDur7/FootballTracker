from ultralytics import YOLO

def yoloModel():
    yolo = YOLO("yolov8m.pt")
    return yolo

def detectFootball(model, frame):
    results = model(frame, conf=0.60)
    result = results[0]
    return result

def getFootballRegion(result):
    if result.boxes is None or len(result.boxes) == 0:
        return
    boxes = result.boxes

    bestId = boxes.conf.argmax()
    bbox = boxes.xyxy[bestId].cpu().numpy()
    confidence = float(boxes.conf[bestId])

    x1,y1,x2,y2 = bbox
    center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
    
    return {
        'bbox': bbox,
        'center': center,
        'confidence': confidence
    }
