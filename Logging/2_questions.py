# Print 10 random numbers using generator functions.
# import random
#
#
# def rand_num(limit):
#     print('hi')
#     for i in range(limit):
#         yield random.randint(0, 100)
#
#
# r = rand_num(10)
# print(list(r))
# for n in r:
#     print(n)
#
# print(list(rand_num(10)))
# print(list(r))  # after the for loop, there is no more next(r), so, you get an empty list
# print(r)
# print(rand_num(10))
# print(next(r))


# Create a generator function for finding squares of numbers.
# def squares(limit):
#     i = 1
#     while i <= limit:
#         yield i**2
#         i += 1
#
#
# for num in squares(10):
#     print(num)
