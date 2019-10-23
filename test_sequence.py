import unittest

from sequence import Sequence

class SequenceTestCase(unittest.TestCase):
    
    def test_get_weight(self):
        sequence = Sequence("G")
        self.assertAlmostEqual(Sequence.WEIGHTS["G"],
                                sequence.get_weight(),
                                msg="Weight returned was unexpected")