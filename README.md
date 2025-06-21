# 🐾 Cat Activity Detector

Projet de détection d'activités de chats via caméra USB + IA locale.

## 🎯 Objectif

Capturer des images des chats pour entraîner un modèle IA (via [Teachable Machine](https://teachablemachine.withgoogle.com/)), puis détecter automatiquement leurs activités à l’aide d’un script Python et OpenCV.

## 📂 Structure du projet

cat-activity-detector/
├── cat_dataset/ # Images classées par activité
├── scripts/ # Scripts Python
│ └── cat_activity_capture.py
├── venv/ # Environnement virtuel Python (non versionné)
├── .gitignore
└── README.md


## 🧪 Installation (via environnement virtuel)

```
sudo apt update
sudo apt install python3-full python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip install opencv-python
```

##▶️ Utilisation
python scripts/cat_activity_capture.py
Appuie sur espace pour capturer une image, q pour quitter.

##🧠 Classes à capturer pour l’IA
vide : aucun chat

dort : chat allongé

mange_ou_bois : chat mangeant ou buvant

interaction : 2 chats en interaction

litiere : chat à la litière

passe : chat passant devant la caméra
