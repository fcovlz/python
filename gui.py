"""
@ Description
    Brief example of how to create a gui

@ Pass/Fail @b criteria
    None

@ Usage
    From terminal:
        gui_example.py
"""
import wx


class SimpleAppWx(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent, id, title)
        print "Object built successfully "

    def setup(self):
        sizer = wx.GridBagSizer()
        entry = wx.TextCtrl(-1, value=u"Enter text here.", style=self.TE_PROCESS_ENTER)
        sizer.Add(entry, (0, 0), (1, 1), self.EXPAND)
        wx.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)

        button = wx.Button(-1, label="Send")
        sizer.Add(button, (0, 1))
        self.Bind(self.EVT_BUTTON, self.OnButtonClick, button)

        label = wx.StaticText(self, -1, label=u'Hello !')
        label.SetBackgroundColour(self.BLUE)
        label.SetForegroundColour(self.WHITE)

        sizer.Add(label, (1, 0), (1, 2), self.EXPAND)
        sizer.AddGrowableCol(0)

        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1, self.GetSize().y, 600, self.GetSize().y)
        self.entry.SetFocus()
        self.entry.SetSelection(-1, -1)
        self.Show(True)

    def button_click(self):
        self.label.SetLabel(self.entry.GetValue() + " (You clicked the button)")
        self.entry.SetFocus()
        self.entry.SetSelection(-1, -1)

    def press_enter(self):
        self.label.SetLabel(self.entry.GetValue() + " (You pressed ENTER)")
        self.entry.SetFocus()
        self.entry.SetSelection(-1, -1)


if __name__ == "__main__":
    title = "hello world"
    parent = 100
    id = 5050
    simplegui = SimpleAppWx(parent=parent, id=id, title=title)
    simplegui.setup()