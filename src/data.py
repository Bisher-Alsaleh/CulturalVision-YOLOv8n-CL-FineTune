import os
import shutil
import pandas as pd
import numpy as np
import random
from pathlib import Path
from sklearn.model_selection import train_test_split
import yaml

# Reproducibility
np.random.seed(42)
random.seed(42)

def prepare_dataset(csv_path, train_folder, dataset_root, num_classes=10, samples_per_class=900):
    mapping_df = pd.read_csv(csv_path)
    counts = mapping_df.landmark_id.value_counts()
    top_ids = counts.head(num_classes).index.tolist()

    # Sample images
    sampled_dfs = []
    for landmark_id in top_ids:
        class_images = mapping_df[mapping_df['landmark_id'] == landmark_id]
        n_samples = min(samples_per_class, len(class_images))
        sampled_dfs.append(class_images.sample(n=n_samples, random_state=42))
    top_df = pd.concat(sampled_dfs, ignore_index=True)

    # Collect paths
    found_paths, _ = find_image_files(top_df['id'].tolist(), train_folder)

    # Build DataFrame
    image_data = []
    for path in found_paths:
        image_name = Path(path).stem
        row = top_df[top_df['id'] == image_name]
        if not row.empty:
            image_data.append({
                'image_path': path,
                'landmark_id': row['landmark_id'].iloc[0]
            })
    df = pd.DataFrame(image_data)

    # Train/val split
    train_df, val_df = train_test_split(df, test_size=0.2, stratify=df['landmark_id'], random_state=42)
    _save_split(train_df, os.path.join(dataset_root, "train"))
    _save_split(val_df, os.path.join(dataset_root, "val"))

    # Dataset YAML
    yaml_content = {
        'path': dataset_root,
        'train': 'train',
        'val': 'val',
        'nc': len(df.landmark_id.unique()),
        'names': {i: str(cid) for i, cid in enumerate(sorted(df.landmark_id.unique()))}
    }
    yaml_path = os.path.join(dataset_root, "dataset.yaml")
    with open(yaml_path, 'w') as f:
        yaml.dump(yaml_content, f)

    return train_df, val_df, yaml_path

def find_image_files(image_names, train_folder_path):
    found, missing = [], []
    for name in image_names:
        folder_path = os.path.join(train_folder_path, name[0], name[1], name[2])
        file_path = os.path.join(folder_path, f"{name}.jpg")
        if os.path.exists(file_path):
            found.append(file_path)
        else:
            missing.append(name)
    return found, missing

def _save_split(df, split_dir):
    for class_id in df['landmark_id'].unique():
        os.makedirs(os.path.join(split_dir, str(class_id)), exist_ok=True)
    for _, row in df.iterrows():
        dest = os.path.join(split_dir, str(row['landmark_id']), os.path.basename(row['image_path']))
        shutil.copy2(row['image_path'], dest)
