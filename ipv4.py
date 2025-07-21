import csv

def convert_geoip_data(input_file, output_file):
    """
    Открывает файл GeoIP-legacy.csv, преобразует строки и сохраняет результат в geo-country.conf.

    Args:
        input_file (str): Путь к входному файлу GeoIP-legacy.csv.
        output_file (str): Путь к выходному файлу geo-country.conf.
    """

    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:

            reader = csv.reader(infile)
            for row in reader:
                if len (row[1])<16:    # Отсекаем IPv6 адреса
                    if len(row) == 6:  # Проверяем, что строка имеет правильную длину
                        ip_start = row[0]
                        ip_end = row[1]
                        cidr_prefix1 = row[2]
                        cidr_prefix2 = row[3]
                        country_code = row[4]
                        country_name = row[5]

                        # Форматируем строку в нужном формате
                        formatted_line = f"{ip_start}-{ip_end} {country_code};"
                        outfile.write(formatted_line + "\n")


    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример использования:
input_file = "GeoIP-legacy.csv"
output_file = "geo-country.conf"
convert_geoip_data(input_file, output_file)
print(f"Файл {output_file} успешно создан.")
