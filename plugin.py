import datetime
import random

def datetime_generator(max_line=100):
    base_date = datetime.datetime.today()
    date_list = [(base_date - datetime.timedelta(minutes=x)).
                strftime("[%Y-%m-%d %I:%M:%S]") for x in range(0, max_line)]
    return date_list

def credit_card_generator(maxNum=100, x=12):
    records = 10
    if len(str(maxNum)) > 100:
        records = maxNum / 100
    return map(lambda st:st[:4]+'-'+st[4:8]+'-'+st[8:],
           ('{0!s}'.format(random.randint(10**(x-1), 10**x-1),
                                x=x) for i in range(records)))

def transaction_id_generator(maxNum=100):
    base_id = 123133
    list_id = [str(x) for x in xrange(base_id, base_id + maxNum)]
    return list_id

functions = {
              "datetime_generator":datetime_generator,
              "transaction_id_generator":transaction_id_generator,
              "credit_card_generator":credit_card_generator
            }
#test program for plugin.py
if __name__ == '__main__':
    print functions
    print transaction_id_generator(100)
    
