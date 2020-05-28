# euler the python way
import math

# def euler29(): 
#     terms = []
#     for a in range(2, 101):
#         for b in range(2, 101):
#             terms.append(a**b)
#     distinct_terms = set(terms)
#     print(len(distinct_terms))

# def euler30():
#     def sum_fifth_powers(n):
#         digits = []
#         curr = n
#         while curr >= 1:
#             digits.append(curr % 10)
#             curr = math.floor(curr / 10)
#         return sum([i**5 for i in digits])

#     winners = []
#     for i in range(10, 1000000):
#         if i % 100000 == 0:
#             print('  -------  ', i)
#         if sum_fifth_powers(i) == i:
#             print(i)
#             winners.append(i)
#     print(sum(winners))

# def euler31():
#     coins = [200, 100, 50, 20, 10, 5, 2, 1]
#     total = 200
#     ways = [0]*(total+1)
#     ways[0] = 1
#     for coin in coins:
#         for i in range(total-coin+1):
#             ways[i + coin] += ways[i]
#     print(ways[200])

# def euler32():
#     def is_pandigital(l):
#         s = 0
#         d = []
#         for i in l:
#             c = i
#             while c >= 1:
#                 d.append(math.floor(c % 10))
#                 s += 1
#                 c /= 10
#         if s != 9 or 0 in d or len(set(d)) != 9:
#             return False
#         return True
#     pands = []
#     for product in range(1, 10**5):
#         for mul in range(1, int(math.sqrt(product))):
#             if product % mul == 0:
#                 if is_pandigital([product, mul, product/mul]):
#                     pands.append(product)
#                     break
#     print(sum(pands))

