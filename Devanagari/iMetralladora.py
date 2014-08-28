#MenuTitle: iMetralladora
# -*- coding: utf-8 -*-
__doc__="""
Combine selected glyphs in a new Tab with all iMatra relatives characters. Useful for Devanagari fonts. Warning: maybe it would blow up your computer.
"""
import GlyphsApp
import re

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

imatras = [ l for l in Font.glyphs if re.search("iMatra-deva", l.name) ]

try:
	Glyphs.clearLog()
	# Glyphs.showMacroWindow()
except:
	pass

outputString = ''

Font.disableUpdateInterface()
for glyph in imatras:
	outputString += glyph.name + ': \n'

	for thisLayer in selectedLayers:
		matra = '/' + glyph.name
		thisGlyphName = '/' + thisLayer.parent.name
		outputString += matra + thisGlyphName +'\n'

	outputString += '\n'


Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", outputString, True )

Font.enableUpdateInterface()