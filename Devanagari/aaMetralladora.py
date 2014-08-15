#MenuTitle: aaMetralladora
# -*- coding: utf-8 -*-
__doc__="""
Combine selected glyphs in a new Tab with 'aaMatra-deva' character. Useful for Devanagari fonts.
"""
import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
selectedLayers = Font.selectedLayers

outputString ="/aaMatra-deva"

for thisLayer in selectedLayers:
	thisGlyphName = thisLayer.parent.name
	outputString +='/'+thisGlyphName+'/aaMatra-deva'


Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", outputString, True )
