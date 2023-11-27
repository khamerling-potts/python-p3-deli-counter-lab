def line(deli):
    result = "The line is currently:"
    if deli:
        for i in range(0, len(deli)):
            result += f" {i+1}. {deli[i]}"
        print(result)
    else:
        print("The line is currently empty.")


def take_a_number(line, name):
    line.append(name)
    print(f"Welcome, {name}. You are number {len(line)} in line.")


def now_serving(deli):
    if deli:
        print(f"Currently serving {deli.pop(0)}.")
    else:
        print("There is nobody waiting to be served!")


KATZ_DELI = []
OTHER_DELI = ["Logan", "Avi", "Spencer"]
ANOTHER_DELI = [
    "Amanda",
    "Annette",
    "Ruchi",
    "Jason",
    "Logan",
    "Spencer",
    "Avi",
    "Joe",
    "Rachel",
    "Lindsey",
]

print(line(KATZ_DELI))
