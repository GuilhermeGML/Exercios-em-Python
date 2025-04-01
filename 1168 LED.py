n = int(input())
for j in range(n):
    # Leia os números como strings e elimine espaços extras
    var = input().strip()
    tot = 0
    for digit in var:
        # Verifique cada caractere como um dígito
        if digit == '1':
            tot += 2
        elif digit == '2':
            tot += 5
        elif digit == '3':
            tot += 5
        elif digit == '4':
            tot += 4
        elif digit == '5':
            tot += 5
        elif digit == '6':
            tot += 6
        elif digit == '7':
            tot += 3
        elif digit == '8':
            tot += 7
        elif digit == '9':
            tot += 6
        elif digit == '0':
            tot += 6
    print(f'{tot} leds')
