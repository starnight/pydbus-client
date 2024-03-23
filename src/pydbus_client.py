from pydbus import SessionBus

class DbusTest:
    DBUS_TEST_BUS_NAME="io.starnight.dbus_test.TestServer"
    DBUS_TEST_OBJECT_PATH="/io/starnight/dbus_test/TestObject"
    DBUS_TEST_INTERFACE_NAME="io.starnight.dbus_test.TestInterface"

    def __init__(self):
        bus = SessionBus()

        # Create an object that will proxy for a particular remote object.
        self.remote_object = bus.get(
            self.DBUS_TEST_BUS_NAME,
            self.DBUS_TEST_OBJECT_PATH
        )

    def show_introspect(self):
        # Introspection returns an XML document containing information about the
        # methods, signals and properties supported by an interface.
        print("Introspection data:\n")
        print(self.remote_object.Introspect())

    def login(self, greeting: str) -> str:
        return self.remote_interface.Login(greeting)

    def send_msg(self, msg: str):
        self.remote_object.SendMsg(msg)

    def get_title(self):
        return self.remote_object.Title

    def set_title(self, title: str):
        self.remote_object.Title = title

    def register_property_changed_handler(self, cb):
        self.remote_object.PropertiesChanged.connect(cb)

    def register_msg_notify_handler(self, cb):
        self.remote_object.MsgNotification.connect(cb)
