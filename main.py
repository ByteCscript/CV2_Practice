import cv2
import mediapipe as mp

def main():
    # Inicialización de MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    )
    mp_drawing = mp.solutions.drawing_utils  # Para dibujar landmarks

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No pude abrir la cámara 😢")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Volteamos horizontalmente para que el espejo sea más intuitivo
        frame = cv2.flip(frame, 1)

        # Convertir BGR a RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # Si se detectan manos, dibuja landmarks y conexiones
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Dibuja los puntos y las líneas entre ellos
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(255,0,0), thickness=2)
                )

        # Mostrar el frame resultante
        cv2.imshow("Detección de Manos", frame)

        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos
    hands.close()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
