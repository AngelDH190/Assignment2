"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    cost = annual_cost / SEMESTERS_PER_YEAR
    return cost


def cost_per_month(annual_cost):
    cost = annual_cost / MONTHS_PER_YEAR
    return cost


def cost_per_day(annual_cost):
    cost = annual_cost / SEMESTERS_PER_YEAR / CLASS_DAYS_PER_SEMESTER
    return cost


def cost_per_credit(annual_cost, credits):
    cost = annual_cost / SEMESTERS_PER_YEAR / credits
    return cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    cost = cost_per_credit(annual_cost, credits)
    cost = cost * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    total_cost = float(input("Total cost of one year: "))
    sem_credits = int(input("Credits this semester: "))

    while True:
        # Show your menu here.

        menu = ["1. Cost per semester",
                "2. Cost per month",
                "3. Cost per class day",
                "4. Cost per credit",
                "5. Cost per CS1430 class",
                "Q. Quit"]

        options = {"1": (f"Cost per semester: ${cost_per_semester(total_cost):.2f}"),
                    "2": (f"Cost per month: ${cost_per_month(total_cost):.2f}"),
                    "3": (f"Cost per day: ${cost_per_day(total_cost):.2f}"),
                    "4": (f"Cost per credit: ${cost_per_credit(total_cost, sem_credits):.2f}"),
                    "5": (f"Cost per class: ${cost_per_class(total_cost, sem_credits):.2f}"),
                    "q": None}

        for i in menu:
            print(f"    {i}")

        choice = input("Choose an option: ").lower()
        choice = options[choice.lower()]

        if choice == None:
            print("Thanks for running the program!")
            break
        else:
            print(choice)
        
        
        # Add a branch for each menu option here.
        


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
