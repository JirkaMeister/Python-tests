# Jirka's python test library
This is a simple python test library, which will be updated based on personal needs. Its main purpose is to provide a simple way to write tests in python and customize the output format. It is not intended to be a full-featured test framework, but rather a simple tool to help with writing tests. It is also not intended to be a replacement for the standard python unittest module. 

## Usage
The library is intended to be used as a source file in your project and cannot be installed as a package. To use it, simply copy the file `test.py` to your project and import it. The library provides a single class `Test` which can be used to write tests. The class provides the following methods:

* `expectEqual(a, b)`: Used in tests. Expects that `a` is equal to `b`. If not, the test fails, but rest of the cases are still executed.
  
* `expectNotEqual(a, b`: Used in tests. Expects that `a` is not equal to `b`. If not, the test fails, but rest of the cases are still executed.

These methods can be used to test any type of data, including lists, dictionaries, etc. They are intended to be used in TestClasses, which must inherit from the `TestClass` class. In this class you can define indivial tests as methods. Names of these methods must not start and end with `__`. In these methods you can use the `expectEqual` and `expectNotEqual` methods to test your code. Every `expect` method used is counted as a single test case. To run the tests simply create instance of your `TestClass`. The class will automatically run all tests and print the results to the standard output.