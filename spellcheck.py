from spylls.hunspell import Dictionary
import re
from pathlib import Path
from lxml import etree
import sys

dictionary = Dictionary.from_files('en_CA-large')
dictionary2 = Dictionary.from_files('en_GB-large')

total_corrections = 0

content_dir = Path("content/")

whitelisted_words = [
    "const",
    "struct",
    "enum",
    "preprocessor",
    "facto",
    "br",
    "async",
    "backend",
    "dereferencing",
    "foreach",
    "bitwise",
    "php",
    "nullable"
]

for file in content_dir.iterdir():
    tree = etree.parse(file)
    root = tree.getroot()

    for elem in root.iter():
        if elem.getparent() == None or elem.getparent().tag != "rightbox":
            if elem.tag == "p":
                allwords = re.findall(r'\b\w+\b', elem.text.strip())
                for word in allwords:
                    if total_corrections == 5:
                        exit(0)
                    if dictionary.lookup(word) == False:
                        if word[0].isupper():
                            # Probably proper name or something
                            continue
                        if word[0].isnumeric():
                            continue
                        if word in whitelisted_words:
                            continue
                        if dictionary2.lookup(word) == True:
                            continue
                        print("Misspelled word in " + str(file) + ":")
                        print(word)
                        if len(list(dictionary.suggest(word))) > 0:
                            print("Correction", list(dictionary.suggest(word))[0])
                        print()
                        total_corrections += 1

if total_corrections > 0:
    sys.exit(1) # fail the github action