import horizon

class HelloWorldPanel(horizon.Panel):
    name = "Hello World"
    slug = "hello"

horizon.get_dashboard("project").register(HelloWorldPanel)
