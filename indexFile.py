from ProcessBase import ProcessBase

descString = raw_input("Enter job Description : ")
resumeString = raw_input("Enter your resume : ")
base = ProcessBase(descString, resumeString)


base.compareKeywords()

