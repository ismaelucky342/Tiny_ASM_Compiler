from collections import deque
from utils import is_number, is_operator

class ASTBuilder:
    def __init__(self):
        self.args = []

    def build_ast(self, output_queue):
        output = output_queue.pop()
        node = {}

        if is_number(output):
            node['op'] = 'imm'
            node['n'] = output
        elif output in self.args:
            node['op'] = 'arg'
            node['n'] = self.args.index(output)
        elif is_operator(output):
            node['op'] = output
            b = self.build_ast(output_queue)
            a = self.build_ast(output_queue)
            node['a'] = a
            node['b'] = b

        return node

    def pass1(self, tokens):
        output_queue = deque()
        operator_stack = deque()
        token_index = 0

        def get_next_token():
            nonlocal token_index
            if token_index < len(tokens):
                token = tokens[token_index]
                token_index += 1
                return token
            return None

        def precedence_is_not_greater(o1, o2):
            precedences = {'/': 3, '*': 3, '+': 2, '-': 2}
            return precedences[o1] <= precedences[o2]

        while True:
            token = get_next_token()
            if token is None:
                break

            if token == '[':
                while (next_token := get_next_token()) != ']':
                    self.args.append(next_token)
            elif is_number(token) or token in self.args:
                output_queue.append(token)
            elif is_operator(token):
                while (operator_stack and is_operator(operator_stack[-1]) and
                       precedence_is_not_greater(token, operator_stack[-1])):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()

        while operator_stack:
            output_queue.append(operator_stack.pop())

        return self.build_ast(output_queue)
