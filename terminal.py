command  = [""]
directory= {
  "website": [["Projects", "Experience", "Contact_Info"], ["root"]],
  "root": [["website"], ["root"]],
  "Projects": [["p1", "p2", "p3"], ["website"]],
  "p1": [[], ["Projects"]],
  "p2": [[], ["Projects"]],
  "p3": [[], ["Projects"]],
  "Experience": [["e1", "e2", "e3"], ["website"]],
  "e1": [[], ["Experience"]],
  "e2": [[], ["Experience"]],
  "e2": [[], ["Experience"]],
  "Contact_Info": [[], ["website"]]
}
currentDirectory = "website"

while command[0] != "exit":
  command = input(f"(base) aryavenkatesan@MacBook-Air {currentDirectory} % ").split(" ")
  if command[0] == "cd":
    if command[1] in directory[currentDirectory][0]:
      currentDirectory = command[1]
    elif command[1] == "..":
      currentDirectory = directory[currentDirectory][1][0]
    else:
      print("Directory not found")
  elif command[0] == "ls":
    if len(directory[currentDirectory][0]) > 0:
      for str in directory[currentDirectory][0]:
        print(str, end="\t")
      print("\n")
    else:
      print("\n")
  elif command[0] == "pwd":
    d = currentDirectory
    pwd = currentDirectory
    while d != "root":
      d = directory[d][1][0]
      pwd = f"{d}/{pwd}"
    print(pwd)
  elif command[0] == "mkdir":
    print(f"{command[0]}: Command not supported")
  elif command[0] == "vi":
    print(f"{command[0]}: Command not supported")
  elif command[0] == "vim":
    print(f"{command[0]}: Command not supported")
  elif command[0] == "touch":
    print(f"{command[0]}: Command not supported")
  elif command[0] == "exit":
    break
  else:
    print("Command not recognized")
