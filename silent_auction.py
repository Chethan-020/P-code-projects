def find_winner(bidder_details):
    for bidder in bidder_details:
        highest_price=0
        Winner=""
        bidder_price=bidder_details[bidder]
        if bidder_price>highest_price:
            highest_price=bidder_price
            Winner=bidder
    print(bidder_details)
    print(f"The winner is{Winner} with bid price of{highest_price}.")
bidder_data={}
End_bidding=False
while not End_bidding:
    name=input("What is your name?:")
    price=int(input("Enter the price:"))
    bidder_data[name]=price
    more_bidder=input("If more bidder is there type'YES' if not type'NO':").lower()
    if more_bidder=="no":
        End_bidding=True
        find_winner(bidder_data)
    

       