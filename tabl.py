#!/usr/bin/env python3

from collections import deque

class Statement: 
    """
    It's a "statement"
    """
    def __init__(self, statement:str):
        self.statement = statement.replace(" ", "")
        try:
            self._polish()
        except:
            raise Exception("Input is not syntatically valid.")

    def _polish(self) -> None: 
        """
        Translating user input to polish notation. Assumes that the input is syntatically valid.
        """
        # special characters ranked in order of importance
        special = { 
            "!": 1,
            "^": 2, # hehe xor
            "&": 3, 
            "|": 4, 
            ">": 5, 
            "=": 6,
            "(": 7, # ( should be a special char, but nothing should force it to evaluate except for ).
            ")": 7
        }
        operations = deque()
        polish = ""
        
        for char in self.statement:
            if char not in special:
                polish += char
                continue

            if char == "(": 
                operations.append(char)
                continue

            if char == ")": 
                while operations[-1] != "(":
                    polish += operations[-1]
                    operations.pop()
                operations.pop()
                continue

            while len(operations) > 0 and special[char] > special[operations[-1]]:
                polish += operations[-1]
                operations.pop()

            operations.append(char)
            continue

        while len(operations) > 0:
            polish += operations[-1]
            operations.pop()

        self.statement = polish

    def evaluate(self, state:dict):
        """
        Evaluates a truth table
        """
        operate = {
            "&": lambda a, b: a and b,
            "|": lambda a, b: a or b,
            ">": lambda a, b: (not a) or b,
            "^": lambda a, b: a != b,
            "=": lambda a, b: a == b,
        }
        vals = deque()
        valsvar = deque()
        for char in self.statement:
            if char in operate:
                b = vals.pop()
                a = vals.pop()

                ans = operate[char](a, b)
                vals.append(ans)

                b = valsvar.pop()
                a = valsvar.pop()
                eqn = f"({a + char + b})"
                valsvar.append(eqn)

                state[eqn] = ans

            elif char == "!":
                a = vals.pop()
                ans = not a
                vals.append(ans)

                a = valsvar.pop()
                eqn = "!"+a
                valsvar.append(eqn)

                state[eqn] = ans
            else:
                vals.append(state[char])
                # row[char] = state[char]
                valsvar.append(char)

    def primitives(self) -> list:
        """
        Returns primitive variables
        """
        prims = set()
        for char in self.statement:
            if char.isalpha():
                prims.add(char)

        prims = list(prims)
        prims.sort()
        return prims

class Printer(): 
    """
    For printing truth tables!!!
    """
    def __init__(self, statement:Statement): 
        self.statement = statement
        self.prims = self.statement.primitives()
        order = {p:0 for p in self.prims}
        # I'm lazy, just do this to get the header
        self.statement.evaluate(order)
        self.order = list(order.keys())
        self._print_table()

    def _print_head(self):
        """
        Print the heading!!!
        """
        print("|", end="")
        for state in self.order:
            print(f"{state:^{len(state)+2}}", end="|")
        print()

    def _print_br(self):
        """
        Print a break between values!!!
        """
        length = 1
        for state in self.order:
            length += len(state)+3
        print("+"+"-"*(length-2)+"+")

    def _print_row(self, values:dict): 
        """
        Print a row (given the values for that row)!!!
        """
        print("|", end="")
        for state in self.order:
            print(f"{values[state]:^{len(state)+2}}", end="|")
        print()

    def _print_table(self):
        """
        Print the table!!!
        """
        self._print_br()
        self._print_head()
        self._print_br()
        for i in range(2**len(self.prims)):
            state = {}
            for p in self.prims[::-1]:
                val = i & 1
                state[p] = val
                i = i >> 1
            try:
                self.statement.evaluate(state)
            except:
                raise Exception("Input is not syntatically valid.")
                return
            self._print_row(state)
        self._print_br()

def main():
    logic = input("logic: ")
    while logic != "!!!": 
        try:
            statement = Statement(logic)
            Printer(statement)
        except Exception as e:
            print(e)
        logic = input("logic: ")

if __name__ == "__main__":
    main()
