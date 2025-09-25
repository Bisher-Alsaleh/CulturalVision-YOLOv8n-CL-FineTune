<div align="center">
  
# YOLOv8n-CL fine-tuned on Google Landmarks (10 classes)
Fine-tuning YOLOv8n-CL on 10 classes from the Google Landmarks Dataset to create a lightweight landmark recognition model supporting cultural heritage preservation.

<img width="888" height="888" alt="Discretized Path Tracking" src="https://github.com/user-attachments/assets/1ae3e131-c2f7-4428-83f6-b8d7f95f7c5b" />
</div>

## 📦 Datasets & Weights

### 1. Full Google Landmarks Dataset v2

- **Official Dataset:**  
  [Google Landmarks Dataset v2 on Kaggle](https://www.kaggle.com/competitions/landmark-recognition-2020/data)  
  This dataset contains over 5 million images spanning 200,000 landmark classes. It is used in this repo.

### 2. Prepared Dataset & Fine-Tuned Weights

- **Kaggle Dataset:**  
  [yolo-landmark-finetuned](https://www.kaggle.com/datasets/bisheralsaleh/yolo-landmark-finetuned)  
  This repository contains a curated subset of the Google Landmarks Dataset v2, focusing on the top 10 landmark classes, along with the fine-tuned YOLOv8n-CL model weights.

- **Demo Notebook:**  
  [Fine-tune YOLOv8 on Google Landmark Dataset](https://www.kaggle.com/code/bisheralsaleh/fine-tune-yolov8-on-google-landmark-dataset)  
  This notebook demonstrates the process of dataset preparation, model training, and evaluation.

⚠️ **Note:** Large assets (dataset & `.pt` weights) are not included in this repository. Please download them from Kaggle.

---

## 📦 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Bisher-Alsaleh/CulturalVision-YOLOv8n-CL-FineTune.git
cd CulturalVision-YOLOv8n-CL-FineTune
pip install -r requirements.txt
```
## 📁 Repository Structure
```bash
CulturalVision-YOLOv8n-CL-FineTune/
├─ README.md
├─ LICENSE.md
├─ requirements.md
├─ data/
│  ├─ README.md
│  └─ dataset.yaml
├─ configs/
│  └─ yolov8n_cl_gld10.yaml
├─ src/
│  ├─ data.md
│  ├─ model.md
│  ├─ train.md
│  ├─ eval.md
│  └─ infer.md
├─ scripts/
│  ├─ train.md
│  └─ eval.md
├─ results/
│  └─ README.md
```
## 🚀 Usage
### 1️⃣ Dataset Preparation
`python src/data.py` Or download the prepared dataset and weights from Kaggle
### 2️⃣ Training
```bash
python src/train.py --data data/dataset.yaml --epochs 24 --imgsz 224 --batch 32
```
### 3️⃣ Evaluation
```bash
python src/eval.py --weights models/best.pt --data data/dataset.yaml
```
### 4️⃣ Inference
```bash
python src/infer.py --weights models/best.pt --test_dir /path/to/test/images
```
## 📊 Results

**Model**: YOLOv8n-CL (classification)

**Dataset**: Google Landmarks v2, Top-10 classes (~9k images)

**Performance**:

✅ Top-1 Accuracy: 0.979

✅ Top-5 Accuracy:0.998

Training logs and plots are available in results/.

## 📜 Citation
```
@misc{CulturalVisionYOLOv8n2025,
  title   = {CulturalVision-YOLOv8n-CL-FineTune: Fine-tuned YOLOv8n-CL for Cultural Heritage Landmark Recognition},
  author  = {Bisher Alsaleh},
  year    = {2025},
  url     = {https://github.com/Bisher-Alsaleh/CulturalVision-YOLOv8n-CL-FineTune}
}
```
