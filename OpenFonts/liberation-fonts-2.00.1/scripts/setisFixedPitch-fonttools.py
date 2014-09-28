#!/usr/bin/env python
#
# setisFixedPitch-fonttools.py
#
# Copyright (c) 2012 Pravin Satpute <psatpute@redhat.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# This program takes a TTF font and set isFixedPitch bit used to detect font as a Monospace.
#
# This script depends on fontTools Python library, available
# in most packaging systems and sf.net/projects/fonttools/
#
# Usage:
#
# $ ./setisFixedPitch-fonttools.py FontIn.ttf
# input font will be overwriten and backup will be created for input font

# Import our system library and fontTools ttLib
import os, sys
from fontTools import ttLib
from fontTools.ttLib.tables import ttProgram

for i in range(1, len(sys.argv)):
# Open the font file supplied as the first argument on the command line
	fontfile = sys.argv[i]
	print fontfile
	font = ttLib.TTFont(fontfile)

# Print the Post table
	if font.has_key('post'):
		if font["post"].isFixedPitch == 0:
			font["post"].isFixedPitch = 1
	        print "isFixedPitch is now: ", font["post"].isFixedPitch
	else:
	  print "Post table not found"

# Save the new file with the name of the input file
	newfont = fontfile[0:-4] + '-fixed' + fontfile[-4:]
	font.save(newfont)
	print newfont, "saved."

#os.system("mv" + " "  + "src/LiberationMono-Regular-fixed.ttf" + " " + "src/LiberationMono-Regular.ttf")
#os.system("mv" + " "  + "src/LiberationMono-Italic-fixed.ttf" + " " + "src/LiberationMono-Italic.ttf")
#os.system("mv" + " "  + "src/LiberationMono-Bold-fixed.ttf" + " " + "src/LiberationMono-Bold.ttf")
#os.system("mv" + " "  + "src/LiberationMono-BoldItalic-fixed.ttf" + " " + "src/LiberationMono-BoldItalic.ttf")

#os.system("mv" + " "  + "export/LiberationMono-Regular-fixed.ttf" + " " + "export/LiberationMono-Regular.ttf")
#os.system("mv" + " "  + "export/LiberationMono-Italic-fixed.ttf" + " " + "export/LiberationMono-Italic.ttf")
#os.system("mv" + " "  + "export/LiberationMono-Bold-fixed.ttf" + " " + "export/LiberationMono-Bold.ttf")
#os.system("mv" + " "  + "export/LiberationMono-BoldItalic-fixed.ttf" + " " + "export/LiberationMono-BoldItalic.ttf")
