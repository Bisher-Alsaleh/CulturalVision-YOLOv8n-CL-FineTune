# Results — Fine-tuning `yolov8n-cls` on 10 Landmark Classes

## 📌 Summary

I fine-tuned the **YOLOv8n classification model** (`yolov8n-cls.pt`) on **10 landmark classes** from the Google Landmark dataset. The training achieved excellent results with **fast convergence** and **very high accuracy**:

* **Top-1 Accuracy:** ~97.8%
* **Top-5 Accuracy:** ~99.9%
* **Per-class Recall:** mostly above **96–99%**

This demonstrates that even the lightweight YOLOv8n backbone is highly effective for small-scale landmark classification when transfer learning is applied.

---

## 📈 Learning Curves
<div align="center">
<img width="600" height="600" alt="results" src="https://github.com/user-attachments/assets/fca29ed8-86c0-4295-9cad-bae5e82dc544" />
</div>
* **Loss:** Rapid decrease within first few epochs → strong transfer learning effect.
* **Accuracy:** Steady improvement until convergence, no overfitting observed.
* **Validation vs Training:** Curves remain tightly aligned → stable training.

---

## 🔍 Confusion Matrices

**Normalized (%):**

<img width="1500" height="1125" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/150d12bd-e158-4f4d-8eda-66e61723ea69" />

* Strong **diagonal dominance** → correct predictions dominate.
* Off-diagonal values mostly within **1–3%** → low confusion.
* Misclassifications rare and evenly distributed.

---

## 🏷️ Predicted Classes

The model outputs predictions mapped to **Google Landmark dataset IDs**. For each image, the final prediction corresponds to the most likely landmark ID from the dataset.

**Training details:**

* Training images were augmented with **scaling, rotation, translation, masking with black patches, etc.**
* These augmentations improved robustness and generalization.

📌 *Example training image with augmentation:*
<div align="center">
<img width="600" height="600" alt="results" src="https://github.com/user-attachments/assets/0af047c0-e720-407f-9f9f-1a431f7ffa43" />
</div>
**Evaluation details:**

* On the validation dataset, **no augmentation** was applied.
* This ensures that results reflect true generalization ability.

📌 *Example validation image prediction:*
<div align="center">
<img width="600" height="600" alt="results" src="https://github.com/user-attachments/assets/687f8912-c4fd-401c-84da-2239447f4e36" />
</div>
**Example mapping of classes (subset of 10):**

* `138982` → Landmark A
* `126637` → Landmark B
* `20409` → Landmark C
* `83144` → Landmark D
* `113209` → Landmark E
* ... (remaining IDs from the 10-class subset)

Thus, each test image is assigned the **predicted class ID** (from Google Landmark dataset) and evaluated against its ground-truth ID.

---

## ✅ Reasons for Success

1. **Pretrained features:** ImageNet-pretrained YOLOv8 backbone provided strong generalization.
2. **Balanced dataset:** Similar number of images per class avoided imbalance issues.
3. **Small label space:** 10 classes → high separability.
4. **Effective hyperparameters:** AdamW + cosine decay stabilized convergence.
