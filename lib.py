from decimal import Decimal, getcontext, ROUND_HALF_UP

def calc(data):
    avg = sum(data) / len(data)

    tmp = 0
    for d in data:
        diff = d - avg
        tmp += diff * diff

    d1 = tmp / len(data)
    return (avg, d1, d1**0.5)

def ru(val):
    c = getcontext()
    c.rounding = ROUND_HALF_UP

    d = Decimal(val)
    return d.quantize(Decimal('0.0'))