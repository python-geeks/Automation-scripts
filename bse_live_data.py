#   install bsedata library using >>> pip install bsedata 

#start
from bsedata.bse import BSE
bse = BSE()
print(bse)
# to execute "updateScripCodes" on instantiation
bse = BSE(update_codes = True)
#to get quotes of companies
codelist = ["500116", "512573"]
for code in codelist:
    quote = bse.getQuote(code)
    print(quote["companyName"])
    print(quote["currentValue"])
    print(quote["updatedOn"])
#top gainers
top_gain = bse.topGainers()
print(top_gain)
#top loser
top_loser = bse.topLosers()
print(top_loser)
#period trend of a specific company {here of 6 months}
trend = bse.getPeriodTrend('534976','6M')
print(trend)
#all info
print(bse.getScripCodes())
