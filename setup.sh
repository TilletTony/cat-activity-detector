#!/bin/bash

echo "[🛠️  SETUP] Initialisation du projet Cat Activity Detector"

sudo apt update
sudo apt install python3-full python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip install opencv-python

echo "[✅] Environnement prêt. Tu peux lancer :"
echo "source venv/bin/activate && python scripts/cat_activity_capture.py"
