#!/usr/bin/env python
# coding: utf-8

# In[51]:


import random
n = 5
k = 3
m = 1155127347
p = 3267000013            # A prime number P s.t. m < P
coeff = [random.randrange(0, p) for _ in range(k - 1)]
coeff.append(m)

shares = []
for i in range(1, n + 1):
    point = 0
    for coeff_index, coeff_value in enumerate(coeff[::-1]):    # Loop through the coeff list and add values
        point += i ** coeff_index * coeff_value                # With x powered   
    point %= p          # We do modular operation for the result
    shares.append((i, point))

print(f'Shares: {", ".join(str(share) for share in shares)}')