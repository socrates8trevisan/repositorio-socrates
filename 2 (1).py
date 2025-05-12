n1=int(input('digite o valor inicial: '))
n2=int(input('digite o valor final: '))
print('\nFahrenheit   celsius')
if n1<=n2:
    step=1
else:
    step=-1
for f in range(n1,n2+step,step):
    c=f*9/5+32
print(f'{f:>5.1f} f {c:.>7.3f} c')