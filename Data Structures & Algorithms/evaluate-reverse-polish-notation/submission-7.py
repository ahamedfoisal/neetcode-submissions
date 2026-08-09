class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = []
        numbers = []
        operator = ["*", "+", "-", "/"]
        number = ["1","2","3","4","5","6","7","8","9","0"]
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