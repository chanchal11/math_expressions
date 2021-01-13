from postfix_evaluation import evaluate_postfix
from infix_to_postfix import infix_to_postfix

print(evaluate_postfix(infix_to_postfix(input('Enter a mathematical expression:'))))