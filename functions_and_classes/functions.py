import sys


def check_args_count():
    if len(sys.argv) >= 3:
        return sys.argv
    else:
        return False


def check_change_arg(txt):
    txt_change_arg_list = txt.split(',')
    if len(txt_change_arg_list) == 3:
        return True, txt_change_arg_list
    else:
        return False, None
