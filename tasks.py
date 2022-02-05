from datetime import datetime, timedelta

def isint(number):
    try:
        int(number)

        return True
    except ValueError:
        return False

def isfloat(num):
    try:
        float(num)

        return True
    except ValueError:
        return False

def military_to_standard_converter(military_time):
    if not ":" in military_time:
        return "Please enter a military timestamp formatted as HH:MM!"

    for unit in military_time.split(":"):
        if not unit.isdecimal():
            return "Please enter a military timestamp formatted as HH:MM!"

    hours, minutes = [int(unit) for unit in military_time.split(":")]

    if not (hours in range(0, 24) and minutes in range(0, 60)):
        return "Please enter a military timestamp formatted as HH:MM!"

    if hours == 0 & minutes == 0:
        return "12:00 AM"

    setting = "PM" if hours >= 12 else "AM"

    hours -= 12 if hours > 12 else 0
    
    return "{}:{} {}".format(hours, minutes, setting)

def pythagorean_theorem_calculator(mode, number1, number2):
    if not (number1.isdecimal() and number2.isdecimal()):
        return "Please enter lengths as positive numbers between 1 and 100!"

    if mode == "H":
        legA, legB = int(number1), int(number2)

        if not (legA in range(1, 100) and legB in range(1, 100)):
            return "Please enter lengths as positive numbers between 1 and 100!"

        hypotenuse = round((legA * legA + legB * legB) ** 0.5, 2)

        return "The length of the hypotenuse is {}".format(hypotenuse)
    elif mode == "L":
        hypotenuse, legA = int(number1), int(number2)

        if not (hypotenuse in range(legA + 1, 100) and legA in range(1, hypotenuse)):
            return "Please enter lengths as positive numbers between 1 and 100!"

        legB = round((hypotenuse ** 2 - legA **2) ** 0.5, 2)

        return "The length of the second leg is {}".format(legB)

def parentheses_balance_checker(s):
    if len(s) >= 128:
        return "Please enter a string of length < 128 with parentheses! Additional non-parentheses characters are permitted."

    count = 0

    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False

    return "All parentheses are {} in the input string".format("balanced" if count == 0 else "not balanced")

def square_checker(number):
    if not number.isdecimal():
        return "Please enter a positive integer < 5000000!"

    if int(number) > 2000000:
        return "Please enter a positive integer < 2000000!"

    sqrt_number = float(number) ** 0.5

    is_square = int(sqrt_number) == sqrt_number

    return "{} {} a perfect square".format(number, "is" if is_square else "isn't")

def secret_function(text):
    if len(text) >= 16:
        return "Please enter a piece of text of length < 16 to run the secret function on!"

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    even_letters = 0

    for letter in text:
        if letter.upper() in alphabet:
            if alphabet.index(letter.upper()) % 2 == 0:
                even_letters += 1

    return even_letters

def leap_year_checker(year):
    if not year.isdecimal():
        return "Please enter a year as a positive integer < 2000000!"

    year = int(year)

    if year >= 2000000:
        if not year.isdecimal():
            return "Please enter a year as a positive integer < 2000000!"
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def monoalphabetic_substitution(plaintext):
    if len(plaintext) >= 128:
        return "Please enter a piece of text of length < 128 to encrypt!"

    plaintext_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext_alphabet = "RBUWVCXOYDAESFZGHJMKNLIPTQ"

    ciphertext = ""

    for character in plaintext:
        if character in plaintext_alphabet:
            i = plaintext_alphabet.index(character)

            ciphertext += ciphertext_alphabet[i]
        else:
            ciphertext += character

    return ciphertext

def number_weaver(a, b):
    if not (a.isdecimal() and b.isdecimal() and len(a) < 128 and len(b) < 128):
        return "Please enter two integers with less than 128 digits!"

    a = int(a)
    b = int(b)

    pos = 1
    num = 0
    
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

def secret_word_counter(s):
    if len(s) >= 1024:
        return "Please enter a string of length < 1024 to scan!"
    
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

def descriptive_statistics(data):
    data = data.replace(",", " ").replace("  ", " ").split(" ")
    
    if len(data) < 2 or len(data) > 50:
        return "Please enter a list of between 2 and 50, inclusive, numbers < 2000000 without commas separated by commas or spaces!"
        
    for d in range(len(data)):
        datum = data[d]
        
        if not isint(datum):
            return "Please enter a list of between 2 and 50, inclusive, numbers < 2000000 without commas separated by commas or spaces!"

        data[d] = int(datum)

    data.sort()

    sample_size = len(data)

    mean = round(sum(data)/sample_size, 2)

    if sample_size % 2 == 0:
        median = (data[sample_size//2 - 1] + data[sample_size//2])/2
    else:
        median = data[sample_size//2]

    mode = 0
    mode_count = 0
    mode_changed = False
    
    for datum in data:
        if datum != mode:
            datum_count = data.count(datum)
            
            if datum_count > mode_count:
                mode = datum
                mode_count = datum_count
                mode_changed = True
    
    if not mode_changed:
        mode = "More than one mode, last mode was {}".format(mode)

    data_min = data[0]

    data_max = data[sample_size - 1]

    data_range = data_max - data_min
    
    sum_of_squared_differences = 0
    
    for datum in data:
        squared_difference = (datum - mean) ** 2

        sum_of_squared_differences += squared_difference
    
    standard_deviation = round((sum_of_squared_differences/(sample_size - 1)) ** 0.5, 4)

    return """
    Mean: {}
    Median: {}
    Mode: {}
    Minimum: {}
    Maximum: {}
    Range: {}
    Standard Deviation: {}
    """.format(mean, median, mode, data_min, data_max, data_range, standard_deviation)

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    
    if len(hex) != 6:
        return "Please enter a valid hexadecimal color code (# optional)!"

    rgb = []

    for i in range(0, 2, 4):
        val = hex[i:i+2]
        rgbVal = 0
        base = 1

        for i in val:
            i = ord(i)

            if i >= 48 and i <= 57:
                rgbVal += (i - 48) * base
            elif i >= 65 and i <= 70:
                rgbVal += (i - 55) * base
            else:
                return "Please enter a valid hexadecimal color code (# optional)!"

            base *= 16

        rgb.append(str(rgbVal))

    return rgb

def primality_tester(number):
    if not number.isdecimal():
        return "Please enter a positive integer under 1000!"

    number = int(number)

    if number >= 1000:
        return "Please enter a positive integer under 1000!"

    if number < 2:
        return False

    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False

    return True

def typing_test(quote_selection):
    if not isint(quote_selection):
        return "Please type a number from 1 to 5 to select a quote!"
    
    quote_number = int(quote_selection)
    
    if quote_number in range(1, 6):
        quotes = [
            "Never gonna give yo up, never gonna let you down, never gonna turn around and desert you.",
            "The quick brown fox jumped over the lazy dog.",
            "At the end of the 50 minute period, teams will submit their program as source code (.cpp, .java, .py, etc.).",
            "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?",
            "The first recorded competition that called itself Science Olympiad was held in 1974 at St. Andrews Presbyterian College in North Carolina."
        ]
        
        quote = quotes[quote_number]
    else:
        return "Please type a number from 1 to 5 to select a quote!"
    
    print(quote)
    
    start_time = datetime.now()
    
    user_input = input("Type the quote!\n")
    
    end_time = datetime.now()
    
    quote_len = len(quote)
    user_input_len = len(user_input)
    
    correct_characters = 0
    
    for c in range(quote_len):
        if c >= user_input_len:
            break
        elif user_input[c] == quote[c]:
            correct_characters += 1
    
    correct_words = correct_characters/5
    
    time = (end_time - start_time).total_seconds()
    wpm = correct_words/time * 60
    accuracy = correct_characters/quote_len * 100

    return "You typed {} words ({} characters) at an average of {} words per minute for {} seconds with an accuracy of {}%!".format(round(correct_words, 1), correct_characters, round(wpm), round(time), round(accuracy))

def main():
    now = datetime.now()
    date = now.strftime('%A %d/%m/%Y')
    time = now.strftime('%I:%M %p')

    print("""
    Welcome the task selection menu!

    Today's date: {}
    Program start time: {}
    --------------------------------------------
    | 1.  Military to standard time converter  |
    | 2.  Pythagorean theorem calculator       |
    | 3.  Parentheses balancer                 |
    | 4.  Square checker                       |
    | 5.  Secret function                      |
    | 6.  Leap year checker                    |
    | 7.  Monoalphabetic substitution          |
    | 8.  Number weaver                        |
    | 9.  Secret word counter                  |
    | 10. Descriptive statistics               |
    | 11. Hex-to-RGB converter                 |
    | 12. Primality tester                     |
    | 13. Typing test                          |
    --------------------------------------------
    """.format(date, time))

    task = input("Choose a task to run by entering the corresponding number!\n").replace(".", "")

    if not task.isdecimal():
        return print("Please enter a valid task number between 1 and 15!")

    task_num = int(task)

    output_string = ""

    if task_num == 1:
        print("This task will convert a military timestamp to a standard 12-hour timestamp.")
        input_string = input("Please enter a military timestamp formatted as HH:MM!\n")
        output_string = military_to_standard_converter(input_string)
    elif task_num == 2:
        print("This task will calculate the missing side length given two sides of a triangle using the Pythagorean theorem.")
        
        input_string_1 = input("What would you like to calculate? Type H for hypotenuse or L for leg!\n")
        
        if input_string_1 == "H":
            input_string_2 = input("Let's calculate the hypotenuse! Please enter the first leg length as a positive number < \n")
            input_string_3 = input("Please enter the second leg length as a positive number between 1 and 100!\n")

            output_string = pythagorean_theorem_calculator("H", input_string_2, input_string_3)
        elif input_string_1 == "L":
            input_string_2 = input("Let's calculate the missing leg length! Please enter the hypotenuse length as a positive number < \n")
            input_string_3 = input("Please enter the first leg length as a positive number between 1 and 100!\n")

            output_string = pythagorean_theorem_calculator("H", input_string_2, input_string_3)
        else:
            output_string = "Please enter a valid option!"
    elif task_num == 3:
        print("This task will check whether or not a string with parentheses is balanced based on whether or not every open parenthesis is closed correctly.")
        input_string = input("Please enter a string of length < 128 with parentheses! Additional non-parentheses characters are permitted.\n")
        output_string = parentheses_balance_checker(input_string)
    elif task_num == 4:
        print("This task will check whether or not a number is a perfect square.")
        input_string = input("Please enter a positive integer < 2000000!\n")
        output_string = square_checker(input_string)
    elif task_num == 5:
        print("This task will run a secret function on a piece of text, outputting a number.")
        input_string = input("Please enter a piece of text of length < 16 to run the secret function on!\n")
        output_string = secret_function(input_string)
    elif task_num == 6:
        print("This task will check whether or not a given year is a leap year.")
        input_string = input("Please enter a year as a positive integer < 2000000!\n")
        output_string = leap_year_checker(input_string)
    elif task_num == 7:
        print("This task will encrypt a piece of text using a predetermined monoalphabetic substitution.")
        input_string = input("Please enter a piece of text of length < 128 to encrypt!\n")
        output_string = monoalphabetic_substitution(input_string)
    elif task_num == 8:
        print("This task \"weaves\" two numbers together.")
        input_string_1 = input("Please enter the first integer with less than 128 digits!\n")
        input_string_2 = input("Please enter the second integer with less than 128 digits!\n")
        output_string = number_weaver(input_string_1, input_string_2)
    elif task_num == 9:
        print("This task will print the number of appearances of the colloquial term for a certain secret furry house pet in a string.")
        input_string = input("Please enter a string of length < 1024 to scan!\n")
        output_string = secret_word_counter(input_string)
    elif task_num == 10:
        print("This task will print the mean, median, mode, range, minimum, maximum, and sample standard deviation of a dataset.")
        input_string = input("Please enter a list of between 2 and 50, inclusive, numbers < 2000000 without commas separated by commas or spaces!\n")
        output_string = descriptive_statistics(input_string)
    elif task_num == 11:
        print("This task will convert a hexadecimal color code to RGB.")
        input_string = input("Please enter a valid hexadecimal color code (# optional)!\n")
        output_string = hex_to_rgb(input_string)
    elif task_num == 12:
        print("This task will check whether or not a given integer is a prime number.")
        input_string = input("Please enter a positive integer under 1000!\n")
        output_string = primality_tester(input_string)
    elif task_num == 13:
        print("This task will perform a typing test using one of five quotes! For this test, each group of 5 characters counts as a word.")
        input_string = input("Please type a number from 1 to 5 to select a quote and press enter when you are ready to start!\n")
        output_string = typing_test(input_string)
    else:
        output_string = "Please select a valid task!"

    print(output_string)

main()