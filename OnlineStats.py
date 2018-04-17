"""
Elijah Molloy
70 - 510 Spring I - 2018
16 JAN 2018

PROGRAMMING ASSIGNMENT #1
"""

from __future__ import division


class OnlineStats:
    def __init__(self):
        self.n = 0
        self.x_n = 0
        self.s2_n = 0

        self.run()   # Program engine is called in class constructor


    @staticmethod
    def print_instructions():
        """
        Print course info, name, assignment number, and brief program description to console.

        :return:
        """

        print "70 - 510, SPRING I - 2018"
        print "ELIJAH MOLLOY"
        print "PROGRAMMING ASSIGNMENT #1 \n"

        print "This program will compute and display the mean of all non-negative numbers entered."
        print "To exit the program, simply enter a negative number. \n"


    @staticmethod
    def print_error_message(user_input = "Previous input"):
        """
        Print error message when user attempts to input an invalid number.

        :param user_input:
        :return:
        """

        print "ERROR : " + user_input + " is not a valid input. Please enter an int or a double."


    def print_mean_and_variance_message(self):
        """
        Prints mean and variance to the console.

        :return:
        """

        print "Mean is " + str(self.x_n) + "\tvariance is " + str(self.s2_n) +"\n"


    def update_mean_and_variance(self, number):
        """
        Update self.n, self.s2_n, then self.x_n.
        self.n and self.s2_n are updated before self.x_n so that self.x_n is defacto x(n-1)

        :param number:
        :return:
        """

        # Increment self.n
        self.n += 1

        # Update self.s2_n if self.n > 1
        if self.n > 1:
            self.s2_n = (((self.n - 2) / (self.n - 1)) * self.s2_n) + (((number - self.x_n) ** 2) / self.n)

        # Update self.x_n
        self.x_n = self.x_n + ((number - self.x_n) / self.n)


    @staticmethod
    def number_is_positive_or_zero(number):
        """
        Returns if number is positive or not.

        :param number:
        :return:
        """

        # If number is equal to or greater than 0
        if number >= 0:
            return True

        # Else number is less than 0
        else:
            return False


    def run(self):
        """
        While continue_program is True, attempt to get user_input, update n, mean, variance, and print results.

        If user_input was invalid (not a float or int), print error message and attempt to get new user input.
        If user_input was valid and positive, update n, mean, variance, and print results.
        If user_input was valid and negative, exit program.
        :return:
        """

        continue_program = True

        self.print_instructions()

        while continue_program:
            try:
                user_input = float(raw_input("Enter a number: "))

                # If user_input is positive or zero
                # Update n, use user_input to update mean and variance, then print results
                if self.number_is_positive_or_zero(user_input):
                    self.update_mean_and_variance(user_input)
                    self.print_mean_and_variance_message()

                # Else user_input is negative
                else:
                    continue_program = False

            except ValueError:
                self.print_error_message()
                self.print_mean_and_variance_message()


if __name__ == "__main__":
    OnlineStats()