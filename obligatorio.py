        
#[(size,price)]
#order
#Pre: que venga ordenado de mayor a menor
#priceSize = [(6,7),(5,1),(4,5),(3,5),(2,4),(1,1)]
priceSize = [(3,5),(2,7),(1,3)]
clientOrder = 3
 
def corteVarillaRecursivo(priceSize,clientOrder):
    result = list()
    for position in range(len(priceSize)):
        order = clientOrder
        resultSize = list()
        cutControl(priceSize,order,position,resultSize)
        result.append(resultSize)

    printResult(getBestOffer(result))
    return result

def cutControl(priceSize,order,position,result): 
    
    if(position<=len(priceSize)-1):
        
        (size,price) = priceSize[position]
        if(size>order):
            cutControl(priceSize,order,position+1,result)
        else:
            order=order-size
            result.append((size,price))
            if(order!=0):
                cutControl(priceSize,order,position,result)
            else:
                cutControl(priceSize,order,position+1,result)

    else:
        return

        
def getBestOffer(results): #obtiene la mejor oferta de todas las posibles
    highestPrice = 0
    for result in results:
        actualPrice = 0
        for (size,price) in result:
            actualPrice += price
        if(actualPrice>highestPrice):
            highestPrice = actualPrice
            bestOffer = result
    return bestOffer

def printResult(result): ##imprime el resultado
    for (size,price) in result:
            print("-")
            print("tamano: ")
            print(size)
            print("precio: ")
            print(price)

respuestas = corteVarillaRecursivo(priceSize,clientOrder)






