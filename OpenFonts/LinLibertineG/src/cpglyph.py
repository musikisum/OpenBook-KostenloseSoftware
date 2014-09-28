import sys
import re
import fontforge
import psMat

# copy new characters and kerning corrections of Magyar Linux Libertine
# to the new version of Linux Libertine
# Usage: copychar.py source target new_file

if len(sys.argv) < 4:
	print "cpglyph - copy glyphs"
	print "Usage: copyglyph source_font target_font new_file glyph(s)"
	sys.exit(1)


font=fontforge.open(sys.argv[1])
font2=fontforge.open(sys.argv[2])
font.em = font2.em

# Add heavy asterisk (U+2731)

font2.selection.select("asterisk")
font2.copy()
font2.selection.select("uni2731")
font2.paste()
g = font2["uni2731"]
g.transform(psMat.scale(1/0.58))
g.transform(psMat.translate(font2.em*(font2.italicangle/100),-font2.em*0.6))

for i in sys.argv[4:]:
	print i	
	font.selection.select(i)
	font.copy()
	font2.selection.select(i)
	font2.paste()
	if i == "uniE0F7":
		font2[i].glyphname = "g_y"
 	elif i == "uniE0F8":
		font2[i].glyphname = "j.short"
 	elif i == "uniFB03":
		font2[i].glyphname = "f_f_i"


# fix a bad name in LinLibertine_It

if "LinLibertine_RI" in sys.argv[2] and 0x0359 in font2 and font2[0x0359].glyphname == "acute.cap":
	font2[0x0359].glyphname = "uni0359"

# create glyphs for hanging punctuation

font2.selection.select("hyphen")
font2.copy()
font2.selection.select("uniE130")
font2.paste()
g = font2["uniE130"]
hang = int(g.width*0.51)
g.width -= hang

codepoint = 57649 # U+E131

for i in [0.7, "hyphen", "period", "comma", "quoteleft", "quoteright", 0.5, "colon", "semicolon", "quotedblleft", "quotedblright", 0.3, "endash", 0.2, "emdash", "question", "exclam"]:
	if type(i) == type(0.1):
		hang = 1 - i
	else:
		font2.selection.select(i)
		font2.copy()
		font2.selection.select(codepoint)
		font2.paste()
		font2[codepoint].width = int(hang * font2[codepoint].width)
		codepoint += 1

for i in [0.7, "quoteleft", "quoteright", "quotesinglbase", 0.5, "quotedblleft", "quotedblright", "quotedblbase"]:
	if type(i) == type(0.1):
		hang = i
	else:
		font2.selection.select(i)
		font2.copy()
		font2.selection.select(codepoint)
		font2.paste()
		g = font2[codepoint]
		g.transform(psMat.translate(-int(hang * font2[codepoint].width),0))
		codepoint += 1

# correct A, O, U + dieresis in Biolinum Bold

if "LinLibertine_R." in sys.argv[2]:
	# fix width of double-stroke letters (Linux Libertine )
	a = ["A", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	b = [ "u1D538", "u1D539", "u1D53B", "u1D53C", "u1D53D", "u1D53E", "uni210D", "u1D540", "u1D541", "u1D542", "u1D543", "u1D544", "uni2115", "u1D546", "u1D547", "u1D54A", "u1D54B", "u1D54C", "u1D54D", "u1D54E", "u1D54F", "u1D550", "uni2124"]
	c = [ 100, 95, 40, 90, 85, 0, 95, 80, 85, 95, 90, 130, 132, 20, 60, 0, 90, 90, 90, 80, 130, 85, 120]
	# help(font2["A"])
	for i in range(0, len(a)):
		font2[b[i]].width = font2[a[i]].width + c[i]


if "LinLibertine_R" in sys.argv[2]:
	font2.selection.select(("ranges",None),"a.sc","z.sc")
#	font2.addSmallCaps(scheight=500, capheight=1000, lcstem=500, ucstem=500, hscale=1, vscale=1, stem_height_factor=1)
	font2.copy()
	font2.selection.select(("ranges",None),"uniE162","uniE17B")
	font2.paste()
	font2.selection.select(("ranges",None),"a.sc","z.sc")
	if "LinLibertine_R." in sys.argv[2]:
		for i in [["germandbls", 0xE17C], ["ae", 0xE1C6], ["oe", 0xE1C7], ["oslash", 0xE1C8], ["eth", 0xE1C9], ["thorn", 0xE1CA], ["dcroat", 0xE1CB], ["lcaron", 0xE1CC], ["lslash", 0xE1CD]]:
			try:		
				font2.selection.select(i[0] + ".sc")
				font2.copy()
				font2.selection.select(i[1])
				font2.paste()
				font2[i[1]].glyphname = i[0].capitalize().replace("German","german") + ".superior"
			except:
				print i, sys.argv[2]
		for i in range(0xE162, 0xE17D) + range(0xE1C6, 0xE1CE):
			g = font2[i]
#	g.layers[0].stemControl(1.3, 1.6)
			g.transform(psMat.scale(0.75, 0.75))
			g.transform(psMat.translate(0,font2.em*0.366))
	for i in [["dotlessi", 0xE17D, "dotlessi.superior"], ["dotlessj", 0xE1C5, "dotlessj.superior"]]:
		if "LinLibertine_R." in sys.argv[2]:
			font2[i[1]].glyphname = i[2]
		else:
			font2.selection.select(i[0])
			font2.copy()
			font2.selection.select(i[1])
			font2.paste()
			g = font2[i[1]]
			g.transform(psMat.scale(0.6, 0.6))
			g.transform(psMat.translate(0,font2.em*0.366))
			g.glyphname = i[2]
	for i in [["exclam",  0xE17E, "exclam.sups"], ["comma", 0xE17F, "comma.sups"], ["period", 0xE180, "period.sups"], ["colon", 0xE181, "colon.sups"], ["semicolon", 0xE182, "semicolon.sups"], ["question", 0xE183, "question.sups"], ["quotedblleft", 0xE184, "quotedblleft.sups"], ["quotedblright", 0xE185, "quotedblright.sups"], ["quotedblbase", 0xE186, "quotedblbase.sups"], ["quotedblrev", 0xE187, "quotedblrev.sups"], ["slash", 0xE18A, "slash.sups"], ["underscore", 0xE18B, "underscore.sups"], ["guillemotleft", 0xE18C, "guillemotleft.sups"], ["guillemotright", 0xE18D, "guillemotright.sups"], ["endash", 0xE18E, "endash.sups"], ["emdash", 0xE18F, "emdash.sups"], ["percent", 0xE190, "percent.sups"], ["ampersand", 0xE191, "ampersand.sups"], ["quoteleft", 0xE192, "quoteleft.sups"], ["quoteright", 0xE193, "quoteright.sups"], ["quotesinglbase", 0xE194, "quotesinglbase.sups"], ["hyphen", 0xE195, "hyphen.sups"]]:
		font2.selection.select(i[0])
		font2.copy()
		font2.selection.select(i[1])
		font2.paste()
		g = font2[i[1]]
		g.transform(psMat.scale(0.66, 0.6))
		g.transform(psMat.translate(0,font2.em*0.366))
		g.glyphname = i[2]
	# extend combining diacritics for sups
if "LinLibertine_R." in sys.argv[2]:
	for i in [["uni0308", 0xE0D9, "dieresis.sups", -0.05], ["uni030B", 0xE0DA, "hungarumlaut.sups", -0.024], ["grave.cap", 0xE0D5, "uniE0D5", 0.01], ["acute.cap", 0xE0D6, "uniE0D6", 0.01], ["dieresis.cap", 0xE0D7, "uniE0D7", 0.08], ["hungarumlaut.cap", 0xE0D8, "uniE0D8", 0.025], ["uni0326", 0xE0CD, "comma.sups", 0.025], ["uni0327", 0xE0CE, "cedilla.sups", 0.025], ["uni0328", 0xE0CF, "ogonek.sups", 0.025], ["brevecomb", 0xE0D1, "breve.sups", -0.02], ["uni0307", 0xE0D2, "dotaccent.sups", -0.02], ["uni030A", 0xE0D3, "ring.sups", -0.005], ["uni030C", 0xE0D4, "caron.sups", -0.001]]:
		font2.selection.select(("ranges",None),i[0],i[0])
		font2.copy()
		font2.selection.select(("ranges",None),i[1],i[1])
		font2.paste()
		g = font2[i[1]]
		g.transform(psMat.scale(0.65, 0.65))
#		if i[2] == "ring.sups":
#			g.transform(psMat.translate(font2.em*0.04 - 0.3,-font2.em*i[3]))
#		else:
		g.transform(psMat.translate(0, font2.em*0.366))
#		g.transform(psMat.translate(font2.em*0.04,-font2.em*i[3]))
		g.glyphname = i[2]

if "LinBiolinum_Bd" in sys.argv[2]:
#	font2.selection.select(("ranges",None),"A","Z")
#	font2.addSmallCaps(scheight=100, capheight=172, lcstem=100, ucstem=75)
#	font2.copy()
#	font2.selection.select(("ranges",None),"a.sc","z.sc")
#	font2.paste()
##	g = font2["A"]
###	g.layers[0].stemControl(1.3, 1.6)
##	g.transform(psMat.scale(0.75, 0.72))
##	font2.selection.select("A")
##	font2.copy()
##	font2.selection.select("a.sc")
##	font2.paste()
#	g.layers[0].stemControl(3)
#	g.transform(psMat.translate(font2.em*(font2.italicangle/100),-font2.em*0.6))
	for i in ["A", "O", "U"]:
		font2.selection.select("dieresis")
		w1 = font2["dieresis"].width
		font2.copy()
		font2.selection.select(i + "dieresis.alt")
		w2 = font2[i + "dieresis.alt"].width
		font2.paste()
		font2[i + "dieresis.alt"].transform(psMat.translate((w2-w1)/2,175))
		font2.selection.select(i)
		font2.copy()
		font2.selection.select(i + "dieresis.alt")
		font2.pasteInto()
	

font2.selection.all()
font2.unlinkReferences()
font2.removeOverlap()
font2.em = 2048
# instead of autoInstr, hint by ttfautohint
#font2.autoInstr()

fn = re.sub("^[^/]*/", "", sys.argv[2])
fn2 = sys.argv[3] + "/" + fn.replace(".sfd", ".ttf")
font2.generate(fn2, "old-kern")
