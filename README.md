# Lab 5 Pseudocode

```markdown

sampX = empty list
sampY = empty list
sampZ = empty list

def collectData(samples)
  accelX = collection of data in x-direction

  for i in range of samples
    sampX.append(accelX)

  accelY = collection of data in y-direction

  for i in range of samples
    sampY.append(accelY)

  accelZ = collection of data in z-direction

  for i in range of samples
    sampZ.append(accelZ)

  AveX = sum of sampX / length of sampX
  AveY = sum of sampX / length of sampX
  AveZ = sum of sampX / length of sampX

  return the values of AveX, AveY, and AveZ

samples = interger value
call the function collectData(samples)
