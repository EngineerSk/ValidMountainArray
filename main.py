# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


class Solution:
    def valid_mountain_array(self, array: List[int]) -> bool:
        array_size = len(array)
        if array_size < 3:
            return False
        current_array_index = 0
        for i in range(1, array_size):
            if array[i] > array[i - 1]:
                if i == array_size - 1:
                    return False
                continue
            elif array[i] < array[i - 1]:
                if i == array_size - 1:
                    return True
                if i - 1 == 0:
                    return False
                if i - 1 > 0:
                    current_array_index = i - 1
                    break
            else:
                return False
        for j in range(current_array_index, array_size - 1):
            if array[j] > array[j + 1]:
                if j + 1 == array_size - 1:
                    return True
                continue
            else:
                return False
        return False


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
