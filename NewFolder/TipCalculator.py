#Tip Calculator, Author: Mike Brown

#Problem Solving Life Cycle 
#1. Describe 
#           Construct a program that prompts the user for a bill 
#           and tip percentage and then displays the total amount of 
#           money charged for the sum of the bill and tip  
#2. Analyze 
#a.     Input: the pre-tip bill and tax percentage 
#b.     Output: the tax dollar amount and the total bill 
#c.         Relationship between Input & Output: the total bill is the result of taking 
#           the inital price and multiplying it by the percentage (decimal value)
#           given
#d.     Constraints: bill and percentage must be equal to or greater than 0
#3. Design (Done on Paper)                                                  
#4. Test: Cost: 200, Tip Percentage: 10% : Expected Output, Total: 220 : Actual Output, Total: 220 

#Implementation (Python)
#prompt the user for the bill and tip percentage 
bill = float(input('Please enter the billed amount: '))
tip_percentage = float(input('Please enter the tip as a percentage: '))

#calculate the tip cost and total using the information prompted above 
tip = float(bill*(tip_percentage/100))
total = float(bill + tip)

#output the information
print(f'A bill of ${bill:.2f} and a tip of {tip_percentage:.2f}% will add ${tip:.2f} to the bill.\nYour new total is: ${total:.2f}')
