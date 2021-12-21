
## Problem Statement 
### Food ordering system 
Implement an online food ordering system.

#### Features:
1. This system has tie-up with restaurants where each restaurant has a menu, with all its servable items with their individual price.
2. Each restaurant has a maximum processing capacity of items at any given time. Beyond that, it won't accept any further item requests until items which are in processing are completed.
3. Each restaurant takes some time to prepare and dispatch food. Once an item is prepared and dispatched, it notifies the system about it. After which, it can take new request.
4. Once one restaurant can be selected based on restaurant selection strategy for one order.
5. Order is accepted from the customer only if all the items can be fulfilled by one selected restaurant.

#### Requirements:
1. Onboard new restaurant with its menu and item processing capacity.
2. Restaurant should be able to change its menu or update price.
3. Customer should be able to place an order by giving items.
4. Implement one restaurant selection strategy. (Eg.: select available restaurant which offers the lowest price for that order item). There should be an option of giving different strategies in future.
5. System should be able to keep track of all items served by each restaurant.

#### Other Details:
1. use in-memory store for now.
2. Do not create any UI for the application. You can take input from command line or read from file.
3. Start the system with onboarding 3 restaurants, each restaurant serving 5 items and has processing power for 3 items.


#### Expectations:
* Your code should be working by end of given time.
* Your code should be functionally correct.
* Code should be modular and readable. Clean and professional level code.
* Your code should address separation of concern.
* Code should be extensible and scalable. Means it should be able to accommodate new requirements with minimal changes.
* Code should have good OOPs design.


