import wx

class sizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title="Sizer Test Frame")
        panel = wx.Panel(self,-1)
        panel.SetBackgroundColour("black")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
     
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.TextCtrl(panel,-1,"Muti line text test",style=wx.TE_MULTILINE)
        box1.Add(text,proportion=1,flag=wx.EXPAND)
        sizer.Add(box1,proportion=1,flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=2)
                
        ok_button = wx.Button(panel,wx.ID_ABORT,"OK")
        canel_button = wx.Button(panel,wx.ID_APPLY,"Canel")
        
        sizer.Add(ok_button,flag=wx.EXPAND)
        sizer.Add(canel_button,flag=wx.EXPAND)
        
        panel.SetSizer(sizer)
        

if __name__ == "__main__":
    app = wx.PySimpleApp()
    window = sizerFrame()
    window.Show()
    app.MainLoop()