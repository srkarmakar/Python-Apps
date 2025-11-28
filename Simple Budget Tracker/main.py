budget = 0

def budget_tracker():
    global budget
    initial_budget = input("Please enter your Current Balance: INR ")
    budget = float(initial_budget)
    purchase_amount = input("Please enter the Purchased Amount: INR ")

    return {"initial_budget": budget, "purchase_amount": purchase_amount}


def calculation(initial_budget, purchase_amount):
    global budget
    print(f"Initial Budget: INR {initial_budget}")
    print(f"Purchase Amount: INR {purchase_amount}")
    half_of_budget = round(float(initial_budget) / 2, 2)  # rounding the half of budget

    if float(initial_budget) >= float(purchase_amount):
        remaining_amount = round(float(initial_budget) - float(purchase_amount),2)
        budget = remaining_amount
        print(f"Remaining Balance: INR {remaining_amount}")
        if half_of_budget > float(purchase_amount):
            print(f"Did the purchase exceed half the budget? - No")
        elif half_of_budget == float(purchase_amount):
            print(
                f"Did the purchase exceed half the budget? - No, It equal Half of the budget."
            )
        else:
            print(f"Did the purchase exceed half the budget? - Yes")
    else:
        print("Purchase amount is greater than or equal to the initial budget.")

def is_shopping_done():
    global budget
    is_done = input('Did you bought anything more? [Y/N] - ')
    if is_done == 'Y' or is_done == 'y':
        purchase_amount = input("Please enter the Purchased Amount: INR")
        recalculate = calculation(budget,float(purchase_amount))
        is_shopping_done()
    else :
        print(f'Your final Balance is INR {budget}.Have a Great Day!')


decision = budget_tracker()
calculations = calculation(decision["initial_budget"], decision["purchase_amount"])
reconsider = is_shopping_done()
