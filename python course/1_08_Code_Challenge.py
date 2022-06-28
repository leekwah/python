# plus, minus, times, division, negation, power, reminder
def plus(a, b):
  return int(a) + int(b)

def minus(a, b):
  return int(a) - int(b)

def times(a, b):
  return int(a) * int(b)

def division(a, b):
  return int(a) / int(b)

def negation(a):
  return -(int(a))

def power1(a, b):
  return (int(a) ** int(b))

def power2(a, b):
  return pow(int(a), int(b))

def reminder(a, b):
  return int(a) % int(b)

p_rst = plus("2", 4)
m_rst = minus(4, "3")
t_rst = times(7, "7")
d_rst = division("4","8")
n_rst = negation("100")
p1_rst = power1(10, "10")
p2_rst = power2("10", 10)
r_rst = reminder(4, "3")

print(p_rst)
print(m_rst)
print(t_rst)
print(d_rst)
print(n_rst)
print(p1_rst)
print(p2_rst)
print(r_rst)