def binary_search_recursive(phonebook, name, left, right):
    if left > right:
        return -1  # Friend not found
    mid = (left + right) // 2
    if phonebook[mid][0] == name:
        return mid  # Friend found
    elif phonebook[mid][0] < name:
        return binary_search_recursive(phonebook, name, mid + 1, right)
    else:
        return binary_search_recursive(phonebook, name, left, mid - 1)

def binary_search_non_recursive(phonebook, name):
    left, right = 0, len(phonebook) - 1
    while left <= right:
        mid = (left + right) // 2
        if phonebook[mid][0] == name:
            return mid  # Friend found
        elif phonebook[mid][0] < name:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Friend not found

def insert_friend(phonebook, name, number):
    index = binary_search_non_recursive(phonebook, name)
    if index == -1:
        # Friend not found, insert them at the correct position
        for i in range(len(phonebook)):
            if phonebook[i][0] > name:
                phonebook.insert(i, (name, number))
                return
        phonebook.append((name, number))  # Add at the end

def main():
    phonebook = []  # List of tuples (name, number)
    
    while True:
        print("1. Add Friend")
        print("2. Search Friend (Recursive)")
        print("3. Search Friend (Non-Recursive)")
        choice = int(input("Enter your choice (1/2/3): "))
        
        if choice == 1:
            name = input("Enter friend's name: ")
            number = input("Enter friend's number: ")
            insert_friend(phonebook, name, number)
            phonebook.sort()  # Ensure the phonebook remains sorted
            print(f"{name} added to the phonebook.")
        
        elif choice == 2:
            name = input("Enter friend's name to search (Recursive): ")
            index = binary_search_recursive(phonebook, name, 0, len(phonebook) - 1)
            if index != -1:
                print(f"{name} found. Mobile number: {phonebook[index][1]}")
            else:
                print(f"{name} not found in the phonebook.")
        
        elif choice == 3:
            name = input("Enter friend's name to search (Non-Recursive): ")
            index = binary_search_non_recursive(phonebook, name)
            if index != -1:
                print(f"{name} found. Mobile number: {phonebook[index][1]}")
            else:
                print(f"{name} not found in the phonebook.")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    
if __name__ == "__main__":
    main()

