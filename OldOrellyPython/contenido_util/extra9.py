import argparse
#EL STORE_FALSE ME VA A TIRAR EL MENSAJE SIN DIGITAR NADA ENCAMBIO EL STORE_TRUE SI TENDREMOS QUE DIGITAR

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")

args = parser.parse_args()

if args.version:
    print('This is myProgram version 1.0.1')