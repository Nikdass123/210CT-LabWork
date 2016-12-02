class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print "List: ",",".join(values)
      def listRemove(self,value):
        currentNode = self.head # 
        while currentNode != None:
            if currentNode.value == value:
                if currentNode.prev != None:
                    currentNode.prev.next = currentNode.next
                else:
                    self.head = currentNode.next
                if currentNode.next != None:
                    currentNode.next.prev = currentNode.prev
                else:
                    self.tail = currentNode.prev
            currentNode = currentNode.next
          
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(8))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(3))
      l.insert(l.head,Node(2))
      l.insert(l.head,Node(7))
      l.insert(l.head,Node(9))
      l.display()
      l.listRemove(3)
      l.display()