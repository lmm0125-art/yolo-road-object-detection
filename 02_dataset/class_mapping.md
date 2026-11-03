# Class Mapping

본 프로젝트에서는 DAWN 데이터셋과 조원 데이터셋을 함께 사용하였다.
두 데이터셋의 클래스 구성이 서로 달라서 조원 데이터셋의 클래스를 DAWN 기준으로 변환하였다.

## DAWN classes
bicycle, bus, car, motorcycle, person, train, truck

## Member dataset original classes
bike, bus, car, motor, person, rider, traffic light, traffic sign, train, truck

## Mapping rule
bike -> bicycle
motor -> motorcycle
bus -> bus
car -> car
person -> person
rider -> person
train -> train
truck -> truck

traffic light와 traffic sign은 DAWN 데이터셋에 없는 클래스이므로 학습 대상에서 제외하였다.