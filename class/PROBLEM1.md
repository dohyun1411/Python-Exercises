# Problem 1
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

## Example
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