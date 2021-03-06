#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.


class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        temp = []
        while len(self.queue) > 0:
            temp.append(self.queue.pop())
        self.queue.append(x)
        while len(temp) > 0:
            self.queue.append(temp.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        elem = self.queue.pop()
        self.queue.append(elem)
        return elem

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.queue == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
