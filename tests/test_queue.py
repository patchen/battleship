import unittest
from queue import Queue
from queue import EmptyQueueError
'''Based off lecture test_stack'''


class QueueEmptyTestCase(unittest.TestCase):
    """Test behaviour of an empty Queue."""

    def setUp(self):
        """Set up an empty queue."""
        self.queue = Queue()

    def tearDown(self):
        """Clean up."""

        self.queue = None

    def testIsEmpty(self):
        """Test is_empty() on empty Queue."""

        self.assertTrue(self.queue.is_empty(), \
                        'is_empty returned False on an empty Queue!')

    def testPush(self):
        """Test enqueue to empty Queue."""

        self.queue.enqueue("foo")
        self.assertEqual(self.queue.dequeue(), "foo", \
                         'Wrong item on top of the Queue!\
                                  Expected "foo" here.')

    def testEmpty(self):
        """Test dequeue from an empty Queue."""

        try:
            self.queue.dequeue()
            self.fail('dequeue from empty queue does not produce error')
        except EmptyQueueError:
            pass

    def testDel(self):
        """Test queue_del from Queue"""

        self.queue.queue_del()
        self.assertEqual(self.queue.contents, [], \
                         'Wrong item on top of the Queue! \
                                     Expected "foo" here.')


class QueueAllTestCase(unittest.TestCase):
    """Tests of (non-empty) Queue."""

    def setUp(self):
        """Set up an empty queue."""

        self.queue = Queue()

    def tearDown(self):
        """Clean up."""

        self.queue = None

    def testAll(self):
        """Test enqueueing and dequeueing multiple elements."""

        for item in range(20):
            self.queue.enqueue(item)
            self.assertFalse(self.queue.is_empty(), \
                            'is_empty() returned True on a non-empty Queue!')

        expect = 0
        while not self.queue.is_empty():
            self.assertEqual(self.queue.dequeue(), expect, \
                             'Something wrong on top of the Queue! Expected ' \
                             + str(expect) + '.')
            expect = expect + 1


def empty_suite():
    """Return a test suite for an empty Queue."""

    return unittest.TestLoader().loadTestsFromTestCase(QueueEmptyTestCase)


def all_suite():
    """Return a comprehensive test suite for a non-empty Queue."""

    return unittest.TestLoader().loadTestsFromTestCase(QueueAllTestCase)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(empty_suite())
    runner.run(all_suite())
