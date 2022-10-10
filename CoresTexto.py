# Podemos utilizar dicionário:
class printer():
    _colors_ = {
        **dict.fromkeys(("RED", "ERROR", "NO"), "\033[1;31m"),
        **dict.fromkeys(("GREEN", "OK", "YES"), "\033[0;32m"),
        **dict.fromkeys(("YELLOW", "WARN", "MAYBE"), "\033[0;93m"),
        "BLUE": "\033[1;34m",
        "CYAN": "\033[1;36m",
        "RESET": "\033[0;0m",
        "BOLD": "\033[;1m",
        "REVERSE": "\033[;7m"
    }
    #O próximo passo é criar uma função que recebe o nome da cor e retorna o código ANSI correspondente:

    def _get_color_(self, key):
        """Gets the corresponding color ANSI code... """
        try:
            return self._colors_[key]
        except:
            return self._colors_["RESET"]

    #Agora é só criar a função que faz o print da mensagem:

    def print(self, msg , color="RESET"):
        """Main print function..."""

        # Get ANSI color code.
        color = self._get_color_(key=color)

        # Printing...
        print("{}{}{}".format(color, msg, self._colors_["RESET"]))

    #Para utilizar é simples:
p = printer()

p.print(msg="\n\nSUCCESS Test...", color="GREEN")
p.print(msg="WARN Test...", color="YELLOW")
p.print(msg="ERRPR Test...\n\n", color="RED")




#Podemos utilizar caracteres ANSI:

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
    # Agora um exemplo de como aplicar essas cores:

print(BOLD + RED + "ERROR!" + RESET + "Something went wrong...")
print(RED + "ERROR!" + RESET + "Something went wrong...\n\n")




# Podemos usar TermColor, um pacote mais flexível:
from termcolor import colored

print(colored('Error Test!!!', 'red'))
print(colored('Warning Test!!!', 'yellow'))
print(colored('Success Test!!!\n\n', 'green'))




# Podemos usar Sty, tendo mais possibilidades:
from sty import fg, bg, ef, rs

print(fg.red + 'ERROR Test!' + fg.rs)
print(fg.li_yellow + 'WARNING Test!' + fg.rs)
print(fg.green + 'SUCCESS Test!\n\n' + fg.rs)