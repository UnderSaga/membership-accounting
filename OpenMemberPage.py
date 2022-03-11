import os
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

def search(data):
    global datain
    datain = data + ".kv"
    directory = "TestPages/designs"
    filelist = os.listdir(directory)
    if datain in filelist:
        MembershipAccounting().run()
        return datain
    else:
        print("Fail")

class MembershipAccounting(App):
    def build(self):
        sm = ScreenManager()

        Builder.load_file(os.path.join(os.getcwd(), 'TestPages', 'designs', datain))
        return sm
