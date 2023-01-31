"""С рыбками хорошо работать — они ведут себя тихо и не кусаются. Главное — работникам не заболеть!

Перенесите в подсписок vaccinated только сотрудников, которые прошли вакцинацию,
а остальных отправьте в not_vaccinated. Затем распечатайте оба списка в таком формате:

Вакцинированные:
Киселёв Всеволод Эдуардович
...
Остальные:
Довлатова Эмилия Ефимовна"""

employees = [

 {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
 {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
 {"fio": "Аверин Мартын Егорович", "vaccinated": True},
 {"fio": "Князева Августа Егоровна", "vaccinated": False},
 {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
 {"fio": "Куприна Марина Викторовна", "vaccinated": False},
 {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for item in employees:
    if item['vaccinated'] == True:
        vaccinated.append(item['fio'])
    else:
        not_vaccinated.append(item['fio'])
print("Вакцинированные:")
for item in vaccinated:
    print(item)

print("Остальные:")
for item in not_vaccinated:
    print(item)