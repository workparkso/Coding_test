"""
✅문제 설명
문자열 str과 정수 n이 주어집니다.
str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 10
1 ≤ n ≤ 5
입출력 예
입력 #1

string 5
출력 #1

stringstringstringstringstring

✅목적
문자열의 반복 출력을 아는지 확인하려는 목적
"""

# 코드 작성
a, n = input().strip().split(' ')
n = int(n)
print(a*n)


"""
✅다른 사람들의 풀이

1.
a=input()
print(a[:-2]*int(a[-1]))


2.
a, b = input().strip().split(' ')
b = int(b)
for i in range(b):
    print(a, end='')

2-1.
for i in range(b):
range(b)는 0부터 b-1까지의 숫자들을 생성하며, b번 반복하도록 설정된다.
예를 들어, b가 5이면 반복문은 5번 실행된다.
2-2.
print(a, end='')
print(a)는 a의 값을 출력한다.
end=''는 출력 후에 줄 바꿈을 하지 않도록 설정합니다. 즉, 각 a 값은 같은 줄에 계속 이어서 출력된다.

3.
a, b = input().strip().split(' ')
print(a*int(b))
"""


# ✅ 분명 end=''를 사용한 코드들을 많이 봤는데, 기억에 흐릿해서
# 이번 코딩테스트를 복습하면서 한번 더 다지는 시간을 갖게 되었다. 잊어버리지말자.
