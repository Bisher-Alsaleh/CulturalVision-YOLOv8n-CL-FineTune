import argparse
from ultralytics import YOLO

def main(args):
    model = YOLO(args.weights)
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        optimizer='AdamW',
        lr0=0.001,
        lrf=0.01,
        weight_decay=0.01,
        augment=True,
        dropout=0.1,
        cos_lr=True,
        warmup_epochs=2,
        device=0,
        workers=4,
        seed=42,
        pretrained=True,
        val=True,
        plots=True,
        save_dir=args.save_dir,
        exist_ok=True,
        save_period=2
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", default="yolov8n-cls.pt")
    parser.add_argument("--data", default="data/dataset.yaml")
    parser.add_argument("--epochs", type=int, default=24)
    parser.add_argument("--imgsz", type=int, default=224)
    parser.add_argument("--batch", type=int, default=32)
    parser.add_argument("--save_dir", default="results/train")
    args = parser.parse_args()
    main(args)
