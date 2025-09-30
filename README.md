<div align="center">
  
# YOLOv8n-CL fine-tuned on Google Landmarks (10 classes)
Fine-tuning YOLOv8n-CL on 10 classes from the Google Landmarks Dataset to create a lightweight landmark recognition model supporting cultural heritage preservation.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue?style=plastic)](https://opensource.org/licenses/Apache-2.0)
[![](https://img.shields.io/badge/Kaggle-Notebook-%2320BEFF?style=plastic&logo=kaggle)](https://www.kaggle.com/code/bisheralsaleh/fine-tune-yolov8-on-google-landmark-dataset)
![](https://img.shields.io/badge/v3.11-green?style=plastic&logo=python&label=Python3&labelColor=black&color=green)
<img width="888" height="888" alt="Discretized Path Tracking" src="https://github.com/user-attachments/assets/1ae3e131-c2f7-4428-83f6-b8d7f95f7c5b" />
</div>

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

✅ Top-5 Accuracy: 0.998

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
## 🙏 Acknowledgments

I would like to express my sincere gratitude to the following projects and datasets that made this work possible:

- 🔹 YOLOv8: This project uses **[YOLOv8](https://github.com/ultralytics/ultralytics)** (Ultralytics) as the base classification model.  
YOLOv8 provides a state-of-the-art classification framework, which has enabled rapid experimentation and fine-tuning on the landmark dataset.

- 🔹 Google Landmarks Dataset v2: The dataset used in this project is based on the **[Google Landmarks Dataset v2](https://www.kaggle.com/competitions/landmark-recognition-2020/data)**.  
I acknowledge Google and Kaggle for providing this dataset to facilitate research in landmark recognition and cultural heritage preservation.
- 🔹 Kaggle: I acknowledge **[Kaggle](https://www.kaggle.com/)** for providing the GPU-enabled environment, which was crucial for training and fine-tuning the YOLOv8n-CL model efficiently on the landmark dataset.
