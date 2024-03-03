import sys

from .upload import load_access
from .views import view_accesses

if __name__ == '__main__':
    args = sys.argv

    if len(args) == 1:
        raise AttributeError('Отстуствют параметры')

    initial_command = sys.argv[1]

    match initial_command:
        case 'upload_data':
            load_access()
        case 'selection':
            view_accesses()
        case _:
            raise AttributeError('Некорректный параметр\n'
                                 'upload_data - загрузить данные\n'
                                 'selection - выборка\n',)
