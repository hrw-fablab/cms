from django_components import component
import datetime
from calendar import monthrange
from cms.fablab_components.components.calendar.utils import (
    get_events,
    get_event,
    get_repeats,
    get_next_date,
    get_before_date,
)

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

def get_days_events(days, elements, year, month, start):
    for element in elements:
        if element.repeat == "0":
            day_index = element.start.day + start
            days[day_index]["events"].append(get_event(element, element.start.day))

        if element.length > 1 and element.repeat == "0":
            for day in range(element.length - 1):
                day_index = element.start.day + day + start + 1
                days[day_index]["events"].append(
                    get_event(element, element.start.day + day, redirect=True)
                )
                days[day_index]["repeat"] = True
            continue

        if element.repeat == "1":
            repeats = get_repeats(element, year, month)
            for repeat in repeats:
                day_index = repeat["day"] + start
                days[day_index]["events"].append(repeat)
    
    return days

def get_data(year, month):
    days = {key: {"repeat": None, "events": []} for key in range(38)}
    date = datetime.date(year, month, 1)

    date_start = date.weekday() - 1

    elements = get_events(year, month)

    days = get_days_events(days, elements, year, month, date_start)

    return {
        "index": date_start,
        "month_length": monthrange(year, month)[1] + date_start + 1,
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
