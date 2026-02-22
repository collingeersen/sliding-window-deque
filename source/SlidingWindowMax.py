#
# Student Name: Collin Geersen
# Date: November 8, 2025
#
# Description: Sliding Window Maximum - Uses a deque to implement a sliding window.
#
from Deque import Deque


def sliding_window_max(nums, deque_size):
    """
    :param nums:
    :param deque_size:
    :return number:

    Description: Uses the deque defined to create a user defined sized sliding window that moves over a list,
    returning a list of maximum values found in the windows as it moves over the list.

    """
    number = []  # Number list that will be returned
    window_deque = Deque(deque_size)  # Create a deque based on user deque_size
    list_counter = 0
    nums_length = len(nums)

    if nums_length == deque_size and nums_length > 0:  # Edge case where window size and number list are same length
        number.append(max(nums))  # Just return the max from the number list
        return number
    elif nums_length == 0:  # Other edge case where the number list is empty
        return number

    while list_counter != nums_length:  # Keep processing list as long as there are unprocessed elements in nums
        while window_deque.get_length() != deque_size:  # Initializes the deque by filling it up
            window_deque.push_back(nums[list_counter])
            list_counter += 1

        # Once the deque is full, start getting the maximums
        number.append(window_deque.max())
        window_deque.pop_front()  # Remove the front deque item
        window_deque.push_back(nums[list_counter])  # Push the next item on the deque from the back
        list_counter += 1
    number.append(window_deque.max())  # Last maximum from the deque that includes the last nums element

    return number  # Return the final list with the sliding window maximums
