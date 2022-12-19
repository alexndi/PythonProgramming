import wx
import time


class BMICalculator(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "BMI Calculator", pos=wx.DefaultPosition, size=wx.Size(420, 300))
        self.panel = wx.Panel(self)
        self.Centre()
        self.label_text = wx.StaticText(self.panel, -1, "Body Mass Index: ", (20, 50))
        self.result_text = wx.StaticText(self.panel, -1, "... kg/(m*m)", (120, 50))
        self.static_text_height = wx.StaticText(self.panel, -1, "Height:", (20, 90))
        self.height = wx.SpinCtrlDouble(self.panel, -1, pos=(65, 87), size=(60, -1), min=0, max=300)
        self.static_text_height_extra = wx.StaticText(self.panel, -1, "(in centimeters)", (130, 90))
        self.static_text_weight = wx.StaticText(self.panel, -1, "Weight:", (20, 130))
        self.weight = wx.SpinCtrlDouble(self.panel, -1, pos=(65, 127), size=(60, -1), min=0, max=300)
        self.static_text_weight_extra = wx.StaticText(self.panel, -1, "(in kilograms)", (130, 130))
        self.bmi_underweight = wx.StaticText(self.panel, -1, "Underweight = < 18.5", (253, 90))
        self.bmi_normal_weight = wx.StaticText(self.panel, -1, "Normal weight = 18.5-24.9", (239, 110))
        self.bmi_overweight = wx.StaticText(self.panel, -1, "Overweight = 25-29.9", (254, 130))
        self.bmi_obesity = wx.StaticText(self.panel, -1, "Obesity = > 30", (274, 150))
        self.button_compute = wx.Button(self.panel, label="Compute", pos=(40, 170), size=(60, -1))
        self.button_compute.Bind(wx.EVT_BUTTON, self.onCompute)
        self.button_refresh = wx.Button(self.panel, label="Refresh", pos=(122, 170), size=(60, -1))
        self.button_refresh.Bind(wx.EVT_BUTTON, self.onRefresh)
        self.button_cancel = wx.Button(self.panel, label="Close", pos=(285, 170), size=(60, -1))
        self.button_cancel.Bind(wx.EVT_BUTTON, self.onClose)

    def onCompute(self, event):

        self.result_text.SetLabel(
                str(self.compute_BMI(self.height.GetValue(), self.weight.GetValue())) + " kg/(m*m)")
        time.sleep(0.1)

    def onRefresh(self, event):
        self.result_text.SetLabel("... kg/(m*m)")
        self.height.SetValue(0)
        self.weight.SetValue(0)


    def onClose(self, event):
        self.Close(True)
        time.sleep(0.1)

    def compute_BMI(self, height, weight):
        height_m = float(height) / 100
        BMI = weight / (height_m * height_m)
        return BMI


def main():
    app = wx.App()
    frame = BMICalculator(None, -1)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()