import random

from .models import IpAddress, Access


def load_ips(count=1000):
    ips = []
    counter = 0
    for a in range(1, 256):
        for b in range(1, 256):
            for c in range(1, 256):
                for d in range(1, 256):
                    ips.append(f'{a}.{b}.{c}.{d}')
                    counter += 1
                    if counter == count:
                        return ips
    return ips


def load_access():
    IpAddress.objects.delete()

    ips = load_ips()

    while ips:
        try:
            src = ips.pop(-1)
            dst = ips.pop(0)

            src_ip = IpAddress(ip=src).save()
            dst_ip = IpAddress(ip=dst).save()

            Access(
                src_ip=src_ip,
                dst_ip=dst_ip,
                port=random.randint(0, 8000),
                proto='tcp',
                contract='mongodb/test/contract'
            ).save()
        except IndexError:
            break