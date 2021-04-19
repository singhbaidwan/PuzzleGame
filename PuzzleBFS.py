import copy
class PuzzleGame:
    def __init__(self,st,gl):
        self.start = st
        self.goal = gl
        for i in range(0,3):
            for j in range(0,3):
                if st[i][j]==0:
                    self.i = i
                    self.j = j
    def displayPuzzle(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.start[i][j]),
            print("")
        print("- - - - - - - - - - - - -")
    def isGoal(self):
        if self.start==self.goal:
            return True
        return False
    def upMovement(self):
        if self.i>0:
            self.start[self.i][self.j] = self.start[self.i-1][self.j]
            self.start[self.i-1][self.j]=0
            self.i = self.i-1
            self.j=self.j
            return True
        else:
            return False
    def downMovement(self):
        if self.i<2:
            self.start[self.i][self.j] = self.start[self.i+1][self.j]
            self.start[self.i+1][self.j] = 0
            self.i = self.i+1
            self.j = self.j
            return True
        else:
            return False
    def rightMovement(self):
        if self.j<2:
            self.start[self.i][self.j] = self.start[self.i][self.j+1]
            self.start[self.i][self.j+1] = 0
            self.i = self.i
            self.j = self.j+1
            return True
        else:
            return False
    def leftMovement(self):
        if self.j>0:
            self.start[self.i][self.j] = self.start[self.i][self.j-1]
            self.start[self.i][self.j-1] = 0
            self.i = self.i
            self.j = self.j-1
            return True
        else:
            return False
def checker(start,closed):
    if start in closed:
        return False
    else:
        return True
def BFS(start):
    closed=[]
    openList=[]
    print("Starting :-")
    start.displayPuzzle()
    openList.append(start)
    depth = 1
    while len(openList)!=0:
        v = openList.pop(0)
        closed.append(v.start)
        if v.isGoal():
            print("Goal Reached")
            v.displayPuzzle()
            print("Length of Open list is ",len(openList))
            print("Length of Closed List is",len(closed))
            break
        mv = copy.deepcopy(v)
        if mv.upMovement() and checker(mv.start,closed):
            openList.append(mv)
        mv = copy.deepcopy(v)
        if mv.leftMovement() and checker(mv.start,closed):
            openList.append(mv)
        mv = copy.deepcopy(v)
        if mv.rightMovement() and checker(mv.start,closed):
            openList.append(mv)
        mv = copy.deepcopy(v)
        if mv.downMovement() and checker(mv.start,closed):
            openList.append(mv)
        print("Content of Open list at depth = {}".format(depth))
        for x in openList:
            x.displayPuzzle()
        depth=depth+1      

if __name__=="__main__":
    print("Enter start ")
    start = []
    for i in range(0,3):
        a=[]
        for j in range(0,3):
            a.append(int(input()))
        start.append(a)
    goal = []
    print("Enter the Goal")
    for i in range(0,3):
        a=[]
        for j in range(0,3):
            a.append(int(input()))
        goal.append(a)
    
    ply = PuzzleGame(start,goal)
    BFS(ply)