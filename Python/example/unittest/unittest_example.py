#!/usr/bin/env python

import unittest


class TestAssert(unittest.TestCase):
    """sample unit test example"""

    def test_fail_example(self):
        self.assertEqual('foo', 'FOO')

    def test_success_example(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
