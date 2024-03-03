import pprint
from .models import Access


def view_accesses():
    queryset = Access.objects.filter(port__gte=7000, port__lte=8000)
    print('Выполнен запрос на поиск записей с фильтром 7000 <= port <= 8000')
    print(f'Найдено {queryset.count()} записей!')

    def serialize(instance):
        return dict(
            src_ip=instance.src_ip.ip,
            dst_ip=instance.dst_ip.ip,
            port=instance.port,
            proto=instance.proto,
            contract=instance.contract
        )

    pprint.pprint(
        [serialize(x) for x in queryset[:3]]
    )
