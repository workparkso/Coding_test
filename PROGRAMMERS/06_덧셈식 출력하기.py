"""
✅문제 설명
두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

a + b = c

제한사항
1 ≤ a, b ≤ 100
입출력 예
입력 #1
4 5
출력 #1
4 + 5 = 9

✅목적: 덧셈식 출력하는 방법을 알고 있는지 확인 목적


"""

# 코드 작성

a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")

#print(a+b)를 작성하지 않는 이유
# 이 코드는 단순히 두 수의 합만 출력하게 된다. 주어진 문제는 a+b=c의 형태로 출력해야한다.


"""
✅다른 사람 풀이

1.
a, b = map(int, input().strip().split(' '))
print(a, '+', b,'=',a+b)

2.
a, b = map(int, input().strip().split(' '))
c = a + b
print('{} + {} = {}'.format(a, b, c))

2-1.
format()는 문자열을 편리하게 출력해줄 수 있는 함수이다.
"형식문자열 {}".format(값)
ex) print("{0}는 {1}이고, {1}는 {0}입니다.".format("가위", "바위"))

f-string과의 차이점:
format() 함수는 문자열을 처리하는 오래된 방법 중 하나이며, 
파이썬 3.6 이상에서는 f-string(formatted string literals)을 사용하는 것이 더 간편하다고 한다. 
예를 들면,
name = "Alice"
age = 25
print(f"이름: {name}, 나이: {age}")

이름: Alice, 나이: 25로 f-string을 사용해서 표현할 수 있다.

"""


# ✅ format 함수를 다시금 익히는 시간을 갖게되었다. 유용한 f-string을 잊지말자. 