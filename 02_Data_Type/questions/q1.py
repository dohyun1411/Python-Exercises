##################################################
# 연습문제 Q1
# 홍길동 씨의 국어, 영어, 수학 점수의 평균을 구하여라.

# Input
# 80 75 55
# Output
# 70.0
##################################################


def solve(korean, english, math):
    ## Do not modify outside of this area ##
    ############ Your code here ############

    answer = (korean + english + math) / 3 # your answer here

    ########################################
    return answer


if __name__ == '__main__':
    korean, english, math = input().split()
    korean, english, math = int(korean), int(english), int(math)
    answer = solve(korean, english, math)
    print(answer)
