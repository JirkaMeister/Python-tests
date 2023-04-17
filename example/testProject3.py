import sys
sys.path.append("../")
import testLib
from isj_proj3_xchara04 import first_odd_or_even, to_pilot_alpha

class TestProject3(testLib.TestClass):

    # Assignment 1
    def testSingleNumberInput(self):
        self.expectEqual(first_odd_or_even([0]), 0)
        self.expectEqual(first_odd_or_even([3]), 0)
        self.expectEqual(first_odd_or_even([2]), 0)
        self.expectEqual(first_odd_or_even([5]), 0)
        self.expectEqual(first_odd_or_even([3]), 0)

    def testSingleNumberType(self):
        self.expectEqual(first_odd_or_even([1, 3]), 0)
        self.expectEqual(first_odd_or_even([1, 3, 5, 7]), 0)
        self.expectEqual(first_odd_or_even([2, 8]), 0)
        self.expectEqual(first_odd_or_even([4, 8, 6, 8]), 0)

    def testSameAmount(self):
        self.expectEqual(first_odd_or_even([1, 2]), 0)
        self.expectEqual(first_odd_or_even([2, 3, 2, 3]), 0)
        self.expectEqual(first_odd_or_even([2, 3, 3, 2, 2, 3]), 0)

    def testMoreEvenNumbers(self):
        self.expectEqual(first_odd_or_even([2, 4, 3]), 3)
        self.expectEqual(first_odd_or_even([8, 4, 5, 6]), 5)
        self.expectEqual(first_odd_or_even([3, 8, 8, 5, 4, 3, 2]), 3)
        self.expectEqual(first_odd_or_even([2, 8, 1, 1, 4, 3, 2]), 1)

    def testMoreOddNumbers(self):
        self.expectEqual(first_odd_or_even([1, 3, 2]), 2)
        self.expectEqual(first_odd_or_even([9, 1, 4, 7]), 4)
        self.expectEqual(first_odd_or_even([4, 7, 7, 5, 4, 3, 2]), 4)
        self.expectEqual(first_odd_or_even([3, 9, 2, 2, 5, 8, 3]), 2)


    # Assignment 2
    def testValidInput(self):
        self.expectEqual(to_pilot_alpha("Smrz"), ["Sierra", "Mike", "Romeo", "Zulu"])
        self.expectEqual(to_pilot_alpha("BoReC"), ["Bravo", "Oscar", "Romeo", "Echo", "Charlie"])
        self.expectEqual(to_pilot_alpha("NIGht"), ["November", "India", "Golf", "Hotel", "Tango"])
        self.expectEqual(to_pilot_alpha("aDfJklPqUvWxY"), ["Alfa", "Delta", "Foxtrot", "Juliett", "Kilo", "Lima", "Papa", "Quebec", "Uniform", "Victor", "Whiskey", "Xray", "Yankee"])
    
    def testInvalidInput(self):
        self.expectEqual(to_pilot_alpha("Chybka_"), "Invalid input")
        self.expectEqual(to_pilot_alpha("IHateMyL1fe"), "Invalid input")
    

if __name__ == "__main__":
    TestProject3()