import time

my_time = int(input("Please enter your time in seconds: "))

for x in range(my_time, 0, -1):#or jst use reversed to count backwards lol
   seconds = x % 60
   minutes = int(x / 60) % 60
   hours = int(x / 3600)
   print(f"{hours:02}:{minutes:02}:{seconds:02}") #:02 is basically zero padding the digits
   time.sleep(1) #basically our program sleeps or shuts down for 3 seconds in this case

print("And Time.")

