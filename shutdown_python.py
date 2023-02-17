import os

while True:
    print('='*41)
    print('Suspenser = 1', 'Reiniciar = 2', 'Desligar = 3')
    print('='*41)
    choice = int(input('\nO que deseja fazer?'))

    if choice == 1:
        suspend = input('Suspender? [Y/N]').upper()
        
        if suspend in 'Yy':
            time_suspend = int(input('Em quantos segundos? '))
            os.system(f"shutdown /h /t {time_suspend}")

    elif choice == 2:
        restart = input('Reiniciar? [Y/N]').upper()
        
        if restart in 'Yy':
            time_restart = int(input('Em quantos segundos? '))
            os.system(f"shutdown /r /t {time_restart}")

    elif choice == 3:
        shutdown = input('Desligar?[Y/N]').upper()

        if shutdown in 'Yy':
            time_shutdown = int(input('Em quantos segundos?'))
            os.system(f"shutdown /s /t {time_shutdown} ")

    else:
        print('\nDesculpe, esta não é uma opção válida.\n')
