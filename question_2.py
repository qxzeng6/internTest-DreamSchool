def check_parentheses(strings):
    results = []
    for s in strings:
        left_count = 0
        right_count = 0

        for char in s:
            if char == '(':
                left_count += 1
            elif char == ')':
                right_count += 1
        # get result line by line
        result_in_lst = s + "\n"
        spaces = len(s) - max(left_count, right_count)
        result_in_lst += " " * spaces

        if left_count > right_count:
            result_in_lst += "x" * (left_count - right_count)
        elif right_count > left_count:
            result_in_lst += "?" * (right_count - left_count)

        results.append(result_in_lst)

    return results


sample_input = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

output = check_parentheses(sample_input)
# print(output)
res = ""
for result in output:
    res += result + '\n'

print(f'For question 2, the result of sample example is: \n{res}')


# solve question 2 with stack
def check_parentheses_v2(input_string):
    results = []
    for s in input_string:
        stack = []
        result_line = s + "\n"
        output_marks = [' '] * len(s)
        for i, char in enumerate(s):
            if char == '(':
                stack.append((char, i))
            elif char == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    output_marks[i] = '?'

        while stack:
            _, idx = stack.pop()
            output_marks[idx] = 'x'

        result_line += ''.join(output_marks)

        results.append(result_line)

    return results


output_2 = check_parentheses_v2(sample_input)
# print(output_2)
res_2 = ""
for result in output_2:
    res_2 += result + '\n'

print(f'For the stack solution of question 2, the result of sample example is: \n{res_2}')
