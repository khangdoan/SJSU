'''
Stock Calculator

Input:
- A stock symbol
- Allotment (number of shares)
- Final share price (in dollars)
- Sell commission (in dollars)
- Inital share price (in dollars)
- Buy commission (in dollars)
- Captial gain tax rate (in %)

Output:
- Proceeds (Allotment x Final share price)
- Cost (Allotment x Initial Share Price + commissions + Tax on Capital Gain)
- Net Profit (in dollars)
- Return on investment (in %)
- Break even price (in dollars)
'''


def readInput():
    '''Takes input and returns a dict'''


    return {'StockSymbol': input("Stock Symbol: "),
            'Allotment': float(input("Allotment: ")),
            'FinalSharePrices': float(input("Final share price (USD): ")),
            'SellCommission': float(input("sell Commission (USD): ")),
            'InitialSharePrices': float(input("Initial share prices (USD: ")),
            'BuyCommission': float(input("Buy Commission (USD): ")),
            'CapitalGainTaxRate': float(input("Capital gain tax rate (%): "))
            }


def calculateProceeds(allotment, finalSharePrice):
    return allotment * finalSharePrice


def calculateCost(allotment, initialSharePrice, commissions, capitalGainTaxRate):
    return allotment * initialSharePrice + commissions + capitalGainTaxRate


def printReport():
    userInput = readInput()
    proceeds = calculateProceeds(userInput['Allotment'], userInput['FinalSharePrices'])
    cost = calculateCost(userInput['Allotment'], userInput['InitialSharePrices'],
                         userInput["SellCommission"] + userInput["BuyCommission"],
                         (userInput['CapitalGainTaxRate']) / 100 *
                         (proceeds - userInput['Allotment'] * userInput['InitialSharePrices'] -
                          userInput["SellCommission"] - userInput["BuyCommission"]))

    print("*****************PROFIT REPORT**********************")
    print("Proceeds: ")
    print(proceeds)
    print("Cost: ")
    print(cost)
    print("Net Profit: ")
    print(proceeds - cost)
    print("Return on Investment: ")
    print((proceeds - cost) / cost * 100, "%")
    print("To break even, you should have a final share price of: ")
    print((userInput['Allotment'] * userInput['InitialSharePrices'] + userInput['SellCommission']
           + userInput["BuyCommission"]) / userInput['Allotment'])


printReport()
