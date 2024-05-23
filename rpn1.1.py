
import math

stack = []

def push(num): # Pushing on the stack.
    if '.' in num:
        stack.append(float(num))
    else:
        stack.append(int(num))
    print_stack()

def delfromstack(): # Deleting elements from the stack.
    if len(stack) == 0:
        print("Stack is empty")
    return stack.pop()

def print_stack():
    print("Стек:", stack)

def performa(): # Addition.
    if len(stack) < 2:
        print("Ошибка: Для выполнения операции сложения нужно минимум 2 элемента в стеке.")
    else:
        b = delfromstack()
        a = delfromstack()
        stack.append(a + b)
        print_stack()

def performs(): # Substraction.
    if len(stack) < 2:
        print("Ошибка: Для выполнения операции вычитания нужно минимум 2 элемента в стеке.")
    else:
        b = delfromstack()
        a = delfromstack()
        stack.append(a - b)
        print_stack()

def performm(): # Multiplication.
    if len(stack) < 2:
        print("Ошибка: Для выполнения операции умножения нужно минимум 2 элемента в стеке.")
    else:
        b = delfromstack()
        a = delfromstack()
        stack.append(a * b)
        print_stack()

def performd(): # Division.
    if len(stack) < 2:
        print("Ошибка: Для выполнения операции деления нужно минимум 2 элемента в стеке.")
    else:
        b = delfromstack()
        a = delfromstack()
        if b == 0:
            print("Ошибка: Деление на ноль.")
            stack.append(a)
            stack.append(b)
        else:
            stack.append(a / b)
        print_stack()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def performf(): # Factorial.
    if len(stack) < 1:
        print("Ошибка: Для выполнения операции факториала нужен минимум 1 элемент в стеке.")
    else:
        a = delfromstack()
        if isinstance(a, int) and a >= 0:
            stack.append(factorial(a))
        else:
            print("Ошибка: Факториал можно вычислить только для неотрицательных целых чисел.")
            stack.append(a)
        print_stack()

def performp(): # The power.
    if len(stack) < 2:
        print("Ошибка: Для выполнения операции возведения в степень нужно минимум 2 элемента в стеке.")
    else:
        b = delfromstack()
        a = delfromstack()
        stack.append(a ** b)
        print_stack()

def performr(): # The root.
    if len(stack) < 1:
        print("Ошибка: Для выполнения операции вычисления квадратного корня нужен минимум 1 элемент в стеке.")
    else:
        a = delfromstack()
        if a < 0:
            print("Ошибка: Невозможно вычислить квадратный корень из отрицательного числа.")
            stack.append(a)
        else:
            stack.append(math.sqrt(a))
        print_stack()
        
def performmd(): # The modulo.
    if len(stack) < 2:
        print("Ошибка: Для выполнения операции нахождения остатка нужно минимум 2 элемента в стеке.")
    else:
        b = delfromstack()
        a = delfromstack()
        stack.append(a % b)
        print_stack()

def main():
    while True:
        command = input("Введите число или команду ('+', '-', '*', '/', '!', '^', '%', 'sqrt', 'pop', 'exit'): ").strip()
        
        if command in ['exit', 'quit']:
            print("Завершение работы программы.")
            break
        
        elif command == '+':
            performa()
        elif command == '-':
            performs()
        elif command == '*':
            performm()
        elif command == '/':
            performd()
        elif command == '!':
            performf()
        elif command == '^':
            performp()
        elif command == '%':
            performmd()
        elif command == 'pop':
            delfromstack()
            print_stack()
        elif command == 'sqrt':
            performr()
        else:
            try:
                push(command)
            except ValueError:
                print("Ошибка: Некорректный ввод.")

if __name__ == "__main__":
    main()
