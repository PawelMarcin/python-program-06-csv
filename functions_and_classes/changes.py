
class Changes:
    
    def __init__(self, change_list, csv_table):
        self.change_list = change_list
        self.csv_table = csv_table

    def check_cell_range(self):
        if int(self.change_list[0]) <= len(self.csv_table) + 1:
            if int(self.change_list[1]) <= len(self.csv_table[0]) + 1:
                return True
            else:
                print()
                print('Adres komorki (wiersz: ' +
                      self.change_list[0] + ', kolumna: ' +
                      self.change_list[1] + ') poza tablica csv.')
                return False
        else:
            print()
            print('Adres komorki (wiersz: ' +
                  self.change_list[0] + ', kolumna: ' +
                  self.change_list[1] + ') poza tablica csv.')
            return False

    def make_a_change(self):
        old_csv_line = self.csv_table[int(self.change_list[0])]
        print()
        print('Oryginalny wiersz ' + self.change_list[0] + ' w pliku csv:')
        print(old_csv_line)
        self.csv_table[int(self.change_list[0])][int(self.change_list[1])] = \
            self.change_list[2]
        print()
        print('Zmieniony wiersz ' + self.change_list[0] +
              ' w pliku csv (komorka ' + self.change_list[1] + '):')
        print(self.csv_table[int(self.change_list[0])])
