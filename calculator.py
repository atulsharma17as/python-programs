#simple calculator
class cal:
    def __init__(self):
        self.a=int(input('Enter the first number'))
        self.b=int(input('Enter the second number '))

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def mod(self):
        return self.a%self.b
    def pow(self):
        return self.a**self.b
o=cal()
while True:
    c=input('Enter the character ')
    if c=='a':
        print(o.add())
        break
    elif c=='s':
        print(o.sub())
        break
    elif c == 'd':
        print(o.div())
        break
    elif c == 'mo':
        print(o.mod())
        break
    elif c=='p':
        print(o.pow())
        break
    elif c=='m':
        print(o.mul())
        break
    else:
        print('invalid charater')
        break
