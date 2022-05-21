from rich.console import Console
from time import *
from rich.progress import track
from time import sleep
from rich import *
from rich.progress import Progress
from tkinter import *
from tkinter.ttk import Combobox
import keyboard 
 

def process_data():
    sleep(0.06)
 


def progress(d):
    for _ in track(range(100), description=d):
        process_data()


console = Console()
 
 
def merge_dict(dict_one, dict_two):
    merged_dict = dict_one | dict_two
    console.log(merged_dict, log_locals=True)
 
clicks = 0

def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
    if clicks >= 25:
        root.destroy()

 
 
class Hero():
    def __init__(self, name, health, impact_force, armor, weapon):
        self.name = name
        self.health = health
        self.impact_force = impact_force
        self.armor = armor
        self.weapon = weapon
 
    def print_info(self):
        print('Вот наш герой -', self.name)
        sleep(0)
        print('Здоровье:', self.health)
        sleep(0)
        print('Сила удара:', self.impact_force)
        sleep(0)
        print('Броня:', self.armor)
        sleep(0)
        print('Оружие:', self.weapon)
        sleep(0)
 
    def strike(self, target):
        self.health -= (self.impact_force // 2)
        target.health -= self.impact_force
        print('Удар!')
        print(self.health)
        print(target.health)
 
 
 
    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'Умер(-ла)\n')
                break
            sleep(3)
            enemy.strike(self)
            if self.health <= 0:
                print(enemy.name, 'Умер(-ла)\n')
                break
            sleep(3)


def choise():
    print('Нажми Y если да или нажми N если нет.')  
    while True:
        if keyboard.is_pressed("y"):
            return True
        elif keyboard.is_pressed("n"):
            return False
        elif keyboard.is_pressed("q"):
            print(inventory)
            return True
 
 


 
inventory = []
print("Приветствую вас в новой MMO RPG в консоли!")
print("Вы готовы?")
otvet123 = choise()
if otvet123 == True:
    name = input("Введите ваше имя:\n")
    ghoul = Hero(name, 15, 3, 3, 'меч')
    ccg = Hero('Вор', 20, 5, 5, 'Лук')
    print("Чтобы открыть инвентарь нажми q")
    print("При открытии инвентаря сразу будет ответ да")
    print("Начинаем!")
    for _ in track(range(100), description='[black]Идёт ночь'):
        process_data()
    print("[yellow]День[yellow]")
    ghoul.print_info()
    for _ in track(range(100), description='[black]Внезапная атака!'):
        process_data()
    print("Вы хотите сбежать с боя?")
    otvet = choise()
    if otvet == True:
        for _ in track(range(100), description='[blue]Побег!'):
            process_data()
        print("Вы сбежали!")
        print("Вы видете толпу. ")
        print("Подойти к толпе?")
        otvet1 = choise()
        if otvet1 == True:
            for _ in track(range(100), description='[black]Вы подходите к толпе...'):
                process_data()
            print("На вас напала толпа, и обвинила вас в воровстве")
            print("Вы хотите сбежать от толпы?")
            otvet3 = choise()
            if otvet3 == True:
                progress("[blue]Побег...")
                print("Вы сбежали, и всё обошлось.")
            else:
                progress("[black]Толпа избивает вас...")
                progress("[gray]Проходит много времени...")
                print("Вы очнулись в подвале.")
                print("Вы хотите сбежать из подвала?")
                otvet4 = choise()
                if otvet4 == True:
                    progress("[light blue]Вы находите лом и пытаетесь выбраться из подвала...")
                    print("У вас получилось!")
                    print("Вы свободны")
                    print("Вы оглядываетесь и видите не знакомую вам деревню...")
                    print("Это похоже на деревню из игры")
                    print("Вы видите NPC")
                    print("Подойти к NPC ???")
                    otvet6 = choise()
                    if otvet6 == True:
                        print("???: Что тебе здесь нужно сталкер?")
                        sleep(1)
                        print(name, ": Я не знаю как тут оказался, помогите мне пожалуйста...")
                        sleep(1)
                        print("???: А, ты тут новичок, меня зовут Иван, но все тут зовут друг друга сталкерами")
                        sleep(1)
                        print(name, ": Меня зовут", name)
                        print(name, ": А можешь дать мне какое нибудь оружие или что-нибудь?")
                        sleep(1)
                        print("Иван: Да я могу дать тебе оружие, но если ты выполнишь для меня задание.")
                        print("Вы согласны на задание?")
                        otvet7 = choise()
                        if otvet7 == True:
                            print("Иван: На вот тебе КПК, на нём карта и с помощью него мы будем связываться.")
                            print("Консоль: Получен предмет КПК.")
                            inventory.append("КПК")
                            sleep(1)
                            print("Консоль: Получено задание.")
                            progress("[gray]Вы идёте до нужного места...")
                            print("Вы дошли до места и видите там зомби которого поручил убить Иван")
                            print("Вы начинаете его бить кулаками:")
                            root = Tk()
                            root.title("Attack табличка")
                            root.geometry("100x100")
                            btn = Button(text="Бей!", background="#555", foreground="#ccc",
                                        padx="20", pady="8", font="16", command=click_button)
                            btn.pack()
                            root.mainloop()
                            print("Вы убили зомби")
                            print("Консоль: Получена голова зомби")
                            sleep(1)
                            progress("Вы забираете его голову и несёте Ивану...")
                            print("Иван: Ооо молодец, на, вот тебе пистолет")
                            sleep(1)
                            print("Консоль: Получен пистолет Макарова.")
                            inventory.append("Пистолет Макарова")
                            print("Вы хотите прогуляться по городу?")
                            otvet8 = choise()
                            if otvet8 == True:
                                progress("Вы гуляете по городу...")
                                print("Вы нашли несколих NPC, как вы поняли их было несколько, потому что в этой деревне было всего 4 здания и несколько гаражей")
                                print("Подойти к первому NPC?")
                                otvet9 = choise()
                                if otvet9 == True:
                                    progress("Вы подходите к NPC...")
                                    print(name, ": Привет, меня зовут", name)
                                    sleep(1)
                                    print("???: Хм, привет, меня зовут Андрей")
                                    sleep(1)
                                    print("Андрей: Как я понял ты у нас новенький, я тут инженер, а ты тут без машины")
                                    print("Андрей смеётся.")
                                    sleep(1)
                                    print(name, ": Ну и что, что без машины? Будто у тебя есть машина")
                                    sleep(1)
                                    print("Андрей: Да, есть, (указывает на гараж) вон там мои машины")
                                    sleep(1)
                                    print(name, "В шоке")
                                    sleep(2)
                                    print("Андрей: Хочешь себе одну из них?")
                                    otvet10 = choise()
                                    if otvet10 == True:
                                        progress("Андрей рассказывает о задании")
                                        print("Консоль: Получено задание")
                                        print("Консоль: Вам надо убить нескольких кровососов")
                                        progress("Вы идёте до логова кровососов...")
                                        print("Вы заходите в него и видите трёх кровососов")
                                        print("Вы аттакуете первого...")
                                        root = Tk()
                                        root.title("Attack табличка")
                                        root.geometry("100x100")
                                        btn = Button(text="Бей!", background="#555", foreground="#ccc",
                                                padx="20", pady="8", font="16", command=click_button)
                                        btn.pack()
                                        root.mainloop()
                                        print("Вы убили первого!")
                                        print("Вы начинаете бить второго...")
                                        root = Tk()
                                        root.title("Attack табличка")
                                        root.geometry("100x100")
                                        btn = Button(text="Бей!", background="#555", foreground="#ccc",
                                                padx="20", pady="8", font="16", command=click_button)
                                        print("Вы убили второго!")
                                        print("Вы начинаете бить третьего, последнего...")
                                        root = Tk()
                                        root.title("Attack табличка")
                                        root.geometry("100x100")
                                        btn = Button(text="Бей!", background="#555", foreground="#ccc",
                                                padx="20", pady="8", font="16", command=click_button)
                                        print("Вы убили третьего.")
                                        print("Консоль: Получено три головы кровососа")
                                        progress("Вы возвращаетесь к Андрею...")
                                        print("Андрей: Ого! Ты молодец! На вот тебе ключи от машины, иди в гараж и забери машину.")
                                        print("Консоль: Вы получили ключи")
                                        inventory.append("Ключи от машины")
                                        print("Вы заходите в гараж и сажаетесь в машину")
                                        progress("Вы едете ко второму NPC...")
                                        print("Вы выходите из машины и подходите к NPC")
                                        print("???: Вау, вот это у тебя машина,")
                                        sleep(1)
                                        print(name, ": Спасибо, меня кстати зовут", name, "а тебя как?")
                                        sleep(1)
                                        print("???: Меня зовут Алексей, и как я понял ты тут новенький")
                                        sleep(1)
                                        print(name, "Да, я тут новенький, можешь подсказать мне где здесь монжо ночевать или жить?")
                                        sleep(1)
                                        print("Алексей: Да, я знаю где ты можешь пожить, у меня тут есть ненужный мне гараж, но ты просто так не сможешь в нём жить, выполни для меня задание")
                                        sleep(1)
                                        print(name, ": Хорошо, я выполню задание")
                                        progress("Алексей рассказывает о задании...")
                                        print("Консоль: Получено задание")
                                        print("Консоль: Нужно достать пару артефактов для Алексея")
                                        progress("Вы идёте до места где много артефактов...")
                                        print("Вы дошли и видите артефакт Глаз")
                                        progress("Вы идёте и наконец-то доходите до него, после чего забираете.")
                                        print("Консоль: Получен предмет Артефакт-Глаз")
                                        print("Вы видите второй артефакт Яблоко")
                                        progress("Вы прыгаете и наконец-то допрыгиваете до артефакта.")
                                        print("Консоль: Получен предмет Артефакт-Яблоко")
                                        progress("Вы их относите Алексею...")
                                        print("Алексей: Молодец! На, вот тебе ключ, сходи до гаража и можешь уже поспать.")
                                        progress("Вы едете до гаража...")
                                        print("Вы открываете гараж, загоняете машину... И ложитесь спать...")
                                        sleep(5)
                                        print("Вы прошли игру!")
                                        sleep(1)
                                        print("Хоть эта игра была и короткая, но надеюсь вам понравилась")
                                        sleep(1)
                                        print("Создатель игры: Кирилл Гардер")
                                elif otvet9 == False:
                                        print("???: Привет, ")
                                        sleep(1)
                                        print(name, ": Привет меня зовут", name, "а тебя как?")
                                        sleep(1)
                                        print("???: Меня зовут Алексей, и как я понял ты тут новенький")
                                        sleep(1)
                                        print(name, "Да, я тут новенький, можешь подсказать мне где здесь монжо ночевать или жить?")
                                        sleep(1)
                                        print("Алексей: Да, я знаю где ты можешь пожить, у меня тут есть ненужный мне гараж, но ты просто так не сможешь в нём жить, выполни для меня задание")
                                        sleep(1)
                                        print(name, ": Хорошо, я выполню задание")
                                        progress("Алексей рассказывает о задании...")
                                        print("Консоль: Получено задание")
                                        print("Консоль: Нужно достать пару артефактов для Алексея")
                                        progress("Вы идёте до места где много артефактов...")
                                        print("Вы дошли и видите артефакт Глаз")
                                        progress("Вы идёте и наконец-то доходите до него, после чего забираете.")
                                        print("Консоль: Получен предмет Артефакт-Глаз")
                                        print("Вы видите второй артефакт Яблоко")
                                        progress("Вы прыгаете и наконец-то допрыгиваете до артефакта.")
                                        print("Консоль: Получен предмет Артефакт-Яблоко")
                                        progress("Вы их относите Алексею...")
                                        print("Алексей: Молодец! На, вот тебе ключ, сходи до гаража и можешь уже поспать.")
                                        progress("Вы идёте до гаража...")
                                        progress("Вы открываете гараж и спите...")
                                        progress("Вы идёте ко второму NPC...")
                                        print(name, ": Привет, меня зовут", name)
                                        sleep(1)
                                        print("???: Хм, привет, меня зовут Андрей")
                                        sleep(1)
                                        print("Андрей: Как я понял ты у нас новенький, я тут инженер, а ты тут без машины")
                                        print("Андрей смеётся.")
                                        sleep(1)
                                        print(name, ": Ну и что, что без машины? Будто у тебя есть машина")
                                        sleep(1)
                                        print("Андрей: Да, есть, (указывает на гараж) вон там мои машины")
                                        sleep(1)
                                        print(name, "В шоке")
                                        sleep(2)
                                        print("Андрей: Хочешь себе одну из них?")
                                        otvet10 = choise()
                                        if otvet10 == True:
                                            progress("Андрей рассказывает о задании")
                                            print("Консоль: Получено задание")
                                            print("Консоль: Вам надо убить нескольких кровососов")
                                            progress("Вы идёте до логова кровососов...")
                                            print("Вы заходите в него и видите трёх кровососов")
                                            print("Вы аттакуете первого...")
                                            root = Tk()
                                            root.title("Attack табличка")
                                            root.geometry("100x100")
                                            btn = Button(text="Бей!", background="#555", foreground="#ccc",
                                                    padx="20", pady="8", font="16", command=click_button)
                                            btn.pack()
                                            root.mainloop()
                                            print("Вы убили первого!")
                                            print("Вы начинаете бить второго...")
                                            root = Tk()
                                            root.title("Attack табличка")
                                            root.geometry("100x100")
                                            btn = Button(text="Бей!", background="#555", foreground="#ccc",
                                                    padx="20", pady="8", font="16", command=click_button)
                                            print("Вы убили второго!")
                                            print("Вы начинаете бить третьего, последнего...")
                                            root = Tk()
                                            root.title("Attack табличка")
                                            root.geometry("100x100")
                                            btn = Button(text="Бей!", background="#555", foreground="#ccc",
                                                    padx="20", pady="8", font="16", command=click_button)
                                            print("Вы убили третьего.")
                                            print("Консоль: Получено три головы кровососа")
                                            progress("Вы возвращаетесь к Андрею...")
                                            print("Андрей: Ого! Ты молодец! На вот тебе ключи от машины, иди в гараж и забери машину.")
                                            print("Консоль: Вы получили ключи")
                                            inventory.append("Ключи от машины")
                                            print("Вы заходите в гараж и сажаетесь в машину")
                                        elif otvet10 == False:
                                            print("Алексей: Ну как знать.")
                                            progress("Вы идёте в гараж и ложитесь спать...")
                                            print("Вы прошли игру!")
                                            sleep(1)
                                            print("Хоть эта игра была и короткая, но надеюсь вам понравилась")
                                            sleep(1)
                                            print("Создатель игры: Кирилл Гардер")
                                            sleep(1)
                                            print("А также я могу продолжить эту игру если вы захотите")
                        else:
                            print("Вы просто бродите по деревне, после чего попадаете в лес и там теряетесь...")
                    else:
                        print("Вы просто бродите по деревне, после чего попадаете в лес и там теряетесь...")
                else:
                    print("Вы засыпаете после чего вы не можете проснуться...")
        else:
            for _ in track(range(100), description='[black]Толпа к вам подходит и избивает вас...'):
                process_data()
            print("Вы мертвы...")
    else:
        sleep(1)
        ccg.print_info()
        sleep(1)
        ccg.fight(ghoul)
elif otvet123 == False:
    print("ну тогда пока!")