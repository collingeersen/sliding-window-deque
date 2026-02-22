#
# Student Name: Collin Geersen
# Date: November 8, 2025
#
# Description: Tests to show that the deque is fully implemented with all needed methods.
#
from Deque import Deque


def test_deque_driver():
    test_deque_1()
    input(f'\nPress Enter to continue to the next test.\n')
    test_deque_2()
    input(f'\nPress Enter to continue to the next test.\n')
    test_deque_3()
    input(f'\nPress Enter to continue to the next test.\n')
    test_deque_4()
    input(f'\nPress Enter to continue to the next test.\n')
    test_deque_5()
    print('---Done with tests---')
    input(f'\nPress Enter to continue back to menu.\n')



def test_deque_1():  # Test the is_empty() and is_full() methods
    print('-----------------------------------------------')
    print('Test 1 - Call is_empty() and is_full() on an empty deque')
    try:
        deque_to_test = Deque(4)
        assert deque_to_test.is_empty()
        assert deque_to_test.is_full() == False
        print('✅ Test Passed: Deque is empty.')
    except AssertionError:
        print('❌ Test Failed: Deque should be empty.')


def test_deque_2(): # Test both push methods
    print('-----------------------------------------------')
    print('Test 2 - Push value to both ends of the deque')
    try:
        deque_to_test = Deque(4)
        print('Create: Deque with a capacity of 4.')
        print(deque_to_test)

        test_deque_push_back(deque_to_test, 10) # Push 10 to back of deque

        test_deque_push_front(deque_to_test, 2) # Push 2 to front of deque

        test_deque_push_front(deque_to_test, 57) # Push 57 to front of deque

        test_deque_push_back(deque_to_test, -2) # Push -2 to back of deque

        assert deque_to_test.get_current_deque() == [57, 2, 10, -2]
        print('✅ Test Passed: Deque is [57, 2, 10, -2].')
    except AssertionError:
        print(f'❌ Test Failed: Deque should be [57, 2, 10, -2], got {deque_to_test.get_current_deque()}.')


def test_deque_3(): # Test both pop methods
    print('-----------------------------------------------')
    print('Test 3 - Pop values from both ends of the deque')
    try:
        deque_to_test = Deque(4)
        print('Create: Deque with a capacity of 4. With values: 13, 90, -23, and 2.')

        deque_to_test.push_back(13)
        deque_to_test.push_back(90)
        deque_to_test.push_back(-23)
        deque_to_test.push_back(2)
        print(f'Deque is {deque_to_test}.')

        test_deque_pop_front(deque_to_test) # Pop front item

        test_deque_pop_back(deque_to_test) # Pop back item

        test_deque_pop_back(deque_to_test) # Pop back item

        test_deque_pop_back(deque_to_test) # Pop back item

        assert deque_to_test.is_empty()
        print('✅ Test Passed: Deque is empty.')
    except AssertionError:
        print('❌ Test Failed: Deque should be empty.')


def test_deque_4(): # Test both peek methods
    print('-----------------------------------------------')
    print('Test 4 - Peeking the front and back values of deque.')
    try:
        deque_to_test = Deque(4)
        print('Create: Deque with a capacity of 4.')

        deque_to_test.push_back(3)
        deque_to_test.push_back(0)
        deque_to_test.push_back(-3)
        deque_to_test.push_back(56)
        print(f'Deque is {deque_to_test}.')

        print('Calling peek_back() method...')
        assert deque_to_test.peek_back() == 56
        print('✅ Test Passed: peek_back() returned 56.')

        print('Calling peek_front() method...')
        assert deque_to_test.peek_front() == 3
        print('✅ Test Passed: peek_front() returned 3.')
    except AssertionError:
        print('❌ Test Failed: peek_back() or peek_front() returned wrong value.')


def test_deque_5(): # Test the max() method after rapidly pushing and popping
    print('-----------------------------------------------')
    print('Test 5 - Pushing and popping values to a deque and getting a maximum.')
    try:
        deque_to_test = Deque(4)
        print('Create: Deque with a capacity of 4.')
        print(deque_to_test)

        test_deque_push_back(deque_to_test, 13) # Push 13 to the back of deque

        test_deque_push_back(deque_to_test, 63) # Push 63 to the back of deque

        test_deque_push_front(deque_to_test, -8) # Push -8 to the front of deque

        test_deque_push_front(deque_to_test, 7) # Push 7 to the front of deque

        test_deque_pop_back(deque_to_test) # Pop from the back of deque

        test_deque_pop_front(deque_to_test) # Pop from the front of deque

        test_deque_push_back(deque_to_test,4) # Push 4 to the back of deque

        test_deque_push_front(deque_to_test,23) # Push 23 to the front of deque

        test_deque_push_back(deque_to_test,34) # Try to push 34 to the back of deque, should be able

        print(f'The maximum is: {deque_to_test.max()}')
        assert deque_to_test.max() == 23
        print(f'✅ Test Passed: Max returned {deque_to_test.max()}.')

    except AssertionError:
        print(f'❌ Test Failed: Deque max should be {deque_to_test.max()}.')


# Helper functions to use deque methods and print results
def test_deque_push_back(deque, value):
    if deque.is_full():
        deque.push_back(value)
        print(f'Push: {value} will not be pushed since the capacity of the deque is reached.')
        print(deque)
    else:
        deque.push_back(value)
        print(f'Push: {value} to the back of deque')
        print(deque)

def test_deque_push_front(deque, value):
    deque.push_front(value)
    print(f'Push: {value} to the front of deque')
    print(deque)

def test_deque_pop_back(deque):
    deque.pop_back()
    print('Pop the back value.')
    print(deque)

def test_deque_pop_front(deque):
    deque.pop_front()
    print('Pop the front value.')
    print(deque)

