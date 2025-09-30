import pandas as pd
from pathlib import Path
from ultralytics import YOLO

def run_inference(weights, test_dir, out_csv="results/test_predictions.csv", n_samples=1000):
    test_image_paths = [str(p) for p in Path(test_dir).rglob("*.jpg")]
    model = YOLO(weights)
    results = model.predict(source=test_image_paths[:n_samples], imgsz=224, batch=32, device=0)

    predictions = []
    for r in results:
        predictions.append({
            'image_path': r.path,
            'predicted_class': int(r.probs.top1),
            'confidence': float(r.probs.top1conf)
        })
    df = pd.DataFrame(predictions)
    df.to_csv(out_csv, index=False)
    return df
