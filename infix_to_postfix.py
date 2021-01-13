precidence_map = {'/': 2,'*': 2, '+': 1, '-': 1, '(':9, ')':9}
operator_list = ['/','*','+','-']
temp_number_str = ''

def is_in_operator_list(character: str):
    for op in operator_list:
        if op.startswith(character):
            return True
    return False

def infix_to_postfix(infix_exp : str):
    postfix_stack = list()
    syntax_stack = list()
    
    
    def process_alpha_str():
        global temp_number_str
        if not temp_number_str.__len__() == 0:         
            postfix_stack.append(temp_number_str)
            temp_number_str = ''
        
    global temp_number_str

    for character in infix_exp:
        if character.isalnum():
            temp_number_str = temp_number_str + character 
        elif is_in_operator_list(character):
            process_alpha_str()
            if syntax_stack.__len__() == 0:
                syntax_stack.append(character)
            elif precidence_map[character] <= precidence_map[syntax_stack[syntax_stack.__len__() -1]]:
                if syntax_stack[syntax_stack.__len__() -1].startswith('('):
                    syntax_stack.append(character)
                else:
                    postfix_stack.append(syntax_stack.pop())
                    syntax_stack.append(character)
        elif character.startswith('('):
            process_alpha_str()
            syntax_stack.append(character)
        elif character.startswith(')'):
            process_alpha_str()
            while(True):
                if syntax_stack.__len__() == 0:
                    break
                elif syntax_stack[syntax_stack.__len__() -1].startswith('('):
                    syntax_stack.pop()
                else:
                    poped_char = syntax_stack.pop()
                    postfix_stack.append(poped_char) 

    process_alpha_str()

    while (syntax_stack.__len__() > 0):
        postfix_stack.append(syntax_stack.pop())
    return postfix_stack

print(infix_to_postfix(input('Enter a mathematical expression:')))
