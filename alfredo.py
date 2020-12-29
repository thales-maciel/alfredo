from multiprocessing import Queue
import threading

from conf import PLUGINS, DEFAULT_CALCULATOR, DEFAULT_PLUGIN


class Alfredo:

    def __init__(self, g):
        self.gui = g
        self.plugins = PLUGINS
        self.calculator = DEFAULT_CALCULATOR
        self.default_plugin = DEFAULT_PLUGIN
        self.current_plugin = None
        self.command = ''
        self.q = Queue()
        self.t = threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        v = None
        while True:
            value = self.q.get()
            if v is not value:
                self.callback(value)
                v = value

    def parse_input(self, query):
        # If query is a math expression, send It to the calc plugin
        # TODO Bring the calc plugin to the class, to stop double eval
        try:
            eval(query.split(' ', 1)[0])
            plugin = self.calculator
            command = query
            self.setup_plugin(plugin, command)
        except (SyntaxError, NameError):
            candidate = query.split(' ', 1)[0]
            if ' ' in query and candidate in self.plugins:
                plugin = self._get_plugin(candidate)
                command = query.split(' ', 1)[1]
            else:
                # If there is no prefix, send to default plugin
                plugin = self.default_plugin
                command = query
        self.setup_plugin(plugin, command)

    def setup_plugin(self, plugin, query):
        if self.current_plugin:
            self.current_plugin.kill()
        self.current_plugin = plugin(alf=self, query=query, q=self.q)
        self.command = query
        self.set_mode_label(self.current_plugin.label)

    def callback(self, options):
        self.refresh_options(options)

    def _get_plugin(self, prefix):
        """Returns the plugin associated with a prefix"""
        return self.plugins.get(prefix, None)

    def refresh_options(self, options):
        self.gui.refresh_options(options)

    def action(self, command):
        self.current_plugin.action(command)

    def set_mode_label(self, new_label):
        self.gui.set_mode_label(new_label)

if __name__ == "__main__":
    import os
    os.environ["KIVY_NO_CONSOLELOG"] = "1"
    from gui.gui import MainApp
    MainApp().run()
