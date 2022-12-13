var1 = [6, 0]
var2 = [4, 23]

diff = [var1[x]-var2[x] for x in range(len(var1))]

order = []
if abs(diff[0]) > abs(diff[1]):
    order.append('down')
    if diff[1] > 0:
        order.append('right')
        order.append('left')
    else ['left', 'right']
    order.append('up')
else:
    order = ['left', 'up', 'down', 'right'] if diff < 0 else ['up', 'left', 'right', 'down']
        