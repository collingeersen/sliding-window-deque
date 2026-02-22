#
# Student Name: Collin Geersen
# Date: November 3, 2025
#
# Description: Implementation of a deque using a Python array.
#
from DequeADT import DequeADT


class Deque(DequeADT):
    def __init__(self, max_length):
        self.deque_list = [None] * max_length  # uses None to remove unused indexes from printing
        self.__front_index = 0
        self.__back_index = 0
        self.__length = 0
        self.__max_length = max_length

    def __str__(self):
        return str(self.get_current_deque())  # Return the print_list as a str

    def get_length(self):
        """
        Description: Return the length of the deque.

        Returns:
            int: Length of the internal list

        """
        return self.__length

    def max(self):
        """
        Description: Return the max value from the deque.

        Returns:
            int: Max of the current internal list

        """
        # use max() on current deque
        return max(self.get_current_deque())

    def push_back(self, item):
        """
        Description: Add the value to the back of the deque.

        Args:
            item (int): Integer to push at back

        Returns:
            bool: True or False depending on if the item was pushed

        """
        # When no more items can be added
        if self.is_full():
            return False

        # Add item to end of deque
        # Calculates the end of the internal list by modulus since this is a bounded deque without need for resizing.
        # Additionally, item_index is calculated this way to have the internal array as a shifting one that does
        # not need to be reindex.
        item_index = (self.__front_index + self.__length) % self.__max_length
        self.__back_index = item_index  # Set the new back item as the back of the array
        self.deque_list[item_index] = item  # Add the value to item_index position
        self.__length += 1

        return True

    def push_front(self, item):
        """
        Description: Add the value to the front of the deque.

        Args:
            item (int): Integer to push in front

        Returns:
            bool: True or False depending on if the item was pushed

        """
        # When no more items can be added
        if self.is_full():
            return False

        # Add item to the front of the deque
        # Calculates the "previous" index relative to the front index
        # Uses modulus calculation since the deque wraps around on itself with a shifting internal array that
        # does not need to be reindexed. The basic way of adding an element before index 0 is to shift all the values
        # up, reindexing. This can be avoided by using modulus to calculate the "previous" element of index 0 to
        # be the end of the array, and so on.
        # Adds item be constantly shifting indexes so it does not have to reindex
        item_index = (self.__front_index + self.__max_length - 1) % self.__max_length
        self.__front_index = item_index  # Make the new front_index this newly added value
        self.deque_list[item_index] = item  # Add the value to the calculated index
        self.__length += 1

        return True

    def pop_front(self):
        """
        Description: Return and remove the front index value.

        Returns:
            int: Pops off front deque item

        """
        # Cannot remove an item when none exist
        if self.is_empty():
            popped_item = None
            return popped_item

        # Get the value from the internal array based on the front_index
        popped_item = self.deque_list[self.__front_index]
        self.__length -= 1
        # Make the new front_index the next value after front_index, which is calculated with modulus
        # since the next index is not necessarily the next index in the internal list.
        # For example, front_index of 3 with a list the length of 4 means the next index is 0 and not 4 since that
        # is out of range.
        self.__front_index = (self.__front_index + 1) % self.__max_length
        return popped_item

    def pop_back(self):
        """
        Description: Return and remove the back index value.

        Returns:
            int: Pops off back deque item

        """
        # Cannot remove an item when none exist
        if self.is_empty():
            popped_item = None
            return popped_item

        # Get the value from the internal array based on the back_index
        popped_item = self.deque_list[self.__back_index]
        self.__length -= 1
        # Make the new back_index the previous value before back_index, which is calculated with modulus
        # since the previous index is not necessarily the previous index in the internal list.
        # For example, back_index of 0 with a list the length of 4 means the previous index is 3 and not -1 since that
        # is not possible.
        self.__back_index = (self.__front_index + self.__length) % self.__max_length
        return popped_item

    def peek_back(self):
        """
        Description: Return the current back index value.

        Returns:
            int: Current back index of deque

        """
        return self.deque_list[self.__back_index]  # Returns the back_index

    def peek_front(self):
        """
        Description: Return the current front index value.

        Returns:
            int: Current front index of deque

        """
        return self.deque_list[self.__front_index]  # Returns the front_index

    def is_empty(self):
        """
        Description: Whether a deque is empty or not.

        Returns:
            bool: True or False depending on length of internal list

        """
        # The deque is empty based on the length variable equaling 0
        # and not len(self.deque_list) equalling 0 since that always equals the max_length
        # used to initialize the internal array
        if self.__length == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        Description: Whether a deque is full or not.

        Returns:
            bool: True or False depending on the length of internal list

        """
        # The deque is full based on the length variable equaling the max_length
        # since this is a bounded deque
        if self.__length == self.__max_length:
            return True
        else:
            return False

    def get_current_deque(self):
        """
        Description: Get internal list used for deque without possible holes denoted as None.

        Returns:
            List: Current deque as a list, omitting holes

        """
        current_deque_list = [0] * self.__length  # Initializes a list set to length of deque to push values to
        current_index = self.__front_index  # Set the starting index of the list to the deque front_index
        counter = 0  # Tracks number of pushed to print_list
        while counter != self.__length:
            if not None:  # Skips over elements that do not have a value since "holes" can exist in a nonfull deque
                current_deque_list[counter] = self.deque_list[
                    current_index]  # From front_index add values to print_list
                # Calculates the next position for the deque. Uses modulus calculation since the deque uses
                # the internal list as a shifting array that does not need to reindex.
                # This means that current_index + 1 is not necessarily the next index since the array wraps around.
                current_index = (current_index + self.__max_length + 1) % self.__max_length
                counter += 1
        return current_deque_list
