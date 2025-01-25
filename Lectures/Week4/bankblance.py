# You put $10,000 into a bank account that earns 5 percent 
# interest per year. How many years does it take for the account 
# balance to double the original investment?

#Start with a year value of 0, a column for the interest, and a 
#balance of $10,000.

#initial balance = 10,000
#interest = 0.05
#final balance = 2 * initial balance
#year = 0 to start, incriment as we go

INITIAL_BALANCE = 10000
INTEREST_RATE = 0.05
FINAL_BALANCE = 2 * INITIAL_BALANCE

year = 0
current_balance = INITIAL_BALANCE

while(current_balance < FINAL_BALANCE):
    year = year + 1
    current_balance = current_balance + (current_balance * INTEREST_RATE)

print(f"The original investment doubles in {year} years.")
