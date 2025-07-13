from itertools import combinations

N = int(input())
# 0 ~ 9의 값으로 조합만들거니까 (미리 내림차순 만들기)
nums = list(range(9, -1, -1))
deacresing_list = []

# 1자리수 ~ 10자리수의 조합 만들기 (0 ~ 9,876,5432,10)
for i in range(1, 11):
    # 생성한 조합을 다시 숫자로 바꿔서 nums에 추가
    for comb in list(combinations(nums, i)):
        deacresing_list.append(int(''.join(list(map(str, comb)))))

deacresing_list.sort()

# if len(deacresing_list) <= N으로하면 .. 터짐 .. 왜 ?
try:
    print(deacresing_list[N - 1])
except:
    print(-1)

