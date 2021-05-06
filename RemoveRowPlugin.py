import PyPluMA

class RemoveRowPlugin:
   def input(self, filename):
      #self.myfile = filename
      txtfile = open(filename, 'r')
      parameters = dict()
      for line in txtfile:
         contents = line.split('\t')
         parameters[contents[0]] = contents[1].strip()
      filestuff = open(PyPluMA.prefix()+"/"+parameters['inputfile'], 'r')
      self.lines = []
      for line in filestuff:
         self.lines.append(line)
      self.row = int(parameters['row'])

   def run(self):
      pass

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      for i in range(0, self.row-1):
         filestuff2.write(self.lines[i])

      for i in range(self.row, len(self.lines)):
         filestuff2.write(self.lines[i])


