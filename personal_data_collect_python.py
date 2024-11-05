# Personal Data Collect System in Python


print("1. Add new person")
print("2. Search for a person")
selection = input("Please select an option")


if selection == '1':

    print('Add new person - Enter the information for the new preson:\t')
    first_name = input('First name:\t')
    last_name = input('Last name:\t')
    age = input('Age:\t')
    adress_street = input('Street:\t')
    adress_number = input('Number:\t')
    birth_date = input('Birth date:\t')


    new_person = {}
    new_person['First name'] = first_name
    new_person['Last name'] = last_namer
    new_person['Age'] = age
    new_person['Street'] = adress_street
    new_person['Number'] = adress_number
    new_person['Birth Date'] = birth_date
