import cv2
import os
from datetime import datetime

output_dir = "cat_dataset"
classes = ["vide", "dort", "mange_ou_bois", "interaction", "litiere", "passe"]
cam_index = 0

print("[INFO] Initialisation de la caméra...")
cap = cv2.VideoCapture(cam_index)

if not cap.isOpened():
    raise Exception("La caméra ne peut pas être ouverte.")

print("Classes disponibles :", ", ".join(classes))
current_class = input("Entrez la classe à capturer (ex: dort) : ").strip().lower()

if current_class not in classes:
    raise ValueError("Classe inconnue.")

class_dir = os.path.join(output_dir, current_class)
os.makedirs(class_dir, exist_ok=True)

print(f"[INFO] Capture pour : {current_class}")
print("Appuie sur 'espace' pour capturer une image, 'q' pour quitter.")

counter = len(os.listdir(class_dir))

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERREUR] Échec de lecture caméra.")
        break

    cv2.imshow("Capture", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord(' '):
        filename = os.path.join(
            class_dir, f"{current_class}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{counter}.jpg"
        )
        cv2.imwrite(filename, frame)
        print(f"[OK] Image : {filename}")
        counter += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
