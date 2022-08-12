# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?

initial_price = 24.95
discount = .60
shipping_cost = 3 # .75 after each additional copy 
number_of_books = 60


book_printing_price = (initial_price * discount) * 60
shipping_total = (shipping_cost * 1) + .75 * (number_of_books - 1)

print(book_printing_price + shipping_total) # 945.44 