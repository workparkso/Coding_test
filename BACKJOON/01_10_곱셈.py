"""
✅문제 설명
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
          4 7 2 ... (1)
        × 3 8 5 ... (2)
-----------------
        2 3 6 0 ... (3)
      3 7 7 6   ... (4)
    1 4 1 6     ... (5)
-----------------   
    1 8 1 7 2 0 ... (6)

(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

출력
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

✅목적: 각 자리수의 곱셈 확인

"""

# 코드 작성

a = int(input())  
b = int(input())  

# 각 단계를 계산
step1 = a * (b % 10)           # (3)
step2 = a * ((b // 10) % 10)   # (4)
step3 = a * (b // 100)         # (5)
final_result = a * b           # (6)

# 결과 출력
print(step1)
print(step2)
print(step3)
print(final_result)




#✅ 각 ~의 자리 숫자를 어떻게 활용할 수 있는지 확인하는 문제였다.
# 이런 간단한 코드들은 외우는게 더 빠르지 않을까싶다.

