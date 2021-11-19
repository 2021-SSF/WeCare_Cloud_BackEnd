import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from graph.models import ElderStatus,Elder

current_path = os.path.abspath(__file__)
dir = os.path.dirname(current_path)


def testDB():
    file_path = os.path.join(dir, 'test_graph_01.csv')
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            eid = Elder.objects.get(id=row[0])
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


