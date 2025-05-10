# comp_math
from sympy import Symbol, exp, series
from decimal import *
import numpy as np

# Propogation class: a class that is meant to handle Errors and error propogation
# in Computational Mathematics
class Propogation:
    # Initializer
    def __init__(self):
        # Superscript unicode item dictionary
        self.superscripts = ({"0" : "\u2070", "1" : "\u00b9", "2" : "\u00b2", "3" : "\u00b3", "4" : "\u2074", "7" : "\u2077"})
    # Exponential function: Unicode converts a number to its exponent version
    def exponential(self, string_given, string_received = ""):
        string_received += self.superscripts[string_given[0]]
        if len(string_given) == 1:
            return string_received
        else:
            return self.exponential(self, string_given[1:], string_received)
    # Recursive function to find whether a unicode is in the superscript dictionary
    def unicode_check(self, string, exp_point = 1, exp_seeker = 0):
        # Experience seeker increments
        for item in self.superscripts.values():
            if item in string:
                if len(string) == 1:
                    return [True, 1]
                else:
                    exp_point += 1
                    self.unicode_check(string[string.index(item)+ 1:], exp_point, 1)
        if exp_seeker == 1:
            print("Exponent not found.")
        return [False, exp_point, exp_seeker]
    # Normalized function: Returns the normalized number
    # Either as the pure numerical result
    # Or the normalized string format
    def normalized(self, mantissa_comp, base, exponent, form = False):
        if 1 > mantissa_comp and mantissa_comp > -1:
            front = mantissa_comp
        elif mantissa_comp <= -1:
            front = float("-0." + str(mantissa_comp)[1:])
        else:
            front = float("0." + str(mantissa_comp))
        if form == True:
            normalized_form = str(front) + "x" + str(base) + self.exponential(str(exponent))
            return normalized_form
        return front * (base**exponent)
    # x_hat function: converts the x_hat variable into a rounded, normalized form
    # (in other words, an expansion on normalization)
    def x_hat(self, mantissa_comp, base, exponent, float_value, form = False):
        if mantissa_comp <= -1:
            mantissa_comp = float("-0." + str(mantissa_comp[1:]))
        elif mantissa_comp >= 1:
            mantissa_comp = float("0." + str(mantissa_comp))
        return self.normalized(round(mantissa_comp, float_value), base, exponent, form)
    # to_normalized: converts a number into its normalized form (string or numeric result)
    def to_normalized(self, number, base = 10, exponent = 2, float_value = "Default", form = False):
        print(number)
        if number >= 1 or number <= -1:
            getcontext().prec = len(str(number))
            number1 = float(Decimal(number)/Decimal(base))
            print(Decimal(number)/Decimal(base))
            return self.to_normalized(number1, base, exponent + 1, float_value, form)
        elif number < 0.1 and number > -0.1:
            getcontext().prec = len(str(number))
            number1 = float(Decimal(number)*Decimal(base))
            return self.to_normalized(number1, base, exponent - 1, float_value, form)
        if float_value == "Default":
            float_value = len(str(number)) - 2
        return self.x_hat(number, base, exponent, float_value, form)
    # Function to check the type of a number
    def normalization_type(self, number):
        if isinstance(number, float):
            return "float"
        elif isinstance(number, int):
            return "int"
        else:
            try:
                normal_in_question = number[:number.index("x")]
            except ValueError as ve:
                print("ValueError:", ve)
                print("Substring Not Found: No Multiplication Symbol to Reach")
                return None
            except TypeError:
                return None
            try:
                normal_in_question = float(normal_in_question)
            except ValueError as ve:
                print("ValueError:", ve)
                if (normal_in_question == ''):
                    print("No item in question")
                else:
                    print("Item is not a base 10 number.")
                return None
            normal_in_question = number[number.index("x") + 1 : ]
            unicode_value = self.unicode_check(str(normal_in_question))
            if not unicode_value[0]:
                if unicode_value[2] == 1:
                    print("String not normalized: Exponent term error starts at point " + unicode_value[1] + " of exponents")
                return None
            return "normalized"
    # Relative Error Function (to be added): Potential redundancies can be
    # reduced due to the acceptance of the plethora of potential data types,
    # Something Python is plenty capable of handling due to being an interpreted language
    
# Basic Taylor Expansion print function
def taylor_exp():
    x = Symbol('x')
    print(series(exp(x), x))

# Propogation object
test = Propogation()

# Print the normalized form of 0.1 * 10^3
print(test.normalized(1, 10, 3))
# Print the numerical form of 10^3
print(test.to_normalized(1, 10, 3))

# A default number, normalized to 0.1 * 10^4
# As a string
print(test.to_normalized(10, form = True))
taylor_exp()

print("1x\u00b9")

print(test.normalization_type("1x\u00b98"))

## Source: https://climate.ucdavis.edu/AM341.pdf
