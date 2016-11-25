__author__ = ["Artur Gomes", "github.com/arturgoms"]
import gi
gi.require_version('WebKit2', '4.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from gi.repository import WebKit2
from threading import Thread
from Flask.run import *
Gtk.rc_parse_string("""style "hide-scrollbar-style"
{
  GtkScrollbar::slider_width = 0
  GtkScrollbar::min-slider-length = 0
  GtkScrollbar::activate_slider = 0
  GtkScrollbar::trough_border = 0
  GtkScrollbar::has-forward-stepper = 0
  GtkScrollbar::has-backward-stepper = 0
  GtkScrollbar::stepper_size = 0
  GtkScrollbar::stepper_spacing = 0
  GtkScrollbar::trough-side-details = 0
  GtkScrollbar::default_border = { 0, 0, 0, 0 }
  GtkScrollbar::default_outside_border = { 0, 0, 0, 0 }
  GtkScrolledWindow::scrollbar-spacing = 0
  GtkScrolledWindow::scrollbar-within-bevel = False
}
widget_class "*Scrollbar" style "hide-scrollbar-style"
widget_class "*ScrolledWindow" style "hide-scrollbar-style"
""")

class  ReloadView:
    def __init__(self):
        window = Gtk.Window()
        window.set_size_request(648, 432)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_decorated(False)
        window.set_resizable(False)
        window.set_icon_from_file('/home/arturgomes/Documents/CHIP-Project/img/logo2.png')
        self.view = WebKit2.WebView()
        self.view.load_uri('http://0.0.0.0:8080')

        window.add(self.view)
        window.show_all()
if __name__ == "__main__":
    ReloadView()
    Gtk.main()

