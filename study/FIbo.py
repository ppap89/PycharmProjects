from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if hp > 0:
            self._hp = hp
        else:
            self._hp = 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class ultraman(Fighter):
    __slots__ = ('name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp = random.randint(15, 25)

    def hug_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            if injury >= 50:
                injury = injury
            else:
                injury = 50
            return True

        else:
            self.attack(other)
            return False

    def magic_attack(self, others):

        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def hpreturn(self):
        returnHP = randint(5, 10)
        self._mp += returnHP
        return returnHP

    def __str__(self):
        return 'people:%s has hp:%d has mp:%d' % (self._name, self._hp, self._mp)


class Bad(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return 'bad name:%s hp:%d\n' % (self._name, self._hp)


def is_any_alive(mosters):
    for moster in mosters:
        if moster.alive > 0:
            return True
    return False


def choseone(mosters):
    mosters_len = len(mosters)
    index = randrange(mosters_len)
    moster = mosters[index]
    if moster.alive > 0:
        return moster


def show_message(ultraman, mosters):
    print(ultraman)
    for moster in mosters:
        print(moster, end='')

#debug
import pdb
def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())

def main():
    u = ultraman('dijia', 1000, 120)
    b4 = Bad('gesila', 500)
    b2 = Bad('baigujing', 100)
    b3 = Bad('niumowang', 750)
    m1 = [b3, b2, b4]
    fight_round = 1
    while u.alive > 0 and is_any_alive(m1):
        print('\n======%d round===========\n' % fight_round)
        m = choseone(m1)  # 选中
        skill = randint(1, 10)  # 随机选择attack way
        if skill <= 6:
            print('%s attack %s' % (u.name, m.name))
            u.attack(m)
            print('%s  magic huilan %d' % (u.name, u.hpreturn()))
        elif skill <= 9:
            if u.magic_attack(m):
                print('%s use magic' % u.name)
            else:
                print('magic use fail')
        else:
            if u.hug_attack(m):
                print('%s use huge magic attack %s' % (u.name, m.name))
            else:
                print('%sattack%s' % (u.name, m.name))
                print('%smagic%d' % (u.name, u.hpreturn()))
        if m.alive > 0:
            print('%s counterattack %s' % (m.name, u.name))
            m.attack(u)
        show_message(u, m1)
        fight_round += 1
    print('\n======over=======\n')
    if u.alive > 0:
        print('%swin' % u.name)
    else:
        print('moster win')


if __name__ == '__main__':
    main()
