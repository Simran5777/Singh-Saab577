def remove_uneven(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = remove_uneven(numbers)
    print(f"Original list: {numbers}")
    print(f"List with only even numbers: {even_numbers}")

if __name__ == "__main__":
    main()
