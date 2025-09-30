from ultralytics import YOLO

def evaluate(weights, data_yaml):
    model = YOLO(weights)
    return model.val(data=data_yaml)

if __name__ == "__main__":
    metrics = evaluate("models/best.pt", "data/dataset.yaml")
    print(metrics)
