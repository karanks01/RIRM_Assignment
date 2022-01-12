from collections import deque

def stock_max_profit(prices):
    max = 0
    prices = deque(prices)
    buy_price = prices.popleft()

    for price in prices:
        if price < buy_price:
            buy_price = price
        else:
            profit = price - buy_price
            if profit > max:
                max = profit
    if max:
        return max
    else:
        return -1

if __name__ == '__main__':
        
    prices = []
    
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        prices.append(ele)
        
    print(prices)
    max_profit = stock_max_profit(prices)
    print(max_profit)
