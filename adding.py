import fileinput
print sum(map(lambda x:float(x.rstrip()), fileinput.input()))