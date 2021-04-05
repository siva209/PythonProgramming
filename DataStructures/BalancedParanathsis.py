def are_bracket_balance(expression):
    """
    function : to check if brackets are balanced,
    if condition : Push the element in the stack
    else condition : IF current character is not opening bracket,
                        then it must be closing.So stack cannot be empty at this point.
    :param expression: expression is input from the user
    :return: True or False
    """
    try:
        stack = []

        # Traversing the Expression
        for character in expression:
            if character in ["(", "{", "["]:

                stack.append(character)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(':
                    if character != ")":
                        return False
                if current_char == '{':
                    if character != "}":
                        return False
                if current_char == '[':
                    if character != "]":
                        return False

        # Check Empty Stack
        if stack:
            return False
        return True
    except ValueError as ve:
        print("Value Error", ve)
    except KeyError as ke:
        print("Key Error", ke)
    except Exception as excp:
        print("Errror occurred : ", excp)


if __name__ == "__main__":
    # expr = "{()}[]"
    expr = input("Please enter parentheses : ")
    # Function call
    try:
        if are_bracket_balance(expr):
            print("Balanced")
        else:
            print("Not Balanced")
    except Exception as exception:
        print("Error occurred ", exception)