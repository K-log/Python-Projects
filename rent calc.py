

def calc_rent(total, power):
    rent = 1475
    utilities = total - rent
    ballance_amount = 150
    two_thirds_power = 2/3 * power

    Quinn = {
        "Rent": (rent / 2) - 150,
        "Utilities": utilities / 3,
        "Power": power / 3
        }

    Noah = {
        "Rent": (rent / 4) + 75,
        "Utilities": utilities / 3,
        "Power": power / 3
        }

    Ella = {
        "Rent": (rent / 4) + (75 - two_thirds_power)  ,
        "Utilities": utilities / 3,
        "Power": 0
        }


    people = {
        "Quinn": Quinn,
        "Noah": Noah,
        "Ella": Ella
        }
    
    print("Total Rent is $%0.2f" % rent)
    print("Total Utilities is $%0.2f" % utilities)
    print("Total Power is $%0.2f" % power)


    for i in people:
        print("\n---" + i)
        for j in people[i].keys():
            print(j + ": %0.2f" % people[i][j] )
            


def main():
    total = float(input("Please enter the total rent for this month\n"))
    power = float(input("Please enter the total power for this month\n"))

    calc_rent(total, power);


if __name__ == "__main__":
          main()
