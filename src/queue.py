class EmptyQueueError(Exception):
    '''Raised when pop is called on an empty Queue.'''
    pass


class Queue(object):
    '''A First-in, first-out (FIFO) Queue of items'''

    def __init__(self):
        '''(Queue) -> None
        A new empty Queue.
        '''
        self.contents = []

    def __str__(self):
        return str(self.contents)

    def enqueue(self, v):
        '''(Queue, object) -> None
        Adds v to the end of the line.
        '''
        self.contents.append(v)

    def dequeue(self):
        '''(queue) -> object
        Remove and return the first item of the queue. Also adjusts front position.
        '''
        if self.is_empty():
            raise EmptyQueueError
        return self.contents.pop(0)

    def is_empty(self):
        '''(Queue) -> bool
        Return whether this Queue is empty.
        '''
        return not self.contents

    def queue_del(self):
        '''(Queue) -> None
        Deletes everything from the Queue.
        '''
        self.contents = []

