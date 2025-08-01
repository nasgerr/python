import random
from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        if not self._is_move:
            return False
        if self._tp == 1:
            self._x += go
        else:
            self._y += go
        return True

    def is_collide(self, ship):
        if self._x is None or self._y is None or ship._x is None or ship._y is None:
            return False

        if self._tp == 1:
            self_x1, self_y1 = self._x, self._y
            self_x2, self_y2 = self._x + self._length - 1, self._y
        else:
            self_x1, self_y1 = self._x, self._y
            self_x2, self_y2 = self._x, self._y + self._length - 1

        if ship._tp == 1:
            ship_x1, ship_y1 = ship._x, ship._y
            ship_x2, ship_y2 = ship._x + ship._length - 1, ship._y
        else:
            ship_x1, ship_y1 = ship._x, ship._y
            ship_x2, ship_y2 = ship._x, ship._y + ship._length - 1

        self_x1 -= 1
        self_y1 -= 1
        self_x2 += 1
        self_y2 += 1

        if (self_x1 > ship_x2 or self_x2 < ship_x1 or
                self_y1 > ship_y2 or self_y2 < ship_y1):
            return False
        return True

    def is_out_pole(self, size):
        if self._x is None or self._y is None:
            return True
        if self._tp == 1:
            return (self._x < 0 or self._x + self._length - 1 >= size or
                    self._y < 0 or self._y >= size)
        else:
            return (self._x < 0 or self._x >= size or
                    self._y < 0 or self._y + self._length - 1 >= size)

    def __getitem__(self, indx):
        return self._cells[indx]

    def __setitem__(self, indx, value):
        if value == 2:
            self._is_move = False
        self._cells[indx] = value

    def is_alive(self):
        return any(cell == 1 for cell in self._cells)


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        self._ships = [
            Ship(4, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2))
        ]

        for ship in self._ships:
            placed = False
            attempts = 0
            while not placed and attempts < 1000:
                attempts += 1
                x = randint(0, self._size - 1)
                y = randint(0, self._size - 1)
                ship.set_start_coords(x, y)

                if ship.is_out_pole(self._size):
                    continue

                collide = False
                for other_ship in self._ships:
                    if other_ship == ship or other_ship.get_start_coords() == (None, None):
                        continue
                    if ship.is_collide(other_ship):
                        collide = True
                        break

                if not collide:
                    placed = True

            if not placed:
                self._ships = []
                self.init()
                return

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            if not ship._is_move:
                continue

            go = random.choice([-1, 1])
            original_x, original_y = ship._x, ship._y
            ship.move(go)

            valid = True
            if ship.is_out_pole(self._size):
                valid = False
            else:
                for other_ship in self._ships:
                    if other_ship == ship:
                        continue
                    if ship.is_collide(other_ship):
                        valid = False
                        break

            if not valid:
                ship._x, ship._y = original_x, original_y
                go = -go
                ship.move(go)

                valid = True
                if ship.is_out_pole(self._size):
                    valid = False
                else:
                    for other_ship in self._ships:
                        if other_ship == ship:
                            continue
                        if ship.is_collide(other_ship):
                            valid = False
                            break

                if not valid:
                    ship._x, ship._y = original_x, original_y

    def show(self):
        pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            if x is None or y is None:
                continue
            if ship._tp == 1:
                for i in range(ship._length):
                    if x + i < self._size:
                        pole[y][x + i] = ship[i]
            else:
                for i in range(ship._length):
                    if y + i < self._size:
                        pole[y + i][x] = ship[i]
        for row in pole:
            print(' '.join(map(str, row)))

    def get_pole(self):
        pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            if x is None or y is None:
                continue
            if ship._tp == 1:
                for i in range(ship._length):
                    if x + i < self._size:
                        pole[y][x + i] = ship[i]
            else:
                for i in range(ship._length):
                    if y + i < self._size:
                        pole[y + i][x] = ship[i]
        return tuple(tuple(row) for row in pole)

    def is_alive_ships(self):
        return any(ship.is_alive() for ship in self._ships)

    def get_shot_result(self, x, y):
        for ship in self._ships:
            ship_x, ship_y = ship.get_start_coords()
            if ship._tp == 1:
                if y == ship_y and ship_x <= x < ship_x + ship._length:
                    idx = x - ship_x
                    if ship[idx] == 1:
                        ship[idx] = 2
                        return "попал"
            else:
                if x == ship_x and ship_y <= y < ship_y + ship._length:
                    idx = y - ship_y
                    if ship[idx] == 1:
                        ship[idx] = 2
                        return "попал"
        return "промах"


class SeaBattle:
    def __init__(self, size=10):
        self.size = size
        self.player_pole = GamePole(size)
        self.computer_pole = GamePole(size)
        self.player_shots = [[0 for _ in range(size)] for _ in range(size)]
        self.computer_shots = [[0 for _ in range(size)] for _ in range(size)]
        self.current_player = "player"

    def init_game(self):
        self.player_pole.init()
        self.computer_pole.init()
        self.player_shots = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.computer_shots = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = "player"

    def print_boards(self):
        print("\nВаше поле:")
        self.player_pole.show()
        print("\nПоле противника:")
        computer_pole = self.computer_pole.get_pole()
        for y in range(self.size):
            row = []
            for x in range(self.size):
                if self.player_shots[y][x] == 1:
                    row.append('O')
                elif self.player_shots[y][x] == 2:
                    row.append('X')
                else:
                    row.append('.')
            print(' '.join(row))

    def player_turn(self, x, y):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return "Неверные координаты"
        if self.player_shots[y][x] != 0:
            return "Вы уже стреляли в эту клетку"
        result = self.computer_pole.get_shot_result(x, y)
        if result == "попал":
            self.player_shots[y][x] = 2
        else:
            self.player_shots[y][x] = 1
        if result == "промах":
            self.current_player = "computer"
        return result

    def computer_turn(self):
        free_cells = []
        for y in range(self.size):
            for x in range(self.size):
                if self.computer_shots[y][x] == 0:
                    free_cells.append((x, y))
        if not free_cells:
            return "no_moves"
        x, y = random.choice(free_cells)
        result = self.player_pole.get_shot_result(x, y)
        if result == "попал":
            self.computer_shots[y][x] = 2
        else:
            self.computer_shots[y][x] = 1
        if result == "промах":
            self.current_player = "player"
        return (x, y, result)

    def check_game_over(self):
        if not self.computer_pole.is_alive_ships():
            return "player"
        if not self.player_pole.is_alive_ships():
            return "computer"
        return None

    def play(self):
        self.init_game()
        print("Морской бой - начали игру!")
        while True:
            self.print_boards()
            if self.current_player == "player":
                print("\nВаш ход. Введите координаты выстрела (x y):")
                try:
                    x, y = map(int, input().split())
                    result = self.player_turn(x, y)
                    print(f"Результат: {result}")
                except ValueError:
                    print("Ошибка ввода. Введите два числа через пробел.")
                    continue
            else:
                print("\nХод компьютера...")
                x, y, result = self.computer_turn()
                print(f"Компьютер стреляет в ({x}, {y}). Результат: {result}")
            winner = self.check_game_over()
            if winner:
                self.print_boards()
                if winner == "player":
                    print("\nПоздравляем! Вы победили!")
                else:
                    print("\nКомпьютер победил. Попробуйте еще раз!")
                break
            if self.current_player == "computer":
                self.computer_pole.move_ships()
            else:
                self.player_pole.move_ships()


if __name__ == "__main__":
    game = SeaBattle()
    game.play()