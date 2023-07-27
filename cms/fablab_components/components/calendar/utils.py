import datetime
from cms.events.models import Event
from calendar import monthrange
from django.db.models import Q

FILLED_SLOTS_CONTEXT_KEY = "_DJANGO_COMPONENTS_FILLED_SLOTS"

MONTHS = [
    "Januar",
    "Februar",
    "März",
    "April",
    "Mai",
    "Juni",
    "Juli",
    "August",
    "September",
    "Oktober",
    "November",
    "Dezember",
]


def get_events(year, month):
    return Event.objects.filter(
        (Q(repeat="0") & Q(start__year=year) & Q(start__month=month))
        | (
            Q(repeat="1")
            & Q(repeatStart__year__lte=year)
            & Q(repeatStart__month__lte=month)
            & Q(repeatEnd__year__gte=year)
            & Q(repeatEnd__month__gte=month)
        )
    )


def get_event(element, day, redirect=None):
    result = {
        "title": element.title,
        "adress": element.adress,
        "link": element.link,
        "link_text": element.link_text,
        "length": element.length,
        "timeStart": element.timeStart,
        "timeEnd": element.timeEnd,
        "start": element.start.weekday(),
        "description": element.description,
        "category": element.category,
        "day": day,
    }

    if redirect:
        result["redirect"] = "redirect"

    if element.length > 1:
        result["type"] = "multi"
        result["timeStart"] = element.start.strftime("%m.%d %H:%M")
        result["timeEnd"] = element.end.strftime("%m.%d %H:%M")

    return result


def check_for_exception(element, date):
    for exception in element.related_expection.all():
        if date >= exception.start and date <= exception.end:
            return False

    return True


def get_repeats(element, year, month):
    repeated = []
    count = monthrange(year, month)[1]
    weekday = element.start.weekday()

    for days in range(count):
        current_date = datetime.date(year, month, days + 1)

        exception = check_for_exception(element, current_date)
        if exception is False:
            continue

        if weekday == current_date.weekday():
            repeated.append(get_event(element, current_date.day))

    return repeated


def get_next_date(year, month):
    new_month = month + 1
    new_year = year

    if month == 12:
        new_year = year + 1
        new_month = 1

    return f"?year={new_year}&month={new_month}"


def get_before_date(year, month):
    new_month = month - 1
    new_year = year

    if month == 1:
        new_year = year - 1
        new_month = 12

    return f"?year={new_year}&month={new_month}"