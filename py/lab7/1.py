class node:
    def __init__(self,val):
         self.data=val
         self.next=None
class linkedlist:
     def __init__(self):
          self.head=None
     def insert(self,val,pos):
          newnode=node(val)
          if not self.head:
           self.head=newnode
          temp=self.head
          if pos==1:
              self.head=newnode
              return
          if not self.head and pos > 1:
              print("Invalid position")
              return
          temp=self.head
          for i in range(1,pos-1):
              if not temp.next:
                  break
              temp=temp.next
          newnode.next=temp.next
          temp.next=newnode
     def delete(self,pos):
          temp=self.head
          if not temp:
              print("list empty")
              return
          if pos==1:
              self.head=temp.next
              temp=None
              return
          prev=None
          for i in range(1,pos-1):
              if not temp.next:
                  print("invalid position")
                  return
              prev=temp
              temp=temp.next
          if not temp.next:
              print("invalid")
              return
          prev.next=temp.next
          temp=None
     def display(self):
         temp=self.head
         while  temp:
             print(temp.data,end="->")
             temp=temp.next
         print("None")
ll=linkedlist()
while 1:
 c=int(input('''enter 1 for insertion
enter 2 for deletion
enter 3 for display
enter 4 to exit:'''))

 match c:
     case 1:
         a=int(input('enter the pos at which u want to insert:'))
         b=int(input('enter the value:'))
         ll.insert(b,a)
     case 2:
         a=int(input('enter the pos at which u want to delete:'))
         ll.delete(a)
     case 3:
         ll.display()
     case 4:
         break