from bsedata.bse import BSE

b = BSE(update_codes = True)
tg = b.topGainers()
print("Top Gainers - Now")
for i in tg:
    print(i)

print('\n-------------------------\n')

tl = b.topLosers()
print("Top Losers - Now")
for j in tl:
    print(j)

# indices catagory parameter
'''
market_cap/broad, sector_and_industry, thematics, strategy
sustainability, volatility, composite, government, corporate, money_market
'''
indices = b.getIndices(category='government')
print(indices)

# Updates scrip code and updates library cache
b.updateScripCodes()

# print(b.verifyScripCode(code))
# print(b.getScripCodes)