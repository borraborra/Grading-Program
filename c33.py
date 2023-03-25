xy=input('Enter a score between 0.0 and 1.0:')
try:
    xyz = float(xy)
    de = 0.0
    be = 1.0
    if xyz >= de and xyz <= be:
        if xyz >= 0.9:
            print('A')
        elif xyz >= 0.8:
            print('B')
        elif xyz >= 0.7:
            print('C')
        elif xyz >= 0.6:
            print('D')
        elif xyz < 0.6:
            print('F')
    else:
        print('Bad Score')
except:
    print ('Bad Score')

