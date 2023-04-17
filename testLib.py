from colorama import Fore

class TestClass:
    totalCases = 0
    totalPassedCases = 0
    
    totalTests = 0
    totalPassedTests = 0

    def __runAllTests__(self):
        for name in dir(self):
            obj = getattr(self, name)
            if callable(obj) and name[:2] != '__' and name != "expectEqual":
                TestClass.cases = 0
                TestClass.passedCases = 0
                TestClass.totalTests += 1
                print(Fore.GREEN + "[TEST {:2}] ".format(TestClass.totalTests) + Fore.RESET + "Name: " + name)
                obj()
                if TestClass.passedCases == TestClass.cases:
                    print(Fore.GREEN + "[OK]" + Fore.RESET)
                else:
                    print(Fore.RED + "[ERROR]" + Fore.RESET)
                    
                
    def __init__(self):
        print("Started testing!")
        print("______________________________________\n")
        self.__runAllTests__()
        print("______________________________________\n")
        self.__printResults__()
    
    def __printSuccessfulTest__():
        print(Fore.GREEN + "   [Case {:2}: OK]".format(TestClass.cases) + Fore.RESET)
        
    def __printFailedTest__(self, value, expectedValue):
        print(Fore.RED +"   [Case {}: ERROR]".format(TestClass.cases) + Fore.RESET)
        print("     Expected value: {}".format(expectedValue))
        print("     Received value: {}".format(value))
        print(Fore.RED +"   [===========]" + Fore.RESET)

    def __printResults__(self):
        print("All tests finished!")
        print("Result:", end = " ")
        if TestClass.totalPassedCases == TestClass.totalCases:
            print(Fore.GREEN, end = "")
        elif TestClass.totalPassedCases < TestClass.totalCases/2:
            print(Fore.RED, end = "")
        else:
            print(Fore.YELLOW, end = "")
        print("{} / {} ".format(TestClass.totalPassedCases, TestClass.totalCases) + Fore.RESET + "tests passed!\n")

    def __addCase__():
        TestClass.totalCases += 1
        TestClass.cases += 1

    def __addSuccessfulCase__():
        TestClass.passedCases += 1
        TestClass.totalPassedCases += 1
    

    def expectEqual(self, value, expectedValue):
        TestClass.__addCase__()
        if value == expectedValue:
           TestClass.__addSuccessfulCase__()
           TestClass.__printSuccessfulTest__()
        else:
            TestClass.__printFailedTest__(self, value, expectedValue)

    def expectNotEqual(self, value, expectedValue):
        TestClass.__addCase__()
        if value != expectedValue:
           TestClass.__addSuccessfulCase__()
           TestClass.__printSuccessfulTest__()
        else:
            TestClass.__printFailedTest__(self, value, expectedValue)

    