while True:
    input_expression = input("Enter: ")
    if input_expression.isdigit() or input_expression.isinstance():
        continue  
    
    input_expression = list(input_expression)  
    #for cleaning backspaces 
    while " " in input_expression:
        index_of_a = input_expression.index(" ")
        input_expression.pop(index_of_a)    
    #finding index of expression's sign
    try:
        if "+" in input_expression:
            sign_index = input_expression.index("+")
        elif "-" in input_expression:
            sign_index = input_expression.index("-")    
        elif "/" in input_expression:
            sign_index = input_expression.index("/")
        elif "*" in input_expression:
            sign_index = input_expression.index("*")
        elif "%" in input_expression:
            sign_index = input_expression.index("%")
    except:
        ValueError
    try:    
        first_expression = input_expression[:sign_index]
        first_expression = "".join(first_expression)
        first_expression = float(first_expression)

        second_expression = input_expression[sign_index+1:]
        second_expression = "".join(second_expression)
        second_expression = float(second_expression)
    except:
        ValueError
        print('Enter expression correctly')
    #Adding numbers to each other
    sign_of_expression = input_expression[sign_index]
    try:

        if sign_of_expression == "+":
            print(first_expression + second_expression)
        elif sign_of_expression == "-":
            print(first_expression - second_expression)
        elif sign_of_expression == "*":
            print(first_expression * second_expression)
        elif sign_of_expression == "/":
            print(first_expression / second_expression)
        elif sign_of_expression == "%":
            print(first_expression * second_expression / 100)
    except:
        TypeError
#new changes
