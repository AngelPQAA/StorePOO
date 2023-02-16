def validate_number(message):
    print(message)

    while True:

        try:
            option = int(input())
            return option
        except ValueError:
            print('\n Ingrese una opción válida.'.upper() + '\n')
            continue
