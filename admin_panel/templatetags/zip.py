from django import template

register = template.Library()

@register.filter
def zip_lists(list1, list2):
    return zip(list1, list2)

# 自訂過濾器：將西元年轉換為民國年
@register.filter(name='to_roc_year')
def to_roc_year(date):
    # 113年4月3日 07:59
    return f'{date.year-1911}年{date.month}月{date.day}日 {date.strftime("%H:%M")}'
