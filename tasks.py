import math

# parentheses balancer
def parentheses_balancer(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False

    if count == 0:
        return True
    else:
        return False

def leap_year(year):
    if not year.isdecimal():
        return "Please enter a valid year"

    year = int(year)
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def weave(a, b):
    pos = 1
    num = 0
    if not (a.isdecimal() and b.isdecimal()):
        return "Please enter two valid integers"

    a = int(a)
    b = int(b)
    
    while a > 0 or b > 0:
        digit = b % 10
        digit *= pos
        num += digit
        b //= 10
        pos *= 10

        digit = a % 10
        digit *= pos
        num += digit
        a //= 10
        pos *= 10

    return num

def hex_to_rgb(h):
    h = h.lstrip('#')
    rgb = ""
    
    if len(h) != 6:
        return "Please enter a valid hex color code"
    
    for i in (0, 2, 4):
        val = h[i:i+2]
        rgbVal = 0
        base = 1
        for i in val:
            i = ord(i);
            if (i) >= 48 and (i) <= 57:
                rgbVal += (i - 48) * base
            elif i >= 65 and i <= 70:
                rgbVal += (i - 55) * base
            else:
                return "Please enter a valid hex color code"
            base *= 16
        rgb += (str(rgbVal) + " ")
    return rgb

def word_count(s):
    word = "cat"
    count = 0
    arr = s.split()
    for i in arr:
        if i[0:3] == word:
            if len(i) == 3:
                count += 1
            elif len(i) > 3 and i[3] in ('?', ',', '.', '!'):
                count += 1
    return count

def timeConvert(miliTime):
    hours, minutes = miliTime.split(":")
    hours, minutes = int(hours), int(minutes)
    setting = "AM"
    if hours == 0 & minutes == 0:
        print("12:00 AM")
    elif hours > 12:
        setting = "PM"
        hours -= 12
        print(("%02d:%02d " + setting) % (hours, minutes))
    else:
        print(("%02d:%02d " + setting) % (hours, minutes))

def pythag(numbers):
        legA, legB = numbers.split(" ")
        legA = int(legA)
        legB = int(legB)
        print(math.sqrt(legA*legA + legB*legB))

def square_checker(number):
    print(math.sqrt(int(number)) - int(math.sqrt(int(number))) == 0)

def most_frequency(my_string):
    max_frequency = {}
    for i in my_string:
        if i in max_frequency:
            max_frequency[i] += 1
        else:
            max_frequency[i] = 1
    print(max(max_frequency, key = max_frequency.get))

def primality_tester(a):
    a = int(a)
    if a < 2: return False
    for x in range(2, int(math.sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True
most_frequency("heyyy wsp")
square_checker("16")
timeConvert("13:45")
pythag("7 18")
print(primality_tester("36"))
