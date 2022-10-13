from bsedata.bse import BSE

b = BSE(update_codes=True)
tg = b.topGainers()
print("\nTOP GAINERS - Now\n")
for i in tg:
    for j in i:
        print(j, i[j])

print('\n-------------------------\n')

tl = b.topLosers()
print("\nTOP LOSERS - Now\n")
for j in tl:
    for j in i:
        print(f"{j}: {i[j]}")

# indices catagory parameter
category = ["market_cap/broad", "sector_and_industry", "thematics",
            "strategy", "sustainability", "volatility", "composite",
            "government", "corporate", "money_market"]

for i in category:
    indices = b.getIndices(category=i)
    print(f"\nIndices based on {i}")
    print(indices)

# Updates scrip code and updates library cache
b.updateScripCodes()

# print(b.verifyScripCode(code))
# print(b.getScripCodes)
