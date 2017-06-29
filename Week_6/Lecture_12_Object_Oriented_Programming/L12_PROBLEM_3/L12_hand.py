import random 

class Hand(object): # Hand是object对象的子类
    def __init__(self, n): # self是Hand类的实例
        '''
        Initialize a Hand. # 初始化Hand

        n: integer, the size of the hand. # n是int型，hand的size
        '''
        assert type(n) == int # n必须是int型，如果不是，则报AssertError错误。
        self.HAND_SIZE = n 
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute（属性） to the new hand. # and给新的hand类设置hand属性
        '''
        # Set self.hand to a new, empty dictionary
        # 给self.hand赋一个空值，self.hand是字典类型。
        self.hand = {}

        # Build the hand # 建立一个hand
        numVowels = self.HAND_SIZE / 3
        # self.HAND_SIZE = n
        # numVowels = n / 3
    
        for i in range(numVowels): # 在 0 到 n / 3 循环（不含n / 3）
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            # self.VOWELS = 'aeiou'
            # len(self.VOWELS)等于5
            # random.randrange(0,len(self.VOWELS))随机返回0到4中的一个数
            # x = self.VOWELS[random.randrange(0,len(self.VOWELS))]即x = self.VOWELS[random.randrange(0,5))]
            # x = self.VOWELS[random.randrange(0,5))]是把'aeiou'中的5个字母随机赋值1个给x
            # x从'aeiou'中随机取值
            self.hand[x] = self.hand.get(x, 0) + 1 # get方法是访问字典项的方法
            # d是字典，d[k]=v将值v关联到键k上
            # x是字典hand的键
            # self.hand.get(x, 0)是将字典hand的键x对应的值设置为0
            # self.hand[x] = self.hand.get(x, 0) + 1是将字典hand的键x对应的值设置为1
        
        for i in range(numVowels, self.HAND_SIZE): # 在 n / 3 到 n 循环（不含n）
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            # x从'bcdfghjklmnpqrstvwxyz'中随机取值
            self.hand[x] = self.hand.get(x, 0) + 1
            # self.hand[x] = self.hand.get(x, 0) + 1是将字典hand的键x对应的值设置为1
            
    def setDummyHand(self, handString): # dummy 假的，做样品的
        '''
        Allows you to set a dummy hand. Useful for testing your implementation（实现）.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.
        handString是你期望握在手中的字母字符串，长度必须是self.HAND_SIZE

        This method converts sets the hand attribute（属性） to a dictionary 
        containing the letters of handString.
        这个方法把hand属性设置为包含了handString字母的字典。
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        # handString的长度必须是self.HAND_SIZE，否则提示AssertError
        self.hand = {}
        # 初始化hand为一个空字典{}
        for char in handString: # 循环handString字符串中的字符char
            self.hand[char] = self.hand.get(char, 0) + 1
            # 将hand字典的键——每一个char的值设置为1
            


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        计算hand的长度
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Your code here
        
        raise NotImplementedError()

    
myHand = Hand(7)
print myHand
print myHand.calculateLen()

myHand.setDummyHand('aazzmsp')
print myHand
print myHand.calculateLen()

myHand.update('za')
print myHand
