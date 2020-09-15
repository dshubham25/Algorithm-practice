#Write a program that takes two arrays representing integers, and retums an integerWrite a program that takes two arrays representing integers, and retums an integer
#representing their product


def multiply(n1, n2):
    sign = -1 if (n1[0] < 0) ^ (n2[0] < 0) else 1
    n1[0], n2[0] = abs(n1[0]), abs(n2[0])
    result = [0] * ((len(n1) + len(n2))
    for i in reversed(range(len(n1))):
        
        for j in reversed(range(len(n2))):

            result[i+j+1] += n1[i]*n2[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10
    result = result[next((i for i, x in enumerate(result)
                            if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]