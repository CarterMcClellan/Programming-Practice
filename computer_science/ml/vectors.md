# Dot Product
What is the geometric interpretation of the dot product of two vectors.
```
The dot product between 2 vectors represents the cosine of the angle between those 2 vectors.
```

Given a vector u, find vector v of unit length such that the dot product of u and v is maximum
```
Cosine ranges between -1 and 1. Cosine(0) is 1 therefore to maximize the dot product between u and v
I would have v be the unit vector of u. So I would divide u by its length
```

# Outer Product
Given 2 vectors a = [3, 2, 1] and b = [-1, 0, 1] caulcate the outer product aTb.
```
3 [-1, 0, 1]    [-3, 0, 3]
2             = [-2, 0, 2]
1               [-1, 0, 1]
```

Give an example of how the outer product can be useful in ML.
```
To reduce the number of parameters needed to store a rank 1 matrix, you could instead serialize model
weights as the outer product of 2 vectors.
```

# Misc
What does it mean for 2 vectors to be linearly independent.
```
To be linearly dependent means that we can express 1 vector as another simply by multipliying by a coefficent, for instance [-1, 0, 1] and [-2, 0, 2] are linearly depedent. Linearly independent is the opposite of this.
```

Given 2 sets of vectors A = [a1, a2, ...] and B = [b1, b2, ...]. How do you check if they share the same basis
```
A basis would be the minimum number of vectors in the set which it takes to express every other
vector in the set. We can find the dimension of the space for sets A, B and A union B. If they are 
all the same, then they share a basis.
```

Given n vectors each of d dimensions, what is the dimension of their span?
```
The dimension will ber min(n, d, rank M)
```

What is a norm?
```
L0 = Does not exist
L1 = a + b + c + ...
L2 = sqrt(a^2 + b^2 + ....)
LNorm = (abs(a)^p + abs(b)^p + ...) ^ (1/p)
```

How do norm and metric differ?
```
A norm is the measure of the size/ length of a single vector, a metric is the distance between
2 vectors.

Every norm can be expressed as a metric because the norm of (a-b) is the same as metric(a, b)

However not every metric can be expressed as a norm, eg the distance metric d(x, y) = 0 if x=y, else 1 is a valid metric but doesn't come from a norm.
```