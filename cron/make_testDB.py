import csv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from facility.models import ElderStatus,Elder



def test():
    e = Elder.objects.get(id=1)
    # t =ElderSerializer(e)
    print(e)
#
def testDB():
    file_path = 'test_db.csv'
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            eid = Elder.objects.get(id=row[0])
            # print(eid.id)
            test = Elder.objects.filter(id=1)
            # print(test.id)
            ElderStatus.objects.create(
                elder_id=eid,
                time=row[1],
                lay=row[2],
                sit=row[3],
                empty=row[4],
                recent_status=row[5],
                today_status=row[6],
                max_status=row[7]
            )

testDB()
# test()

