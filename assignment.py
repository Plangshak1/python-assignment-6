# assignment 
# ======================
# FUNCTIONS & SCOPE TASKS
# ==========

"""
Task 1:
Write a function that accepts two numbers (a and b) as parameters
and returns their sum.
Test the function by calling it with different numbers.
"""
def sum_of_two_numbers(a, b):
    return a + b

print(sum_of_two_numbers(3, 4))
print(sum_of_two_numbers(-2, 5))
print(sum_of_two_numbers(0, 0))  
print(sum_of_two_numbers(1.5, 2.5))


# 2
"""
def task2_square_number(n):
    Task 2:
    Write a function that accepts a number and returns its square.
    Example: square_number(5) → 25
    """
square_number(num):
    return num * num

print(square_number(3))
print(square_number(-2)
print(square_number(0))


"""
#def task3_greet_user(name):
    Task 3:
    Write a function that accepts a person's name as a parameter
    and prints a greeting message like: "Hello, John!"
    pass
"""

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("John")
greet_person("")

# 4
"""
def task4_area_of_rectangle(length, width):
   Task 4:
    Write a function that accepts the length and width of a rectangle
    and returns its area.
    Formula: area = length * width
    pass
"""
def area_of _rectangle(length, width):
    area = length * width
    return area

print(area_of_rectangle(8, 7))
print(area_of_rectangle(9, 5))


# 5
"""
def task5_perimeter_of_square(side):
   Task 5:
    Write a function that accepts the side length of a square
    and returns its perimeter.
    Formula: perimeter = 4 * side
    pass
"""
def perimeter_of_sqaure(side):
    perimeter = 4 * side
    return perimeter

print(perimer(9))
print(perimeter(54))



# 6
"""def task6_celsius_to_fahrenheit(celsius):
   Task 6:
    Write a function that converts a temperature from Celsius to Fahrenheit.
    Formula: (celsius * 9/5) + 32
   pass
"""
def_celcius_to_fahrenheit(celcius):
    cf = (celcius * 9/5) + 32
    return cf
print(celcius_to_fahrenheit(99))
print(celcius_to_fahrenheit(-16))


# 7
"""
def task7_find_max(a, b, c):
    Task 7:
    Write a function that accepts three numbers as parameters
    and returns the largest number.
    pass
"""
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(78, 43, 23))
print(find_max(-45, 0.1, 0))


# 8
"""
def task8_even_or_odd(n):
    Task 8:
    Write a function that accepts a number and returns
    "Even" if the number is even, and "Odd" if the number is odd.
    pass
"""
def even_or_odd(n):
    return "Even" if n%2 == 0 else "Odd"

print(even_or_odd(56))
print(even_or_odd(-89))
print(even_or_odd(1111))

# 9
"""
def task9_count_vowels(word):
   Task 9:
    Write a function that accepts a word as a parameter
    and returns the number of vowels (a, e, i, o, u) in the word.
    Example: count_vowels("apple") → 2
    pass
"""

def_count_vovels(word):
    vowels = (a, e, i, o, u)    
    count = 0
    for char in word.lower():
        if char in vowels:
        count += 1
    return count

print(count_vowels(apple))
print(count_vowels(nostalgia))
print(count_vowels(mercedez))


# 10
"""
def task10_multiply_list(numbers):
    Task 10:
    Write a function that accepts a list of numbers as a parameter
    and returns the product of all the numbers in the list.
    Example: multiply_list([1, 2, 3, 4]) → 24
    pass
"""
def multiply_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

print(multiply_list(56, 2, 3))
print(multiply_list(3, -3, 32))
print(multiply_list([]))
"""
# 11
def task11_reverse_string(text):
Task 11:
    Write a function that accepts a string as a parameter
    and returns the string reversed.
    Example: reverse_string("hello") → "olleh"
    pass
"""
def reverse_string(text):
    return text[::-1]

print(reverse_string(tunde ednut))
print(reverse_string(manchester united))


# 12
"""
def task12_is_prime(n):
   "
    Task 12:
    Write a function that accepts a number as a parameter
    and returns True if the number is prime, otherwise False.
    pass
"""
 def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check divisibility up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 13
"""
def task13_scope_demo():

    Task 13:
    Demonstrate local and global scope.
    Create a global variable, and then inside a function,
    create a local variable with the same name. Print both
    to show how local and global scope works.
    pass
"""
message = "I am a global scope"

def scope_demo():
    message = "I am a local variable"
    print("Inside the function:", message)

scope_demo()
print("Outside the function:", message)


# 14
"""
def task14_sum_list(numbers):
    Task 14:
    Write a function that accepts a list of numbers
    and returns the sum of all the elements in the list.
    Do not use Python's built-in sum() function.
    """
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(list_sum(34, 23, 78, 12))


# 15
"""
def task15_average_of_list(numbers):
   Task 15:
    Write a function that accepts a list of numbers
    and returns the average.
    Formula: average = sum of numbers / count of numbers
    pass
"""
def average_of_list(numbers):
    if len(numbers) == 0:
        return 0
    average = sum(numbers) / len(numbers)
    return average
print(average_of_list([34, 23, 43, 24, 32, 34, 42]))

# 16
"""
def task16_factorial(n):
   Task 16:
    Write a function that accepts a number and returns its factorial
    using a loop (not recursion).
    Example: factorial(5) → 120
    """
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i  
    return result

print(factorial(5))  
print(factorial(0))



# 17
"""
def task17_palindrome_check(word):
   
    Task 17:
    Write a function that checks if a word is a palindrome.
    A palindrome reads the same forwards and backwards.
    Example: palindrome_check("madam") → True
    """
def palindrom_check(word):
    word = word.lower()
    return word == word[::-1]

print(palindrom_check("tundeednut"))
print(palindrom_check("madam"))
print(palindrom_check("pad"))
print(palindrom_check("racecar"))
print(palindrom_check("level"))


# 18
"""
def task18_convert_minutes_to_hours(minutes):
    Task 18:
    Write a function that accepts minutes as input
    and converts it into hours and minutes.
    Example: 130 minutes → "2 hour(s) 10 minute(s)"
    pass
"""
def convert_minutes_to_hours(minutes):
    def convert_minutes(total_minutes):
    hours = total_minutes // 60     
    minutes = total_minutes % 60   
    return f"{hours} hour(s) {minutes} minute(s)"

print(convert_minutes_to hours(230))
print(convert_minutes_to hours(780))
print(convert_minutes_to_hours(45))


# 19
"""
def task19_find_min(numbers):
    Task 19:
    Write a function that accepts a list of numbers
    and returns the smallest number.
    Do not use Python's built-in min() function.
    """
def find_smallest(numbers):
    if len(numbers) == 0:
    return None  

    smallest = numbers[0] 
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
print(find_smallest([34, 23, 43, 24, 32, 34, 42]))  
print(find_smallest([-5, -10, 0, 15]))     
print(find_smallest([100]))                        
print(find_smallest([]))                           

# 20
"""
def task20_simple_interest(principal, rate, time):
    Task 20:
    Write a function that calculates simple interest.
    Formula: (principal * rate * time) / 100
    pass
"""
def simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

print(calculate_simple_interest(1000, 5, 2))   
print(calculate_simple_interest(5000, 7.5, 3)) 
print(calculate_simple_interest(1200, 10, 1))  

#21
"""
Task 21:
Write a function that works like a simple calculator.
It should accept two numbers and an operation (+, -, *, /)
and return the result.
Example: calculator(4, 2, "+") → 6
"""
def simple_calculator(a, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Error: Division by zero is not allowed"
        return a / b
    else:
        return "Error: Invalid operation"

print(calculator(13, 2, "+")) 
print(calculator(1, 2, "-")) 
print(calculator(7, 2, "*")) 
print(calculator(10, 2, "/")) 


# task22_string_length(text):
    """
    Task 22:
    Write a function that accepts a string
    and returns its length without using len().
    pass
"""
def string_length(text):
    count = 0
    for _ in text
        count =+ 1
    return count
print(string_length("sesko"))
print(string_length("goat Ronaldo"))


# 23
"""
def task23_grade_student(score):
    Task 23:
    Write a function that accepts a score (0–100)
    and returns the grade based on this scale:
    A: 70–100
    B: 60–69
    C: 50–59
    D: 40–49
    E: 30–39
    F: 0–29
    pass
"""
def grade_student(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    elif score >= 30:
        return "E"
    else:
        return "F"
print(grade_student(67))
print(grade_student(99))
print(grade_student(89))
print(grade_student(-23))

# 24
"""
def task24_swap_values(a, b):
Task 24:
Write a function that accepts two values
and returns them swapped.
Example: swap_values(3, 7) → (7, 3)
pass
"""
def swap_values(a, b):
    return b, a
print(swap_values(56, 56))
print(swap_values(56, 34))
print(swap_values(69, 96))

# 25
    """
    Task 25:
    Create a counter function that uses a global variable.
    Each time the function is called, it should increase
    the counter by 1 and print the current count.
    This demonstrates modifying global variables inside functions.
    """
def scope_counter():
    global counter   # tell Python we want to modify the global variable
    counter += 1
    print("Current count:", counter)
print(increment_counter())  
print(increment_counter())
print(increment_counter()) 


# ================================
# ADDITIONAL 25 FUNCTION TASKS
# ================================

# 26
#def task26_calculate_bmi(weight, height):
    """
    Task 26:
    Write a function that accepts weight (kg) and height (m),
    and returns the Body Mass Index (BMI).
    Formula: BMI = weight / (height^2)
    Round the result to 2 decimal places.
    pass
"""
def calculate_bmi(weight, height):
    if height <= 0:
        return "Error: Height must be greater than 0"
    bmi = weight / (height ** 2)
    return round(bmi, 2)
print(calculate_bmi(56, 6.4)
print(calculate_bmi(79, 5.7)


# 27
"""
def task27_discounted_price(price, discount_percent):
    Task 27:
    Write a function that accepts an item's price and discount percentage,
    and returns the final price after discount.
    Example: discounted_price(1000, 20) → 800
    pass
"""
def discounted_price(price, discounted_percent):
    if discount_percent < 0 or discount_percent > 100:
        return "Error: Discount must be between 0 and 100"
    
    discount_amount = (price * discount_percent) / 100
    final_price = price - discount_amount
    return final_price
print(discounted_price(1000, 18)) 
print(discounted_price(500, 50)) 
print(discounted_price(200, 12)) 


# 28
"""
def task28_movie_ticket_price(age):
    Task 28:
    Write a function that determines ticket price based on age:
    - Age < 12: 500
    - 12 <= Age < 18: 700
    - 18 <= Age < 60: 1000
    - Age >= 60: 600
    Return the ticket price.
    """
def movie_ticket_price(age):
    if age < 12:
        price = 500
    elif age < 18:
        price = 700
    elif age < 60:
        price = 1000
    else:
        price = 600
    
    return f"Your ticket price is {price}"
print(ticket_price(18))   
print(ticket_price(22))  
print(ticket_price(10))  
print(ticket_price(65))  

# 29
"""
def task29_shopping_total(prices):
    Task 29:
    Write a function that accepts a list of item prices
    and returns the total cost of all items.
    pass
"""
def shopping_total(prices)
    total = 0
    for price in prices:
        total += price
    return f"The total cost is {total}"
print(total_cost([200, 300, 150]))   
print(total_cost([1000, 2500, 500])) 
print(total_cost([]))                


# 30
"""
def task30_convert_to_seconds(hours, minutes, seconds):
    Task 30:
    Write a function that accepts hours, minutes, and seconds
    and converts the entire time to total seconds.
    Example: 1h 1m 1s → 3661 seconds
    """
def convert_to_second(hours, minutes, seconds): 
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return f"The total time in seconds is {total_seconds}"
print(time_to_seconds(4, 1, 1))   
print(time_to_seconds(1, 30, 0))  
print(time_to_seconds(0, 45, 15)) 


# 31
def task31_find_median(numbers):
    """
    Task 31:
    Write a function that accepts a list of numbers
    and returns the median value.
    (Hint: Sort the list first, then handle odd/even length cases.)
    """
    pass


# 32
def task32_parking_fee(hours):
    """
    Task 32:
    Write a function that calculates parking fees:
    - First 2 hours: 200 Naira flat
    - Every additional hour: 100 Naira
    Example: parking_fee(5) → 200 + 3*100 = 500
    """
    pass


# 33
def task33_word_count(sentence):
    """
    Task 33:
    Write a function that accepts a sentence
    and returns the number of words in it.
    Example: "I love Python" → 3
    """
    pass


# 34
def task34_capitalize_names(names):
    """
    Task 34:
    Write a function that accepts a list of names in lowercase
    and returns a new list with each name capitalized.
    Example: ["john", "mary"] → ["John", "Mary"]
    """
    pass


# 35
def task35_student_pass_fail(score):
    """
    Task 35:
    Write a function that accepts a student's score
    and returns "Pass" if score >= 50, otherwise "Fail".
    """
    pass


# 36
def task36_calculate_fine(days_late):
    """
    Task 36:
    Write a function that calculates library book fine:
    - First 5 days: 20 per day
    - 6–10 days: 50 per day
    - Beyond 10 days: 100 per day
    Example: calculate_fine(7) → 5*20 + 2*50 = 200
    """
    pass


# 37
def task37_convert_currency(amount, rate):
    """
    Task 37:
    Write a function that converts money from one currency to another
    using a given conversion rate.
    Example: convert_currency(100, 1500) → 150000
    """
    pass


# 38
def task38_gas_station_bill(liters, price_per_liter):
    """
    Task 38:
    Write a function that accepts the number of liters purchased
    and the price per liter, then returns the total cost.
    """
    pass


# 39
def task39_is_leap_year(year):
    """
    Task 39:
    Write a function that accepts a year and returns True if it is a leap year,
    otherwise False.
    Rule: Year divisible by 4 → leap year, but divisible by 100 → not leap,
    unless divisible by 400.
    """
    pass


# 40
def task40_password_strength(password):
    """
    Task 40:
    Write a function that checks password strength:
    - Length >= 8
    - Contains at least one digit
    - Contains at least one uppercase letter
    Return "Strong" if all conditions are met, otherwise "Weak".
    """
    pass


# 41
def task41_shirt_order(quantity, price_per_shirt, discount_threshold=10, discount_rate=0.1):
    """
    Task 41:
    Write a function to calculate the total price of a shirt order.
    - If quantity >= discount_threshold, apply discount_rate.
    Example: shirt_order(12, 2000) → discounted price
    """
    pass


# 42
def task42_find_mode(numbers):
    """
    Task 42:
    Write a function that finds the mode (most frequent number) in a list.
    If there are multiple modes, return any one of them.
    """
    pass


# 43
def task43_student_average(scores):
    """
    Task 43:
    Write a function that accepts a dictionary of subject:score
    and returns the student's average score.
    Example: {"math": 80, "english": 70} → 75.0
    """
    pass


# 44
def task44_calculate_age(current_year, birth_year):
    """
    Task 44:
    Write a function that accepts current year and birth year,
    and returns the age.
    Example: calculate_age(2025, 2000) → 25
    """
    pass


# 45
def task45_salary_after_tax(salary, tax_rate=0.15):
    """
    Task 45:
    Write a function that calculates net salary after deducting tax.
    Example: salary_after_tax(100000) → 85000
    """
    pass


# 46
def task46_water_bill(units):
    """
    Task 46:
    Write a function to calculate water bill based on units:
    - First 30 units → 50 per unit
    - Next 20 units → 75 per unit
    - Beyond 50 units → 100 per unit
    """
    pass


# 47
def task47_find_longest_word(sentence):
    """
    Task 47:
    Write a function that accepts a sentence
    and returns the longest word in it.
    Example: "I love programming" → "programming"
    """
    pass


# 48
def task48_banking_withdraw(balance, withdraw_amount):
    """
    Task 48:
    Write a function to simulate ATM withdrawal.
    - If withdraw_amount <= balance, return new balance
    - Otherwise return "Insufficient funds"
    """
    pass


# 49
def task49_calculate_grade_point(score):
    """
    Task 49:
    Write a function that converts score (0–100) into grade points:
    - 70–100 → 5
    - 60–69 → 4
    - 50–59 → 3
    - 45–49 → 2
    - 40–44 → 1
    - <40 → 0
    """
    pass


# 50
def task50_weather_advice(temperature, raining):
    """
    Task 50:
    Write a function that gives advice based on weather:
    - If raining → "Take an umbrella"
    - Else if temperature > 30 → "Wear light clothes"
    - Else if temperature < 15 → "Wear a jacket"
    - Else → "Weather is fine"
    """
   pass

"""
