# Tensor Programming — coursework

Coursework for **텐서프로그래밍 (Tensor Programming)**, 2026-1학기, Hanyang
University ERICA. Assignments and the final group project.

| folder | contents |
|---|---|
| [`homework/`](homework/) | HW1–HW5 notebooks (PyTorch / tensor basics) |
| [`yolo-project/`](yolo-project/) | final project: YOLO-based road object detection (team TGroup) |

## yolo-project

Object detection on road scenes, trained with Ultralytics YOLO11s on a
combination of the DAWN dataset and a teammate's dataset (class names remapped
to the DAWN taxonomy).

| metric | value |
|---|---|
| precision | 0.603 |
| recall | 0.356 |
| mAP50 | 0.373 |
| mAP50-95 | 0.215 |

```
yolo-project/
├── 01_code/train_yolo_final.py        training entry point
├── 02_dataset/                        class mapping and the merged data.yaml
├── 04_results/                        confusion matrices, PR curves, prediction examples
└── TGroup_YOLO_Final_Project.ipynb    the submitted notebook, outputs included
```

Training was run with YOLO11s, 30 epochs, image size 640, batch 16, AdamW, on a
GPU. The dataset zips (~800 MB) and the trained weights (`best.pt`, `last.pt`,
37 MB) are **not** in this repository: the datasets are third-party and the
weights can be regenerated with `01_code/train_yolo_final.py`.

## What is not in this repository

| excluded | why |
|---|---|
| `Lec1–Lec9.pdf` | lecture slides, course material, not mine to republish |
| `HW1–HW5.pdf` | assignment sheets, same reason |
| presentation PDF / `.docx` script | presentation material |
| `02_dataset/*.zip` | DAWN and BDD100K subsets, 800 MB, downloadable from the original sources |
| `03_model/*.pt` | trained weights, reproducible from the training script |

## Team

Final project by TGroup — 종열, 손첸디, 이멍멍, 유천일, 후예항.
