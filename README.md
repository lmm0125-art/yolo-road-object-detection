# YOLO 기반 도로 객체 탐지 프로젝트

YOLO 기반 도로 객체 탐지 모델 학습 및 평가 — 텐서프로그래밍 2026-1 기말 프로젝트, TGroup.

## Model

YOLO11s pretrained model을 사용하여 학습하였다.

## Dataset

본 프로젝트에서는 DAWN 데이터셋과 조원 데이터셋을 사용하였다.
두 데이터셋의 클래스 구성이 달라서 조원 데이터셋의 클래스를 DAWN 기준으로 변환하였다.

## Final Training Setting

| | |
|---|---|
| Model | YOLO11s |
| Epochs | 30 |
| Image size | 640 |
| Batch size | 16 |
| Optimizer | AdamW |
| Device | GPU |

## Final Result

| Precision | Recall | mAP50 | mAP50-95 |
|---|---|---|---|
| 0.603 | 0.356 | 0.373 | 0.215 |

## External Git Usage

외부 Git 저장소를 직접 clone하여 사용하지 않았으며, Ultralytics YOLO 라이브러리를 pip install 방식으로 사용하였다.

---

## What is in this repository

```
01_code/train_yolo_final.py        training entry point
02_dataset/class_mapping.md        how the teammate dataset classes were remapped
02_dataset/combined_dawn_member_converted.yaml   merged dataset definition
04_results/                        confusion matrices, training curves, prediction examples
TGroup_YOLO_Final_Project.ipynb    the submitted notebook, with outputs
```

Run it with:

```bash
pip install ultralytics
python 01_code/train_yolo_final.py
```

## What is not in this repository

| excluded | why |
|---|---|
| `Lec1–Lec9.pdf`, `HW*.pdf` | course material, not mine to republish |
| presentation PDF and script | presentation material |
| `02_dataset/*.zip` (802 MB) | DAWN and BDD100K subsets, available from their original sources |
| `03_model/*.pt` (37 MB) | trained weights, reproducible from `01_code/train_yolo_final.py` |

## Team

TGroup — 종열, 손첸디, 이멍멍, 유천일, 후예항.
