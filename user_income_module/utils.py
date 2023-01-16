import calendar
from datetime import datetime, timedelta

from django.db.models import Sum

def calculate_income_general_stats(incomes):
    
    this_month, this_year = str(datetime.now().month).zfill(2), datetime.now().year
    first_day, day_count = calendar.monthrange(int(this_year), int(this_month))
    incomes_this_month = incomes.filter(created_at__range=[f"{this_year}-{this_month}-01", f"{this_year}-{this_month}-{day_count}"])

    previous_date = datetime.now() - timedelta(days=30)
    previous_month, previous_year = previous_date.month, previous_date.year
    first_day, day_count = calendar.monthrange(previous_year, previous_month)
    incomes_previous_month = incomes.filter(created_at__range=[f"{previous_year}-{previous_month}-01", f"{previous_year}-{previous_month}-{day_count}"])
    previous_sum = incomes_previous_month.aggregate(Sum('amount')).get('amount__sum', 0)
    if previous_sum is None:
        previous_sum = 0
    
    
    two_month_ago_date = datetime.now() - timedelta(days=60)
    two_month_ago_month, two_month_ago_year = two_month_ago_date.month, two_month_ago_date.year
    first_day, day_count = calendar.monthrange(two_month_ago_year, two_month_ago_month)
    incomes_previous_month = incomes.filter(created_at__range=[f"{two_month_ago_year}-{two_month_ago_month}-01", f"{two_month_ago_year}-{two_month_ago_month}-{day_count}"])
    two_month_ago_sum = incomes_previous_month.aggregate(Sum('amount')).get('amount__sum', 0)
    if two_month_ago_sum is None:
        two_month_ago_sum = 0
    
    sum_of_incomes = incomes.aggregate(Sum('amount')).get('amount__sum', 0)
    this_month_income = incomes_this_month.aggregate(Sum('amount')).get('amount__sum', 0)
    progress = previous_sum - two_month_ago_sum
    
    return sum_of_incomes, this_month_income, progress