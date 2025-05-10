class queue:
    def __init__(self):
        self.list=[]
        self.front=0
        self.rear=0
    def enque(self,val):
        self.list.append(val)
        self.rear+=1
    def deque(self):
        self.list[self.front]=None
        self.front+=1
    def display(self):
        print(self.list)
ll=queue()
while 1:
 c=int(input('''enter 1 for enque
enter 2 for deque
enter 3 for display
enter 4 to exit:'''))
 match c:
     case 1:
         b=int(input('enter the value to enque:'))
         ll.enque(b)
     case 2:
         ll.deque()
     case 3:
         ll.display()
     case 4:
         break
