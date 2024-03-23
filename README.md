# pydbus-client

This is a D-Bus client example written with Python.
The corresponding D-Bus server example is [gdbus-server](https://github.com/starnight/gdbus-server/tree/main).

## Build & Execute

It is based on GNOME 45 runtime now.

```sh
$ flatpak-builder build-dir build-aux/flatpak/io.starnight.pydbus-client.yaml --force-clean --install --user
$ flatpak run io.starnight.pydbus-client
```

## Reference

* [GTK](https://docs.gtk.org/gtk4/index.html)
* [Taiko's GTK4 Python tutorial](https://github.com/Taiko2k/GTK4PythonTutorial)
* [pydbus](https://github.com/LEW21/pydbus)
* [pydbus' example client.py](https://github.com/LEW21/pydbus/blob/master/examples/clientserver/client.py)
* [pydbus tutorial](https://github.com/LEW21/pydbus/blob/master/doc/tutorial.rst)
