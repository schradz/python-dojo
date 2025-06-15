def extract_digits(number):
    extracted_digits = []
    while(number >= 10):
        digit = number % 10
        extracted_digits.append(int(digit))
        number /= 10
    extracted_digits.append(int(number))
    return extracted_digits


def sum_digits(number):
    extracted_digits = extract_digits(number)
    sum = 0
    for digit in extracted_digits:
        sum += digit
    return sum
