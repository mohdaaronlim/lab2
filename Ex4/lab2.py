def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    get_user_input()
def get_user_input():
    userinput = input().split(",")
    userinput = [float(item) for item in userinput]
    print(userinput)
    calc_average(userinput)
    find_min_max(userinput)
def calc_average(data):
    total = sum(data)
    avg = total / len(data)
    print("The avg is: " + str(avg))
def find_min_max(data):
    datamax = max(data)
    datamin = min(data)
    print("Min temp is: " + str(datamin) + "Max temp is: " + str(datamax))
def sort_temperature():
    print("List of Floats sorted in ascending order")
def calc_median_temperature():
    print("Float")

display_main_menu()