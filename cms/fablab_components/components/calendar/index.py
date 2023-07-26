from django_components import component
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


def get_event(element, day):
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

    return result


def get_repeats(element, year, month):
    repeated = []
    count = monthrange(year, month)[1]
    weekday = element.start.weekday()

    for days in range(count):
        switch = True
        current_date = datetime.date(year, month, days + 1)

        for exception in element.related_expection.all():
            if current_date >= exception.start and current_date <= exception.end:
                switch = False

        if weekday == current_date.weekday() and switch:
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


def get_data(year, month):
    days = {key: [] for key in range(38)}
    date = datetime.date(year, month, 1)

    date_start = date.weekday()

    elements = Event.objects.filter(
        (Q(repeat="0") & Q(start__year=year) & Q(start__month=month))
        | (
            Q(repeat="1")
            & Q(repeatStart__year__lte=year)
            & Q(repeatStart__month__lte=month)
            & Q(repeatEnd__year__gte=year)
            & Q(repeatEnd__month__gte=month)
        )
    )

    for element in elements:
        if element.repeat == "0":
            print(element.start.day)
            days[element.start.day + date_start - 1].append(
                get_event(element, element.start.day)
            )
        else:
            repeats = get_repeats(element, year, month)
            for repeat in repeats:
                days[repeat["day"] + date_start - 1].append(repeat)

    return {
        "index": date_start - 1,
        "month_string": MONTHS[month - 1],
        "month": month,
        "year": year,
        "date_next": get_next_date(year, month),
        "date_before": get_before_date(year, month),
        "days": days,
    }


@component.register("calendar")
class Calendar(component.Component):
    template_name = "calendar/index.html"

    def get_context_data(self):
        return {}

    def render(self, context):
        request = context.get("request")

        year = request.GET.get("year")
        month = request.GET.get("month")

        if year is None or month is None:
            result = get_data(
                datetime.datetime.today().year, datetime.datetime.today().month
            )
        else:
            result = get_data(int(year), int(month))

        print(result)

        context.update({"data": result})

        template_name = self.get_template_name(context)
        template = self.get_template(context, template_name)
        self.validate_fills_and_slots_(context, template)
        updated_fill_stacks = self.get_updated_fill_stacks(context)
        with context.update({FILLED_SLOTS_CONTEXT_KEY: updated_fill_stacks}):
            return template.render(context)

    class Media:
        css = "calendar/index.css"
        js = "calendar/index.js"
