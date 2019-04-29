#!/usr/bin/env python3

from unittest import (TestLoader, TestSuite, TextTestRunner, TestCase)
import timeit
import random

def test(modules):
    test_correctness(modules)
    test_performance(modules)

def test_correctness(modules):
    print("\n\n ~~ Correctness testing ~~")
    for module in modules:
        print("\nTesting: {}".format(module.__name__))
        suite = TestSuite()
        suite.addTest(ChopModuleTest(module))
        TextTestRunner(verbosity=2).run(suite)

def test_performance(modules):
    print("\n\n ~~ Performance testing ~~")
    global test_module
    for module in modules:
        test_module = module
        print("\nTesting: {}".format(module.__name__))
        print("Time: {}".format(timeit.timeit('chop_a_big_list(test_module.chop)',
                                              globals=globals(),
                                              number=500)))

def chop_a_big_list(chop):
    big_list_size = 10000
    tst = random.randrange(0, big_list_size)
    try:
        assert tst == chop(tst, list(range(big_list_size)))
    except AssertionError:
        print("Oops... Assertion error when chopping: element={} list range={}".format(tst, big_list_size))
        raise


class ChopModuleTest(TestCase):
    def __init__(self, module):
        TestCase.__init__(self, methodName='test_chop')
        self._chopper = module.chop
    
    def test_chop(self):
        chop = self._chopper
        self.assertEqual( 2, chop(3, [1, 2, 3, 4, 5]))
        self.assertEqual( 0, chop(1, [1, 2, 3, 4, 5]))
        self.assertEqual(-1, chop(6, [1, 2, 3, 4, 5]))
        self.assertEqual( 4, chop(5, [1, 2, 3, 4, 5]))
        self.assertEqual( 1, chop(2, [1, 2, 3, 4, 5]))

        self.assertEqual( 0, chop(2, [2, 3, 4, 5]))
        self.assertEqual( 1, chop(3, [2, 3, 4, 5]))
        self.assertEqual( 2, chop(4, [2, 3, 4, 5]))
        self.assertEqual( 3, chop(5, [2, 3, 4, 5]))
        self.assertEqual(-1, chop(1, [2, 3, 4, 5]))

        self.assertEqual( 0, chop(7, [7]))
        self.assertEqual(-1, chop(8, [7]))

        self.assertEqual(-1, chop(8, []))

        long_list = list(range(1000))
        for i in range(1000):
            self.assertEqual(i, chop(i, long_list))


import iterativechop
import recursivechop
import slicingchop
import enumeratedchop
import oochop

if __name__ == '__main__':
    test([
        iterativechop
      , recursivechop
      , slicingchop
      , enumeratedchop
      , oochop
    ])