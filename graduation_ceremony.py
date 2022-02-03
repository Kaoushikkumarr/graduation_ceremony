

def graduation_ceremony(number):

    if number == 0:
        return "Invalid input value, must be greater than or equal to 1"
    if number < 4:
        return str(1 << (number - 1)) + "/" + str(1 << number)
    
    value = [0 for _ in range(number + 1)]
    value[0] = None
    value[4] = 1
    for i in range(5, number + 1):
        value[i] = (2 ** (i - 4)) + value[i - 4] + value[i - 3] + value[i - 2] + value[i - 1]
    allowed = [0 for _ in range(number + 1)]
    allowed[0] = None
    for i in range(1, number + 1):
        allowed[i] = (2 ** i) - value[i]
    graduation_miss = allowed[number] - allowed[number - 1]
    return str(graduation_miss) + "/" + str(allowed[number])


if __name__ == "__main__":
    assert graduation_ceremony(5) == "14/29"
    assert graduation_ceremony(10) == "372/773"
    print("Sample Test Passed")