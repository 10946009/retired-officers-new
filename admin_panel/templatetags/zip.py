from django import template
from django.utils import timezone
register = template.Library()


@register.filter
def zip_lists(list1, list2):
    return zip(list1, list2)


# 自訂過濾器：將西元年轉換為民國年
@register.filter(name="to_roc_year")
def to_roc_year(date):
    # Make sure the date is timezone-aware
    if timezone.is_naive(date):
        date = timezone.make_aware(date)

    # Convert the date to the current timezone
    date = timezone.localtime(date)

    # Format the date
    return f"{date.year-1911}年{date.month}月{date.day}日 {date.strftime('%H:%M')}"