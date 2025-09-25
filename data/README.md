# Dataset Information

This directory contains information about the datasets used in **CulturalVision-YOLOv8n-CL-FineTune**.

---

## 1️⃣ Full Google Landmarks Dataset v2

The full dataset is used as the source for training and evaluation:

- **Official Dataset (Kaggle):**  
  [Google Landmarks Dataset v2](https://www.kaggle.com/competitions/landmark-recognition-2020/data)  

> ⚠️ Note: The full dataset is large and is **not included in this repository**. Users must download it directly from Kaggle.

---

## 2️⃣ Curated Dataset & Fine-Tuned Model

For ease of experimentation, a **Top-10 landmark subset** is provided:

- **Prepared Dataset & Weights:**  
  [Kaggle Dataset → yolo-landmark-finetuned](https://www.kaggle.com/datasets/bisheralsaleh/yolo-landmark-finetuned)  

- **Demo Notebook:**  
  [Fine-tune YOLOv8 on Google Landmark Dataset](https://www.kaggle.com/code/bisheralsaleh/fine-tune-yolov8-on-google-landmark-dataset)  

This subset contains ~9,000 images across 10 landmark classes and the **pretrained/fine-tuned YOLOv8n-CL model weights** (`best.pt`).

---

## 3️⃣ Dataset Usage

1. **Download the prepared dataset** from Kaggle and place it in the `data/` directory:
```bash
data/
├── train/
├── val/
└── dataset.yaml
```
