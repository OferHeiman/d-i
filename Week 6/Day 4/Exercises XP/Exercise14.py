sandwich_orders = ['pastrami sandwich','chicken sandwich','philiy cheesesteak','pastrami sandwich','tuna melt','croque madames','club sandwich','pastrami sandwich']
finished_sandwiches = []
print("The deli has run out of pastrami sandwich's")
while True:
    if not sandwich_orders:
        break
    if(sandwich_orders[0] == 'pastrami sandwich'):
        sandwich_orders.pop(0)
    else:
        finished_sandwiches.append(sandwich_orders[0])
        sandwich_orders.pop(0)
for i in finished_sandwiches:
    print("I made your "+i,end=',')