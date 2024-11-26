# Tiny_ASM_Compiler
This is a small three-pass compiler designed to process arithmetic expressions written in infix notation. It generates an Abstract Syntax Tree (AST), optimizes the tree, and produces assembly-like code that can be executed by a simulator.

The compiler supports basic operations (`+`, `-`, `*`, `/`) and user-defined arguments.

---

## **Project Structure**
The project follows a modular architecture and is organized into the following files:

### **Main Files**
- `compiler.py`: Contains the main implementation of the compiler, including its three phases (`pass1`, `pass2`, and `pass3`).
- `tests/`: A folder with unit tests and example cases to validate the compiler's functionality.
- `Makefile`: A file to manage build tasks, offering options for running, cleaning, and testing the compiler.

---

## **Compiler Workflow**
The compiler processes an input program in three distinct passes:

1. **Pass 1**: Parses the input expression into an **Abstract Syntax Tree (AST)**.
   - Converts infix notation to a structured tree format.
   - Handles operator precedence and parentheses.

2. **Pass 2**: Optimizes the AST.
   - Precomputes constant expressions to reduce runtime calculations.

3. **Pass 3**: Generates **assembly-like instructions**.
   - Produces a low-level instruction set for execution by a simulator.

---

## **Features**
- **Tokenization**: Supports parsing of variables, constants, and arithmetic operators.
- **AST Generation**: Builds a structured representation of the input program.
- **Optimization**: Simplifies the AST by evaluating constant subexpressions at compile-time.
- **Assembly Output**: Outputs instructions for a stack-based virtual machine.

---

## **Usage**
1. Clone the repository:
```bash
git clone https://github.com/your-username/TinyThreePassCompiler.git
```
```bash
cd TinyThreePassCompiler/src
```
### Use the provided Makefile to interact with the project:

#### Run the Compiler:
```bash
make run
```
#### Test the Compiler:
```bash

make test
```
#### Clean the Build:
```bash
make clean
```
#### Input a program in the following format:

```text
[x y z] (2 * 3 * x + 5 * y - 3 * z) / (1 + 3 + 2 * 2)
```
### The compiler will produce:

- The AST after Pass 1.
- The optimized AST after Pass 2.
- The final assembly instructions after Pass 3.
