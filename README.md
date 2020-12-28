# Alfredo
Alfredo is an attempt to copy some of [Alfred's](https://www.alfredapp.com/) features to run on linux.

Alfredo was a POC project originally made to follow a book, but since It actually became useful to me I'm opening the repo with It's obvious flaws.

## How It Works
Alfredo implements a simple interface written in kivy that receives input from the user. The input is then parsed at runtime by Alfredo that resolves what plugin should be used to get options for the current query. Thus, Alfredo works with prefixes. One can have a prefix 'p' for running python scripts for example, or the prefix 'y' to quickly search and open youtube.

Plugins are just python classes that implements two methods: `get_options` and `action`. The former takes in the current query and returns a list of options, the latter is a definition of the action to take when the user selects an option, like copying to the clipboard or opening a document.

## Writing a Plugin
To write a plugin you should write a python class that inherit the `Plugin` class, from `plugins.base`. Your class should implement at least two methods:

### `action(command)`
This is the method that will run once the user selects an option. The command argument is a string defined in the option.

### `get_options(query)`
This is the method that gives the options to the user. It receives a query, and It should return a list of options. An option is defined as a dict with a `title` key and an optional `subtitle` key (that will be displayed in the gui) and with a `command` key that will be passed to the `action` method one the option is selected.

## Defining plugins and prefixes
For the moment, Alfredo gets Its configs from the conf.py file in the root of the project. There you can find simple examples on how the plugins and prefixes are set.

## Drawbacks
To aviod a frozen screen while expensive functions run to search for results (like searching for files in a disk or querying a slow api), every time the user types a new character a new process is spawned to handle the plugin's search for results, taking place of the previous process that is brutally killed. That means that It's not possible to cache the results, and that a lot of processes are created and killed while using Alfredo.
I don't really know how to handle this and would appreciate any help on the matter.

There is no installable package or decent dependency management yet (some default actions assume that the user has a certain package installed, like `xclip`).
