def alphabet_position(letter):
  x=ord(letter)
  if x<97:
    x-=65
  else:
    x-=97
  return x

def rotate_character(char, rot):
  x=ord(char)
  y=(alphabet_position(char)+rot)%26
  if 65<=x<=90:
    new=chr(y+65)
  elif 97<=x<=122:
    new=chr(y+97)
  else:
    new=char
  return new

def rotate_string(text,rot):
  new_string = ''
  for i in text:
    new_string+=rotate_character(i, rot)
  return new_string

def main():
  l=input("Phrase?")
  r=int(input('Number?'))
  print(rotate_string(l, r))

if __name__ == "__main__":
    main()