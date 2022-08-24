# Написать строку из чисел слепленных один к другому
# print(''.join(str(i) for i in range(101)))


# Написать счетчик простых чисел
import math

n = 1000
result = [1, 2, 3, 5, 7]
for i in range(11, n+1):
    if str(i)[-1] in ['0', '2', '4', '5', '6', '8']:
        continue
    else:
        for j in range(3, int(math.sqrt(i))+1, 2):
            if i % j == 0:
                break
        else:
            result.append(i)
print(result)