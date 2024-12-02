## guiGame() Function Pseudocode
```markdown
score = 0
humList = []
compList = []
colours = [yellow, blue,red, green]
waiting = False

func guiGame()
  global score, humList, compList, waiting

  screen fills with black
  call drawButtons()

  drawTitle(f"Score: {score}")
  update display

  if not waiting
    wait 1000 ms
    choose from random set of colours
    append that colour to the list

    for flashColour in compList:
      flash the colour by calling flashAnimation(flashColour)
      wait 300 ms
  waiting = True

  if waiting
    if the event is quit
      pygame will quit

    if the event is mouse button down
      if the collided point is red
        put red on the new list

    if the collided point is blue
        put blue on the new list

    if the collided point is yellow
        put yellow on the new list

    if clicked and humList and compList are the same
      score += 1
    else
      game over screen
