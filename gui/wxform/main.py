"""Subclass of MyFrame, which is generated by wxFormBuilder."""

import wx
import mwhois2
from controller import WorkerThread

# Implementing MyFrame
class MainGUI( mwhois2.MyFrame ):
	def __init__( self, parent ):
		mwhois2.MyFrame.__init__( self, parent )
	
	# Handlers for MyFrame events.
	def create_new_tab( self, event ):
		# TODO: Implement create_new_tab
		pass
	
	def do_save_results( self, event ):
		# TODO: Implement do_save_results
		pass
	
	def do_print_results( self, event ):
		# TODO: Implement do_print_results
		pass
	
	def close_app( self, event ):
		# TODO: Implement close_app
		pass
	
	def open_about_dialog( self, event ):
		# TODO: Implement open_about_dialog
		pass
	
	def set_preveiw_results( self, event ):
		# TODO: Implement set_preveiw_results
		pass
	
	def do_whois_search( self, event ):
		domain = self.m_textctrl_domain.GetValue()
		worker = WorkerThread(1, domain, self.m_textctrl_results)	
		pass
	
	def open_file_select( self, event ):
		# TODO: Implement open_file_select
		pass
	
	def set_dead_only( self, event ):
		# TODO: Implement set_dead_only
		pass
	
	def set_sleep( self, event ):
		# TODO: Implement set_sleep
		pass
	
	def do_multi_search( self, event ):
		# TODO: Implement do_multi_search
		pass
	
if __name__ == "__main__":
	app = wx.App(False)
	frame = MainGUI(None)
	frame.Show(True)
	app.MainLoop()	
