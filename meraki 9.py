# You have a dictionary called shopping

import json
list={"shopping_list":{ "chaco":"15","Biscuits":"50","Diarymilk":
    "30","icecream":"20",}}
item=input("enter the item:")
quantity=int(input("how much you want to buy:"))
a=list["shopping_list"][item]
r=int(a)-quantity
list["shopping_list"][item]=r
print(list)

# {
#     "shopping_list":{ 
#         "chaco":"15",
#         "Biscuits":"50",
#         "Diary_milk":"30",
#         "ice_cream":"20",
#          } 
# }
