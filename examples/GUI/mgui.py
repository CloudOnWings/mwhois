#!/usr/bin/env python

from mthread import *
import mwhois.const as CONST
import tempfile
import threading
import wx

# begin wxGlade: extracode
# end wxGlade

class AboutDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AboutDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.NullBitmap)
        self.label_txt = wx.StaticText(self, -1, "Author: Joel Cumberland\n" \
            "Version: 0.1.10a Alpha\n" \
            "Website: jrosco.github.io/mwhois/\n" \
            "Email: joel_c@zoho.com")
        self.button_close = wx.Button(self, -1, "Close")
        
        self.__set_properties()
        self.__do_layout()
         
        self.Bind(wx.EVT_BUTTON, self.close_app, self.button_close)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AboutDialog.__set_properties
        self.SetTitle("About mwhois")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AboutDialog.__do_layout
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add(self.bitmap_1, 0, 0, 0)
        sizer_13.Add(self.label_txt, 0, 0, 0)
        sizer_12.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_14.Add(self.button_close, 0, 0, 0)
        sizer_12.Add(sizer_14, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_12)
        sizer_12.Fit(self)
        self.Layout()
        # end wxGlade
    
    def close_app(self, event): # wxGlade: MyApp.<event_handler>
        
        #wx.Window.Close(self, force=False)
        wx.Dialog.Close(self, force=True);
        # end of class AboutDialog


class MyApp(wx.Frame):
    
        
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyApp.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.notebook_1_pane = wx.Panel(self.notebook_1, -1)
        self.sizer_5_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "mwhois")
        self.sizer_1_staticbox = wx.StaticBox(self.notebook_1_pane, -1, "mwhois")
        
        # Menu Bar
        self.mwhois_top_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.close = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Close", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.close)
        self.mwhois_top_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        self.about = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "About", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.about)
        self.mwhois_top_menubar.Append(wxglade_tmp_menu, "Help")
        self.SetMenuBar(self.mwhois_top_menubar)
        # Menu Bar end
        self.single_lbl = wx.StaticText(self.notebook_1_pane, -1, "Enter domain Name:", style=wx.ALIGN_CENTRE)
        self.single_txt = wx.TextCtrl(self.notebook_1_pane, -1, "", style=wx.TE_PROCESS_ENTER)
        self.single_button = wx.Button(self.notebook_1_pane, -1, "Single Search")
        self.single_txt_area = wx.TextCtrl(self.notebook_1_pane, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.single_quit_btn = wx.Button(self.notebook_1_pane, -1, "Quit")
        self.input_lbl = wx.StaticText(self.notebook_1_pane_2, -1, "Input Wordlist:")
        self.input_txt = wx.TextCtrl(self.notebook_1_pane_2, -1, "", style=wx.TE_PROCESS_ENTER)
        self.input_btn = wx.Button(self.notebook_1_pane_2, -1, "Open")
        self.save_lbl = wx.StaticText(self.notebook_1_pane_2, -1, "Output Domainlist:")
        self.save_txt = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.save_btn = wx.Button(self.notebook_1_pane_2, -1, "Save")
        self.adv_txt = wx.StaticText(self.notebook_1_pane_2, -1, "Advanced Search:")
        self.adv_chkbox = wx.CheckBox(self.notebook_1_pane_2, -1, "")
        self.tld_lbl = wx.StaticText(self.notebook_1_pane_2, -1, "Select TLD:")
        self.tld_combo = wx.ComboBox(self.notebook_1_pane_2, -1, choices=["com", "net", "edu", "biz"], style=wx.CB_DROPDOWN)
        self.adv_txt_area = wx.TextCtrl(self.notebook_1_pane_2, -1, "", style=wx.TE_MULTILINE)
        self.begin_btn = wx.Button(self.notebook_1_pane_2, -1, "Begin")
        self.adv_quit_btn = wx.Button(self.notebook_1_pane_2, -1, "Quit")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.close_app, self.close)
        self.Bind(wx.EVT_MENU, self.about_diag, self.about)
        self.Bind(wx.EVT_BUTTON, self.single_search, self.single_button)
        self.Bind(wx.EVT_BUTTON, self.close_app, self.single_quit_btn)
        self.Bind(wx.EVT_BUTTON, self.open_file, self.input_btn)
        self.Bind(wx.EVT_BUTTON, self.save_file, self.save_btn)
        self.Bind(wx.EVT_CHECKBOX, self.adv_search, self.adv_chkbox)
        self.Bind(wx.EVT_COMBOBOX, self.get_tld, self.tld_combo)
        self.Bind(wx.EVT_BUTTON, self.multi_search, self.begin_btn)
        self.Bind(wx.EVT_BUTTON, self.close_app, self.adv_quit_btn)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyApp.__set_properties
        self.SetTitle("mwhois")
        _icon = wx.EmptyIcon()
        #_icon.CopyFromBitmap(wx.Bitmap("D:\\My Documents\\development\\xwh0i5\\media\\icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((550, 642))
        self.single_lbl.SetMinSize((130, 14))
        self.single_lbl.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.single_txt.SetMinSize((178, 21))
        self.single_txt.SetFocus()
        self.single_button.SetMinSize((99, 23))
        self.single_txt_area.SetMinSize((524, 483))
        self.input_lbl.SetMinSize((120, 13))
        self.input_lbl.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.input_txt.SetMinSize((200, 21))
        self.save_lbl.SetMinSize((120, 13))
        self.save_lbl.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.save_txt.SetMinSize((200, 21))
        self.adv_txt.SetMinSize((120, 20))
        self.adv_txt.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.adv_chkbox.SetMinSize((25, 13))
        self.tld_lbl.SetMinSize((80, 13))
        self.tld_lbl.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.tld_combo.SetMinSize((50, 21))
        self.tld_combo.SetForegroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_DESKTOP))
        self.tld_combo.SetSelection(-1)
        self.adv_txt_area.SetMinSize((524,440))
        self.adv_txt_area.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.adv_txt_area.SetForegroundColour(wx.Colour(0, 255, 0))
        self.adv_txt_area.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Arial"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyApp.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.StaticBoxSizer(self.sizer_1_staticbox, wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.single_lbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.single_txt, 0, 0, 0)
        sizer_2.Add(self.single_button, 0, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(sizer_2, 0, 0, 0)
        sizer_3.Add(self.single_txt_area, 60, wx.EXPAND, 0)
        sizer_3.Add(self.single_quit_btn, 0, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(sizer_3, 100, wx.EXPAND, 0)
        self.notebook_1_pane.SetSizer(sizer_1)
        sizer_7.Add(self.input_lbl, 0, 0, 0)
        sizer_7.Add(self.input_txt, 0, 0, 0)
        sizer_7.Add(self.input_btn, 0, 0, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add(self.save_lbl, 0, 0, 0)
        sizer_8.Add(self.save_txt, 0, 0, 0)
        sizer_8.Add(self.save_btn, 0, 0, 0)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_9.Add(self.adv_txt, 0, 0, 0)
        sizer_9.Add(self.adv_chkbox, 0, 0, 0)
        sizer_9.Add(self.tld_lbl, 0, 0, 0)
        sizer_9.Add(self.tld_combo, 0, 0, 0)
        sizer_6.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_11.Add(self.adv_txt_area, 60, wx.EXPAND, 0)
        sizer_6.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_10.Add(self.begin_btn, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        sizer_10.Add(self.adv_quit_btn, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        sizer_6.Add(sizer_10, 1, wx.ALIGN_RIGHT, 0)
        sizer_5.Add(sizer_6, 10, 0, 0)
        self.notebook_1_pane_2.SetSizer(sizer_5)
        self.notebook_1.AddPage(self.notebook_1_pane, "Single Search")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "Multi Search")
        sizer_4.Add(self.notebook_1, 17, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        self.Centre()
        # end wxGlade
        
        # And indicate we don't have a worker thread yet
        self.worker = None
    
    def open_file(self, event): # wxGlade: MyApp.<event_handler>
        
        self.dialog = wx.FileDialog (None, style=wx.OPEN)
        
        if self.dialog.ShowModal() == wx.ID_OK:
           self.input_txt.SetValue(self.dialog.GetPath())
        else:
            self.dialog.Destroy()


    def save_file(self, event): # wxGlade: MyApp.<event_handler>
        
        self.dialog = wx.FileDialog (None, style=wx.SAVE)
        if self.dialog.ShowModal() == wx.ID_OK:
           self.save_txt.SetValue(self.dialog.GetPath())
        else:
           self.dialog.Destroy()


    def adv_search(self, event): # wxGlade: MyApp.<event_handler>
        
        return

    def get_tld(self, event): # wxGlade: MyApp.<event_handler>
        
        return
    
    def single_search(self, event): # wxGlade: MyApp.<event_handler>
       
        self.domain = self.single_txt.GetValue()
        self.single_txt_area.Clear()
        self.type = CONST.SINGLE_TYPE
        
        if len(self.domain) == 0:
             wx.MessageBox('Please Enter a Domain Name', 'Error', wx.OK | wx.ICON_ERROR)
        
        if not self.worker and len(self.domain) != 0:
            self.worker = WorkerThread(self.type,self.domain,self.single_txt_area)
         
        self.worker = None

    def multi_search(self, event): # wxGlade: MyApp.<event_handler>
        
        self.wordlist = self.input_txt.GetValue()
        self.domainlist = self.save_txt.GetValue()
        self.tld = self.tld_combo.GetValue()
        self.adv_txt_area.Clear()
        self.adv_txt_area.AppendText("Performing a multi domain search\n\n")
        
        if len(self.domainlist) == 0:
            tmp_dir = tempfile.gettempdir()
            self.domainlist = tmp_dir+"/mwhois_output.txt"
            
        if len(self.wordlist) == 0:
            wx.MessageBox('Please Enter Files', 'Error', wx.OK | wx.ICON_ERROR)
        else:
            
            self.domain_array = ([self.tld, self.wordlist, self.domainlist])
            
            if self.adv_chkbox.GetValue() == True:
                self.type = CONST.ADV_TYPE
            else:
                self.type = CONST.BASIC_TYPE
            if not self.worker:
                self.worker = WorkerThread(self.type,self.domain_array,self.adv_txt_area)
        
            self.worker = None


    def close_app(self, event): # wxGlade: MyApp.<event_handler> 
        
        #print "Closing App"
        wx.Window.Close(self, force=False)
        #self.worker.abort
        
    def about_diag(self, event): # wxGlade: MyApp.<event_handler>
        about = wx.PySimpleApp(0)
        about_frame = AboutDialog(None, -1, "")
        #app.SetTopWindow(about_frame)
        about_frame.Show()
        about.MainLoop()

# end of class MyApp

class StartGUI():
        
    def main(self):
        try:
            app = wx.PySimpleApp(0)
            wx.InitAllImageHandlers()
            mwhois_frame = MyApp(None, -1, "")
            app.SetTopWindow(mwhois_frame)
            mwhois_frame.Show()
            app.MainLoop()
        except Exception, e:
            print e
            
if __name__ == "__main__":
        StartGUI().main()