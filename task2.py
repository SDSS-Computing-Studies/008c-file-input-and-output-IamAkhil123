#!python3

from os import X_OK


a_file = open("task02.csv", "r")
list = [(line.strip()) for line in a_file]
a_file.close()
print(list)

x = input("Enter stock symbol")
y = list.index(x)

"""
##### Task 2
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches

(2 points)
"""
