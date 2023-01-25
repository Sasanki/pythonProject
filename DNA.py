import Levenshtein

def closest_string(target_string, string_list):
    closest = ""
    closest_distance = float("inf")
    for stringg in string_list:
        distance = Levenshtein.distance(target_string, stringg)
        if distance < closest_distance:
            closest_distance = distance
            closest = stringg
    return closest


if __name__ == "__main__":
    target_string = input("Podaj lancuch domyslny: ")
    string_list = input("Podaj lancuchy ktore chcesz porownac oddzielajac je spacja: ").split(' ')
    print("Closest string: ", closest_string(target_string, string_list))

