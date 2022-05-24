#basic calculator code
num1=float(input('enter the first number: '))
num2=float(input('Enter second number: '))
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
  