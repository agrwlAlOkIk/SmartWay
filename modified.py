import cv2
from ultralytics import YOLO

# Loading the YOLOv8 model
model = YOLO("yolov8n.pt")

# Defining vehicle-related class names
vehicle_classes = [2, 3, 5, 7]  # class IDs for 'car', 'motorcycle', 'bus', 'truck'

# Running the model on the input image
image_path = "images/traffic1.jpg"
detection_output = model.predict(source=image_path, conf=0.25, save=False)

# Loading the input image using OpenCV
image = cv2.imread(image_path)

vehicle_count = 0

if len(detection_output) > 0:
    for result in detection_output:
        # Get the bounding boxes, class IDs, and confidence scores
        boxes = result.boxes.xyxy
        detected_classes = result.boxes.cls
        confidence_scores = result.boxes.conf
        
        # Iterating over each detected object
        for box, cls, conf in zip(boxes, detected_classes, confidence_scores):
            if int(cls) in vehicle_classes:
                vehicle_count += 1
                
                x1, y1, x2, y2 = map(int, box)
                
                # Draws the bounding box on the image using opencv
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

                label = f"Vehicle {int(conf * 100)}%"
                cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


def get_traffic_density_score(vehicle_count):

    # Defined thresholds for density
    if vehicle_count < 5:
        return 1
    elif 5 <= vehicle_count < 10:
        return 2
    elif 10 <= vehicle_count < 15:
        return 3
    elif 15 <= vehicle_count < 20:
        return 4
    elif 20 <= vehicle_count < 25:
        return 5
    elif 25 <= vehicle_count < 30:
        return 6
    elif 30 <= vehicle_count < 35:
        return 7
    elif 35 <= vehicle_count < 40:
        return 8
    elif 40 <= vehicle_count < 45:
        return 9
    else:
        return 10


traffic_density_score = 0
traffic_density_score = get_traffic_density_score(vehicle_count)

# Outputs the number of vehicles
print(f" \nNumber of vehicles detected: {vehicle_count} \n")

# Outputs the weight of traffic based on the number of vehicles
print(f"Weight according to vehicle count: {traffic_density_score} \n")

# Outputs the image with bounding boxes in a window
cv2.imshow("Detected Vehicles", image)

# Saves the output image with bounding boxes
output_image_path = "output_detected_vehicles.jpg"
cv2.imwrite(output_image_path, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
