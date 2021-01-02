from abc import ABC, abstractmethod
import multiprocessing
from multiprocessing import Queue
from alfredo_types.item import Item


class Plugin(ABC, multiprocessing.Process):
    """Base class for plugin creation.
    All plugins should inherit this class
    in order to be registered."""

    def __init__(self, alf, query, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.alfredo: 'Alfredo' = alf
        self.query: str = query
        self.q: Queue = q
        self.start()

    @abstractmethod
    def get_options(self, query: str) -> [Item]:
        """Should be overwritten. Method to return the options"""
        pass

    @abstractmethod
    def action(self, command: str) -> None:
        """Define the action that should be taken
        by this plugin once the user selects an option"""
        pass

    def run(self) -> None:
        options = self.get_options(self.query)
        self.q.put(options)

    @staticmethod
    def make_item(title, command='', subtitle=''):
        return {
            'title': title,
            'subtitle': subtitle,
            'command': command,
        }
