from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self, color):

        self.depth  = 3
        if color == "Green":
            colorRGB = '0 1.0 0 1.0'
        else:
            colorRGB = '0 1.0 1.0 1.0'
        
        self.string1 = '<material name="'+color+'">'

        self.string2 = '    <color rgba="'+colorRGB+'"/>'

        self.string3 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
