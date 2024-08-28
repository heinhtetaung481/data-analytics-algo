import numpy as np

data1 = [4, 3, 5, 3.3]
ndarray1 = np.array(data1)
print(ndarray1)
print(ndarray1.ndim)
print(ndarray1.shape)

# 2d array
data2 = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(data2)
print(array_2d)
print(array_2d.ndim)
print(array_2d.shape)
print(array_2d.dtype)

# math operation
ndarray3 = np.round(ndarray1 * 0.5, 2)
ndarray4 = np.round(array_2d * 0.5, 2)
print(ndarray3)
print(ndarray4)

array5 = np.random.standard_normal((3,2))
print(array5)

array6 = np.zeros(5)
print(array6)
array7 = np.zeros((2,3))
print(array7)

array8 = np.ones(5)
print(array8)
array9 = np.ones((2,3))
print(array9)

array10 = np.arange(5)
print(array10)

array11 = np.arange(1,6)
print(array11)

array12 = np.array([array10, array11])
print(array12)
print(array12.ndim)
print(array12.shape)


array13 = np.arange(2, 7)
array14 = np.arange(3, 8)
array15 = np.array([array13, array14])

print(array12, array15)

array16 = array12 + array15
print('Add', array16)

array16 = array12 - array15
print('Substract', array16)

array16 = array12 * array15
print('Mutiplication', array16)

array16 = np.round(array12 / array15, 2)
print('Mutiplication', array16)

array16 = np.round(array12 ** array15, 2)
print('Mutiplication', array16)

# comparison
array17 = array15<array16
print('comparison', array17)

# indexing and slicing
array18 = np.arange(10)
print('index 8', array18[8])
print('index 3:6', array18[3:6])
print('index :6', array18[:6])
print('index 3:', array18[3:])
print('index -1', array18[-1])

# array reference
print('original array', array18)
array19 = array18[3:6]
print('sliced array', array19)
array19[0] = 10
print('updated sliced array', array19)
print('original array', array18)

array20 = np.array([[1,2,3], [4,5,6]])
print(array20)
print(array20[0])
print(array20[1])
print(array20[0,1])

names = np.array(["Ada", "Bob", "Charles", "Ada", "Charles"])
data = [[3,4,3], [6, 2, 4], [8, 5, 2], [2, 7, 9], [6, 4, 7]]

data = np.array(data)

print(data.mean(axis=0))
print(data.mean(axis=1))

print('sum column', data.sum(axis=0))
print('sum row', data.sum(axis=1))

# data = np.array([3, 2, 4, 5])
# print('cum sum', data.cumsum())
# print('cum prod', data.cumprod())

print('2d cumsum', data.cumsum())
print('2d cumprod', data.cumprod())

print('2d cumsum by column', data.cumsum(axis=0))
print('2d cumprod by column', data.cumprod(axis=0))

print('2d cumsum by row', data.cumsum(axis=1))
print('2d cumprod by row', data.cumprod(axis=1))

print(data > 5)
print((data > 5).sum())

print((data > 10).any())
print((data > 5).all())

data_1d = [3, 2, 4, 3, 1, 6]
# data_1d.sort()
# print(data_1d)

data.sort()
print(data)

data.sort(axis=0)
print(data)

print(np.argsort(data_1d))

names = np.array(["Ada", "Bob", "Charles", "Ada"])
scores = np.array([80, 70, 90, 70])

print(scores.argsort())
print(names[scores.argsort()])

print('unique', np.unique(names))
print('unique', np.unique(scores))

# set defference
array1 = np.array(['a', 'b', 'c'])
array2 = np.array(['a', 'b', 'd'])
set1 = np.setdiff1d(array1, array2)
set2 = np.setdiff1d(array2, array1)
set3 = np.concatenate((set1, set2))
print(set3)

set1 = np.union1d(array1, array2)
print(set1)

print(np.flip(array1))
