def coca_cola_machine():
  accepted_coins = [25, 10, 5]
  total_due = 50
  inserted_amount = 0 

  while inserted_amount < total_due:
    print("Amount due: {} cents".format(total_due - inserted_amount))
    
    coin = int(input("Insert coin: "))
   
    if coin in accepted_coins:
      inserted_amount += coin
    else:
      print("Invalid coin")

  

    
  change = inserted_amount - total_due
  print(f"Change owed: {change} cents")

coca_cola_machine()
