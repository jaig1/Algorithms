"""
Let x and y be represented as n-digit strings in some base B. For any positive integer m less than n, one can write the two given numbers as

x = x1 B^m + x0
y = y1 B^m + y0,

where x0 and y0 are less than B^m. The product is then

xy = (x1 B^m + x_0)(y1 B^m + y0)
xy = z2 B^{2m} + z1 B^m + z0

where

z2 = x1y1
z1 = x1y0 + x0y1
z0 = x0y0

To compute the product of 12345 and 6789, choose B = 10 and m = 3. Then we decompose the input operands using the resulting base (Bm = 1000), as:

12345 = 12 · 1000 + 345
6789 = 6 · 1000 + 789

Only three multiplications, which operate on smaller integers, are used to compute three partial results:

z2 = 12 × 6 = 72
z0 = 345 × 789 = 272205
z1 = (12 + 345) × (6 + 789) − z2 − z0 = 357 × 795 − 72 − 272205 = 283815 − 72 − 272205 = 11538
We get the result by just adding these three partial results, shifted accordingly
(and then taking carries into account by decomposing these three inputs in base 1000 like for the input operands):

result = z2 · B2m + z1 · Bm + z0, i.e.
result = 72 · 10002 + 11538 · 1000 + 272205 = 83810205.


"""
def zeroPad(numberString, zeros, left = True):
    """Return the string with zeros added to the left or right."""
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString

def karatsubaMultiplication(x ,y):
    """Multiply two integers using Karatsuba's algorithm."""
    #convert to strings for easy access to digits
    x = str(x)
    y = str(y)
    #base case for recursion
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))
    n = len(x)
    j = n//2
    #for odd digit integers
    if (n % 2) != 0:
        j += 1
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    #recursively calculate
    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication(a + b, c + d)
    A = int(zeroPad(str(ac), AZeroPadding, False))
    B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))
    return A + B + bd





product = karatsubaMultiplication(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627 )
#product = karatsubaMultiplication(12045, 6709 )
print(product)
