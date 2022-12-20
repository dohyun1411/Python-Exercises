# Assignment

## Problem 1
클래스를 이용하여 도서 관리 시스템을 만들어보자.

아래 조건에 맞추어 `Library`, `Book`, `User` 클래스를 구현하여라.
* `Library`
    * attributes
        * `name`: 도서관명
        * `book_list`: 도서 목록
    * methods:
        * `add_book`: 도서 추가
        * `remove_book`: 도서 제거
        * `info`: 도서 목록을 보기좋게 출력 (아래 예시 참고)
* `Book`
    * attributes
        * `title`: 제목
        * `location`: 현재 자신이 어떤 library 또는 user에게 있는지
        * `is_borrowed`: 대출되었는지
* `Uswer`
    * attributes
        * `name`: 이름
        * `book_list`: 가지고 있는 도서 목록
    * methods:
        * `borrow_book(library, book_name)`: library로부터 book을 빌림
        * `return_book(library, book_name)`: library에 book을 반납

### Example
다음과 같이 `library`를 선언해보자.
```python
library = Library('대전중앙도서관')
print(library.name)
```
Output:
```bash
대전중앙도서관
```
다음과 같이 `book` 2개를 선언한 후 `library`에 추가해보자.
```python
book1 = Book('죄와 벌')
book2 = Book('해리포터')
library.add_book(book1)
library.add_book(book2)
library.info()
```
Output:
```bash
죄와 벌을 대전중앙도서관에 추가합니다.
해리포터를 대전중앙도서관에 추가합니다.
현재 대전중앙도서관이 보유하고 있는 책은 죄와벌, 해리포터 총 2권입니다.
```
다음과 같이 `user`를 선언한 후 도서를 대출하여보자.
```python
minsoo = User('민수')
minsoo.borrow_book(library, '해리포터')
library.info()
```
Output:
```bash
민수가 대전중앙도서관에서 해리포터를 빌렸습니다.
현재 대전중앙도서관이 보유하고 있는 책은 죄와벌 총 1권입니다.
```
다음과 같이 새로운 `user`를 선언한 후 도서를 대출/반납하여보자.
```python
jiwoo = User('지우')
jiwoo.borrow_book(library, '해리포터') 
minsoo.return_book(library, '해리포터') 
jiwoo.borrow_book(library, '해리포터') 
jiwoo.borrow_book(library, '죄와 벌')
```
Output:
```bash
현재 대전중앙도서관은 해리포터를 보유하고 있지 않습니다.
민수가 대전중앙도서관에 해리포터를 반납하였습니다.
지우가 대전중앙도서관에서 해리포터를 빌렸습니다.
지우가 대전중앙도서관에서 죄와 벌을 빌렸습니다.
```
다음과 같이 도서를 반납한 후 도서의 위치를 출력해보자.
```python
minsoo.return_book(library, '죄와 벌')
jiwoo.return_book(library, '죄와 벌')
print(book1.location) 
print(book2.location)
```
Output:
```bash
민수는 죄와 벌을 보유하고 있지 않습니다.
지우가 대전중앙도서관에 죄와 벌을 반납하였습니다.
대전중앙도서관
지우
```

출처: https://www.zehye.kr/python/2018/05/28/11python_class_test2/

## Problem 2
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


## Problem 3
클래스를 이용하여 N차원 도형을 구현해보자. (단, N은 2이상 5 이하의 자연수)

아래 조건에 맞추어 `Point`, `Segment`, `Triangle` 클래스를 구현하여라.

* `Point`
    * N개의 좌표값을 모두 저장
    * 점의 차원(N)을 저장 (단, 차원을 명시적으로 입력받지 말 것)
    * 두 점의 N개의 좌표값들이 모두 같다면 그 두 점은 같다
* `Segment`
    * 두 개의 점을 저장
    * 만약, 주어진 두 개의 점이 하나의 선분을 구성할 수 없다면 에러 메시지를 출력
    * 만약, 주어진 두 개의 점의 차원이 다르다면 에러 메시지를 출력
    * 선분의 길이를 저장
    * 두 선분의 길이와 기울기가 같으면 그 두 선분은 같다
* `Triangle`
    * 세 개의 점을 저장
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
