from ast import ASTBuilder
from tokenizer import Tokenizer

class Compiler:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.ast_builder = ASTBuilder()

    def pass2(self, ast):
        def reduce_tree(ast):
            if ast['op'] in {'imm', 'arg'}:
                return ast
            ast['a'] = reduce_tree(ast['a'])
            ast['b'] = reduce_tree(ast['b'])
            if ast['a']['op'] == 'imm' and ast['b']['op'] == 'imm':
                n = eval(f"{ast['a']['n']} {ast['op']} {ast['b']['n']}")
                return {'op': 'imm', 'n': n}
            return ast

        return reduce_tree(ast)

    def pass3(self, ast):
        operator_map = {'+': 'AD', '-': 'SU', '*': 'MU', '/': 'DI'}
        operation_depths = {}
        max_depth = float('-inf')

        def mark_depth(ast, depth=0):
            nonlocal max_depth
            if 'a' in ast and 'b' in ast:
                max_depth = max(max_depth, depth)
                if depth not in operation_depths:
                    operation_depths[depth] = []
                operation_depths[depth].append(ast)
                mark_depth(ast['a'], depth + 1)
                mark_depth(ast['b'], depth + 1)

        mark_depth(ast)
        asm = []

        current_depth = max_depth
        while current_depth >= 0:
            current_depth_operations = operation_depths.get(current_depth, [])
            while current_depth_operations:
                current_operation = current_depth_operations.pop(0)

                # Handle right branch
                if current_operation['b']['op'] == 'imm':
                    asm.append(f'IM {current_operation["b"]["n"]}')
                elif current_operation['b']['op'] == 'arg':
                    asm.append(f'AR {current_operation["b"]["n"]}')
                else:
                    asm.append('PO')

                asm.append('SW')

                # Handle left branch
                if current_operation['a']['op'] == 'imm':
                    asm.append(f'IM {current_operation["a"]["n"]}')
                elif current_operation['a']['op'] == 'arg':
                    asm.append(f'AR {current_operation["a"]["n"]}')
                else:
                    asm.append('PO')

                # Apply operation
                asm.append(operator_map[current_operation['op']])

                # Push result to stack
                asm.append('PU')

            current_depth -= 1

        return asm

    def compile(self, program):
        tokens = self.tokenizer.tokenize(program)
        ast = self.ast_builder.pass1(tokens)
        ast = self.pass2(ast)
        return self.pass3(ast)
