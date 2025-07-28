import cv2

def main():
    cap = cv2.VideoCapture(0)  # 0 es el índice de la cámara por defecto
    if not cap.isOpened():
        print("No pude abrir la cámara 😢")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Mi Cámara 📷", frame)
        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
