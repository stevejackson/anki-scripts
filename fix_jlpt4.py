#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
    # found deck by doing str(mw.col.decks.all())
    #cards = showInfo("card count: %d" % mw.col.db.scalar("select count() from cards where did=1426817704383"))
    cardIds = mw.col.findCards("\"deck:Japanese::JLPT::JLPT N4 Vocab\"")
    showInfo("Card count: %d" % len(cardIds))

    for cardId in cardIds:
    	card = mw.col.getCard(cardId)

    	note = card.note()

    	starters = ['-', '(', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
    			    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    			    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    			    'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    			    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
    			    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    			    '~']

    	for (name, value) in note.items():
    		if name == 'Reading':
		    	reading = value

		    	hitEnglish = False
		    	hitEnglishPoint = 0
		    	index = 0
		    	for character in reading:
		    		if character in starters:
		    			hitEnglishPoint = index
		    			break
		    		index += 1

		    	# we've now found the beginning of hte pronunciation
		    	# get it
		    	meaning = reading[hitEnglishPoint:]
		    	reading = reading[0:hitEnglishPoint]

		    	# showInfo("--")
		    	# showInfo("Original: `%s`" % value)
		    	# showInfo("Reading: `%s`" % reading)
		    	# showInfo("Meaning: `%s`" % meaning)

		    	note["Meaning"] = meaning
		    	note["Reading"] = reading[0:hitEnglishPoint]

		note.flush()

    showInfo("Completed.")

    #showInfo("Removing newlines from expression column.")
    # query = """
    # 		update cards
    # 		set expression = REPLACE(expression, '\n', '')
    # 		where did = 1426817704383
    # 		"""
    #mw.col.db.execute(query)

# create a new menu item, "test"
action = QAction("Fix JLPT N4", mw)
# set it to call testFunction when it's clicked
mw.connect(action, SIGNAL("triggered()"), testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
