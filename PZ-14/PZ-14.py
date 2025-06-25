"""Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
– все остальные. Посчитать количество полученных строк в каждом файле."""



with open('ip_address.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

zero_octet = []
other_octet = []

in_target_section = False

for line in lines:
    line = line.strip()

    if "Частоупотребимые маски" in line:
        in_target_section = True
        continue

    if in_target_section:
        if line.startswith("Количество адресов подсети"):
            break

        if line.count('.') == 3 and len(line.split('.')) == 4:
            octets = line.split('.')
            if octets[-1] == '0':
                zero_octet.append(line)
            else:
                other_octet.append(line)

with open('zero_octet.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(zero_octet))

with open('other_octet.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(other_octet))

print(f"Найдено масок с 0: {len(zero_octet)}")
print(f"\nНайдено остальных масок: {len(other_octet)}")