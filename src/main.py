#!/usr/bin/env python3

from pydbus_client import DbusTest

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    remote_dbus = DbusTest()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(-1, 350)
        title = self.remote_dbus.get_title()
        self.update_window_title(title)

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)

        self.textview_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_hexpand(True)
        self.scrolledwindow.set_vexpand(True)
        self.textview = Gtk.TextView()
        self.scrolledwindow.set_child(self.textview)
        self.textview_box.append(self.scrolledwindow)
        self.box1.append(self.textview_box)

        self.send_msg_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.entry = Gtk.Entry()
        self.entry.set_hexpand(True)
        self.entry.connect('activate', self.button_click_handler)
        self.button = Gtk.Button(label="Send")
        self.button.connect('clicked', self.button_click_handler)
        self.send_msg_box.append(self.entry)
        self.send_msg_box.append(self.button)
        self.box1.append(self.send_msg_box)

        self.remote_dbus.register_msg_notify_handler(self.msg_notify_handler)
        self.remote_dbus.register_property_changed_handler(self.dbus_property_changed_handler)

    def update_window_title(self, title: str):
        self.set_title(title)

    def button_click_handler(self, button):
        magic_title_cmd = "/title "

        msg = self.entry.get_text()
        if msg.startswith(magic_title_cmd):
            title = msg[len(magic_title_cmd):].strip()
            if len(title) > 0:
                self.update_dbus_title(title)
        else:
            self.send_msg(msg)

        self.entry.set_text("")

    def update_dbus_title(self, title: str):
        self.remote_dbus.set_title(title)

    def send_msg(self, msg: str):
        self.remote_dbus.send_msg(msg)

    # The arguments map to "MsgNotification" signal
    # https://github.com/starnight/gdbus-server/?tab=readme-ov-file#introspect-the-bus-object
    def msg_notify_handler(self, sender, msg):
        self.update_textview(f"{sender}: {msg}\n")

    def update_textview(self, msg: str):
        buffer = self.textview.get_buffer()
        end_itr = buffer.get_end_iter()
        buffer.insert(end_itr, msg)

    # The arguments map to "PropertiesChanged" signal
    # https://github.com/starnight/gdbus-server/?tab=readme-ov-file#introspect-the-bus-object
    def dbus_property_changed_handler(self, interface, changed_properties, invalidated_properties):
        for k, v in changed_properties.items():
            if k == "Title":
                self.update_window_title(v)

def on_activate(app):
    win = MainWindow(application=app)
    win.present()

if __name__ == '__main__':
    app = Gtk.Application()
    app.connect('activate', on_activate)
    app.run(None)
