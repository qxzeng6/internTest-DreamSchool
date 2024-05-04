def min_subsequence_to_reach_target(source, target):
    if not set(target).issubset(set(source)):
        return -1
    result, index = 0, 0
    while index < len(target):
        count = 0
        for char in source:
            if index < len(target) and char == target[index]:
                index += 1
                count += 1
        if count == 0:
            return -1

        result += 1

    return result


# test cases
test_cases_in_handout = [("abc", "abcbc"), ("abc", "acdbc"), ("xyz", "xzyxz")]
results = [min_subsequence_to_reach_target(source, target) for source, target in test_cases_in_handout]
print(f'For the first question, three cases show up in the handout :{results}')


# using dp idea to solve this question
def min_subsequence_to_reach_target_v2(source, target):
    dp = [float('inf')] * (len(target) + 1)
    dp[0] = 0
    n = len(target)
    for i in range(n):
        if dp[i] == float('inf'):
            continue
        s_index = 0
        for t_index in range(i, n):
            while s_index < len(source) and (t_index >= len(target) or source[s_index] != target[t_index]):
                s_index += 1
            if s_index < len(source):
                if dp[t_index + 1] > dp[i] + 1:
                    dp[t_index + 1] = dp[i] + 1
                s_index += 1

    if dp[n] == float('inf'):
        return -1
    else:
        return dp[n]


results_v2 = [min_subsequence_to_reach_target_v2(source, target) for source, target in test_cases_in_handout]
print(f'Solving problem with dp idea, three cases show up in the handout :{results_v2}')
