
def houseRob(givenHouse:list) -> str:
    robHouse1:int = 0
    robHouse2:int = 0
    houseRobbed:list = []
    for num in givenHouse:
        currentSum:int = max(robHouse1 + num, robHouse2)
        #houseRobbed.append(max(robHouse1 + num, robHouse2))
        robHouse1 = robHouse2
        robHouse2 = currentSum
    
    #print(houseRobbed)
    return f"The max profit is {robHouse2}."
def main():
    givenHouse:list = [1,9,5,7,13,6]
    print(houseRob(givenHouse))

if __name__ == "__main__":
    main()