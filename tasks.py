# parentheses balancer
def parenthesesBalancer(s):
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

# leap year
# year must be a valid year
def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

# weave
# a and b must be positive integers
def weave(a, b):
    pos = 1;
    num = 0;

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

# hex to rgb
# h should be a valid hexadecimal color code
def hexToRGB(h):
    h = h.lstrip('#')
    rgb = ""
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
            base *= 16
        rgb += (str(rgbVal) + " ")
    return rgb
