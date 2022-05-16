"""Count words in file."""


# # put your code here.
# import sys

# # file_obj = open(sys.argv[1])
# # result_dict = {}

# for line in file_obj:
#     line_lst = line.rstrip().split()

#     for word in line_lst:
#         # if word not in result_dict:
#         #     result_dict[word] = 1
#         # else:
#         #     result_dict[word] += 1
#         result_dict[word] = result_dict.get(word, 0) + 1

# for key, value in result_dict.items():
#     print(key, value)


from itertools import count


def tokenize(filename):
    file_obj = open(filename)
    get_token = []
    for line in file_obj:
        line_lst = line.rstrip().split()
        get_token.extend(line_lst)

    return get_token


print(tokenize("test.txt"))


def count_words(words):
    result_dict = {}
    for word in words:

        result_dict[word] = result_dict.get(word, 0) + 1
    return result_dict


print(count_words(tokenize("test.txt")))


def print_words_count(dict):
    for key, value in dict.items():
        print(key, value)


dict = count_words(tokenize("test.txt"))
print_words_count(dict)


def normalize(word):
    result_st = ''
    for char in word:
        if char.isalpha():
            result_st += char
