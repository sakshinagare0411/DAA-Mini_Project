import time
import random
import concurrent.futures

# Merge function to merge two sorted halves
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Regular merge sort implementation
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Multithreaded merge sort implementation
def threaded_merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(threaded_merge_sort, arr, left, mid)
            future2 = executor.submit(threaded_merge_sort, arr, mid + 1, right)
            future1.result()
            future2.result()
        merge(arr, left, mid, right)

# Function to create array based on case
def create_array(size, case):
    if case == "best":
        return list(range(size))  # Best case (already sorted)
    elif case == "worst":
        return list(range(size, 0, -1))  # Worst case (reverse sorted)
    elif case == "random":
        return random.sample(range(size), size)  # Random case
    else:
        raise ValueError("Invalid case type!")

# Function to run merge sort based on user selection
def run_sorting_algorithm(algorithm, arr):
    start_time = time.time()

    if algorithm == "regular":
        merge_sort(arr, 0, len(arr) - 1)
    elif algorithm == "multithreaded":
        threaded_merge_sort(arr, 0, len(arr) - 1)
    else:
        raise ValueError("Invalid algorithm type!")

    end_time = time.time()
    return end_time - start_time

# Menu for user interaction
def display_menu():
    print("\n=== Merge Sort Performance Menu ===")
    print("1. Regular Merge Sort")
    print("2. Multithreaded Merge Sort")
    print("3. Exit")
    return input("Select an option (1/2/3): ")

def select_case():
    print("\n--- Choose Case Type ---")
    print("1. Best Case (already sorted array)")
    print("2. Worst Case (reverse sorted array)")
    print("3. Random Case")
    print("4. Input your own array")
    case_option = input("Select a case (1/2/3/4): ")

    if case_option == "1":
        return "best"
    elif case_option == "2":
        return "worst"
    elif case_option == "3":
        return "random"
    elif case_option == "4":
        return "input"
    else:
        print("Invalid option! Defaulting to random case.")
        return "random"

def select_array_size():
    try:
        size = int(input("\nEnter the size of the array: "))
        return size
    except ValueError:
        print("Invalid input! Defaulting to size 10000.")
        return 10000

def get_user_array():
    try:
        arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
        return arr
    except ValueError:
        print("Invalid input! Please provide a list of integers.")
        return get_user_array()

def main():
    while True:
        choice = display_menu()

        if choice == "1" or choice == "2":
            case = select_case()
            if case == "input":
                arr = get_user_array()
            else:
                size = select_array_size()
                arr = create_array(size, case)

            algorithm = "regular" if choice == "1" else "multithreaded"

            print(f"\nRunning {algorithm} merge sort...")
            time_taken = run_sorting_algorithm(algorithm, arr)
            print(f"Sorted array: {arr}")
            print(f"Time taken: {time_taken:.6f} seconds")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option! Please select a valid menu option.")

if __name__ == "__main__":
    main()
