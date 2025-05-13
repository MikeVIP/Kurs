def bubble_sort(arr):
    n = len(arr)
    # Pętla wykonuje się n razy
    for i in range(n):
        # Przejście po nieposortowanej części listy
        for j in range(0, n - i - 1):
            # Jeśli element jest większy od następnego
            if arr[j] > arr[j + 1]:
                # Zamiana miejscami
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                

arr1 = [11, 5, 3, 8, 4, 2, 44, 12, 43]


bubble_sort(arr1)

print(arr1)
print("\n"*2)

arr2 = ["apple", "banana", "cherry", "apple", "cherry", "Jack", "Computer Science"]

bubble_sort(arr2)

print(arr2)
print("\n"*2)

def bubble_sort_debug(arr):
    n = len(arr)
    for i in range(n):
        print(f"--- Przejście {i+1} ---")
        for j in range(0, n - i - 1):
            print(f"Porównanie {arr[j]} i {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"Zamiana {arr[j]} z {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print("Aktualny stan:", arr)
        print("Po przejściu:", arr)
        
arr3 = [11, 5, 3, 8]


bubble_sort_debug(arr3)
