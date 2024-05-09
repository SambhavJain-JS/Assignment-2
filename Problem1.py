def power(base, exponent):
    result = 1

    if exponent==0:
        return 1

    else:
        while exponent > 0:
            result = result * base
            exponent = exponent - 1

    return result


b=int(input('Enter Base: '))
e=int(input('Enter Exponent: '))
print(power(b,e))
