# Binary Search Algorithm
# ------------------------
# Binary search is an efficient algorithm for finding an item in a sorted list.
# It works by repeatedly dividing the search range in half.
# 1. Compare the target item with the middle element of the list.
# 2. If they are equal, the search is complete.
# 3. If the target is smaller, search in the left half of the list.
# 4. If the target is larger, search in the right half of the list.
# 5. Repeat this process until the item is found or the search range is empty.
# This algorithm has a time complexity of O(log n).

def binary_search(a_list, item):
    """
    Perform binary search on a sorted list to find the given item.

    Parameters:
    a_list (list): A sorted list of numbers.
    item (int): The number to be searched for.

    Returns:
    Prints the index of the found item or a message if not found.
    """
    
    first = 0  # Starting index of the list
    last = len(a_list) - 1  # Ending index of the list

    # Continue searching while the search range is valid
    while first <= last:
        mid = int((first + last) / 2)  # Calculate the middle index

        # If the middle element matches the item, print the result and exit
        if a_list[mid] == item:
            print(f"The {item} is found at index {mid}")
            break
        
        # If the middle element is greater than the item, search in the left half
        elif a_list[mid] > item:
            last = mid - 1  
        
        # If the middle element is smaller than the item, search in the right half
        elif a_list[mid] < item:
            first = mid + 1

    # If the item is not found in the list
    else:
        print(f"The {item} is not found in the list")


# Main execution
if __name__ == "__main__":
    # Test the binary search function with a sorted list
    binary_search([2, 3, 7, 9, 50, 57, 79, 550], 50)
