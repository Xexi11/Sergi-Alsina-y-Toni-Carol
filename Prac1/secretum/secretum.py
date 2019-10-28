#!/bin/python3

"""Methods to decrypt the secretum."""

import sys


# def decrypt(value):
#     suma = 0
#
#     for i in range(len(value)):
#         suma = suma + int(value[i])
#
#     final = suma
#
#     while final > 10:
#         suma=0
#         for i in str(final):
#             suma = suma + int(i)
#             final = suma
#
#     return final


def decrypt(value,final,i):


    if(int(value)< 10):

        return int(value)
    else:
        if (i == len(value)):
            i = 0
            value=str(final)
            final= 0
        final = final + int(value[i])
        i +=1
    return decrypt(value,final,i)








def main():
    """Main function to parse input/output
    and decrypt the secretum."""
    digits = str(sys.argv[1])
    last = int(sys.argv[2])
    result = decrypt(0)
    print('La clau per utilitzar el descodificador és {0}'.format(result))


if __name__ == '__main__':
    main()
