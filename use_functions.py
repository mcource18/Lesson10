"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""


class Buyer:
    __account = 0
    __list_shop = {}

    def add(self, sum):
        self.__account += sum

    def buy(self, sum):
        if sum > self.__account:
            print("Денег не хватает")
            return

        product = input("Введите название покупки ")
        if product in self.__list_shop:
            self.__list_shop[product] += sum
        else:
            self.__list_shop[product] = sum
        self.__account -= sum

    def history(self):
        for key, val in self.__list_shop.items():
            print(f'{key} - {val}')


buyer=Buyer()
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        sum=input("Введит сумму для пополнения счета ")
        buyer.add(int(sum))
    elif choice == '2':
        sum = input("Введит сумму для покупки ")
        buyer.buy(int(sum))
    elif choice == '3':
        buyer.history()
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')