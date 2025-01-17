import sys; args = sys.argv[1:]
idx = int(args[0])-70

myRegexLst = [
  r"/^(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u)[a-z]*$/m",
  r"/^(?=(.*[aeiou]){5})(?!(.*[aeiou]){6})[a-z]*$/m",
  r"/^(?=.*[^aeiouy\W]w[^aeiouy]($|[^aeiouy]))[a-z]*$/m",
  r"/^(?=([a-z]?)(.)(\w))[a-z]*\3\2\1$|^a$/m",
  r"/^(?!.*(b|t).*\1.*)[a-z]*(tb|bt)[a-z]*$/m",
  r"/^([a-z])*\1\w*$/m",
  r"/([a-z])*(.*\1){2}\w*/m",
  r"//",
  r"/^([a-z]*[^aieou\W]){13}\w*$/m",
  r"/^(?!(.)*.*\1.*\1)[a-z]*$/m",
  ] 

if idx < len(myRegexLst):
  print(myRegexLst[idx])
# Find all words ...
# 70: ... where each vowel occurs at least once
# 71: ... containing exactly 5 vowels
# 72: ... with w acting as vowel
# 73: ... where if all but the first 3 and last 3 letters are removed, a palindrome results
# 74: ... where there is exactly one b and one t, and they are adjacent to each other
# 75: ... with the longest contiguous block of one letter
# 76: ... with the greatest number of a repeated letter
# 77: ... with the greatest number of adjacent pairs of identical letters
# 78: ... with the greatest number of consonants
# 79: ... where no letter is repeated more than once
# brian zhou, period 4, 2024