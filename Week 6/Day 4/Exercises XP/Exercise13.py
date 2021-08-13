sandwich_orders = ['chicken sandwich','philiy cheesesteak','tuna melt','croque madames','club sandwich']
finished_sandwiches = []
while True:
    if not sandwich_orders:
        break
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.pop(0)
for i in finished_sandwiches:
    print("I made your "+i,end=',')