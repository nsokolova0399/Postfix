from pythonds.basic.stack import Stack

# проверяем символы и точку в том числе
def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

# перевод в постфиксную запись
def infix_to_postfix(infix):
    buf = ''
    check_altern = True
    flag = False
    if infix[0] == '-':
        flag = True
    elif infix[0] == '+':
        infix = infix[1:]
    for i in range(len(infix)):
        if infix[i] != ' ':
            if infix[i] == '.' or flag:
                if flag:
                    buf += infix[i]+' '
                else:
                    buf += infix[i]
                flag = False
            else:
                if infix[i] != '(' and infix[i] != ')':
                    if check_altern:
                        if infix[i].lower() in "abcdefghijklmnopqrstuvwxyz" or is_digit(infix[i]):
                            if i != len(infix) - 1:
                                if not is_digit(infix[i + 1]) and infix[i + 1] != '.':
                                    check_altern = False
                        # else:
                        #     raise Exception("Ошибка!Некорректная запись!")
                    else:
                        if infix[i] == '+' or infix[i] == '-' or infix[i] == '*' or infix[i] == '/':
                            check_altern = True
                        else:
                            raise Exception("Ошибка!Некорректная запись!")
                    if i != len(infix) - 1 or infix[-1] == ')' or infix[-1] == '(':
                        if (is_digit(infix[i + 1]) or infix[i + 1] == '.') and infix[i] != '+' and infix[i] != '*' and \
                                infix[i] != '-' and infix[i] != '/':
                            buf += infix[i]
                        else:
                            buf += infix[i] + ' '
                    else:
                        buf += infix[i] + ' '
                else:
                    buf += infix[i] + ' '

    infix = buf
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


# вычисляем выражение в постфиксной записи
def postfix_calculation(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()
    map = {}
    # new_list = list(set(token_list) & set(token_list))
    for token in token_list:
        if token.lower() in "abcdefghijklmnopqrstuvwxyz" or is_digit(token):
            if token.lower() in "abcdefghijklmnopqrstuvwxyz":
                if token in map:
                    operand_stack.push(map[token])
                else:
                    map[token] = float(input(token + " = "))
                    operand_stack.push(map[token])
            elif is_digit(token):
                operand_stack.push(float(token))
        else:
            operand2 = operand_stack.pop()
            if operand_stack.isEmpty() and token == "-":
                operand1 = '~'
            else:
                operand1 = operand_stack.pop()
            result = calculation(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

# получение результата
def calculation(sign, a, b):
    if sign == "*":
        return a * b
    elif sign == "/":
        return a / b
    elif sign == "+":
        return a + b
    elif a == "~":
        return -b
    else:
        return a - b


while True:
    try:
        print("\n")
        infix = input("Исходная строка: ")
        postfix = infix_to_postfix(infix)
        if not postfix and ('+' not in postfix and '-' not in postfix and '*' not in postfix and '/' not in postfix):
            raise Exception
        print("Постфиксная запись: {}".format(postfix))
        try:
            answer = postfix_calculation(postfix)
            print("Результат = {}".format(answer))
        except ValueError:
            print("Необхходимо ввести вещественное число")
        except ZeroDivisionError:
            print("Нельзя делить на ноль!")
        except TypeError:
            print("Ошибка типа записи")
    except Exception:
        print("Ошибка!Некорректная запись!")