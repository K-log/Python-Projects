

def calc_rent(total, power):
    rent = 1475
    utilities = total - rent
    ballance_amount = 150
    two_thirds_power = 2/3 * power
    total = rent + utilities + power


    # Nathan
    r_na = (rent / 2) - ballance_amount
    u_na = utilities / 3
    p_na = power / 3

    Nathan = {
        "Rent": r_na,
        "Utilities": u_na,
        "Power": p_na,
        "Total": r_na + u_na + p_na
        }

    
    # Noah
    r_no = (rent / 4) + (ballance_amount / 2)
    u_no = utilities / 3
    p_no = power / 3
    
    Noah = {
        "Rent": r_no,
        "Utilities": u_no,
        "Power": p_no,
        "Total": r_no + u_no + p_no
        }

    # Ella
    r_el = (rent / 4) - two_thirds_power + (ballance_amount / 2)  
    u_el = utilities / 3
    p_el = 0

    Ella = {
        "Rent": r_el,
        "Utilities": u_el,
        "Power": p_el,
        "Total": r_el + u_el + p_el
        }


    people = {
        "Nathan": Nathan,
        "Noah": Noah,
        "Ella": Ella
        }
    
    print("Total Rent is $%0.2f" % rent)
    print("Total Utilities is $%0.2f" % utilities)
    print("Total Power is $%0.2f" % power)
    print("Total for Rent + Utilites + power is $%0.2f" % total)


    for i in people:
        print("\n---" + i)
        for j in people[i].keys():
            print(j + ": %0.2f" % people[i][j] )
            


def main():
    total = float(input("Please enter the total rent + utilites for this month\n"))
    power = float(input("Please enter the total power for this month\n"))

    calc_rent(total, power);


if __name__ == "__main__":
          main()
