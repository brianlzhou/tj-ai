import sys; args = sys.argv[1:]
idx = int(args[0])-60

myRegexLst = [
  r"/^(?!.*010)[01]*$/", #16
  r"/^(?!.*010|.*101)[01]*$/", #22
  r"/^(0|1)([01]*\1)?$/", #17
  r"/(?!(\w)*\w*\1\b)\b\w+/i", #23
  r"/(\w)*(\w*\1(\w)*\3|(\w)*\w*(\4\w*\1|\1\w*\4))\w*/i", #54
  r"/\b(?=(\w)*(\w*\1){2})(?:\1*(\w)(?!\w*\3))+\b\w*/i", #47
  r"/(?!\w*([aeiou])\w*\1)(\w*[aeiou]){5}\w*/", #39
  r"/^(?=.(..)*\b)0*(10*10*)*$/", #25
  r"/^(0|(1(01*0)*10*)+)$/", #20
  r"/^(?!(0|1(01*0)*1)*$)1[01]*$/" #27
  ] 

if idx < len(myRegexLst):
  print(myRegexLst[idx])
# Q60: Match all binary strings that do not contain the forbidden substring 010.  (14)
# Q61: Match all binary strings containing neither 101 nor 010 as substrings.  (20)
# Q62: Match on all non-empty binary strings with the same number of 01 substrings as 10 substrings.  (14)
# Q63: Match all words whose final letter is not to be found elsewhere in the word.  (21)  
# Q64: Match all words that have at least two pairs of doubled letters (two pairs of distinct letters or four of the same letter are both OK).  (43)
# Q65: Match all words that have no duplicate letter, except for one, which occurs at least 3 times.  (42)
# Q66: Match all words where each of the five vowels occurs exactly once.  (39)
# Q67: Match all binary strings that have an odd number of 0s and an even number of 1s.  (22)
# Q68: Match all binary integer strings that are divisible by 3.  (19)
# Q69: Match all binary integer strings that are not divisible by 3.  (19)
# brian zhou, period 4, 2024