#MenuTitle: Compound glyphs with different weight
# -*- coding: utf-8 -*-
__doc__="""
Based con mekablue's "New Edit tab with compound glyphs". Opens a new Edit tab with all glyphs which contain the currently selected glyphs as a component and also have different weight
"""

import GlyphsApp

Doc = Glyphs.currentDocument
Font = Glyphs.font
FontMaster = Font.selectedFontMaster
selectedLayers = Font.selectedLayers

editString = ""
Output = ""

for thisLayer in selectedLayers:
	thisGlyphName = thisLayer.parent.name
	compoundList = [ g.name for g in Font.glyphs if thisGlyphName in [ c.componentName for c in g.layers[ FontMaster.id ].components ] and g.layers[ FontMaster.id ].width != thisLayer.width ]
	if len(compoundList) > 1 :
		Output += "Compounds with %s: " % thisGlyphName + " ".join( compoundList ) + "\n"
		editString += "\n/" + thisGlyphName + "/space/" + "/".join( compoundList )
	else :
		Output += "No compound glyphs with %s and different weight" % thisGlyphName + "\n"

editString = editString.lstrip()
print Output

Doc.windowController().performSelectorOnMainThread_withObject_waitUntilDone_( "addTabWithString:", editString, True ) 
