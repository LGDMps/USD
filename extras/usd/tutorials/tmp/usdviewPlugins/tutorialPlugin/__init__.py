from pxr import Tf
from pxr.Usdviewq.plugin import PluginContainer


def printMessage(usdviewApi):
    print("Hello, World!")


class TutorialPluginContainer(PluginContainer):

    def registerPlugins(self, plugRegistry, usdviewApi):

        self._printMessage = plugRegistry.registerCommandPlugin(
            "TutorialPluginContainer.printMessage",
            "Print Message",
            printMessage)

    def configureView(self, plugRegistry, plugUIBuilder):

        tutMenu = plugUIBuilder.findOrCreateMenu("Tutorial")
        tutMenu.addItem(self._printMessage)

Tf.Type.Define(TutorialPluginContainer)