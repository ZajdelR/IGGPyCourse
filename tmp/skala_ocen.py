oceny_upwr = {2.0: "niedostateczny", 3.0: "dostateczny",
             3.5: "dostateczny plus", 4.0: "dobry",
             4.5: "dobry plus", 5.0: "bardzo dobry"}

for ocena in sorted(oceny_uwr, reverse=True):
    print(ocena, oceny_upwr[ocena])
    