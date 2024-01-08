import pyfiglet

def display_name(name):
    ascii_banner = pyfiglet.figlet_format(name)
    print(ascii_banner)

display_name("Ahsan Tariq")