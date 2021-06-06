#!/usr/bin/python

import sys, getopt

example = 'modifier.py -f <inputfile> -z <zoom> -p <page where to insert> -o <prototype iframe>'
jquery_import = '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>'

def main(argv):
   inputfile = ''
   zoom = ''
   page_where_to_inject = ''
   prototype = ''
   try:
      opts, args = getopt.getopt(argv,"f:z:p:o:",["file=","zoom=","page_where_to_inject=","prototype="])
   except getopt.GetoptError:
      print(example)
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print(example)
         sys.exit()
      elif opt in ("-f", "--file"):
         inputfile = arg
      elif opt in ("-z", "--zoom"):
         zoom = arg
      elif opt in ("-p", "--page_where_to_inject"):
         page_where_to_inject = arg
      elif opt in ("-o", "--prototype"):
         prototype = arg
   print('Inputfile ', inputfile)
   print('Zoom ', zoom)
   print('Page ', page_where_to_inject)
   print('Prototype ', prototype)

   with open(inputfile, "r", encoding="utf8") as f:
      contents = f.readlines()
   with open("presentation_transformer_script.js", "r", encoding="utf8") as f:
       transformer = "".join(f.readlines())
       transformer = transformer.replace("%%zoom%%", zoom)
       transformer = transformer.replace("%%page_where_to_inject%%", page_where_to_inject)
       transformer = transformer.replace("%%prototype%%", "'" + prototype + "'")
   contents.insert(len(contents) - 2, jquery_import + "\n" + "<script>" + transformer + "</script>" + "\n")
   with open("new-" + inputfile, "w", encoding="utf8") as f:
       contents = "".join(contents)
       f.write(contents)

if __name__ == "__main__":
   main(sys.argv[1:])
