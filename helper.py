def header(tekst="header"):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def prijs(input):
    output = f"€ {input},00"
    return output