from abc import ABC, abstractmethod


class Light:
    def on(self):
        print("The light is on")

    def off(self):
        print("The light is off")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.on()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.off()


class RemoteControl:
    def __init__(self):
        self._commands = {}

    def set_command(self, button, command):
        self._commands[button] = command

    def press_button(self, button):
        self._commands[button].execute()


light = Light()

light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command("ON", light_on)
remote.set_command("OFF", light_off)

remote.press_button("ON")
remote.press_button("OFF")