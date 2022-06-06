#project deadline
#importing the datetime module 
import datetime
print('PLEASE THE DEADLINE SHOULD BE WRITTEN IN A TWO(2) DIGIT FORMAT !!!')
#Requesting input from user
ultimatum=input('when is the deadline?(dd/mm/yy) ')
#Setting the variables to time covertible
currentdate=datetime.date.today()
deadline=(datetime.datetime.strptime(ultimatum,'%d/%m/%y')).date()
days=deadline - currentdate
#converting the dates into days and weeks
num_days=days.days %7
num_weeks=days.days //7
sum_days=num_weeks*7 + num_days
if num_days == 0 and num_weeks > 1:
   print(f'You have {num_weeks} weeks to submit your project !!!')
else :      
   print(f'You have  {num_weeks} weeks and {num_days} days  to submit your project !!!')
print(f'Equivalent to {sum_days} days to submit your project !!!')