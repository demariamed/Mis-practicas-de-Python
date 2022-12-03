# Solicitud de contraseña

password = input ("Ingrese una contraseña: ")

for i in password :
    if i.isnumeric ():
        confirm = input ('Ingrese la contraseña nuevamente: ')
        if password == confirm :
            print ('Contraseña Correcta. Fin del programa.')
            exit ()
        else :
            print ('Las contraseñas no coinciden.')
            confirm = input ('Ingrese la contraseña nuevamente: ')
            if password == confirm :
                print ('Contraseña Correcta.')
                exit ()
            else :
                print ('Las contraseñas no coinciden. Fin del programa.')
                exit ()
                

    else :
        print ('La contraseña debe comenzar con un número.') # Segunda Alternativa
        

        password = input ('Ingresa una contraseña: ')
        for i in password :
            if i.isnumeric ():
                confirm = input ('Ingrese la contraseña nuevamente: ')
                if password == confirm :
                    print ('Contraseña Correcta.')
                    exit ()
                else :
                    print ('Las contraseñas no coinciden.')
                    confirm = input ('Ingrese la contraseña nuevamente: ')
                    if password == confirm :
                        print ('Contraseña Correcta.')
                        exit ()
                    else :
                        print ('Las contraseñas no coinciden. Fin del programa.')
                        exit ()
                        
                            
            # else :
            #     print ('La contraseña debe iniciar con un número. Por favor, ingrese de nuevo su contraseña.') # Alternativa de prueba
            #     print ('Le resta un intento.')
            #     password = ('Ingrese su contraseña: ')
            #     if i.isnumeric ():
            #         confirm = input ('Vuelva a ingresar su contraseña: ')
            #         if password == confirm :
            #             print ('Contraseña Correcta.')
            #             exit ()
            #         else :
            #             print ('La contraseña no coincide. Le restan 2 intentos.')
            #             confirm = input ('Vuelva a ingresar su contraseña: ')
            #             if password == confirm :
            #                 print ('Contraseña Correcta.')
            #                 exit ()
            #             else :
            #                 print ('La contraseña nuevamente no coincide. Le resta 1 intento.')
            #                 confirm = input ('Vuelva a ingresar su contraseña: ')
            #                 if password == confirm :
            #                     print ('Contraseña Correcta.')
            #                     exit ()
            #                 else :
            #                     print ('Las contraseñas no coinciden. No le restan intentos.')
            #                     exit ()