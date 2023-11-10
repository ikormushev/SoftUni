import re

barcode_pattern = r"\@\#+[A-Z][a-zA-Z0-9]{4,}[A-Z]\@#+"
barcodes_num = int(input())

for _ in range(barcodes_num):
    barcode = input()

    if re.search(barcode_pattern, barcode):
        found_digits = re.findall(r"\d", barcode)
        if found_digits:
            concatenated_digits = "".join(found_digits)
        else:
            concatenated_digits = "00"
        print(f"Product group: {concatenated_digits}")
    else:
        print("Invalid barcode")