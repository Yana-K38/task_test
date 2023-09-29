import os
import random

import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "send_revenue.settings")
django.setup()


import random
from decimal import Decimal

from django.utils.timezone import make_aware
from faker import Faker
from revenue.models import RevenueStatistic
from spend.models import SpendStatistic

fake = Faker()

for _ in range(20):
    name = fake.company()
    start_date = fake.date_time_between(start_date="-1y", end_date="now")
    spend = Decimal(random.uniform(100, 10000)).quantize(Decimal("0.01"))
    impressions = random.randint(1000, 10000)
    clicks = random.randint(50, 500)
    conversion = random.randint(1, 50)

    spend_stat = SpendStatistic.objects.create(
        name=name,
        date=make_aware(start_date),
        spend=spend,
        impressions=impressions,
        clicks=clicks,
        conversion=conversion,
    )

    revenue = Decimal("100.00")
    RevenueStatistic.objects.create(
        name=name, spend=spend_stat, date=make_aware(start_date), revenue=revenue
    )
