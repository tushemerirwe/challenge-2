from datetime import date
def age():
    current_year=date.today().year
    dob=int (input("inpu1t year of birth:"))
    age = current_year-dob
    if age< 18:
        print (" minor")
    elif age>=18 and age<=36:
        print("youth")
    else:
        print("elder")


age()




