# consider:
# that takes an input a positive integer n
#   if n is even, the algorithm divides it by two
#   if n is odd, the algorithm multiplies it by three and adds one
#
# the algorithm repeats this, until n is one

def weird_algorithm(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(1)

if __name__ == "__main__":
    n = int(input())
    weird_algorithm(n)