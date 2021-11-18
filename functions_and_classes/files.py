import csv
import os


class Files:

    def __init__(self, src_path, dst_path, separator=None, code_page=None):
        self.src_path = src_path
        self.dst_path = dst_path
        if separator:
            self.separator = separator
        else:
            self.separator = ','
        self.code_page = code_page
        self.csv_lines = []

    def print_directory(self, path, mode):
        # print_path = ''
        if mode == 'r':
            print_path = self.src_path
            print()
            print('Nie znaleziono sciezki do pliku odczytu:  ' + print_path)
        elif mode == 'w':
            print_path = os.path.split(self.dst_path)[0]
            print()
            print('Nie znaleziono sciezki do folderu zapisu:  ' + print_path)
        print('Zawartosc katalogu  ' + path + ' :')
        dir_content = os.listdir(path)
        for dir_item in dir_content:
            if not os.path.isfile(path + '/' + dir_item):
                dir_item = '(katalog)\t' + dir_item
            else:
                dir_item = '         \t' + dir_item
            print('\t', dir_item)

    def check_if_path_exists(self, path, mode):
        # zalozenie jest nastepujace: plik csv ma poprawna strukture;
        # metoda nie sprawdza rozszerzenia pliku, sprawdza czy cos jest
        # folderem/katalogiem lub plikiem oraz czy w ogole istnieje
        if mode == 'r':
            if os.path.exists(path) and os.path.isfile(path):
                return True
            elif not os.path.exists(path):
                new_path = os.path.split(path)[0]
                if os.path.exists(new_path):
                    self.print_directory(new_path, mode)
                    return False
                else:
                    self.check_if_path_exists(new_path, mode)
            elif not os.path.isfile(path):
                new_path = os.path.split(path)[0]
                self.print_directory(new_path, mode)
                return False
        elif mode == 'w':
            path = os.path.split(path)[0]
            if os.path.exists(path):
                if path == os.path.split(self.dst_path)[0]:
                    return True
                else:
                    self.print_directory(path, mode)
                    return False
            else:
                new_path = os.path.split(path)[0]
                if os.path.exists(new_path):
                    self.print_directory(new_path, mode)
                    return False
                else:
                    self.check_if_path_exists(new_path, mode)

    def read_csv(self):
        with open(self.src_path, 'r', newline='', encoding=self.code_page) as f:
            csv_reader = csv.reader(f, delimiter=self.separator)
            for csv_line in csv_reader:
                self.csv_lines.append(csv_line)

    def write_csv(self):
        with open(self.dst_path, 'w', newline='', encoding=self.code_page) as f:
            csv_writer = csv.writer(f, delimiter=self.separator)
            for csv_line in self.csv_lines:
                csv_writer.writerow(csv_line)
            print()
            print('Zapisano plik ' + self.dst_path)
