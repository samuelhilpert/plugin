from django.utils.translation import ugettext_lazy as _
import horizon

class HelloWorld(horizon.Panel):
    name = _("Hallo Welt")
    slug = "hallo_welt"
    permissions = ('openstack.roles.admin',)