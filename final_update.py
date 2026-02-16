
import json
import sys

file_path = r'c:\Users\rados\Documents\GitHub\IGGPyCourse\Mod2.ipynb'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
except Exception as e:
    print(f"Error reading notebook: {e}", file=sys.stderr)
    sys.exit(1)

target_header = "## Sekwencje i kolekcje"
found = False

# The improved content
new_source = [
    "## Sekwencje i kolekcje\n",
    "\n",
    "W poprzedniej części wykładu poznaliście już pierwszy typ sekwencyjny – był nim pośrednio typ `str` (napisy). \n",
    "\n",
    "**Czym są sekwencje?**\n",
    "Sekwencje to uporządkowane kolekcje elementów. Ich głównym celem jest organizacja danych w określonej kolejności, co umożliwia szybki dostęp do konkretnych wartości poprzez indeksy. Wyróżnia je to, że zachowują kolejność wprowadzania danych, pozwalają na iterację (przechodzenie element po elemencie), wycinanie fragmentów (slicing) oraz sprawdzanie obecności elementu operatorem `in`.\n",
    "\n",
    "W tej części podsumujemy dostępne struktury:\n",
    "- `str` – niemodyfikowalne napisy; możemy indeksować, robić wycinki, formatować.\n",
    "- `list` – dynamiczne, mutowalne listy.\n",
    "- `tuple` – niemutowalne krotki.\n",
    "- `range` – generator liczb całkowitych używany do pętli.\n",
    "\n",
    "Dodatkowo omówiliśmy kolekcje nieuporządkowane:\n",
    "- `dict` – pary klucz-wartość, gdy potrzebujesz nazwanego dostępu.\n",
    "- `set` – zbiór unikalnych elementów przydatny do deduplikacji i operacji zbiorowych.\n",
    "\n",
    "Na kolejnych sekcjach zobaczysz szczegóły dotyczące list, krotek i zakresów (oraz ich operacji). Pamiętaj, że wszystkie sekwencje wspierają indeksowanie, iteracje, operator `in`, funkcje `len`, `min`, `max` i slicing. Przy `range` niektóre operacje wymagają zrzutowania do listy, aby zobaczyć wynik.\n"
]

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = cell.get('source', [])
        if any(target_header in line for line in source):
            print(f"Updating cell with header: {target_header}")
            cell['source'] = new_source
            found = True
            break

if found:
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print("Notebook updated successfully.")
    except Exception as e:
        print(f"Error writing notebook: {e}", file=sys.stderr)
        sys.exit(1)
else:
    print(f"Header '{target_header}' not found.", file=sys.stderr)
    sys.exit(1)
