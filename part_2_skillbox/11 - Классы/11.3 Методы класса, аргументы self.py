class User:
    user_name = 'Admin'
    password = 'qwerty'
    is_banned = False
    friends = []

    def print_info(self):
        print('Name: {}\n -Password: {}\n -Ban status: {}'.format(self.user_name, self.password, self.is_banned))

    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.user_name)
        else:
            self.friends.append(friend)

user_1 = User()
user_1.print_info()
user_1.add_friend('Bob')
print(user_1.friends)

user_2 = User()
user_2.user_name = 'Алина'
user_1.add_friend(user_2)
print(user_1.friends)

#-----------------------#
class Family:
    surname = 'Ivanov'
    money = int(1e5)
    have_a_house = False

    def info(self):
        print('\nFamily name: {}\nFamily founds: {}\nHaving a house: {}'
              .format(self.surname, self.money, self.have_a_house))

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current value: {}'.format(amount, self.money))

    def buy_house(self, house_price, discount = 0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased! Current money: {}\n'.
                  format(self.money))
        else:
            print('Not enough money!\n')

my_family = Family()
my_family.info()
print('Try to buy house')
my_family.buy_house(int(1e5))
if not my_family.have_a_house:
    my_family.earn_money(int(8e6))
    print('Try to buy a house again')
    my_family.buy_house(8e6, 10)

my_family.info()
