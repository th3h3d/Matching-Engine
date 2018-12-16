import time

current_date = time.strftime("%d %B %Y / %A", time.localtime())
Order_BUY = list()
Order_SELL = list()

with open('Orders.txt') as f: #read file
    lines = f.read().splitlines()

for walk in range(len(lines)):#split data
    line_part = lines[walk].split(' ')
    line_part2 = line_part[3].split('@')
    full_part = (line_part[0]+" "+line_part[1]+" "+line_part[2]+" "+line_part2[0]+" "+line_part2[1])
    full_part = full_part.split(' ')
    full_part[3] = int(full_part[3])
    full_part[4] = float(full_part[4])
    if full_part[1] == "SELL":
        Order_SELL.append(full_part)
    else:
        Order_BUY.append(full_part)

print("----------Order-Book--------\n")#show order book before trading
print("-------------SELL-----------\n")
for i in range(len(Order_SELL)):
    if(Order_SELL[i][3] != 0):
        print(Order_SELL[i])

print("-------------Buy------------\n")
for i in range(len(Order_BUY)):
    if(Order_BUY[i][3] != 0):
        print(Order_BUY[i])
print("----------------------------\n")

def matching_engine():#matching engine function
    for walk in range(len(Order_BUY)):
        for walk2 in range(len(Order_SELL)):
            if(Order_BUY[walk][2] == Order_SELL[walk2][2]):#check firm
                if(Order_BUY[walk][4] >= Order_SELL[walk2][4]):#check price
                    if(Order_BUY[walk][3] >= Order_SELL[walk2][3]):#check quantity
                        if(Order_SELL[walk2][3] == 0):
                            Order_SELL.remove(Order_SELL[walk2])#deleting ordered sell instrument
                            matching_engine()
                            break
                        print("-",current_date,"-Order Entered: ",Order_BUY[walk][0]," ",Order_BUY[walk][1]," ",Order_BUY[walk][2]," ",Order_BUY[walk][3],"@",Order_BUY[walk][4])
                        print("-",current_date,"-Order Entered: ",Order_SELL[walk2][0]," ",Order_SELL[walk2][1]," ",Order_SELL[walk2][2]," ",Order_SELL[walk2][3],"@",Order_SELL[walk2][4])
                        Order_BUY[walk][3] = (Order_BUY[walk][3] - Order_SELL[walk2][3])
                        Order_SELL[walk2][3] = 0
                        Order_SELL[walk2][4] = 0
                        print("-",current_date,"--------Traded: ",Order_BUY[walk][0]," ---> ",Order_SELL[walk2][0])
                        print(Order_BUY[walk][0]," : ",Order_BUY[walk][3]," Quantity left")
                        print(Order_SELL[walk2][0]," : ",Order_SELL[walk2][3]," Quantity left")
                        print("---------------------------------------------------------")
                    else:
                        if(Order_BUY[walk][3] == 0):
                            Order_BUY.remove(Order_BUY[walk])#deleting ordered buy instrument
                            matching_engine()
                            break
                        print("-",current_date,"-Order Entered: ",Order_BUY[walk][0]," ",Order_BUY[walk][1]," ",Order_BUY[walk][2]," ",Order_BUY[walk][3],"@",Order_BUY[walk][4])
                        print("-",current_date,"-Order Entered: ",Order_SELL[walk2][0]," ",Order_SELL[walk2][1]," ",Order_SELL[walk2][2]," ",Order_SELL[walk2][3],"@",Order_SELL[walk2][4])
                        Order_SELL[walk2][3] = (Order_SELL[walk2][3] - Order_BUY[walk][3])
                        Order_BUY[walk][3] = 0
                        Order_BUY[walk][4] = 0
                        print("-",current_date,"--------Traded: ",Order_BUY[walk][0]," ---> ",Order_SELL[walk2][0])
                        print(Order_SELL[walk2][0]," : ",Order_SELL[walk2][3]," Quantity left")
                        print(Order_BUY[walk][0]," : ",Order_BUY[walk][3]," Quantity left")
                        print("---------------------------------------------------------")
                else:
                    pass
            else:
                pass


matching_engine()#call the function for trading

print("----------Order-Book--------")#show order book after trading
print("-------------SELL-----------\n")
for i in range(len(Order_SELL)):
    if(Order_SELL[i][3] != 0):
        print(Order_SELL[i])

print("\n-------------BUY------------\n")
for i in range(len(Order_BUY)):
    if(Order_BUY[i][3] != 0):
        print(Order_BUY[i])
print("----------------------------\n")
