import unittest
from Project5 import isPalindrome


class PalidromeTestCases(unittest.TestCase):
    def test_regular(self):#Tests regular palidrome words
        palin_words = ["mom", "bob", "civic", "madam"]
        for word in palin_words:
            self.assertTrue(isPalindrome(word),"Failed test for {}".format(word))
    def test_num(self):#Tests numbers
        numbers = [35, 111, 2, 12.5]
        for num in numbers:
            self.assertFalse(isPalindrome(num),"Failed test for {}".format(num))
    def test_Cap(self):#Tests words with capital letters
        palin_words = ["Mom", "Bob", "Civic", "Madam"]
        for word in palin_words:
            self.assertTrue(isPalindrome(word),"Failed test for {}".format(word))
    def test_sentence(self):#Tests sentences with spaces and capital letters
        palin_sentences = ["Step on no pets", "Live on Time emit no evil", "Cigar Toss it in a can it is so tragic"]
        for sen in palin_sentences:
            self.assertTrue(isPalindrome(sen),"Failed test for {}".format(sen))
    def test_punct(self):#Tests sentences with punctuation 
        palin_sentences = ["Yen o' money.", "Live on Time..... emit no evil", "Cigar? Toss it in a can it is so tragic."]
        for sen in palin_sentences:
            self.assertTrue(isPalindrome(sen),"Failed test for {}".format(sen))
    
    
    
    

if __name__ == '__main__':
    def results():   
        t = unittest.main(exit=False)
        tests=t.result.testsRun
        fail= len(t.result.failures)
        error=len(t.result.errors)
        final=tests-fail-error
        print(tests,fail,final)
        return tests,fail,final
    results()