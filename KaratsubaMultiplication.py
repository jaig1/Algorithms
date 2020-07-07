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



def karatsuba(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = round(n / 2)
		
		a = int (x / 10**(nby2) ) # x1
		b = int (x % 10**(nby2) )  # x0
		c = int (y / 10**(nby2) ) # y1
		d = int (y % 10**(nby2) ) # y0
		
		ac = karatsuba(a,c)  #z2
		bd = karatsuba(b,d)  #z0
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd #z1
        
        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		    #prod = z2 * B2m + z1 Bm + z0
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod

product = karatsuba(12345, 6789 )
print(product)
