# what about 2 fancy indexes?
import numpy as np
a = np.arange(24).reshape((8,3))
print(a)

fancy1 = [0, 1, 3]
fancy2 = [0, 2, 1]

print(a[fancy1, fancy2])