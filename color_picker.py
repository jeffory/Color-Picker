import sublime, sublime_plugin
import subprocess, os
import _winreg as winreg

class ShowColorPickerCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		color_picker_dir = sublime.packages_path() + '\\Color Picker'
		
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		
		process = subprocess.Popen(['powershell.exe', '-NonInteractive', '-noprofile', '-file', color_picker_dir + '\\getcolor.ps1'], shell=False, stdout=subprocess.PIPE, startupinfo=startupinfo)
		process.poll()
		output = process.communicate()[0]

		if output:
			for region in self.view.sel():
				self.view.insert(edit, region.begin(), output.strip())
		
		return