
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping():
    total_cost = 0
    for i in price_list.keys():
        if i in quantity_list:
            cost = price_list[i] * quantity_list[i]   # Calculate the cost of the item by multiplying its price with its quantity\
            total_cost += cost  # Add the cost of the current item to the total cost
    print("total cost = ", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity):
    for i in price_list.keys(): #key represent the fruit in this scenario 
        if i == fruit:
            cost = quantity*price_list[i]  #eg if key is apple, cost = quantity multiply by price_list[apple] = 1.2
            break

    print("cost of ", quantity, fruit, "=", cost)
    return cost

def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping()


if __name__ == "__main__":
    main()