var = input()
var_str = var.split(' ')

x = float(var_str[2])

if(x <= 1):
    print("f(x) = %.2f" %1)
elif((x > 1) and (x <= 5)):
    print("f(x) = %.2f" %x)
elif((x > 5) and (x <= 10)):
    x = x ** 2
    print("f(x) = %.2f" %x)
else:
    x = x ** 3
    print("f(x) = %.2f" %x)