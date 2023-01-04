# Problem 3
파이썬의 `list`를 상속하여 새로운 클래스 `MyList`를 만들어보자.

`MyList`는 기존 `list`와는 다르게 원소들이 모두 동일한 타입을 가져야한다.

Example:
```python
my_list = MyList([1, 2, 3])
my_list.append(4)
print(my_list)
my_list.append('a')
print(my_list)
```
Output:
```shell
[1, 2, 3, 4]
Cannot append str to list of int
[1, 2, 3, 4]
```

또한, `MyList`는 다음과 같은 추가 기능을 가지고 있다.

* `replace(a, b)`: 리스트 안에 `a`가 있다면, `a`를 `b`로 변환한다.
* `find(e)`: 리스트 안에 `e`가 있다면, index를 반환한다. 없으면 -1을 반환한다.
* `argmax()`: 리스트 안의 원소 중 가장 큰 원소의 index를 반환한다. 빈 리스트의 경우 -1을 반환한다.
* `argmin()`: 리스트 안의 원소 중 가장 작은 원소의 index를 반환한다. 빈 리스트의 경우 -1을 반환한다.

Example:
```python
my_list = MyList([1, 2, 3])
my_list.replace(1, 4)
i = my_list.find(4)
j = my_list.argmax()
k = my_list.argmin()
print(i, j, k)
```
Output:
```shell
0, 2, 0
```