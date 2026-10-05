rice_price, milk_price, fruit_price, number_of_baskets, family_members, = 12 , 4 , 8 , 2 , 4

basket_cost_per_person = (rice_price + milk_price + fruit_price* number_of_baskets)/family_members
print ("Basket cost per person =",int(basket_cost_per_person))

ppl = int(input("Enter total number people : "))
ttl_items = int(input("Enter total items : "))

if ppl==0:
    print ("You cannot share between 0 people")

else:
    if ttl_items%ppl==0:
        print ("They divide equally!")
        print ("Each person gets : ", ttl_items//ppl)
    else:
        print ("They do not divide equally.")
        print ("The remainder is =",ttl_items%ppl)


recorded_avg = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

total_cost_month = recorded_avg * total_weeks
corrected_total = total_cost_month - wrong_week_cost + correct_week_cost
corrected_average = corrected_total / total_weeks

print("Recorded total =", total_cost_month)
print("Corrected total =", corrected_total)
print("Corrected average =", corrected_average)


print("Basket cost per person =", basket_cost_per_person)


print("Corrected average =", corrected_average)