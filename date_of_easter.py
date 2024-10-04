#user inputted year
year = int(input('Enter a year: '))

#easter date calculation
a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25 
g = (b - f + 1) // 3
h = ((19*a) + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + (2*e) + (2*i) - h - k) % 7
m = (a + (11*h) + (22*l)) // 451
n = (h + l - (7*m) + 114) // 31
p = (h + l - (7*m) + 114) % 31 

#variables printed to console
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
print('e =', e)
print('f =', f)
print('g =', g)
print('h =', h)
print('i =', i)
print('k =', k)
print('l =', l)
print('m =', m)
print('n =', n)
print('p =', p)

#print date of easter
print('Easter is on ', year,'-', n, '-', p+1, sep='')