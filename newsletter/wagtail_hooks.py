from wagtail.contrib.modeladmin.options import modeladmin_register, ModelAdmin, ModelAdminGroup
from birdsong.options import CampaignAdmin

from .models import Newsletter, Contact

class NewsletterAdmin(CampaignAdmin):
    campaign = Newsletter
    menu_label = 'Newsletter'
    menu_icon = 'mail'
    menu_order = 200
    contact_class = Contact

class ContactAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Kontakte'
    menu_icon = 'group'
    menu_order = 200

@modeladmin_register
class NewsletterGroup(ModelAdminGroup):
    menu_label = "Newsletter"
    menu_icon = "group"
    menu_order = 200
    items = (NewsletterAdmin, ContactAdmin)