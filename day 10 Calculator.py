#CALCULATOR 
def calculator():
    logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
    print(logo)
    def add(n1, n2):
        return(n1 + n2)
    def subtract(n1, n2):
        return(n1 - n2)
    def multiply(n1, n2):
        return(n1 * n2)
    def divide(n1, n2):
        return(n1 / n2)
        
    operations = {"+" : add, "-": subtract, "/" : divide, "*" : multiply}
    num1 = float(input("enter the first number:  "))
    for operation in operations:
        print(operation)
    not_end = True
    while not_end:
        num2 = float(input("enter the second number:  "))
        symbol = input("enter the symbol you want to perform:  ")
        calculation_function = operations[symbol]
        first_answer = calculation_function(num1, num2)
        print(f'{num1} {symbol} {num2} = {first_answer}')
        new = input("enter y for continuing or n to stop:  ").lower()
        if new == 'y':
            num1 = first_answer
            new_calc = calculation_function(first_answer, num2)
            
        elif new == 'n':
            print(f"Thank you for using our calculator this was your answer {first_answer}")
            not_end = False
            calculator()
calculator()
            