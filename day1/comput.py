print('*****************')
print('1:comput your BMI')
print('Q:quit the comput')
print('*****************')
sSelect = input()
while( not sSelect == 'Q'):
    sLength = input('please input your length:')
    sHeight = input('please input your height:')
    bmi = float(sHeight) / (float(sLength) * float(sLength))
    print('your BMI is %.2f' % bmi)
    print('*****************')
    print('1:comput your BMI')
    print('Q:quit the comput')
    print('*****************')
    sSelect = input()

