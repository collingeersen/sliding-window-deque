#
# Student Name: Collin Geersen
# Date: November 3, 2025
#
# Description: Sliding Window Maximum - Uses a deque to implement a sliding window.
# This window moves over a list to return a list of maximums. These maximums are found within the
# bounds of the window as it moves over the list, popping the front and pushing the back.
#
from SlidingWindowMax import sliding_window_max
from DequeTest import test_deque_driver
from SlidingWindowMaxTest import test_sliding_window_max_driver


def main():
    NUM_OF_MENU_CHOICES = 4

    user_choice = 0
    while user_choice != 4:  # when not exit option

        user_choice = program_options()  # get user choice

        while user_choice not in range(NUM_OF_MENU_CHOICES + 1):  # While the user_choice not an option
            print(f'\nError: Must enter a value from 0 to {NUM_OF_MENU_CHOICES}\n')
            user_choice = program_options()

        if user_choice == 0:  # Help option is selected
            print(f'\n                              HELP')
            print('-----------------------------------------------------------------')
            print('This program is to demonstrate a sliding window maximum using a deque.')
            print('The deque was implemented with an array.')
            print('To use this program please pick from the available options.')
            print('-----------------------------------------------------------------')
            print()

        elif user_choice == 1:  # User provided list option
            while True:
                try:
                    num_list_length = int(input('Enter the size of the list to process: '))
                    if num_list_length > 0:
                        break
                    else:
                        print('Error: Must be greater than zero.')
                except ValueError:
                    print('Error: Must be a valid number.')

            input_list = [0] * num_list_length  # Initialize the input_list with a length of num_list_length
            for i in range(num_list_length):
                # Input validation to make sure user enters a valid list size
                while True:
                    try:
                        input_element = int(input(f'Enter the number value for index {i}: '))
                        if input_element:  # If a valid number
                            input_list[i] = input_element
                            break
                    except ValueError:
                        print('Error: Must be a valid number.')

            # Input validation to make sure user enters a valid window size
            while True:
                try:
                    deque_size = int(input('Enter the size of the deque window: '))
                    if deque_size <= num_list_length:  # if the deque size is less than or equal to list length
                        break
                    else:
                        print('Error: Size of deque must be less than or equal to the number list.')
                except ValueError:
                    print('Error: Deque size must be a valid number')

            # Call sliding_window_max function with the user provided values
            sliding_window_max_list = sliding_window_max(input_list, deque_size)

            # Print the user list and processed sliding window max list
            print(f'\nUser list: {input_list}')
            print(f'Sliding Window Maximum List: {sliding_window_max_list}\n')

        elif user_choice == 2:  # Deque test option
            test_deque_driver()
        elif user_choice == 3:  # Sliding window test option
            test_sliding_window_max_driver()


def program_options():
    """
    :return int(user_choice):

    Description: Displays the program options to the user and take input of user choice.

    """
    print('Sliding Window Maximum - Implemented with Deque')
    print('-----------------------------------------------------------------')
    print('0 - Help')
    print('1 - User provided list of integers to find sliding window maximum')
    print('2 - Run 5 tests proving proper deque implementation')
    print('3 - Run 5 tests proving proper sliding window maximum implementation')
    print('4 - Exit')
    print('------------------------------------------------------------------')
    user_choice = input('Please enter from the menu choices:')
    while not user_choice.isdigit():
        print('Error: Choice must be a number')
        user_choice = input('Please enter from the menu choices:')
    return int(user_choice)


if __name__ == '__main__':
    main()
