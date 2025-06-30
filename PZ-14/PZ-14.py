import re
"""Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
– все остальные. Посчитать количество полученных строк в каждом файле."""

def process_ip_masks(input_file, output_zero, output_non_zero):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    all_ips = ip_pattern.findall(content)

    zero_octet = [ip for ip in all_ips if ip.endswith('.0')]
    non_zero_octet = [ip for ip in all_ips if not ip.endswith('.0')]

    with open(output_zero, 'w', encoding='utf-8') as file:
        file.write('\n'.join(zero_octet))

    with open(output_non_zero, 'w', encoding='utf-8') as file:
        file.write('\n'.join(non_zero_octet))

    return len(zero_octet), len(non_zero_octet)

if __name__ == '__main__':
    input_file = 'ip_address.txt'
    output_zero = 'zero_octet.txt'
    output_non_zero = 'non_zero_octet.txt'

    zero_count, non_zero_count = process_ip_masks(input_file, output_zero, output_non_zero)

    print(f'Количество масок с нулевым четвертым октетом: {zero_count}')
    print(f'Количество масок с ненулевым четвертым октетом: {non_zero_count}')

