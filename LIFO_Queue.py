class QueueError(IndexError):  # Choose base class for the new exception.
       # def __init__(self):
           # IndexError.__init__(self)

        def geterror(self):
            #if self.IndexError:
            return "Stack is Empty!"
            #pass

class Queue:
    def __init__(self):
        self.__stack_list = []

    def put(self, elem):
        self.__stack_list.append(elem)

    def get(self):
        try:
            elem = self.__stack_list[0]
            del self.__stack_list[0]
            return elem

        except:
            error = QueueError()
            print(error.geterror())
            #raise                    # We propagate an exception outside the object

        #except:
            #print ("There is an unexpected error!")

class SuperQueue(Queue):
    #def __init__(self):


    def isempty(self):
        try:
            if self.get(self):
                return True
            else:
                return False
        except:
            return False



que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
