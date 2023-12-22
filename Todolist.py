 #to do list python program
# make a list
# take input
# read write and remove the task
class todo:
    def __init__(self):
        self.a=[]

    def add(self):
        task=input("enter the task to add")
        self.a.append(task)

    def rem(self):
        task=input("enter the task to remove in string or numeric form ")
        if task in self.a:
            self.a.remove(task)
            print('the task is removed')
        elif 1<=int(task)<=len(self.a):
            self.a.pop(int(task)-1)
        else:
            print('task in not present')


    def show(self):
        if self.a:
            print('tasks are :\n')
            for i,value in enumerate(self.a):
                print(f"{i+1}:{value}")

p=todo()
while True:
    c=input('enter the character')
    if c=='a':
        p.add()
    elif c=='r':
        p.rem()
    elif c=='s':
        p.show()
    elif c=='quit':
        break
    else:
        print('invalid keyword')
        break





