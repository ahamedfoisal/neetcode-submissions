class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operator = ["*", "+", "-", "/"]
        s, t = 0,0
        for i in tokens:
            if i in operator:
                s=numbers.pop()
                t = numbers.pop()
                if i == "*":
                    numbers.append(t*s)
                elif i == "/":
                    numbers.append(int(t/s))                
                elif i == "+":
                    numbers.append(t+s)                
                else:
                    numbers.append(t-s)
            else: numbers.append(int(i))
        return numbers.pop()