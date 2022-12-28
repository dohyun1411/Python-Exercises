# Problem 2
## Problem 2-1
클래스를 이용하여 2차원 도형을 구현해보자.

아래 조건에 맞추어 `Point2D`, `Segment2D`, `Triangle2D` 클래스를 구현하여라.

* `Point2D`
    * `x`, `y` 좌표값을 저장
    * 두 점의 `x`와 `y` 값이 모두 같으면 그 두 점은 같다
* `Segment2D`
    * 두 개의 점을 저장
    * 만약, 주어진 두 개의 점이 하나의 선분을 구성할 수 없다면 에러 메시지를 출력
    * 선분의 길이와 기울기를 저장
    * 두 선분의 길이와 기울기가 같으면 그 두 선분은 같다
* `Triangle2D`
    * 세 개의 점을 저장
    * 만약, 주어진 세 개의 점이 하나의 삼각형을 구성할 수 없다면 에러 메시지를 출력
    * 삼각형의 둘레와 넓이를 저장
    * 두 삼각형이 합동이면 그 두 삼각형은 같다

### Example
다음과 같이 점을 선언해보자.
```python
p = Point2D(1, 1)
q = Point2D(2, 2)
r = Point2D(1, 1)
print(p.x, p.y)
print(p == q)
print(p == r)
```
Output:
```bash
1, 1
False
True
```
다음과 같이 선분을 선언해보자.
```python
s = Point2D(3, 3)
l = Segment2D(p, q)
m = Segment2D(q, s)
n = Segment2D(p, r)
print(l.p, l.q)
print(m.length, m.slope)
print(l == m)
```
Output:
```bash
Cannot create a segment with (1, 1) and (1, 1)
(1, 1), (2, 2)
1.414, 1
True
```
다음과 같이 삼각형을 선언해보자.
```python
t = Point2D(1, 2)
u = Point2D(3, 2)
a = Triangle2D(p, q, s)
b = Triangle2D(p, q, t)
c = Triangle2D(q, s, u)
print(b.p, b.q, b.r)
print(b.perimeter, b.area)
print(b == c)
```
Output:
```bash
Cannot craete a triangle with 
(1, 1), (2, 2), (1, 2)
3.414, 0.5
True
```

### Hint
* 삼각형의 넓이를 구하는 8가지 방법: https://miho273.tistory.com/28


## Problem 2-2
클래스를 이용하여 N차원 도형을 구현해보자.

아래 조건에 맞추어 `Point`, `Segment`, `Triangle` 클래스를 구현하여라.

* `Point`
    * 점의 차원(N)을 저장 (단, 차원을 명시적으로 입력받지 말 것)
    * 두 점의 N개의 좌표값들이 모두 같다면 그 두 점은 같다
* `Segment`
    * 만약, 주어진 두 개의 점이 하나의 선분을 구성할 수 없다면 에러 메시지를 출력
    * 만약, 주어진 두 개의 점의 차원이 다르다면 에러 메시지를 출력
    * 선분의 길이를 저장
    * 두 선분의 길이와 기울기가 같으면 그 두 선분은 같다
* `Triangle`
    * 만약, 주어진 세 개의 점이 하나의 삼각형을 구성할 수 없다면 에러 메시지를 출력
    * 만약, 주어진 세 개의 점의 차원이 하나라도 다르다면 에러 메시지를 출력
    * 삼각형의 둘레를 저장
    * 두 삼각형이 합동이면 그 두 삼각형은 같다

### Example
다음과 같이 점을 선언해보자.
```python
p = Point(1, 2, 3, 4, 5)
print(p.dim)
```
Output:
```bash
5
False
```
다음과 같이 선분을 선언해보자.
```python
q = Point(1, 0, 0)
r = Point(0, 1, 0)
s = Point(2, -1, 0)
l = Segment(p, q)
m = Segment(q, r)
n = Segment(q, s)
print(m.length)
print(m == n)
```
Output:
```bash
Cannot create a segment with (1, 2, 3, 4, 5) and (1, 0, 0)
1.414
True
```
다음과 같이 삼각형을 선언해보자
```python
t = Point(2, 1, 0)
a = Triangle(q, r, t)
b = Triangle(q, s, t)
c = Triangle(p, q, r)
print(a == b)
```
Output:
```bash
Cannot create a triangle with (1, 2, 3, 4, 5), (1, 0, 0) and (0, 1, 0)
True
```

### Hint
* N차원 선분의 기울기는 직접 구할 수는 없지만 각 좌표값의 차이의 비율을 비교하여 알 수 있다.
