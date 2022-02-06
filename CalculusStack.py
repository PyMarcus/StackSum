from typing import Any


class Stack:
    def __init__(self: Any):
        self.__stack: list = []

    @property
    def stack(self) -> list:
        return self.__stack

    # @override
    def __str__(self) -> str:
        return str(self.__stack).replace('[', '').replace(']', '')

    def push(self) -> list:
        stdin: str = input('::: ')
        self.__stack: list = stdin.split()
        return self.__stack

    def pop(self) -> Any:
        if self.isEmpty():
            return self.__stack.pop()

    def add(self, valor):
        self.__stack.append(valor)

    def isEmpty(self):
        return not len(self.__stack) == 0


class Calculus(Stack):
    """Classe que contém o método de cálculo e ela herda de uma pilha
           :methods: calculo
    """

    def __init__(self):
        super().__init__()

    def calculo(self) -> Stack:
        """Solicita a operação.Que deve ser inserida como operandos e operadores, com espaços e sem parênteses
           :param: None
           :return: Stack
        """
        stack = Stack()
        operacao: list = self.push()
        for itens in operacao:
            if itens != '-' and itens != '+' and itens != '/' and itens != '*':
                stack.add(itens)
            else:
                x: int = stack.pop()
                y: int = stack.pop()
                result: int = eval(str(f"{x} {itens} {y}"))
                stack.add(result)
        return stack


if __name__ == '__main__':
    # 1 2 + 3 * = (1 + 2) * 3
    stack = Calculus()
    print(stack.calculo())
