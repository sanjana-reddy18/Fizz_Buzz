Code in any language the FizzBuzz Code Kata using TDD.  
Write a short program that prints each number from 1 to 100 on a new line.  
For each multiple of 3, print "Fizz" instead of the number.  
For each multiple of 5, print "Buzz" instead of the number.  
For numbers that are multiples of both 3 and 5, print "FizzBuzz" instead of the number.  

**Example of TDD Process in FizzBuzz**  
**Using the FizzBuzz example:**

  
Red: Start by writing a test that expects the function to return "1" for the input 1.  
Run the test and watch it fail because the fizz_buzz function doesn’t yet return "1" for input 1.  
Green: Implement the code that simply returns "1" for 1, without worrying about the entire FizzBuzz logic.  
Run the test, which should now pass for this specific case.  
Refactor: Since the function currently only handles 1, add more cases by repeating the cycle:  
Write tests for "Fizz" when the number is a multiple of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.  
Implement code to handle each case, running tests to confirm correctness, and then refactor to improve readability and structure. Use
