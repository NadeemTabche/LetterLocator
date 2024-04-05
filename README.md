Players are given 10 random letters and asked to find the largest word they can make from those letters. Each letter can only be used once. The length of the word determines the number of points awarded. e.g. a word with 6 letters would mean 6 points are awarded.

The function validateAnswer takes in the randomletters as an array of letters and the player's answer as a string. It then checks if the word the player has entered only contains letters from the 10 random letters with each letter being used only once. (At this stage the program doesn't check if the answer provided is an actual word.) It then returns a score, out of 10, for a valid word or 0 for an invalid word.

Example
If the random letters are
OPXCMURETN
The word COMPUTER returns 8
Whereas
The word POST returns 0 (there is no S in the random letters).
And
The word RETURN returns 0 (there is only one R in the random letters).
