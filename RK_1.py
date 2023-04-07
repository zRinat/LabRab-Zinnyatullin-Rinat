# используется для сортировки

from operator import itemgetter

class SchoolCh:

    """Школьник"""

    def __init__(self, fam, mid_aver, group_id):

        self.fam = fam

        self.aver = mid_aver

        self.group = group_id

class Grade:

    """Класс"""

    def __init__(self, id, Group_Name):

        self.group = Group_Name

        self.id = id

# Классы

grad = [

    Grade(1, '5А'),

    Grade(2, '5Б'),

    Grade(3, '6')

]

# Сотрудники

schs = [

    SchoolCh('Васечкин', 4.3, 1),

    SchoolCh('Петров', 4.37, 1),

    SchoolCh('Пупкин', 4.9, 2),

    SchoolCh('Иванов', 3.9, 3),

    SchoolCh('Губкин', 4.1, 3)

]

def main():

    """Основная функция"""

    # Соединение данных один-ко-многим 

    one_to_many = [(s.fam , s.aver, g.group) 
        
        for g in grad 
        
        for s in schs
        
        if g.id == s.group]
    
    print('one_to_many: ',one_to_many)
    print('Задание 1')

    res_11 = sorted(one_to_many, key=itemgetter(2))

    print(res_11)

    print('\nЗадание 2')

    res_12_unsorted = []

    # Перебираем все отделы

    for g in grad:

        # Список сотрудников отдела

        g_emp = list(filter(lambda i: i[2] == g.group, one_to_many))

        # Если отдел не пустой       
         
        if len(g_emp) > 0:

            # Зарплаты сотрудников отдела

            g_aver = [aver for _,aver,_ in g_emp]

            # Суммарная зарплата сотрудников отдела

            g_aver_sum = sum(g_aver)/len(g_aver)

            res_12_unsorted.append((g.group, g_aver_sum))

    # Сортировка по суммарной зарплате

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

if __name__ == '__main__':
    main()