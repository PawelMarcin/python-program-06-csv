from functions_and_classes.functions import check_args_count
from functions_and_classes.functions import check_change_arg
from functions_and_classes.files import Files
from functions_and_classes.changes import Changes

args = check_args_count()

if args:
    f = Files(args[1], args[2], ';', 'utf-8')
    path_src_OK = f.check_if_path_exists(args[1], 'r')
    if path_src_OK:
        path_dst_OK = f.check_if_path_exists(args[2], 'w')
        if path_dst_OK:
            f.read_csv()
            if len(args) == 3:
                for csv_line in f.csv_lines:
                    print(csv_line)
                print('=' * 100)
                print('Wypisano plik csv. Nie wprowadzono zmian.')
            if len(args) > 3:
                change_count = 0
                for arg in args[3:]:
                    if check_change_arg(arg)[0]:
                        c = Changes(check_change_arg(arg)[1], f.csv_lines)
                        if c.check_cell_range():
                            c.make_a_change()
                            change_count += 1
                    else:
                        print()
                        print('Za malo argumentow dla zeby zmienic komorke.')

                if change_count > 0:
                    f.write_csv()
                    print('Liczba wprowadzonich zman: ' + str(change_count))
else:
    print('Za mala liczba argumentow !!!\n'
          'Uzyj polecenia:\n'
          '\t reader.py <src_path> <dst_path> [<change1> [<change2> [<...>]]] ')
