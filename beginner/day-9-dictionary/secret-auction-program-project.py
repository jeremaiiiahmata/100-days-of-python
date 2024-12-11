continueBid = True

def findHighestBidder():
    maxBid = 0

    for bidder in biddingDictionary:

        if biddingDictionary[bidder] > maxBid:
            winner = bidder
            maxBid = biddingDictionary[bidder]

    print("\n\n")
    print(f"The winner of the bid is {winner} with a bid of ${maxBid}")

biddingDictionary = {}

while continueBid :

    print("Welcome To The Secret Auction")

    name = input("What is your name : ")
    bidAmount = int(input("How much is your bid : $"))
    biddingDictionary[name] = bidAmount
    nextBidder = input("Are there next bidders? Yes or No : ").lower()

    if nextBidder == "no" :
        findHighestBidder()
        continueBid = False
    if nextBidder == "yes":
        print("\n" * 20)

