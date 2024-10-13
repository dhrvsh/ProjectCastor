import pyglet

# get a list of all low-level input devices:
devices = pyglet.input.get_devices()

# get a list of all controllers:
controllers = pyglet.input.get_controllers()

# get a list of all joysticks:
joysticks = pyglet.input.get_joysticks()

# get a list of tablets:
tablets = pyglet.input.get_tablets()

# get an Apple Remote, if available:
remote = pyglet.input.get_apple_remote()

# create a ControllerManager instance:
controller_manager = pyglet.input.ControllerManager()