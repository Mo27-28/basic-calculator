#basic calculator code
try: 
  num1=float(input('enter the first number: '))
except: 
  print('value is not a number')
  quit()

try:
  num2=float(input('Enter second number: '))
except:
  print('value is not a number')
  quit()
  
operator = input('Enter operator: ')


if operator == '+' :
  print ('the result is: ', num1+num2)
elif operator == '-' :
  print( 'the result is:', num1-num2)
elif operator == '*' :
  print('the result is: ', num1*num2)
elif operator == '/' :
  print('the result is : ', num1/num2)
else:
  print('invalid operator')
  
