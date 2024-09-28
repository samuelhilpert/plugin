from openstack_dashboard.dashboards.project import dashboard
from horizon_plugin import panel

dashboard.Project.register(panel.HelloWorld)
