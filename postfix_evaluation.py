import infix_to_postfix as inf_psfx

def calculate(operand1: str,operand2: str, operator: str):
    if operator == '+':
        return int(operand1) + int(operand2)
    if operator == '-':
        return int(operand1) - int(operand2)
    if operator == '*':
        return int(operand1) * int(operand2)
    if operator == '/':
        if int(operand2) == 0:
            raise Exception('The second operand cannot be zero.')
        return int(operand1) / int(operand2)

def evaluate_postfix(postfix_exp : list):
    temp_stack = list()
    while(not postfix_exp.__len__()==0):
        element = postfix_exp[0]
        postfix_exp.__delitem__(0)
        
        if element.isalnum():
            temp_stack.append(element)

        elif inf_psfx.is_in_operator_list(element):
            operand1 = temp_stack.pop()
            operand2 = temp_stack.pop()
            temp_stack.append(calculate(operand1,operand2,element))

    return temp_stack[0]

print(evaluate_postfix(inf_psfx.infix_to_postfix(input('Enter a mathematical expression:'))))        