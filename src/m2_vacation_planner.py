# ask for type of destination
#   prints out a packing list for that vacation type

###############################################################################
# DONE: 1. (5 pts)
#
#   For this module, we are going to create a vacation planner that will help
#   the user plan what they need to bring on vacation.
#
#   For this _TODO_, write a function called starter_list() that takes 1
#   parameter:
#       - type      <-- str
#
#   This function should use a match case statement that checks for a matching
#   vacation type and returns a list of items that the user should probably
#   bring on that type of vacation.
#
#   So, for example, if the function is given the type "beach", the function
#   would return a list like this:
#
#      ["swimsuit", "towel", "sunscreen"]
#
#   For your function, make sure you have at least 3 vacation types and each
#   type should return a list of at least 3 items.
#
#   If the user types in an invalid vacation type, the function should return
#   an empty list.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def starter_list(type):
        match type:
            case "beach":
                return ["swimsuit", "towel", "sunscreen"]
            case "fishing":
                return ["rod", "bait", "cooler"]
            case "cruise":
                return "clothes", "passport", "I.D."
            case _:
                return []
#print(starter_list("beach"))
###############################################################################
# DONE: 2. (4 pts)
#
#   Now, perhaps the user would like to bring some of their own stuff that they
#   specify.
#
#   For this _TODO_, write a function called gather_items() that will
#   continually ask the user for an item to add to their list.
#
#   The function should meet these criteria:
#
#       1. Prompt the user like so:
#               "Please enter an item: "
#       2. It should keep track of all of the items in a list as it goes.
#       3. If the user types "end", it should stop asking for more items
#       4. Once it is done, it should return the list of items.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def gather_items():
    list=[]
    while True:
        item=input("Please enter an item: ")
        if item=="end":
             break
        list.append(item)
    return(list)
###############################################################################
# DONE: 3. (6 pts)
#
#   For this _TODO_, write a function called main() that will start things off.
#
#   Your function should meet these criteria:
#
#       1. It should first greet the user in a friendly way.
#       2. It should then prompt the user for a vacation type and allow them to
#          enter a vacation type.
#       3. It should then show them what item are already in their list based
#          on the type entered. There should be one item per line.
#       3. Next, it should start asking them for particular items and keep track
#          of them as the user enters more.
#       4. Once the user is done entering items, instead of printing the list of
#          items that they entered, it should print their entire list that
#          includes the starter list from the beginning and all the items that
#          they entered. You should do this by combining the lists and looping
#          through it printing each item. Do NOT just loop through the two lists
#          separately.
#       5. At the very end, it should say goodbye to the user in some friendly
#          way.
#
#   Make sure you call the function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
     print("Hello!")
     vacation=input("Enter a type of vacation! ")
     list=starter_list(vacation)
     for y in list:
          print(y)
     MoreItems=gather_items()
     ultra_list=list + MoreItems
     for x in ultra_list:
          print(x)
     print("Enjoy the vacation!")

main()