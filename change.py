def get_change(input);

#value fo bills and coins in cents
denominations = {
        10000: "100 dollar bill",
        5000: "50 dollar bill",
        2000: "20 dollar bill",
        1000: "10 dollar bill",
        500: "5 dollar bill",
        200: "toonie",
        100: "loonie",
        25: "quarter",
        10: "dime",
        5: "nickel",
        1: "penny",
    }

#create a empty dictionary to store the amounts of change
change_count = {}

# change user input into to cents
amount_in_cents = int(amount * 100)

# go through the denominations and calculate the count for each
for denom, denom_name in denominations.items():
count, amount_in_cents = divmod(amount_in_cents, denom)
if count > 0:
change_count[denom_name] = count

return change_count
