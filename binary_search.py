def binary_search(array, target):
    """
    Perform binary search to find the index of the target element in the array.

    Args:
    - array: A sorted list of elements to search in.
    - target: The element to search for.

    Returns:
    - The index of the target element if found, otherwise returns -1.
    """

    low = 0                          # Set the low index to the beginning of the array.
    high = len(array) - 1            # Set the high index to the end of the array.
    
    # Continue searching until the low index is less than or equal to the high index.
    while low <= high:
        mid = (high + low) // 2      # Calculate the middle index of the current search space.
        if array[mid] == target:     # If the middle element is the target, return its index.
            return mid
        elif array[mid] < target:    # If the middle element is less than the target, search the right half.
            low = mid + 1
        else:                        # If the middle element is greater than the target, search the left half.
            high = mid - 1
    
    return -1  # Return -1 if the target element is not found in the array.

def main():
    array = [-1, 1, 3, 5, 7, 9, 10]
    print("Element is present at index:", binary_search(array, 9))

if __name__ == "__main__":
    main()
