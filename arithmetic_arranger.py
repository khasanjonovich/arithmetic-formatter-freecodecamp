def arithmetic_arranger(problems, op=False):
    con, problems = clear(problems)
    if con:
        return problems

    first = row_format(problems, 1)
    second = row_format(problems, 2)
    _dash = _(problems)

    if op:
        third = row_format(problems, 3)
        return first + second + _dash + third
    return first + second + _dash


def clear(problems):
    res = []
    if len(problems) > 5:
        return True, 'Error: Too many problems.'

    for problem in problems:
        con = False
        msg = None
        valid = ["+", "-"]
        f, op, s = problem.split(" ")

        if op not in valid:
            con = True
            msg = "Error: Operator must be '+' or '-'."
        if (f.isdecimal() is False) or (s.isdecimal() is False):
            con = True
            msg = "Error: Numbers must only contain digits."
        if len(f) > 4 or len(s) > 4:
            con = True
            msg = "Error: Numbers cannot be more than four digits."
        if con:
            return con, msg
        res.append([int(f), op, int(s)])

    return False, res


def digit1(prob, amount_of_blank):
    res = ""
    f, op, s = prob
    space = len(str(max(f, s))) + 2
    blank = " " * amount_of_blank
    if space == 6:
        res = res + f"{f:>6}" + blank
    elif space == 5:
        res = res + f"{f:>5}" + blank
    elif space == 4:
        res = res + f"{f:>4}" + blank
    elif space == 3:
        res = res + f"{f:>3}" + blank

    return res


def row_format(problems, op):
    row = ""
    if op == 1:
        for problem in problems:
            # determine the last elem, and exclude blank
            row = row + digit1(problem, 0) if problem == problems[-1] else row + digit1(problem, 4)
        row = row + "\n"
    elif op == 2:
        for problem in problems:
            row = row + digit2(problem, 0) if problem == problems[-1] else row + digit2(problem, 4)

    elif op == 3:
        row = "\n"
        for problem in problems:
            row = row + result(problem, 0) if problem == problems[-1] else row + result(problem, 4)
    return row


def digit2(prob, amount_of_blank):
    res = ""
    f, op, s = prob
    space = len(str(max(f, s)))
    blank4 = " " * amount_of_blank
    if space == 4:
        res = res + f"{op} {s:>4}" + blank4
    elif space == 3:
        res = res + f"{op} {s:>3}" + blank4
    elif space == 2:
        res = res + f"{op} {s:>2}" + blank4
    elif space == 1:
        res = res + f"{op} {s:>1}" + blank4

    return res


def _(problems):
    res = "\n"
    for problem in problems:
        f, op, s = problem
        amount_of_dash = len(str(max(f, s))) + 2
        res = res + "-" * amount_of_dash
        res = res + "    " if problem != problems[-1] else res
    return res


def result(problem, amount_of_blank):
    res = ""
    f, op, s = problem
    space = len(str(max(f, s))) + 2
    blank = " " * amount_of_blank
    calc = f + s if op == "+" else f - s
    if space == 6:
        res = res + f"{calc:>6}" + blank
    elif space == 5:
        res = res + f"{calc:>5}" + blank
    elif space == 4:
        res = res + f"{calc:>4}" + blank
    elif space == 3:
        res = res + f"{calc:>3}" + blank

    return res
