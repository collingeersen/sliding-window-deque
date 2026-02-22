# Sliding Window Deque
### Description:
Previous project done for my Data Structures and Algorithms class.
Solved an interesting problem for finding a sliding window maximum using a deque data structure.
Additionally, the deque was implemented in an array that uses an algorithm so that changes to the deque do not have to reindex the array.

### Problem:

Problem originally from LeetCode: https://leetcode.com/problems/sliding-window-maximum/description/​

Given an array of numbers and a sliding window that moves from left to right (one value at a time) with a size that is at least 1 and no greater than the array length; 
create a window that returns the maximum integer each time it moves through the array of numbers.
The result is a list of maximums found within the bounds of the window as it moves through the array.

#### Problem Visual:
```python
  window_size = 3
  list_of_numbers = [1, 4, 3, 1, -3, -6, -4, 3]
  # [[1, 4, 3], 1, -3, -6, -4, 3] -> Max in window: 4
  # [1, [4, 3, 1], -3, -6, -4, 3] -> Max in window: 4
  # [1, 4, [3, 1, -3], -6, -4, 3] -> Max in window: 3
  # [1, 4, 3, [1, -3, -6], -4, 3] -> Max in window: 1
  # [1, 4, 3, 1, [-3, -6, -4], 3] -> Max in window: -3
  # [1, 4, 3, 1, -3, [-6, -4, 3]] -> Max in window: 3
  result = [4, 4, 3, 1, -3, 3]
```

### Implementation:
Using an Abstract Data Type, I created a full deque implementation using an array (Python List). Though most of the methods are not used, I wanted to create a full implementation.​

#### Why Not Use a Linked-List?
One of the main reasons is that I wanted to challege myself to use arrays in an atypical way. This allowed me to have a greater understanding of array useage beyond what they are typically used for.
With this implementation, I was able to retain all of the benefits of an array (indexing), while removing the negatives (reindexing). This algorithm I created makes the array implementation superior to
a linked-list implemenation. With a typical array implementation of a deque, pushing or popping at the head/tail causes reindexing in linear time. With my implementation I was able to remove reindexing 
for pushing or popping at the head/tail in constant time like a linked-list.

#### Array Based Deque without Reindexing
This is the most interesting portion of the data structure. Using modulo calculations, an algorithm was used to determine the placement of pushing and popping.
Internal variables were used for pointing at the head and tail.

Example Usage:
```python
  deque_size = 4
  new_deque = Deque(4) # Initilizes as: [None, None, None, None]
  new_deque.push_front(10) # -> [10, None, None, None] front_index is 10
  new_deque.push_front(2)  # -> [10, None, None, 2] front_index is 2 and back_index is 10
  new_deque.push_back(6)   # -> [10, 6, None, 2] front_index is 2 and back_index is 6
  new_deque.push_front(4)  # -> [10, 6, 4, 2] front_index is 4 and back_index is 6
  new_deque.push_front(55) # -> Error: Max deque size is 4
  front_value = new_deque.pop_front()  # -> 4
  back_value = new_deque.pop_back()    # -> 6
```
Interestingly when values are popped from head or tail, they are still present in the list. They are just marked as free space and will not be read.
For example, using the previous example list of ```[10, 6, 4, 2]``` popping the front and back gives a resulting list of ```[10,2]``` with 2 being the head and 10 being the tail,
but internally the list is still ```[10, 6, 4, 2]``` with indexes 1 and 2 being free.

#### Modulo Equations:
Using my knowledge of modulo and how they can be used in hash tables, I applied the same principles to create modulo equations that wrap around and calculate the "previous" and "next"
for the head and tail. The part of the implementation was a lot of trial and error to make sure all cases are accounted for.

Pushing to the Front (Truncated):
```python
  item_index = (self.__front_index + self.__max_length - 1) % self.__max_length
  self.__front_index = item_index  # Make the new front_index this newly added value
  self.deque_list[item_index] = item  # Add the value to the calculated index
  self.__length += 1
  return True
```

Pushing to the Back (Truncated):
```python
  item_index = (self.__front_index + self.__length) % self.__max_length
  self.__back_index = item_index  # Set the new back item as the back of the array
  self.deque_list[item_index] = item  # Add the value to item_index position
  self.__length += 1
  return True
```

Popping the front (Truncated):
```python
  # Get the value from the internal array based on the front_index
  popped_item = self.deque_list[self.__front_index]
  self.__length -= 1
  # Make the new front_index the next value after front_index, which is calculated with modulo
  # since the next index is not necessarily the next index in the internal list.
  # For example, front_index of 3 with a list the length of 4 means the next index is 0 and not 4 since that
  # is out of range.
  self.__front_index = (self.__front_index + 1) % self.__max_length
  return popped_item
```

Popping the back (Truncated):
```python
  # Get the value from the internal array based on the back_index
  popped_item = self.deque_list[self.__back_index]
  self.__length -= 1
  # Make the new back_index the previous value before back_index, which is calculated with modulo
  # since the previous index is not necessarily the previous index in the internal list.
  # For example, back_index of 0 with a list the length of 4 means the previous index is 3 and not -1 since that
  # is not possible.
  self.__back_index = (self.__front_index + self.__length) % self.__max_length
  return popped_item
```

### Using Deque for Sliding Window Maximum
Now using this deque implementation, getting the sliding window maximum for an array is easy.
```python
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
```










​​
