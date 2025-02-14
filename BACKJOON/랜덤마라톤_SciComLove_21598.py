"""
✅문제 설명
당신은 싸이컴을 향해 절을 하려고 합니다. 하지만, 당신이 싸이컴에 들어오고 싶어서 절을 한 번 할 수도 있고, 싸이컴을 매우 싫어해 절을 두 번 할 수도 있습니다.

당신이 절을 할 횟수가 주어질 때, 그 횟수만큼 절하는 프로그램을 작성하세요. 실제로 프로그램을 이용해 절을 할 수는 없기 때문에, 대신 “SciComLove”를 출력하도록 합니다.

입력
첫 줄에 정수 N이 주어집니다.

출력
"SciComLove"를 예제와 같이 N번 출력합니다. 단, 따옴표는 출력하지 않습니다.

제한
1 ≤ N ≤ 2

서브태스크
번호 배점 제한
1    40   N = 1
2    40   N = 2
3    20   추가 제한 조건이 없습니다.

✅목적: 긴 문장이지만 핵심만 알면 쉽게 풀리는 문제 해결 능력 확인 목적
"""

# 코드 작성
N = int(input()) 
for a in range(N):
    print("SciComLove")


#-------
#✅ 다른 사람의 풀이1
N = int(input())  
print("\n".join(["SciComLove"] * N))  # "SciComLove"를 N번 반복하여 출력


#✅ 다른 사람의 풀이2
N = int(input())  
count = 0  # 반복 횟수를 추적하기 위한 변수
while count < N: 
    print("SciComLove")
    count += 1  # 반복 횟수를 증가시킴

#✅ 다른 사람의 풀이3
N = int(input()) 
print(*["SciComLove"] * N, sep="\n")  # "SciComLove"를 N번 반복하여 출력
# * (언패킹 연산자)를 사용하여 리스트를 개별적인 문자열 요소로 변환
# 예시: 
# data = ["SciComLove", "SciComLove"]
# print(*data)

# SciComLove SciComLove


#✅ 다른 사람의 풀이4
N = int(input())  # 입력을 받습니다.
list(map(lambda x: print("SciComLove"), range(N)))  # "SciComLove"를 N번 출력

#range(N)은 0부터 N-1까지의 숫자를 생성하는 이터러블(iterable) 객체
# 예를 들어, N = 2라면 range(2)는 [0, 1]과 같은 값들을 생성


# lambda x: print("SciComLove")
# =
# def my_function(x):
#    print("SciComLove")

# 만약 n =2이라면,
#range(2) → [0, 1]
#lambda 0: print("SciComLove") 실행 → "SciComLove" 출력
#lambda 1: print("SciComLove") 실행 → "SciComLove" 출력

# map()을 list()로 감싸면 모든 요소가 한 번에 실행되면서 출력이 발생


#✅ 다양한 방법이 있는 것을 알게되었다. 
# 조금 더 생각해보고 다른 방안도 있는지 꼭 검토하는 시간을 갖도록 노력해야겠다.


