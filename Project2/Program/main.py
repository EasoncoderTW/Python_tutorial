from typhoon_days import TyphoonDays

tds = TyphoonDays() # init an object

# Method 1: get all info
result = tds() # call
print(result)

# Method 2: get specific city info
result = tds(["高雄市","臺南市"]) # call
print(result)


