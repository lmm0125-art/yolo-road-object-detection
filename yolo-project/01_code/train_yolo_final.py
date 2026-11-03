from pathlib import Path
import yaml
import shutil
import os
from ultralytics import YOLO

# 외부 Git 저장소를 직접 clone하여 사용하지 않았으며,
# Ultralytics YOLO 라이브러리를 pip install 방식으로 사용하였다.
# Pretrained weight: yolo11s.pt

DATA_YAML = "/content/datasets/combined_dawn_member_converted.yaml"

PROJECT_DIR = Path("/content/drive/MyDrive/yolo_runs")
RUN_NAME = "yolo11s_combined_30epochs_safe"

model = YOLO("yolo11s.pt")

results = model.train(
    data=DATA_YAML,
    epochs=30,
    imgsz=640,
    batch=16,
    optimizer="AdamW",
    device=0,
    workers=2,
    seed=42,
    patience=10,
    save=True,
    save_period=1,
    project=str(PROJECT_DIR),
    name=RUN_NAME,
    exist_ok=True
)