def arithmetic_arranger(problems, result=False):
    """
    Receives a list of strings that are arithmetic problems and 
    returns the problems arranged vertically and side-by-side. 
    If result is set to True, the answers are displayed as well.

    Possible errors:
        `Error: Too many problems.`: More than 5 problems supplied to the function.
        `Error: Operator must be '+' or '-'.`: The appropriate operators the function accepts are addition (+) and subtraction (-). 
                Multiplication and division will return an error. 
                Other operators not mentioned in this bullet point are not included.
        `Error: Numbers must only contain digits.`: Each number (operand) should only contain digits.
        `Error: Numbers cannot be more than four digits.`: Each operand (aka number on each side of the operator) has a max of four digits in width.
    """
    if len(problems) > 5:
        return "Error: Too many problems."

    ops = {
        '+': lambda pair: str(pair[0] + pair[1]),
        '-': lambda pair: str(pair[0] - pair[1]),
    }
    arranged_problems = []
    top = []
    bottom = []
    lines = []
    results = []

    for problem in problems:
        chunks = problem.split()
        max_len = len(max(chunks, key=len))

        if not all([i.isnumeric() for i in chunks[::2]]):
            return "Error: Numbers must only contain digits."
        elif chunks[1] not in ops.keys():
            return "Error: Operator must be '+' or '-'."
        elif max_len > 4:
            return "Error: Numbers cannot be more than four digits."

        line_len = max_len + 2

        line = '-' * line_len  # 2 corresponds to the sign and space
        first_num = chunks[0].rjust(line_len, ' ')
        second_num = f"{chunks[1]}{' ' * (line_len - len(chunks[2]) - 1)}{chunks[2]}"

        top.append(first_num)
        bottom.append(second_num)
        lines.append(line)

        if result:
            res = ops[chunks[1]]([int(i) for i in chunks[::2]])
            results.append(f"{res.rjust(line_len, ' ')}")

    arranged_problems = '\n'.join(['    '.join(i)
                                   for i in (top, bottom, lines)])

    if results:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems
