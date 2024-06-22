Mistakes
1) Optional was not imported.
2) The condition check to insert right child was wrong. <= was the written condition. 
3) The flow that should have been passed to the right child if there was already a right child was given wrong, left child was written instead of right child. 
4) The condition check to insert left child was wrong. >= was the written condition.
5) There wasn't a case evaluating to the failed insertion case.

Changes
1) Imported 'Optional' from 'typing' module
2) Changed <= to >=
3) Changed left child to right child
4) Changed >= to <=
5) Added a return for the failed case.
