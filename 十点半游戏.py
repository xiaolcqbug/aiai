#游戏类
class Game:
    #一般游戏进程，从读取存档开始
    def Process(self):
        #初始回合数为0
        self.rounds = 0
        #初始Continue标记为True
        self.Continue = True
        #读取游戏
        self.Read(self)
        #当Continue标记为True时循环进行游戏
        while self.Continue:
            #创建一个玩家集合
            self.player_set = set()
            #初始化扑克牌
            self.Card.InitCard(self)
            #每轮的开始都将重置每名玩家的部分信息
            for i in range(self.player_amount):
                self.player_set.add(i)
                self.player_list[i].banker = False
                self.player_list[i].want = True
                self.player_list[i].inboom = True
                self.player_list[i].bet = 0
                #下面两句是加牌操作，每名玩家1张
                self.player_list[i].hand = [self.cards[0]]
                del self.cards[0]
            #进入叫庄环节
            self.Banker(self,self.player_amount,self.player_set)
    #游戏进程，从零开始
    def Start(self):
        #初始化扑克牌
        self.Card.InitCard(self)
        #初始化玩家
        self.PlayerInit(self)
    #牌点计算器，用于在创建扑克牌对象时提供每张牌的点数
    #输入参数：{牌号}
    def Calculate(rank):
        #字典，数据来源
        dictionary = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":0.5,"Q":0.5,"K":0.5}
        #约定点数并返回
        value = dictionary[rank]
        return value
    #玩家初始化
    def PlayerInit(self):
        while True:
            try:
                #输入玩家数量
                self.player_amount = int(input(">>>欢迎来到全新的十点半Lite！\n>>>请您设定玩家数量，最低2人，最高4人："))
                #当玩家数量正确时执行子程序
                if self.player_amount in (2,3,4):
                    self.__PlayerInit(self,self.player_amount)
                    break
                #否则提示错误
                else:
                    print("\n>>>不支持该数量的玩家哟，换个数试试吧！<<<")
            #输入非数字时报错
            except:
                print("\n>>>系统监测到了错误，但是系统不知道怎么解决")
    #玩家初始化子程序
    #输入参数：{玩家数量}
    def __PlayerInit(self,player_amount):
        #创建空列表，用于放置玩家名
        player_name = []
        print("\n>>>本局游戏共有{}名玩家~！<<<".format(self.player_amount))
        #输入玩家名并添加到列表
        for i in range(self.player_amount):
            player_name.append(input("您好，{}号玩家！\n-请输入您的大名：".format(i + 1)))
        #初始化游戏
        self.InitGame(self,player_name,self.player_amount,2)
    #初始化游戏，有三种初始化方法
    #输入参数：{玩家名称列表，玩家数量，初始化方式}
    def InitGame(self,player_name,player_amount,Action):
        #Action参数小于3时执行游戏初始化
        if Action < 3:
            #创建玩家列表，玩家集合
            self.player_list = []
            self.player_set = set()
            #给每位玩家添加初始数据
            for i in range(self.player_amount):
                self.player_list.append(self.Players(i,player_name[i],[self.cards[0]],False,True,True,0,100,0))
                self.player_set.add(i)
                #因为中间涉及到了发牌，所以要从牌堆删除发给玩家的牌
                del self.cards[0]
            #若Action等于2追加执行，进入叫庄环节
            if Action == 2:
                self.Banker(self,self.player_amount,self.player_set)
        #Action参数等于3时不进行初始化，直接进入叫庄环节（成功读取到游戏数据）
        if Action == 3:
            self.Banker(self,self.player_amount,self.player_set)
    #叫庄环节
    #输入参数：{玩家数量，玩家集合}
    def Banker(self,player_amount,player_set):
        #进入叫庄意味着游戏正式开始，回合数将加1
        self.rounds += 1
        while True:
            try:
                #输入庄家的玩家序号
                banker_number = int(input("第{}局游戏开始，请您选出一名庄家，庄家不需要下注哟！\n>>>请指定庄家的序号，1-{}号都可以：".format(self.rounds,self.player_amount))) - 1
                #若玩家序号没有错误将执行子程序
                if banker_number in range(self.player_amount):
                    self.__Banker(self,self.player_amount,banker_number,self.player_set)
                    break
                #玩家序号输入错误则报错
                else:
                    print(">>>请输入正确的玩家序号哟，再试一次吧！<<<")
            #若输入非数字将报出此错
            except:
                print("\n>>>系统监测到了错误，但是系统不知道怎么解决")
    #叫庄子程序
    #输入参数：{玩家数量，庄家编号，玩家集合}
    def __Banker(self,player_amount,banker_number,player_set):
        #修改该名玩家的庄家标识符
        self.player_list[banker_number].banker = True
        #从玩家集合中除去这名庄家，将其变为闲家集合
        self.player_set -= {banker_number}
        print("\n>>>{}号玩家：[{}]通过选举成为了庄家！".format(banker_number + 1,self.player_list[banker_number].name))
        #进入下注环节
        self.Bet(self,self.player_amount,banker_number,self.player_set)
    #下注环节
    #输入参数：{玩家数量，庄家编号，闲家集合}
    def Bet(self,player_amount,banker_number,player_set):
        #对于每名闲家
        for i in self.player_set:
            while True:
                try:
                    #输入下注值
                    bet = int(input("-闲家{}：[{}]，轮到你下注了！\n>>>最低下1$，最高可以下20$：".format(i + 1,self.player_list[i].name)))
                    #限制下注值在1-20范围之间
                    if bet in range(1,21):
                        #进入下注子程序
                        if self.__Bet(self,i,bet):
                            break
                    #若下注不符合范围规定则报错
                    else:
                        print(">>>下注区间是1-20$，请注意下呢！<<<")
                #若输入非整数将报此错
                except:
                    print("\n>>>系统监测到了错误，但是系统不知道怎么解决")
        #进入补牌环节
        self.AugmentCard(self,self.player_amount,banker_number,self.player_set)
    #补牌环节
    #输入参数：{玩家数量，庄家编号，闲家集合}
    def AugmentCard(self,player_amount,banker_number,player_set):
        #初始化补牌轮数为0
        count = 0
        #完成补牌的玩家数为0
        success = 0
        #设定补牌未完成标识为True
        insuccess = True
        print("\n>>>补牌阶段开始，闲家优先！<<<\n")
        #若补牌未完成标识为True
        while insuccess:
            #补牌轮数加1
            count += 1
            print("-第{}轮补牌开始！".format(count))
            #对于每名闲家
            for i in self.player_set:
                #若该名闲家的要牌标记为True且不爆牌标记为True
                if self.player_list[i].want and self.player_list[i].inboom:
                    #玩家可决定是否补牌，若输入为Y、y将进入补牌子程序
                    if input(">>>闲家{}：[{}]轮到你选择了！\n-目前牌点为{}，若要补牌请输入y：".format(i + 1,self.player_list[i].name,self.__calculate(self,i))) in ("Y","y"):
                        self.__AugmentCard(self,i)
                    #玩家选择不补牌则将玩家的要牌标记设为False
                    else:
                        print("\n>闲家{}不敢补了。".format(i + 1))
                        self.player_list[i].want = False
                #补牌完成了，完成补牌的玩家数量加1
                else:
                    success += 1
                    #若所有闲家均完成补牌，则将未完成标识符设为False，循环将停止
                    if success == self.player_amount - 1:
                        insuccess = False
        #接下来轮到庄家补牌了
        i = banker_number
        while True:
            #循环条件为庄家要牌标记为True且不爆牌标记为True
            if self.player_list[i].want and self.player_list[i].inboom:
                #玩家可决定是否补牌，若输入为Y、y将进入补牌子程序
                if input("\n>>>庄家{}：[{}]请注意！现在轮到你选择了！\n-目前牌点为{}，若要补牌请输入y：".format(i + 1,self.player_list[i].name,self.__calculate(self,i))) in ("Y","y"):
                    self.__AugmentCard(self,i)
                #玩家选择不补牌则将玩家的要牌标记设为False
                else:
                    print("\n>庄家{}不敢补了。".format(i + 1))
                    self.player_list[i].want = False
            #所有玩家完成补牌，结束循环
            else:
                break
        #进入决胜环节
        self.Fight(self,self.player_amount,banker_number)
    #决胜环节
    #输入参数：{玩家数量，庄家编号}
    def Fight(self,player_amount,banker_number):
        #为了方便决出胜负，创建点数列表用于存放所有玩家的牌点
        point_list = []
        #创建奖金，初始值为0
        bouns = 0
        #对所有玩家进行操作
        for i in range(self.player_amount):
            #奖金为玩家下注总和
            bouns += self.player_list[i].bet
            #若玩家未爆牌（手牌点数和小于10.5）
            if self.player_list[i].point <= 10.5:
                #则在点数列表中添加相应玩家的手牌点数
                point_list.append(self.player_list[i].point)
            else:
                #否则为这名玩家添加大小为"-1"的点数
                point_list.append(-1)
        #判断玩家是否全爆，判断依据为："-1"数量是否小于玩家的总数
        if point_list.count(-1) < self.player_amount:
            #玩家未全爆，则找出点数最大值
            biggest = max(point_list)
            #若点数最大值出现重复现象
            if point_list.count(biggest) > 1:
                #创建获胜玩家列表，重复且最高的玩家都将获胜
                winner = [i for i,repeat in enumerate(point_list) if repeat == biggest]
                print("\n>>>本轮游戏共有{}名玩家获胜：".format(len(winner)))
                #对于每名获胜玩家，进入发奖子程序
                for i in winner:
                    self.__Bouns(self,i,bouns/len(winner),banker_number)
            #若点数最大值未出现重复现象
            else:
                #获胜者为该最大点数的所有者
                i = point_list.index(biggest)
                print("\n>>>恭喜玩家{}：[{}]获得本轮的胜利！<<<".format(i + 1,self.player_list[i].name))
                #进入发奖子程序
                self.__Bouns(self,i,bouns,banker_number)
        #若所有玩家都爆牌将不进行任何发奖
        else:
            print(">>>\n你们都爆了，这里的{}$谁也拿不走！".format(bouns),banker_number)
        #程序将在此停顿，接到回车键命令后继续进行
        input("\n>>>戳回车键展示所有玩家的数据<<<\n")
        #保存游戏数据
        self.Save(self,self.player_amount)
        #进入Show程序，程序在展示玩家数据的同时将判断是否有玩家输光，若未出现输光情况则可以继续进行下一轮游戏
        if self.Show(self,self.player_amount):
            if input("\n>>>还来一把？\n-输入n可以结束游戏，不输n继续游戏：") in ("n","N"):
                #若玩家选择不继续，将结束游戏
                self.GameExit(self)
        #若Show程序发现有玩家已经输光
        else:
            print(">>>啊哦，好像有人输光了！<<<")
            #结束游戏
            self.GameExit(self)
    #结束游戏的程序
    def GameExit(self):
        self.Continue = False
        input("\n>>>十点半游戏到此结束！\n-请按回车键结束程序")
    #保存游戏的程序
    #输入参数：{玩家数量}
    def Save(self,player_amount):
        #首先进入保存游戏的子程序，子程序将判断系统是否能够保存游戏数据
        if self.__Save(self):
            #引入时间库，记录存档时间
            import datetime as date
            #重新格式化时间文本
            time = date.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
            #保存数据
            with open("save.txt","w+") as data:
                #游戏数据：保存时间、游戏回合、玩家数量
                data.writelines("{}[Savetime]\n{}[Rounds]{}[Players]\n".format(time,self.rounds,self.player_amount))
                #玩家数据：玩家序号、玩家名称、玩家金钱
                for i in range(self.player_amount):    
                    data.writelines("{}[Num]{}[Name]{}[Money]\n".format(self.player_list[i].number,self.player_list[i].name,int(self.player_list[i].money)))
    #保存游戏的子程序，用于判断能否保存游戏数据
    def __Save(self):
        try:
            with open("save.txt","w+"):
                #若执行成功程序将返回True
                return True
        #执行失败将报错
        except:
            print("\n>>>不知为何，系统无法保存游戏数据<<<")
    #读取游戏的程序
    def Read(self):
        #首先进入读取游戏的子程序，子程序将判断系统是否能够读取游戏数据
        if self.__Read(self):
            #读取游戏存档
            with open("save.txt","r") as data:
                save = data.readlines()
            #让玩家选择是开始新游戏还是继续上一局
            if input(">>>系统检测到您已存在游戏数据：\n{}\n{}\n>>>是否要接着玩呢？输y继续玩，输其它开始新游戏：".format((save[0])[0:save[0].find("[Savetime]")],save[1])) in ("y","Y"):
                player_name = []
                #读取玩家数量信息
                self.player_amount = int((save[1])[save[1].find("[Rounds]")+8:save[1].find("[Players]")])
                #读取游戏回合信息
                self.rounds = int((save[1])[0:save[1].find("[Rounds]")])
                #读取玩家名称信息
                for i in range(self.player_amount):
                    player_name.append((save[i+2])[save[i+2].find("[Num]")+5:save[i+2].find("[Name]")])
                #初始化扑克牌
                self.Card.InitCard(self)
                #初始化游戏，初始化方法为1
                self.InitGame(self,player_name,self.player_amount,1)
                #读取玩家金钱信息
                for i in range(self.player_amount):
                    self.player_list[i].money = int((save[i+2])[save[i+2].find("[Name]")+6:save[i+2].find("[Money]")])
                #清除读取的save，释放内存
                del save
                input(">>>已恢复上局游戏数据~<<<\n\n-戳回车键查看玩家信息并继续游戏")
                #展示所有玩家信息
                self.Show(self,self.player_amount)
                #初始化游戏，初始化方法为3
                self.InitGame(self,player_name,self.player_amount,3)
            #若玩家选择不读取，则开始新游戏
            else:
                self.Start(self)
    #读取游戏的子程序
    def __Read(self):
        try:
            #检验是否能正常读取游戏数据，若能读取则返回True
            with open("save.txt","r"):
                return True
        #否则将直接开始新游戏
        except:
            print(">>>系统未检测到游戏数据喔，新游戏将开始<<<")
            self.Start(self)
    #展示所有玩家信息的程序
    #输入参数：{玩家数量}
    def Show(self,player_amount):
        #此Flag用于记录玩家金钱是否不足以进行下一局游戏，初始值为True
        Flag = True
        #对于所有玩家
        for i in range(self.player_amount):
            #展示玩家信息
            print("\n>>>玩家{}：[{}]\n>>>庄家：{}\n>>>手牌：".format(i + 1,self.player_list[i].name,self.player_list[i].banker),end = "")
            #若此玩家金钱不足，Flag将设定为False，游戏将结束
            if int(self.player_list[i].money) <= 0:
                Flag = False
            #展示玩家信息
            for n in range(len(self.player_list[i].hand)):
                print(self.player_list[i].hand[n].suit + self.player_list[i].hand[n].rank,end = " ")
            print("\n>>>手牌点数：{}\n>>>本轮下注：{}$\n>>>钱包余额：{}$".format(self.player_list[i].point,self.player_list[i].bet,self.player_list[i].money))
        return Flag
    #发奖子程序
    #输入参数：{获奖者玩家编号，奖金，庄家编号}
    def __Bouns(self,i,bouns,banker_number):
        #若该名获奖者不是庄家
        if not self.player_list[i].banker:
            #从庄家的钱包中扣除该名获奖者在本轮中的下注金额，并将其加入奖池
            self.player_list[banker_number].money -= self.player_list[i].bet
            bouns += self.player_list[i].bet
            print("\n>>>闲家获胜，庄家要额外付给他与他下注同样多的钱，总共{}$！".format(self.player_list[i].bet))
        #发奖给获奖者
        self.player_list[i].money += bouns
        print(">>>玩家{}：[{}]共获得{}$奖金，钱包余额为{}$！".format(i + 1,self.player_list[i].name,bouns,self.player_list[i].money))
    #补牌子程序
    #输入参数：{要牌者玩家编号}
    def __AugmentCard(self,i):
        print("\n-玩家{}：[{}]抽到了{}{}：{}点！".format(i + 1,self.player_list[i].name,self.cards[0].suit,self.cards[0].rank,self.cards[0].value))
        #从牌堆顶摸一张牌给玩家
        self.player_list[i].hand.append(self.cards[0])
        del self.cards[0]
        #玩家得牌后计算该名玩家的手牌点数，若大于10.5则爆牌
        if self.__calculate(self,i) > 10.5:
            print(">>>目前的点数为{}！您爆了，神仙也救不了您！".format(self.player_list[i].point))
            #修改不爆牌标记
            self.player_list[i].inboom = False
        #若未爆则对赌徒进行鼓励，增加赌场的预期收入
        else:
            print(">>>目前的点数为{}！再接再励哟！".format(self.player_list[i].point))
    #玩家牌点计算器
    #输入参数：{被计算牌点的玩家编号}
    def __calculate(self,i):
        #计算前先将记录玩家牌点的属性归零，因为稍后将给予新的数值
        self.player_list[i].point = 0
        #将玩家手中每张牌的点数加起来
        for n in range(len(self.player_list[i].hand)):
            self.player_list[i].point += self.player_list[i].hand[n].value
        #返回该名玩家的牌点
        return self.player_list[i].point
    #下注子程序
    #输入参数：{下注者编号，下注金额}
    def __Bet(self,i,bet):
        #判断该名玩家是否下假注（钱包里根本没那么多钱）
        if (self.player_list[i].money - bet) >= 0:
            #未超额，正常下注
            self.player_list[i].money -= bet
            self.player_list[i].bet = bet
            print("\n>>>闲家{}：[{}]下了{}$，钱包还剩{}$！".format(i + 1,self.player_list[i].name,bet,self.player_list[i].money))
            return True
        #超额了，返回False给主程序，主程序将给予回应
        else:
            print(">>>您的钱不够，您只有{}$！请重新下注！".format(self.player_list[i].money))
            return False
    #玩家类
    class Players:
        #初始化方法，包含了玩家对象的9个属性
        #9个属性：{序号，名称，手牌，庄家标记，要牌标记，不爆牌标记，下注，金钱，牌点}
        def __init__(self,number,name,hand,banker,want,inboom,bet,money,point):
           self.number = number
           self.name = name
           self.hand = hand
           self.banker = banker
           self.want = want
           self.inboom = inboom
           self.bet = bet
           self.money = money
           self.point = point
    #扑克牌类
    class Card:
        #初始化方法，包含了扑克牌对象的3个属性
        #3个属性：{花色，牌号，所代表的点数}
        def __init__(self,suit,rank,value):
           self.suit = suit
           self.rank = rank
           self.value = value
        #创建一副全新的扑克牌
        def InitCard(self):
            #创建扑克牌盒子
            self.cards = []
            #创建花色
            for suit in ["♠","♥","♣","♦"]:
                #创建牌号
                for rank in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                    #实例化扑克牌对象，并赋予属性，然后装进扑克牌盒子
                    self.cards.append(self.Card(suit,rank,self.Calculate(rank)))
            #引入随机模块
            from random import shuffle as refresh
            #洗牌
            refresh(self.cards)
#游戏开始运行
Game.Process(Game)
