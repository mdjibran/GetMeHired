import math

class ProcessBase:

    def __init__(self, descString, resumeString):
        self.descString = descString
        self.resumeString = resumeString
        self.descKeyValues = {}
        self.resumeKeyValues = {}

        with open('keyWordsDataBase.csv', 'rb') as f:
            self.reader = file.read(f)
        self.reader = self.reader.replace(', ', ',').replace('\n', '').split(',')
        self.reader = [element.lower() for element in self.reader]
        self.tech_keywords = set(self.reader)

    def getDescKeywords(self):
        descString = self.descString
        descString = str.lower(descString)
        descKeyValues = self.descKeyValues

        for word in descString.split():
            if word in self.tech_keywords:
                if word in self.descKeyValues:
                    descKeyValues[word] += 1
                else:
                    descKeyValues[word] = 1

    def getResumeKeywords(self):
        resumeString = self.resumeString
        resume_length = len(resumeString.split())
        resumeString = str.lower(resumeString)
        print "Word count : " + str(resume_length)
        # Create a empty list to store keywords and a dictionary to count words

        if resumeString != None:
            for word in resumeString.split():
                if word in self.descKeyValues:
                    if word in self.resumeKeyValues:
                        self.resumeKeyValues[word] += 1
                    else:
                        self.resumeKeyValues[word] = 1

    def formatString(self, k_desc, v_desc, v_resume):
        k_descLen = len(k_desc)
        spcLen = 30 - k_descLen
        spcLen = int(math.ceil(spcLen/2))
        displyStr = "|"+" "*spcLen + k_desc + spcLen*" " + "|   " + str(v_desc) + "   |   " + str(v_resume) + "   |   "
        return displyStr

    def compareKeywords(self):
        self.getDescKeywords()
        self.getResumeKeywords()
        resumePer = 0
        totresumePer = 0
        totdescPer = 0
        print "________________________________________________"
        print "|               KEY            |  DESC | VALUE |"
        print "------------------------------------------------"
        for k_desc, v_desc in self.descKeyValues.items():
            totdescPer += 100
            if k_desc in self.resumeKeyValues:
                v_resume = str(self.resumeKeyValues[k_desc])
                resumePer = float(float(v_resume) / float(v_desc) * 100)
                print self.formatString(k_desc, v_desc, v_resume)
                totresumePer += resumePer
            else:
                print self.formatString(k_desc, v_desc, 0)
        print "-------------------------------------------------"
        #print "\n\n Job :" + str(totdescPer) + " | Resume : " + str(totresumePer)
        print "Profile Match : " + str(int(math.ceil((totresumePer/totdescPer)*100)))
