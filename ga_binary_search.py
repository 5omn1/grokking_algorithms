def main():
    def binary_search(arr, item):
        begin = 0
        tail = len(arr) - 1

        while begin <= tail:
            mid = (begin + tail) // 2
            guess = arr[mid]
            if guess == item:
                return mid
            elif guess < item:
                begin = mid + 1
            else:
                tail = mid - 1
        return None

    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 7))
    print(binary_search(my_list, -1))


if __name__ == "__main__":
    main()
