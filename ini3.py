#sample dataset
>>> s = "HrqZPkUedPQfBTIkdCZgq03NMhAfmhae9WBQCRbW0HCrKK3O0Ninoxc9zOdXoA5pDeNeull6OkhCVQqYblFPwi7YcTWPCiMnMbB2fHq4VDjX4Xb0MhHZUyKqmxklFw3VDwDFcKmargaritiferaouCfWqkuHMz0mx7cgo."
>>> a = 49
>>> b = 53
>>> c = 134
>>> d = 146
#get the slice from a to b and c to d
>>> slice1 = s[a:b+1]
>>> slice2 = s[c:d+1]
#combine the slices with a space
>>> result = slice1 + " " + slice2
>>> print(result)
Ninox margaritifera
