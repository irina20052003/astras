def get_gregorian_gate(num):
    num = "24" + str(num).strip() #добавляем к строке 24 и strip обрезаем пробелы с начала и конца
    num = float(num) #преобразуем строку в число
#промежуточные коэф
    a = int(num) + 32044
    b = int((4 * a + 3) / 146097)
    c = a - int((146097 * b) / 4)
    d = int((4 * c + 3) / 1461)
    e = c - int((1461 * d) / 4)
    m = int((5 * e + 2) / 153)
#вычисление выходных данных
    day = e - int((153 * m + 2) / 5) + 1
    month = m + 3 - 12 * int(m / 10)
    year = 100 * b + d - 4800 + int(m / 10)
    hours = int(24 * (num % 1))
    minutes = int(1440 * ((num % 1) - (hours / 24)))
    seconds = int(86400 * ((num % 1) - (hours / 24) - (minutes / 1440)))
    #возвращение значений
    return str(day) + "." + str(month) + "." + str(year) + " " + str(hours) + ":" + str(minutes) + ":" + str(seconds)


def main():
    file = open("task2_data.dat", "r") #открываем файл с входными данными в режиме чтения

    arr = [] #создаем пустой массив в котором будут храниться строчки с данными (один элемент - строка)

    for line in file:
        arr.append(line) #построчно считываем документ и строки кладем в массив

    file.close()

    arr.sort()#сортируем массив

    unique_names = [] #пустой массив для хранения названий звезд

    for i in range(1, len(arr)): #пробегаемся по всему массиву со второго элемента, первый - заголовок
        if arr[i].split("    ")[0] not in unique_names: #если название звезды (0 элемент) не в массиве, мы его туда добавляем
            unique_names.append(arr[i].split("    ")[0])#добавление

    filters = [[] for _ in range(len(unique_names))]#создаем массив для хранения фильтров 0 - фильтр для звезды

    for i in range(1, len(arr)): #заполняем массив названиями фильтров
        ind = unique_names.index(arr[i].split("    ")[0])
        if arr[i].split("    ")[2] not in filters[ind]:
            filters[ind].append(arr[i].split("    ")[2])

    #имеем массив юник неймс с именами звезд и массив фильтрс  где i-ый подмассив это список фильтров для итой звезды в списке юник неймс

    for i in range(len(unique_names)): #вывод данных считанных с объекта на экран
        print("Object: " + unique_names[i] + ". Filters: ", end="")
        for j in range(len(filters[i])):
            print(filters[i][j], end=" ")
        print()
#считывает данные пользователя
    print("Enter Object name: ", end="")
    object_name = input()
    if object_name not in unique_names:
        print("Object does not exist!")
        return
    print("Enter Object filters separated by a space: ", end="")
    object_filters = input().split(" ")
    object_filters.sort()
    #формируем шапку документа
    file = open(str(object_name) + ".dat", "w")
    file.write("Date                    HJD 24...   ")
    for i in range(len(object_filters)):
        file.write("Magnitude" + str(object_filters[i]) + "    ")
    file.write("\n")

    for i in range(1, len(arr)):
        # если название звезды относится к запрашиваемой пользователем то продолжаем работу если нет то перееходим на некст элемент
        if arr[i].split("    ")[0] == object_name:
            temp = arr[i].split("    ") #берем строчку массива и кладем в отдельную переменную разделяя по пробелам то бишь строчку массива превращаем в массив строчек
            temp[2] = temp[2].strip()
            for j in range(len(object_filters)): #проходим по всем фильтрам введенным пользователем
                if temp[2].find(object_filters[j]) != -1: #если во временной переменной есть фильтр то начинаем запись файла иначе ничего не делаем
                    file.write(get_gregorian_gate(temp[1]) + "    " + temp[1] + "     ") #пишем григорианскую и юлианскую дату наблюдения
                    if 'B' in object_filters:#если ввел фильтр б
                        if temp[2] == "B":#если в данной строке фильтр б то
                            file.write(temp[3][:-1] + "     ")#записываем в файл данные по этому фильтру
                        else:#иначе решетки
                            file.write("######      ")
                    if "Ic" in object_filters:
                        if temp[2] == "Ic":
                            file.write(temp[3][:-1] + "     ")
                        else:
                            file.write("######      ")
                    if "V" in object_filters:
                        if temp[2] == "V":
                            file.write(temp[3][:-1] + "     ")
                        else:
                            file.write("######      ")
                    file.write("\n")#перенос строки

    file.close()


if __name__ == "__main__":
    main()
