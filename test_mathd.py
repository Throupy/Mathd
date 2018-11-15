import unittest
import mathd


class TestMathd(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(mathd.fib(5), [1,1,2,3,5])
        self.assertRaises(ValueError, mathd.fib, 0)
        self.assertRaises(ValueError, mathd.fib, -10)

    def test_tri_nums(self):
        self.assertEqual(mathd.tri_nums(5), [1, 3, 6, 10, 15])
        self.assertRaises(ValueError, mathd.tri_nums, -10)
        self.assertRaises(ValueError, mathd.tri_nums, 0)

    def test_square_nums(self):
        self.assertEqual(mathd.square_nums(5), [1, 4, 9, 16, 25])
        self.assertRaises(ValueError, mathd.square_nums, -10)
        self.assertRaises(ValueError, mathd.square_nums, 0)

    def test_linear_seq(self):
        self.assertEqual(mathd.linear_seq([1,3,5,7], 5), 9)
        self.assertRaises(ValueError, mathd.linear_seq, [-1,45,23,4], 6)
        self.assertRaises(ValueError, mathd.linear_seq, [-3], 6)
        self.assertRaises(ValueError, mathd.linear_seq, [], 6)

    def test_quadr_seq(self):
        self.assertEqual(mathd.quadr_seq([5,14,27,44], 5), 65)
        self.assertEqual(mathd.quadr_seq([5,14,27,44], 10, True), "2n²+3n+0")
        self.assertRaises(ValueError, mathd.quadr_seq, [4], 6)

    def test_lcm(self):
        self.assertEqual(mathd.lcm(6,9), 18)
        self.assertRaises(ValueError, mathd.lcm, 0, 10)
        self.assertRaises(ValueError, mathd.lcm, 10, 0)
        self.assertRaises(ValueError, mathd.lcm, 0, 0)

    def test_hcf(self):
        self.assertEqual(mathd.hcf(6,9), 3.0)
        self.assertRaises(ValueError, mathd.hcf, 0, 10)
        self.assertRaises(ValueError, mathd.hcf, 10, 0)
        self.assertRaises(ValueError, mathd.hcf, 0, 0)

    def test_avg(self):
        self.assertEqual(mathd.avg([2,4,6]), 4)
        self.assertEqual(mathd.avg([2.8,6.9,123.4,9.0]), 35.525)
        self.assertRaises(ValueError, mathd.avg, ["wibble", "wobble"])
        self.assertRaises(ValueError, mathd.avg, [])

    def test_mode(self):
        self.assertEqual(mathd.mode([2,2,2,3,3,4]), 2)
        self.assertEqual(mathd.mode([3,2,4]), 2)
        self.assertRaises(ValueError, mathd.mode, ["wibble", "wobble"])
        self.assertRaises(ValueError, mathd.mode, [])

if __name__ == '__main__':
    unittest.main()
