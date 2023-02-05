import math
ang = float(input('Digite um valor:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O angulo {} tem seno valendo {:.2f}'.format(ang, sen))
print('O angulo {} tem cosseno valendo {:.2f}'.format(ang, cos))
print('O angulo {} tem tangente valendo {:.2f}'.format(ang, tg))
