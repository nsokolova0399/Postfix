from pythonds.basic.stack import Stack

def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def infix_to_postfix(infix):
    with_enter = ''
    check_altern = True
    flag = False
    if infix[0] == '-':
        flag = True
    elif infix[0] == '+':
        infix = infix[1:]
    for i in range(len(infix)):
        print(infix[i])
        if infix[i] != ' ':
            if infix[i] == '.' or flag:
                if flag:
                    with_enter += infix[i]+' '
                else:
                    with_enter += infix[i]
                flag = False
            else:
                if infix[i] != '(' and infix[i] != ')':
                    if check_altern:
                        if infix[i].lower() in "abcdefghijklmnopqrstuvwxyz" or is_digit(infix[i]):
                            if i != len(infix) - 1:
                                if not is_digit(infix[i + 1]) and infix[i + 1] != '.':
                                    check_altern = False
                        else:
                            raise Exception("Некорректная запись")
                    else:
                        if infix[i] == '+' or infix[i] == '-' or infix[i] == '*' or infix[i] == '/':
                            check_altern = True
                        else:
                            raise Exception("Некорректная запись")
                    if i != len(infix) - 1 or infix[-1] == ')' or infix[-1] == '(':
                        if (is_digit(infix[i + 1]) or infix[i + 1] == '.') and infix[i] != '+' and infix[i] != '*' and \
                                infix[i] != '-' and infix[i] != '/':
                            with_enter += infix[i]
                        else:
                            with_enter += infix[i] + ' '
                    else:
                        with_enter += infix[i] + ' '
                else:
                    with_enter += infix[i] + ' '

    infix = with_enter
    priority_operation = {}
    priority_operation["*"] = 3
    priority_operation["/"] = 3
    priority_operation["+"] = 2
    priority_operation["-"] = 2
    priority_operation["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix.split()

    for token in token_list:
        if token.lower() in "abcdefghijklmnopqrstuvwxyz" or is_digit(token):
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:

            while (not op_stack.isEmpty()) and (priority_operation[op_stack.peek()] >= priority_operation[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())

    if '(' in postfix_list or ')' in postfix_list:
        raise Exception("Некорректная запись")
    return " ".join(postfix_list)


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token.lower() in "abcdefghijklmnopqrstuvwxyz" or is_digit(token):
            if token.lower() in "abcdefghijklmnopqrstuvwxyz":
                num = float(input(token + " = "))
                operand_stack.push(num)
            else:
                operand_stack.push(float(token))
        else:
            operand2 = operand_stack.pop()
            if operand_stack.isEmpty() and token == "-":
                operand1 = '~'
            else:
                operand1 = operand_stack.pop()
            result = math_compute(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()


def math_compute(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op1 == "~":
        return -op2
    else:
        return op1 - op2


while True:
    print("-" * 20)
    try:
        infix = input("Введите выражение: ")
        postfix = infix_to_postfix(infix)
        if not postfix and ('+' not in postfix and '-' not in postfix and '*' not in postfix and '/' not in postfix):
            raise Exception
        print("Постфиксная запись: {}".format(postfix))
        try:
            answer = postfix_eval(postfix)
            print("Результат = {}".format(answer))
        except ZeroDivisionError:
            print("Деление на ноль запрещено!")
        except ValueError:
            print("Ожидалось вещественное число.")
        except TypeError:
            print("Не тот тип записи")
    except Exception:
        print("Некорректная запись")