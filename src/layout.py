import os, random

from game import Grid
from util import manhattanDistance

vismatcache = {} # a cache of the visibility matrix

class Layout:
    """
    A Layout manages the static information about the game board.
    """
    def __init__(self, layoutText):
        """
        Initialize the layout display the user has chosen.
        """
        self.width = len(layoutText[0])
        self.height= len(layoutText)
        self.walls = Grid(self.width, self.height, False)
        self.food = Grid(self.width, self.height, False)
        self.capsules = []
        self.agentPositions = []
        self.numGhosts = 0
        self.processLayoutText(layoutText)
        self.layoutText = layoutText
        # self.initializeVisibilityMatrix()
      
    def getNumGhosts(self):
        """
        Return the number of ghosts.
        """
        return self.numGhosts
      
    def initializeVisibilityMatrix(self):
        """
        Create the visibility matrix of what"s on the display.
        """
        global vismatcache
        if reduce(str.__add__, self.layoutText) not in vismatcache:
            from game import Directions
            vecs = [(-0.5,0), (0.5,0),(0,-0.5),(0,0.5)]
            dirs = [Directions.NORTH, Directions.SOUTH, Directions.WEST, Directions.EAST]
            vis = Grid(self.width, self.height, {Directions.NORTH:set(), Directions.SOUTH:set(), Directions.EAST:set(), Directions.WEST:set(), Directions.STOP:set()})
            for x in range(self.width):
                for y in range(self.height):
                    if self.walls[x][y] == False:
                        for vec, direction in zip(vecs, dirs):
                            dx, dy = vec
                            nextx, nexty = x + dx, y + dy
                            while (nextx + nexty) != int(nextx) + int(nexty) or not self.walls[int(nextx)][int(nexty)] :
                                vis[x][y][direction].add((nextx, nexty))
                                nextx, nexty = x + dx, y + dy
                self.visibility = vis      
                vismatcache[reduce(str.__add__, self.layoutText)] = vis
        else:
            self.visibility = vismatcache[reduce(str.__add__, self.layoutText)]
        
    def isWall(self, pos):
        """
        Check if there"s a wall.
        """
        x, col = pos
        return self.walls[x][col]
    
    def getRandomLegalPosition(self):
        """
        From possible positions, generate a random position and check
        if it's legal.
        """
        x = random.choice(range(self.width))
        y = random.choice(range(self.height))
        while self.isWall( (x, y) ):
            x = random.choice(range(self.width))
            y = random.choice(range(self.height))
        return (x,y)
  
    def getRandomCorner(self):
        poses = [(1,1), (1, self.height - 2), (self.width - 2, 1), (self.width - 2, self.height - 2)]
        return random.choice(poses)
  
    def getFurthestCorner(self, pacPos):
        poses = [(1,1), (1, self.height - 2), (self.width - 2, 1), (self.width - 2, self.height - 2)]
        dist, pos = max([(manhattanDistance(p, pacPos), p) for p in poses])
        return pos
    
    def isVisibleFrom(self, ghostPos, pacPos, pacDirection):
        row, col = [int(x) for x in pacPos]
        return ghostPos in self.visibility[row][col][pacDirection]
    
    def __str__(self):
        return "\n".join(self.layoutText)
      
    def deepCopy(self):
        return Layout(self.layoutText[:])
      
    def processLayoutText(self, layoutText):
        """
        Coordinates are flipped from the input format to the (x,y) convention here
      
        The shape of the maze.  Each character  
        represents a different type of object.   
         % - Wall                               
         . - Food
         o - Capsule
         G - Ghost
         P - Pacman
        Other characters are ignored.
        """
        maxY = self.height - 1
        for y in range(self.height):       
            for x in range(self.width):
                layoutChar = layoutText[maxY - y][x]  
                self.processLayoutChar(x, y, layoutChar)
        self.agentPositions.sort()
        self.agentPositions = [ ( i == 0, pos) for i, pos in self.agentPositions]
    
    def processLayoutChar(self, x, y, layoutChar):
        """
        Process the layout based on the string of characters.
        """
        if layoutChar == "%":      
            self.walls[x][y] = True
        elif layoutChar == ".":
            self.food[x][y] = True 
        elif layoutChar == "o":    
            self.capsules.append((x, y))   
        elif layoutChar == "P":    
            self.agentPositions.append( (0, (x, y) ) )
        elif layoutChar in ["G"]:    
            self.agentPositions.append( (1, (x, y) ) )
            self.numGhosts += 1
        elif layoutChar in  ["1", "2", "3", "4"]:
            self.agentPositions.append( (int(layoutChar), (x,y)))
            self.numGhosts += 1 

def getLayout(name, back = 2):
    """
    Get the layout file itself.
    """
    if name.endswith(".lay"):
        layout = tryToLoad("layouts/" + name)
        if layout == None: layout = tryToLoad(name)
    else:
        layout = tryToLoad("layouts/" + name + ".lay")
        if layout == None: layout = tryToLoad(name + ".lay")
    if layout == None and back >= 0:
        curdir = os.path.abspath(".")
        os.chdir("..")
        layout = getLayout(name, back -1)
        os.chdir(curdir)
    return layout

def tryToLoad(fullname):
    """
    See if the layout file loads.
    """
    if(not os.path.exists(fullname)): return None
    return Layout([line.strip() for line in open(fullname)])
