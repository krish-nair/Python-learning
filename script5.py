temperature=[10, -20, -289, 100]
def c_to_f(c):
    if c < -273.3:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
for temp in temperature:
    print(c_to_f(temp))
