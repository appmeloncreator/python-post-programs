import random
import time

lower_case = "qwertyuiopasdfghjkl"
upercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
symbal = "!@#$%^&*()_+';,./`"
number = "1234567890"
length = 12

all = lower_case + upercase + symbal + number

password = "".join(random.sample(all,length))

print("Your password is"),
print(password)

time.sleep(10)