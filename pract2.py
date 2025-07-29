import cv2
from ultralytics import YOLO

def main():
    # Carga el modelo YOLOv8 nano pretrained en COCO
    model = YOLO("yolov8n.pt")

    # Inicializa la cámara
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("No pude abrir la cámara 😢")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Infiere sobre el frame
        results = model(frame, verbose=False)[0]

        # Recorre cajas detectadas
        mug_detected = False
        for box, cls in zip(results.boxes.xyxy.tolist(), results.boxes.cls.tolist()):
            label = model.names[int(cls)]
            if label == "cup":   # en COCO la clase “cup”
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)
                cv2.putText(frame, "Mug", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
                mug_detected = True

        # Mensaje arriba
        if mug_detected:
            cv2.putText(frame, "¡Posillo DETECTADO!", (50,50),
                        cv2.FONT_HERSHEY_DUPLEX, 1.2, (0,255,0), 3)

        # Muestra
        cv2.imshow("Detección de posillo", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
