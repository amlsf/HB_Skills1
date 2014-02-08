num_list = [1, 2, 3, 4, 5]
mix_list = [1 , 2, "aweome", 3, 4, 5, -2, "hello"]
word_list = ["amy", "technical", "beta", "cat", "awesome"]


def smallest(some_list):
    for i in range(len(some_list)-1):
        if some_list[i+1] < some_list[i]:
             smallest = some_list[i+1]

    return smallest

print smallest(num_list)