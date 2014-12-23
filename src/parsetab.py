
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'O(\xc8\xbb\xed\x96*\x0b;\xf5\xfd\xbfU`~d'
    
_lr_action_items = {'ITALICOPEN':([0,3,4,5,6,7,9,10,12,13,18,20,21,22,23,25,26,27,29,31,32,33,],[-14,-5,-6,-18,-4,-7,-8,17,-3,-14,-14,-10,-12,-11,-13,-15,-16,-17,17,-20,-19,-21,]),'STRONGOPEN':([0,3,4,5,6,7,9,10,12,13,18,20,21,22,23,25,26,27,29,31,32,33,],[-14,-5,-6,-18,-4,-7,-8,18,-3,-14,-14,-10,-12,-11,-13,-15,-16,-17,18,-20,-19,-21,]),'STRONGCLOSE':([18,20,21,22,23,29,31,32,33,],[-14,-10,-12,-11,-13,32,-20,-19,-21,]),'ITALICCLOSE':([28,],[31,]),'HR':([0,3,4,5,6,7,9,10,12,13,20,21,22,23,25,26,27,31,32,33,],[5,-5,-6,-18,-4,-7,-8,-9,-3,5,-10,-12,-11,-13,-15,-16,-17,-20,-19,-21,]),'H3OPEN':([0,3,4,5,6,7,9,10,12,13,20,21,22,23,25,26,27,31,32,33,],[8,-5,-6,-18,-4,-7,-8,-9,-3,8,-10,-12,-11,-13,-15,-16,-17,-20,-19,-21,]),'H1OPEN':([0,3,4,5,6,7,9,10,12,13,20,21,22,23,25,26,27,31,32,33,],[1,-5,-6,-18,-4,-7,-8,-9,-3,1,-10,-12,-11,-13,-15,-16,-17,-20,-19,-21,]),'H2OPEN':([0,3,4,5,6,7,9,10,12,13,20,21,22,23,25,26,27,31,32,33,],[2,-5,-6,-18,-4,-7,-8,-9,-3,2,-10,-12,-11,-13,-15,-16,-17,-20,-19,-21,]),'H1CLOSE':([14,],[25,]),'H3CLOSE':([16,],[27,]),'ICCLOSE':([30,],[33,]),'ICOPEN':([0,3,4,5,6,7,9,10,12,13,18,20,21,22,23,25,26,27,29,31,32,33,],[-14,-5,-6,-18,-4,-7,-8,19,-3,-14,-14,-10,-12,-11,-13,-15,-16,-17,19,-20,-19,-21,]),'PLAIN':([0,1,2,3,4,5,6,7,8,9,10,12,13,17,18,19,20,21,22,23,25,26,27,29,31,32,33,],[-14,14,15,-5,-6,-18,-4,-7,16,-8,20,-3,-14,28,-14,30,-10,-12,-11,-13,-15,-16,-17,20,-20,-19,-21,]),'H2CLOSE':([15,],[26,]),'BLOCKDIV':([0,3,4,5,6,7,9,10,12,13,20,21,22,23,25,26,27,31,32,33,],[12,-5,-6,-18,-4,-7,-8,-9,-3,12,-10,-12,-11,-13,-15,-16,-17,-20,-19,-21,]),'$end':([0,3,4,5,6,7,9,10,11,12,13,20,21,22,23,24,25,26,27,31,32,33,],[-2,-5,-6,-18,-4,-7,-8,-9,0,-3,-2,-10,-12,-11,-13,-1,-15,-16,-17,-20,-19,-21,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'h2':([0,13,],[3,3,]),'h3':([0,13,],[4,4,]),'h1':([0,13,],[6,6,]),'hr':([0,13,],[7,7,]),'paragraph':([0,13,],[9,9,]),'italic':([10,29,],[21,21,]),'inline':([0,13,18,],[10,10,29,]),'article':([0,13,],[11,24,]),'strong':([10,29,],[22,22,]),'inline-code':([10,29,],[23,23,]),'block':([0,13,],[13,13,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> article","S'",1,None,None,None),
  ('article -> block article','article',2,'p_article_block','/Users/leapoahead/Code/cp-project/src/parser.py',11),
  ('article -> <empty>','article',0,'p_article_empty','/Users/leapoahead/Code/cp-project/src/parser.py',15),
  ('block -> BLOCKDIV','block',1,'p_block','/Users/leapoahead/Code/cp-project/src/parser.py',25),
  ('block -> h1','block',1,'p_block','/Users/leapoahead/Code/cp-project/src/parser.py',26),
  ('block -> h2','block',1,'p_block','/Users/leapoahead/Code/cp-project/src/parser.py',27),
  ('block -> h3','block',1,'p_block','/Users/leapoahead/Code/cp-project/src/parser.py',28),
  ('block -> hr','block',1,'p_block','/Users/leapoahead/Code/cp-project/src/parser.py',29),
  ('block -> paragraph','block',1,'p_block','/Users/leapoahead/Code/cp-project/src/parser.py',30),
  ('paragraph -> inline','paragraph',1,'p_paragraph','/Users/leapoahead/Code/cp-project/src/parser.py',39),
  ('inline -> inline PLAIN','inline',2,'p_inline','/Users/leapoahead/Code/cp-project/src/parser.py',48),
  ('inline -> inline strong','inline',2,'p_inline','/Users/leapoahead/Code/cp-project/src/parser.py',49),
  ('inline -> inline italic','inline',2,'p_inline','/Users/leapoahead/Code/cp-project/src/parser.py',50),
  ('inline -> inline inline-code','inline',2,'p_inline','/Users/leapoahead/Code/cp-project/src/parser.py',51),
  ('inline -> <empty>','inline',0,'p_inline_empty','/Users/leapoahead/Code/cp-project/src/parser.py',57),
  ('h1 -> H1OPEN PLAIN H1CLOSE','h1',3,'p_h1','/Users/leapoahead/Code/cp-project/src/parser.py',65),
  ('h2 -> H2OPEN PLAIN H2CLOSE','h2',3,'p_h2','/Users/leapoahead/Code/cp-project/src/parser.py',72),
  ('h3 -> H3OPEN PLAIN H3CLOSE','h3',3,'p_h3','/Users/leapoahead/Code/cp-project/src/parser.py',79),
  ('hr -> HR','hr',1,'p_hr','/Users/leapoahead/Code/cp-project/src/parser.py',86),
  ('strong -> STRONGOPEN inline STRONGCLOSE','strong',3,'p_strong','/Users/leapoahead/Code/cp-project/src/parser.py',93),
  ('italic -> ITALICOPEN PLAIN ITALICCLOSE','italic',3,'p_italic','/Users/leapoahead/Code/cp-project/src/parser.py',100),
  ('inline-code -> ICOPEN PLAIN ICCLOSE','inline-code',3,'p_inline_code','/Users/leapoahead/Code/cp-project/src/parser.py',107),
]
