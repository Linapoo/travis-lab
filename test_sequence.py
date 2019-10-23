import unittest

from sequence import sequence

class SequenceTestCase(unittest.TestCase):
    
    def test_get_weight(self):
        sequence = Sequence("G")
        self.assertAlmostEqual("get_weight",
                                sequence.get_weight(),
                                delta=0.01,
                                msg="Weight returned was unexpected")