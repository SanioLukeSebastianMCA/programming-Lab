s = {'maths': 40, 'physics': 24, 'english': 41}
l = list(s.items())
l.sort()
print('Ascending order is', l)
l = list(s.items())
l.sort(reverse=True)
dict = dict(l)
print("Descending order is", dict)

