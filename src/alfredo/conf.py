from alfredo.plugins.apps import Apps
from alfredo.plugins.calculator import Calculator
from alfredo.plugins.files import Files
from alfredo.plugins.search import GoogleSearch, YoutubeSearch

DEFAULT_CALCULATOR = Calculator

DEFAULT_PLUGIN = Apps

PLUGINS = {
    'g': GoogleSearch,
    'y': YoutubeSearch,
    'f': Files,
}
