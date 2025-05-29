a = int(input())

leap = (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
huluculu = (a % 15 == 0)
bulukulu = (a % 55 == 0 and leap)

printed = False
if leap:
    print("This is leap year.")
    printed = True
if huluculu:
    print("This is huluculu festival year.")
    printed = True
if bulukulu:
    print("This is bulukulu festival year.")
    printed = True
if not printed:
    print("This is an ordinary year.")
print()