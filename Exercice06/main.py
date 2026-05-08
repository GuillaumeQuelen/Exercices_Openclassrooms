def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average


# Exemple d'utilisation
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"La moyenne est : {average}")


