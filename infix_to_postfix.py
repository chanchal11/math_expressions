precidence_map = {'/': 2,'*': 2, '+': 1, '-': 1, '(':9, ')':9}
operator_list = ['/','*','+','-']

def is_in_operator_list(character: str):
    for op in operator_list:
        if op.startswith(character):
            return True
    return False

def infix_to_postfix(infix_exp : str):
    postfix_stack = list()
    syntax_stack = list()
    for character in infix_exp:
        if character.isalnum(): 
            postfix_stack.append(character)
        elif is_in_operator_list(character):
            if syntax_stack.__len__() == 0:
                syntax_stack.append(character)
            elif precidence_map[character] <= precidence_map[syntax_stack[syntax_stack.__len__() -1]]:
                if syntax_stack[syntax_stack.__len__() -1].startswith('('):
                    syntax_stack.append(character)
                else:
                    postfix_stack.append(syntax_stack.pop())
                    syntax_stack.append(character)
        elif character.startswith('('):
            syntax_stack.append(character)
        elif character.startswith(')'):
            while(True):
                if syntax_stack.__len__() == 0:
                    break
                elif syntax_stack[syntax_stack.__len__() -1].startswith('('):
                    syntax_stack.pop()
                else:
                    poped_char = syntax_stack.pop()
                    postfix_stack.append(poped_char) 

    while (syntax_stack.__len__() > 0):
        postfix_stack.append(syntax_stack.pop())
    return postfix_stack

print(infix_to_postfix(input('Enter a mathematical expression:')))
