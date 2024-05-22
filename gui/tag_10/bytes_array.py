""" 
Bytes Array
"""

x = b"x"
print(type(x))  # <class 'bytes'>

b = bytearray(b"ab")  # <class 'bytesarray'>
print(b)
b.append(ord("a"))
print(b)
b.extend([32, 119, 114])


# numpy (numerisches Python, insbesonde Matrizen),
# pandas (tabellenkalkulation/statistik),
# matplotlib (plotten),
# scipy (Curve Fitting),
# scikit-learn (ML),
# tensorflow/Keras (KNN)
