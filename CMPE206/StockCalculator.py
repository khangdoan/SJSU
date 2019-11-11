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

    # stockSym = input("Stock Symbol: ")
    # allotment = input("Allotment (Number of shares): ")
    # finalSharePrices = input("Final share price (USD): ")
    # sellCommision = input("sell Commission (USD): ")
    # initialSharePrices = input("Initial share prices (USD: ")
    # buyCommission = input("Buy Commission (USD): ")
    # capitalGainTaxRate = input("Capital gain tax rate (%): ")
    return {'StockSymbol': int(input("Stock Symbol: ")),
            'Allotment': int(input("Final share price (USD): ")),
            'FinalSharePrices': int(input("Final share price (USD): ")),
            'SellCommission': int(input("sell Commission (USD): ")),
            'InitialSharePrices': int(input("Initial share prices (USD: ")),
            'BuyCommission': int(input("Buy Commission (USD): ")),
            'CapitalGainTaxRate': int(input("Capital gain tax rate (%): "))
            }


def calculateProceeds(allotment, finalSharePrice):
    return allotment * finalSharePrice


def calculateCost(allotment, initialSharePrice, commissions, capitalGainTaxRate):
    return allotment * initialSharePrice + commissions+capitalGainTaxRate

def printReport():
    userInput = readInput()
    cost = calculateCost(userInput['Allotment'],userInput['InitialSharePrices'],userInput["SellCommision"],
                        (int(userInput['CapitalGainTaxGain']) / 100) *
                        (int(userInput['Allotment'])*int(userInput['FinalSharePrices']) -
                         int(userInput['Allotment'])*int(userInput['InitialSharePrices'])))
    proceeds = calculateProceeds(userInput['Allotment'], userInput['FinalSharePrices'])
    print("*****************PROFIT REPORT**********************")
    print("Proceeds: ")
    print(proceeds)
    print("Cost: ")
    print(cost)
    print("Net Profit: ")
    print(proceeds - cost)
    print("Return on Investment: ")
    print((proceeds-cost)/cost)
    print("To break even, you should have a final share price of: ")
    print(cost/userInput['Allotment'])


printReport()

