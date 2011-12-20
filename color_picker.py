import sublime, sublime_plugin
import subprocess, os
import _winreg as winreg

def is_valid_hex_color(s):
    if len(s) not in (3, 6):
        return False
    try:
        return 0 <= int(s, 16) <= 0xffffff
    except ValueError:
        return False

class ShowColorPickerCommand(sublime_plugin.TextCommand):
	def run(self,edit):
            view = self.view
            sel = view.sel()
            start_color = "#0"

            # get the currently selected color - if any
            if len(sel) > 0:
                selected = view.substr(view.word(sel[0])).strip()
                if selected.startswith('#'): selected = selected[1:]
                if is_valid_hex_color(selected):
                    start_color = "#"+selected

		color_picker_dir = sublime.packages_path() + '\\Color-Picker'

		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		
		process = subprocess.Popen(['powershell.exe', '-NonInteractive', '-noprofile', '-file', color_picker_dir + '\\getcolor.ps1', start_color], shell=False, stdout=subprocess.PIPE, startupinfo=startupinfo)
		process.poll()
		output = process.communicate()[0]

		if output:
			for region in self.view.sel():
				self.view.insert(edit, region.begin(), output.strip())
		
		return