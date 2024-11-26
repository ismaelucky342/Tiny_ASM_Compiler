from compiler import Compiler

if __name__ == "__main__":
    program = "3 + (4 * 5)"
    compiler = Compiler()
    asm = compiler.compile(program)
    print("\n".join(asm))
