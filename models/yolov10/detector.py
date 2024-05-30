import cv2
from ultralytics import YOLOv10

def inference(image_path, weight_path):
    model = YOLOv10(weight_path)
    result = model(source=image_path,
                   verbose=False)[0]
    result_img = result.plot()
    result_img = cv2.cvtColor(result_img, 
                              cv2.COLOR_BGR2RGB)

    return result_img