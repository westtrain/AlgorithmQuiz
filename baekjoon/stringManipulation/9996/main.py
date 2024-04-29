total = int(input())
pattern = input().split('*')
result = []
for i in range(total):
    fileName = str(input())
    nameLen = len(fileName)
    firstPatternLen = len(pattern[0])
    lastPatternLen = len(pattern[1])
    if nameLen < lastPatternLen + firstPatternLen:
        result.append('NE')
    else:
      if pattern[0] == fileName[0:firstPatternLen]:
        if pattern[1] == fileName[-lastPatternLen:]:
          result.append('DA')
        else:
          result.append('NE')
      else:
        result.append('NE')
for answer in result:
  print(answer)


