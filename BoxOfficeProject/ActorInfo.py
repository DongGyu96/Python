
class Actor():
    def __init__(self, code, name, field):
        self.Code = code            # 코드
        self.Name = name            # 이름
        self.Field = field          # 분야

    def GetCode(self):
        return self.Code


    def GetName(self):
        return self.Name

    def SetName(self, cnt):
        self.Name = self.Name + str(cnt)

    def GetField(self):
        return self.Field


class ActorManager():
    def __init__(self):
        self.ActorList = []
        self.index = 0

    def SetActor(self, actor):#
        #for i in self.ActorList:
        #    if actor.GetName() == i.GetName():
        #        i = self.GetSameNameCnt(actor.GetName())
        #        actor.SetName(i)

        self.ActorList.insert(self.index, actor)
        self.index += 1


    def FindCodeFromName(self, name):
        #if name.isdigit:
        #    i = len(name)
        #    cut = name[i - 1]
        #    old = name
        #    print(old)
#
        #    name = old.replace(cut, "")
        #    print(name)

        for actor in self.ActorList:
            if name == actor.GetName():
                return actor.GetCode()

            else:
                return None

    def FindNameFromCode(self, code):
        for actor in self.ActorList:
            if code == actor.GetCode():
                return actor.GetName()

            else:
                return None


    def GetSameNameCnt(self, name):
        cnt = 0
        for actor in self.ActorList:
            if name == actor.GetName():
                cnt += 1

        return cnt

    def FindCodeFromIndex(self, index):
        code = self.ActorList[index].GetCode()
        print(code)
        return code


    def Clear(self):
        self.ActorList.clear()
        self.index = 0