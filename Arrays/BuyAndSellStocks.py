def buy_and_sell_stocks(prices):
    min_price, max_price = float('inf'), 0
    for price in prices:
        max_profit = price - min_price
        max_price = max(max_price, max_profit)
        min_price = min(min_price, price)
    return max_price
