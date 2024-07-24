'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 14:39:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-24 11:00:00
@Title :Program to find the week day of the date

'''


def day_of_week(day,month,year):
    """
    Description:
          function will return weekday in form of integer(0-6)
    Parameter:
        day,month,year:this paramters are used to calculate week day
    return:
        integer          
    """
    
    if month < 3:
            year -= 1
            month += 12
        
    
    year = year - (14 - month) // 12
    x = year + year // 4 - year // 100 + year // 400
    month = month + 12 * ((14 - month) // 12) - 2
    
    
    day = (day + x + (31 * month) // 12) % 7
    
    return day

def main():
      try:
            year=int(input("Enter the year: "))
            month=int(input("Enter the month: "))
            day=int(input("Enter the day between 1 to 31: "))
            if not (1 <= month <= 12):
                raise ValueError("Month must be between 1 and 12.")
            if not (1 <= day <= 31):  
                raise ValueError("Day must be between 1 and 31.")
            if year <= 0:
                raise ValueError("Year must be a positive integer.")
            week_dict={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
            weekday=day_of_week(day,month,year)
            print(f"weekday for date->{day}:{month}:{year} is {week_dict.get(weekday)}")
      except ValueError as e:
           print(f"Invalid input: {e}")
              
if __name__=='__main__':
   main()
    

