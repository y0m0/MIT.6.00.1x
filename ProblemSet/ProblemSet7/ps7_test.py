# 6.00.1x
# Problem Set 7 Test Suite
import unittest
import sys 
from ps7 import *

class ProblemSet7NewsStory(unittest.TestCase):
    def setUp(self):
        pass
    def testNewsStoryConstructor(self):
        story = NewsStory('', '', '', '', '')
    def testNewsStoryGetGuid(self):
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.getGuid(), 'test guid')
    def testNewsStoryGetTitle(self):
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.getTitle(), 'test title')
    def testNewsStoryGetSubject(self):
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.getSubject(), 'test subject')
    def testNewsStoryGetSummary(self):
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.getSummary(), 'test summary')
    def testNewsStoryGetLink(self):
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.getLink(), 'test link')

class ProblemSet7(unittest.TestCase):
    def setUp(self):
        class TrueTrigger:
            def evaluate(self, story): return True

        class FalseTrigger:
            def evaluate(self, story): return False

        self.tt = TrueTrigger()
        self.tt2 = TrueTrigger()
        self.ft = FalseTrigger()
        self.ft2 = FalseTrigger()

    def test1TitleTrigger(self):
        koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
        pillow    = NewsStory('', 'I prefer pillows that are soft.', '', '', '')
        soda      = NewsStory('', 'Soft drinks are great', '', '', '')
        pink      = NewsStory('', "Soft's the new pink!", '', '', '')
        football  = NewsStory('', '"Soft!" he exclaimed as he threw the football', '', '', '')
        microsoft = NewsStory('', 'Microsoft announced today that pillows are bad', '', '', '')
        nothing   = NewsStory('', 'Reuters reports something really boring', '', '' ,'')
        caps      = NewsStory('', 'soft things are soft', '', '', '')

        s1 = TitleTrigger('SOFT')
        s2  = TitleTrigger('soft')
        for trig in [s1, s2]:
            self.assertTrue(trig.evaluate(koala), "TitleTrigger failed to fire when the word appeared in the title")
            self.assertTrue(trig.evaluate(pillow), "TitleTrigger failed to fire when the word had punctuation on it")
            self.assertTrue(trig.evaluate(soda), "TitleTrigger failed to fire when the case was different")
            self.assertTrue(trig.evaluate(pink), "TitleTrigger failed to fire when the word had an apostrophe on it")
            self.assertTrue(trig.evaluate(football), "TitleTrigger failed to fire in the presence of lots of punctuation")
            self.assertTrue(trig.evaluate(caps), "TitleTrigger is case-sensitive and shouldn't be")
            
            self.assertFalse(trig.evaluate(microsoft), "TitleTrigger fired when the word was present, but not as its own word (e.g. 'soft' and 'Microsoft)'")
            self.assertFalse(trig.evaluate(nothing), "TitleTrigger fired when the word wasn't really present in the title")

    def test2SubjectTrigger(self):
        koala     = NewsStory('', '', 'Koala bears are soft and cuddly', '', '')
        pillow    = NewsStory('', '', 'I prefer pillows that are soft.', '', '')
        soda      = NewsStory('', '', 'Soft drinks are great', '', '')
        pink      = NewsStory('', '', "Soft's the new pink!", '', '')
        football  = NewsStory('', '', '"Soft!" he exclaimed as he threw the football', '', '')
        microsoft = NewsStory('', '', 'Microsoft announced today that pillows are bad', '', '')
        nothing   = NewsStory('', '', 'Reuters reports something really boring', '', '')
        caps      = NewsStory('', '', 'soft things are soft', '', '')

        s1 = SubjectTrigger('SOFT')
        s2  = SubjectTrigger('soft')
        for trig in [s1, s2]:
            self.assertTrue(trig.evaluate(koala), "SubjectTrigger failed to fire when the word appeared in the subject")
            self.assertTrue(trig.evaluate(pillow), "SubjectTrigger failed to fire when the word had punctuation on it")
            self.assertTrue(trig.evaluate(soda), "SubjectTrigger failed to fire when the case was different")
            self.assertTrue(trig.evaluate(pink), "SubjectTrigger failed to fire when the word had an apostrophe on it")
            self.assertTrue(trig.evaluate(football), "SubjectTrigger failed to fire in the presence of lots of punctuation")
            self.assertTrue(trig.evaluate(caps), "SubjectTrigger is case-sensitive and shouldn't be")
            
            self.assertFalse(trig.evaluate(microsoft), "SubjectTrigger fired when the word was present, but not as its own word (e.g. 'soft' and 'Microsoft)'")
            self.assertFalse(trig.evaluate(nothing), "SubjectTrigger fired when the word wasn't really present in the subject")

    def test3SummaryTrigger(self):
        koala     = NewsStory('', '', '', 'Koala bears are soft and cuddly', '')
        pillow    = NewsStory('', '', '', 'I prefer pillows that are soft.', '')
        soda      = NewsStory('', '', '', 'Soft drinks are great', '')
        pink      = NewsStory('', '', '', "Soft's the new pink!", '')
        football  = NewsStory('', '', '', '"Soft!" he exclaimed as he threw the football', '')
        microsoft = NewsStory('', '', '', 'Microsoft announced today that pillows are bad', '')
        nothing   = NewsStory('', '', '', 'Reuters reports something really boring', '')
        caps      = NewsStory('', '', '', 'soft things are soft', '')

        s1 = SummaryTrigger('SOFT')
        s2  = SummaryTrigger('soft')
        for trig in [s1, s2]:
            self.assertTrue(trig.evaluate(koala), "SummaryTrigger failed to fire when the word appeared in the summary.")
            self.assertTrue(trig.evaluate(pillow), "SummaryTrigger failed to fire when the word had punctuation on it")
            self.assertTrue(trig.evaluate(soda), "SummaryTrigger failed to fire when the case was different")
            self.assertTrue(trig.evaluate(pink), "SummaryTrigger failed to fire when the word had an apostrophe on it")
            self.assertTrue(trig.evaluate(football), "SummaryTrigger failed to fire in the presence of lots of punctuation")
            self.assertTrue(trig.evaluate(caps), "SummaryTrigger is case-sensitive and shouldn't be")
            
            self.assertFalse(trig.evaluate(microsoft), "SummaryTrigger fired when the word was present, but not as its own word (e.g. 'soft' and 'Microsoft)'")
            self.assertFalse(trig.evaluate(nothing), "SummaryTrigger fired when the word wasn't really present in the summary")

    def test4NotTrigger(self):
        n = NotTrigger(self.tt)
        b = NewsStory("guid", "title", "subj", "summary", "link")

        self.assertFalse(n.evaluate(b), "A NOT trigger applied to 'always true' DID NOT return false")

        y = NotTrigger(self.ft)
        self.assertTrue(y.evaluate(b), "A NOT trigger applied to 'always false' DID NOT return true")

    def test5AndTrigger(self):
        yy = AndTrigger(self.tt, self.tt2)
        yn = AndTrigger(self.tt, self.ft)
        ny = AndTrigger(self.ft, self.tt)
        nn = AndTrigger(self.ft, self.ft2)
        b = NewsStory("guid", "title", "subj", "summary", "link")

        self.assertTrue(yy.evaluate(b), "AND of 'always true' and 'always true' should be true")
        self.assertFalse(yn.evaluate(b), "AND of 'always true' and 'always false' should be false")
        self.assertFalse(ny.evaluate(b), "AND of 'always false' and 'always true' should be false")
        self.assertFalse(nn.evaluate(b), "AND of 'always false' and 'always false' should be false")

    def test6OrTrigger(self):
        yy = OrTrigger(self.tt, self.tt2)
        yn = OrTrigger(self.tt, self.ft)
        ny = OrTrigger(self.ft, self.tt)
        nn = OrTrigger(self.ft, self.ft2)
        b = NewsStory("guid", "title", "subj", "summary", "link")

        self.assertTrue(yy.evaluate(b), "OR of 'always true' and 'always true' should be true")
        self.assertTrue(yn.evaluate(b), "OR of 'always true' and 'always false' should be true")
        self.assertTrue(ny.evaluate(b), "OR of 'always false' and 'always true' should be true")
        self.assertFalse(nn.evaluate(b), "OR of 'always false' and 'always false' should be false")

    def test7PhraseTrigger(self):
        pt = PhraseTrigger("New York City")
        a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
        b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
        c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
        noa = NewsStory('', "something something new york city", '', '', '')
        nob = NewsStory('', '', "something something new york city", '', '')
        noc = NewsStory('', '', '', "something something new york city", '')


        self.assertTrue(pt.evaluate(a), "PhraseTrigger doesn't find phrase in title")
        self.assertTrue(pt.evaluate(b), "PhraseTrigger doesn't find phrase in subject")
        self.assertTrue(pt.evaluate(c), "PhraseTrigger doesn't find phrase in summary")
    
        for s in [noa, nob, noc]:
            self.assertFalse(pt.evaluate(s), "PhraseTrigger is case-insensitive, and shouldn't be")

    def test8FilterStories(self):
        pt = PhraseTrigger("New York City")
        a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
        b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
        c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
        noa = NewsStory('', "something something new york city", '', '', '')
        nob = NewsStory('', '', "something something new york city", '', '')
        noc = NewsStory('', '', '', "something something new york city", '')

        triggers = [pt, self.tt, self.ft]
        stories = [a, b, c, noa, nob, noc]
        filteredStories = filterStories(stories, triggers)
        for story in stories:
            self.assertTrue(story in filteredStories)
        filteredStories = filterStories(stories, [self.ft])
        self.assertEquals(len(filteredStories), 0)

    def test8FilterStories2(self):
        pt = PhraseTrigger("New York City")
        a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
        b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
        c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
        noa = NewsStory('', "something something new york city", '', '', '')
        nob = NewsStory('', '', "something something new york city", '', '')
        noc = NewsStory('', '', '', "something something new york city", '')

        class MatchTrigger(Trigger):
            def __init__(self, story):
                self.story = story
            def evaluate(self, story):
                return story == self.story
        triggers = [MatchTrigger(a), MatchTrigger(nob)]
        stories = [a, b, c, noa, nob, noc]
        filteredStories = filterStories(stories, triggers)
        self.assertTrue(a in filteredStories)
        self.assertTrue(nob in filteredStories)
        self.assertEquals(2, len(filteredStories))


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProblemSet7NewsStory))
    suite.addTest(unittest.makeSuite(ProblemSet7))
#    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite) 

