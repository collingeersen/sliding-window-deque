#
# Student Name: Collin Geersen
# Date: November 8, 2025
#
# Description: Tests to show that the sliding window maximum is implemented correctly.
#
from SlidingWindowMax import sliding_window_max


def test_sliding_window_max_driver():
    test_1()
    input(f'\nPress Enter to continue to the next test.\n')
    test_2()
    input(f'\nPress Enter to continue to the next test.\n')
    test_3()
    input(f'\nPress Enter to continue to the next test.\n')
    test_4()
    input(f'\nPress Enter to continue to the next test.\n')
    test_5()
    print('---Done with tests---')
    input(f'\nPress Enter to continue back to menu.\n')


def test_1():
    print('-----------------------------------------------')
    print('Test 1 - List with 10 values and window size of 3.')
    try:
        test_list = [1, 4, 6, 7, 23, -4, -8, 10, 23, 23]
        test_max_list = sliding_window_max(test_list, 3)
        print(f'List is {test_list}')
        print(f'Sliding Window Max List should be: [6, 7, 23, 23, 23, 10, 23, 23].')
        assert test_max_list == [6, 7, 23, 23, 23, 10, 23, 23]
        print(f'✅ Test Passed: List is {test_max_list}.')
    except AssertionError:
        print('❌ Test Failed: Sliding Window Max List should be: [6, 7, 23, 23, 23, 10, 23, 23].')


def test_2():
    print('-----------------------------------------------')
    print('Test 2 - List with 5 values and window size of 2.')
    try:
        test_list = [1, 100, -3, -20, -1]
        test_max_list = sliding_window_max(test_list, 2)
        print(f'List is {test_list}')
        print(f'Sliding Window Max List should be: [100, 100, -3, -1].')
        assert test_max_list == [100, 100, -3, -1]
        print(f'✅ Test Passed: List is {test_max_list}.')
    except AssertionError:
        print('❌ Test Failed: Sliding Window Max List should be: [100, 100, -3, -1].')


def test_3():
    print('-----------------------------------------------')
    print('Test 3 - List with 2 values and window size of 2')
    try:
        test_list = [30, 2]
        test_max_list = sliding_window_max(test_list, 2)
        print(f'List is {test_list}')
        print(f'Sliding Window Max List should be: [30].')
        assert test_max_list == [30]
        print(f'✅ Test Passed: List is {test_max_list}.')
    except AssertionError:
        print('❌ Test Failed: Sliding Window Max List should be: [30].')


def test_4():
    print('-----------------------------------------------')
    print('Test 4 - List with 12 values and a window size of 6')
    try:
        test_list = [23, -12, 345, 1, -23, 90, 3, 4, 7, 9, 2, 10]
        test_max_list = sliding_window_max(test_list, 6)
        print(f'List is {test_list}')
        print(f'Sliding Window Max List should be: [345, 345, 345, 90, 90, 90, 10].')
        assert test_max_list == [345, 345, 345, 90, 90, 90, 10]
        print(f'✅ Test Passed: List is {test_max_list}.')
    except AssertionError:
        print('❌ Test Failed: Sliding Window Max List should be: [30].')


def test_5():
    print('-----------------------------------------------')
    print('Test 5 - List with zero values and a window size of 1')
    try:
        test_list = []
        test_max_list = sliding_window_max(test_list, 1)
        print(f'List is {test_list}')
        print(f'Sliding Window Max List should be: [].')
        assert test_max_list == []
        print(f'✅ Test Passed: List is {test_max_list}.')
    except AssertionError:
        print('❌ Test Failed: Sliding Window Max List should be: [30].')
