import random 

class Hand(object): # Hand��object���������
    def __init__(self, n): # self��Hand���ʵ��
        '''
        Initialize a Hand. # ��ʼ��Hand

        n: integer, the size of the hand. # n��int�ͣ�hand��size
        '''
        assert type(n) == int # n������int�ͣ�������ǣ���AssertError����
        self.HAND_SIZE = n 
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute�����ԣ� to the new hand. # and���µ�hand������hand����
        '''
        # Set self.hand to a new, empty dictionary
        # ��self.hand��һ����ֵ��self.hand���ֵ����͡�
        self.hand = {}

        # Build the hand # ����һ��hand
        numVowels = self.HAND_SIZE / 3
        # self.HAND_SIZE = n
        # numVowels = n / 3
    
        for i in range(numVowels): # �� 0 �� n / 3 ѭ��������n / 3��
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            # self.VOWELS = 'aeiou'
            # len(self.VOWELS)����5
            # random.randrange(0,len(self.VOWELS))�������0��4�е�һ����
            # x = self.VOWELS[random.randrange(0,len(self.VOWELS))]��x = self.VOWELS[random.randrange(0,5))]
            # x = self.VOWELS[random.randrange(0,5))]�ǰ�'aeiou'�е�5����ĸ�����ֵ1����x
            # x��'aeiou'�����ȡֵ
            self.hand[x] = self.hand.get(x, 0) + 1 # get�����Ƿ����ֵ���ķ���
            # d���ֵ䣬d[k]=v��ֵv��������k��
            # x���ֵ�hand�ļ�
            # self.hand.get(x, 0)�ǽ��ֵ�hand�ļ�x��Ӧ��ֵ����Ϊ0
            # self.hand[x] = self.hand.get(x, 0) + 1�ǽ��ֵ�hand�ļ�x��Ӧ��ֵ����Ϊ1
        
        for i in range(numVowels, self.HAND_SIZE): # �� n / 3 �� n ѭ��������n��
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            # x��'bcdfghjklmnpqrstvwxyz'�����ȡֵ
            self.hand[x] = self.hand.get(x, 0) + 1
            # self.hand[x] = self.hand.get(x, 0) + 1�ǽ��ֵ�hand�ļ�x��Ӧ��ֵ����Ϊ1
            
    def setDummyHand(self, handString): # dummy �ٵģ�����Ʒ��
        '''
        Allows you to set a dummy hand. Useful for testing your implementation��ʵ�֣�.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.
        handString���������������е���ĸ�ַ��������ȱ�����self.HAND_SIZE

        This method converts sets the hand attribute�����ԣ� to a dictionary 
        containing the letters of handString.
        ���������hand��������Ϊ������handString��ĸ���ֵ䡣
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        # handString�ĳ��ȱ�����self.HAND_SIZE��������ʾAssertError
        self.hand = {}
        # ��ʼ��handΪһ�����ֵ�{}
        for char in handString: # ѭ��handString�ַ����е��ַ�char
            self.hand[char] = self.hand.get(char, 0) + 1
            # ��hand�ֵ�ļ�����ÿһ��char��ֵ����Ϊ1
            


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        ����hand�ĳ���
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
