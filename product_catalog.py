from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print (products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
 
for product in products:
    converted_products.append ({'name': product['name'], 'tags': set(product['tags'])})




#print (customer_tags)
#print (converted_products)

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        matches = count_matches(product['tags'],customer_tags)
        if matches > 0:
            recommendations.append({'name': product['name'], 'matches': matches})
    return recommendations



# TODO: Step 7 - Call your function and print the results

recommended = recommend_products(converted_products, customer_tags)
print('Recommended Products:')
for product in recommended:
    print(f'- {product['name']} ({product['matches']} match(es))')



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?

# I used set intersections and loops at the main operations. Set intersections allow the program to 
# quickly check which tags are the same between the customer's preferences and each product. This is 
# better than comparing one tag at a time because it is faster and easier to read. Loops are important 
# because we need to go through the whole list of products and calculate how many matches each product 
# has with the customer's preferences. Without the loops, the program would only be able to check one 
# product at a time. These two operations work well together to make the program simple and effective.

# 2. How might this code change if you had 1000+ products?

# If the product catalog had more than 1,000 products, the program would still work, but it might run 
# more slowly. One way to improve it would be to make sure that all product tags are stored as sets 
# from the very beginning, so the program does not have to change them later. Another change would be 
# to limit the number of results shown to the customer, sorting them and only showing the top 10 
# products that match the most. If the catalog grew even larger, the products could also be stored in 
# a database, which would help manage and search through big lists of information more efficiently. 
# These changes would make the program easier to use when working with a much larger product list.
