# ask the user for a start number and store it
def get_start_stop():
    ''' obtains start and stop number from the user'''
    start_number = int(input("Enter a reasonable number to be used as your start number: "))
    stop_number = int(input("Enter another reasonable number to be used as your start number: "))
    number_tuple = (start_number, stop_number)
    return number_tuple


# check if the numbers in the list are divisible by three
def getnums_divisible_by_three(nums):
    '''return numbers divisible by three'''
    number_list = []
    for number in nums:
        if number % 3 == 0:
            number_list.append(number)
    return number_list


def main():
    '''Main entry point of program.'''
    start_stop = get_start_stop()
    numbers = range(start_stop[0], start_stop[1])
    hits = getnums_divisible_by_three(numbers)
    for hit in hits:
        print(hit, end=' ')
    print()



if __name__ == '__main__':
    main()
