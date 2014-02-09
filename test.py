num_list = [1, 2, 3, 4, 5,-1]
mix_list = [1 , 2, "aweome", 3, 4, 5, -2, "hello"]
word_list = ["amy", "technical", "beta", "cat", "awesome"]


def average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = float(total) / len(numbers)
    return average

print average(num_list)
