# YOLO Road Object Detection Final Project

## Project Topic
YOLO 기반 도로 객체 탐지 모델 학습 및 평가

## Model
YOLO11s pretrained model을 사용하여 학습하였다.

## Dataset
본 프로젝트에서는 DAWN 데이터셋과 조원 데이터셋을 사용하였다.
두 데이터셋의 클래스 구성이 달라서 조원 데이터셋의 클래스를 DAWN 기준으로 변환하였다.

## Final Training Setting
- Model: YOLO11s
- Epochs: 30
- Image size: 640
- Batch size: 16
- Optimizer: AdamW
- Device: GPU

## Final Result
- Precision: 0.603
- Recall: 0.356
- mAP50: 0.373
- mAP50-95: 0.215

## External Git Usage
외부 Git 저장소를 직접 clone하여 사용하지 않았으며, Ultralytics YOLO 라이브러리를 pip install 방식으로 사용하였다.

## Submitted Files
- code
- dataset
- trained model weights
- training result images
- prediction examples