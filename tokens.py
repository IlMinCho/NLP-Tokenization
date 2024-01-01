import sys
import gzip
import re
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def spaceToken(nonTokenText):
    tokenText = nonTokenText.split()
    return tokenText

def fancyToken(tokenText, tokenList):
    if type(tokenText) == str:
         # writing original text
                # testOutput.write(token) # orgin
                # testOutput.write(" ")
                token = tokenText

                if token.startswith('https://') or token.startswith('http://'):
                    # print("URL: "+token) # return
                    #broken
                    if token.endswith(")"):
                         tokenfil = token
                         tokenfil = token[::-1].replace(")","",1)[::-1]
                         fancyToken(tokenfil, tokenList)
                    else:
                        tokenList.append(token)
                else: 
                    token = token.lower()
                    if re.match(r'^[-+,.\d]+$', token) and not re.match(r'^[-+,.]+$', token):
                            tokenList.append(token)
                    elif '\'' in token:
                        token = token.replace('\'','')
                        # print('apostrophes: '+token)
                        fancyToken(token, tokenList)
                    elif '.' in token and not token.startswith('https://') and not token.startswith('http://') and not re.match(r'^[-+,.\d)]+$', token):
                        ## broken - > rematch ) ? 
                            token = token.replace('.','')
                            if token == '': print("Token is empty!") # ??
                            # print('abbreviation: '+token)
                            fancyToken(token, tokenList)
                    elif '-' in token:
                        splitToken = token.split('-')
                        # print(splitToken)
                        token = token.replace('-','')
                        splitToken.append(token)
                        # print(splitToken)
                        # print(token)
                        fancyToken(splitToken, tokenList)  
                    elif re.search(r'[/(){}^@#!&?_–,—":;…~|$*%\[\]]', token):
                        #  print("---------------------------------------------")
                        #  print(token)
                         splitToken = re.split(r'[/(){}^@#!&?_–,—":;…~|$*%\[\]]', token) 
                        #  print(splitToken)
                        #  print("---------------------------------------------")
                         fancyToken(splitToken, tokenList)
                    else:
                         tokenList.append(token)     
    else: 
         
        for token in tokenText:
                # writing original text
                # testOutput.write(token) # orgin
                # testOutput.write(" ")
                if token.startswith('https://') or token.startswith('http://'):
                    # print("URL: "+token) # return
                    tokenList.append(token)
                else: 
                    token = token.lower()

                    if re.match(r'^[-+,.\d]+$', token) and not re.match(r'^[-+,.]+$', token):
                        # print('number: '+token) # return
                            tokenList.append(token)
                    elif '\'' in token:
                        token = token.replace('\'','')
                        # print('apostrophes: '+token)
                        fancyToken(token, tokenList)
                    elif '.' in token:
                        ## rematch ) ?
                        if not token.startswith('https://') and not token.startswith('http://') and not re.match(r'^[-+,.\d)]+$', token):
                            token = token.replace('.','')
                            if token == '': print("Token is empty!") # ??
                            # print('abbreviation: '+token)
                            fancyToken(token, tokenList)
                        else: fancyToken(token, tokenList)
                        
                    elif '-' in token:
                        splitToken = token.split('-')
                        # print(splitToken)
                        token = token.replace('-','')
                        splitToken.append(token)
                        fancyToken(splitToken, tokenList)  
                    elif re.search(r'[/(){}^@#!&?_–,—":;…~|$*%\[\]]', token):
                        #  print("---------------------------------------------")
                         splitToken = re.split(r'[/(){}^@#!&?_–,—":;…~|$*%\[\]]', token) 
                        #  print(splitToken)
                        #  print("---------------------------------------------")
                         fancyToken(splitToken, tokenList)
                    else:
                         tokenList.append(token)
                         
    

def tokenization(nonTokenText, tokenize_type):
    if tokenize_type == "spaces":
        return spaceToken(nonTokenText)

    elif tokenize_type == "fancy":

        tokenText = nonTokenText
        tokenList = []
        fancyToken(tokenText, tokenList)
        
        return tokenList


def stopping(nonStopText, stopword_lst, stoplist_type):
    if stoplist_type == "noStop": return nonStopText
    elif stoplist_type == "yesStop":
        for nonText in nonStopText:
             if not nonText.startswith('https://') or not nonText.startswith('http://'):
                if nonText in stopword_lst:
                    nonStopText.remove(nonText)
        return nonStopText
    
    
def stemming(nonStemText, stemming_type):
    stemText = ""
    returnList = []
    if stemming_type == "noStem": return nonStemText
    elif stemming_type == "porterStem":
        for nonText in nonStemText:
            if len(nonText) != 0:
             if not nonText.startswith('https://') or not nonText.startswith('http://'):
                    vowel_lst = vowel_lst = ["a", "e", "i", "o", "u", "y"]
                    if nonText.endswith("sses"):
                        stemText = nonText[::-1].replace("sess","ss",1)[::-1]
                        # print(stemText)
                    elif nonText.endswith("ied") or nonText.endswith("ies"):
                        if nonText.endswith("ied"):
                            if len(nonText) > 4:
                                stemText = nonText[::-1].replace("dei","i",1)[::-1]
                            else: stemText = nonText[::-1].replace("dei","ei",1)[::-1]
                        elif nonText.endswith("ies"):
                            if len(nonText) > 4:
                                stemText = nonText[::-1].replace("sei","i",1)[::-1]
                            else: stemText = nonText[::-1].replace("sei","ei",1)[::-1]
                    elif nonText.endswith("us") or nonText.endswith("ss"): 
                        stemText = nonText
                    elif nonText.endswith("s"):
                        sliceText = nonText[:len(nonText)-2]

                        eachSlice = []
                        for char in sliceText:
                            eachSlice.append(char)

                        if not set(eachSlice).isdisjoint(set(vowel_lst)):
                            stemText = nonText[::-1].replace("s","",1)[::-1]
                        else: stemText = nonText
                    else: stemText = nonText

                    if stemText.endswith("eed") or stemText.endswith("eedly"):
                        if stemText.endswith("eed"):
                            sliceText = stemText[:len(stemText)-3]
                            
                            vowel_index = []
                            for vowel in vowel_lst:
                                if sliceText.find(vowel) != -1:
                                    vowel_index.append(sliceText.find(vowel))
                            if len(vowel_index) > 0:
                                if not sliceText[min(vowel_index)+1] in vowel_lst:
                                        stemText = stemText[::-1].replace("dee","ee",1)[::-1]
                        else: 
                            sliceText = stemText[:len(stemText)-5]

                            vowel_index = []
                            for vowel in vowel_lst:
                                if sliceText.find(vowel) != -1:
                                    vowel_index.append(sliceText.find(vowel))
                            if len(vowel_index) > 0:
                                if not sliceText[min(vowel_index)+1] in vowel_lst:
                                        stemText = stemText[::-1].replace("yldee","ee",1)[::-1]
                        if stemText.endswith("y"):
                            if len(stemText) > 2:
                                if stemText[len(stemText)-2] not in vowel_lst:
                                        stemText = stemText[::-1].replace("y","i",1)[::-1]
                    elif stemText.endswith("ed") or stemText.endswith("edly") or stemText.endswith("ing") or stemText.endswith("ingly"):
                        if stemText.endswith("ed"):
                            sliceText = stemText[:len(stemText)-2]
                            
                            vowel_index = []
                            for vowel in vowel_lst:
                                if sliceText.find(vowel) != -1:
                                    vowel_index.append(sliceText.find(vowel))

                            if len(vowel_index) == 0:
                                if stemText.endswith("y"):
                                    if len(stemText) > 2:
                                        if stemText[len(stemText)-2] not in vowel_lst:
                                            stemText = stemText[::-1].replace("y","i",1)[::-1]
                            else:
                                stemText = sliceText
                                if sliceText.endswith("at") or sliceText.endswith("bl") or sliceText.endswith("iz"):
                                    stemText = sliceText + "e"
                                elif sliceText.endswith("bb") or sliceText.endswith("dd") or sliceText.endswith("ff") or sliceText.endswith("gg") or sliceText.endswith("mm") or sliceText.endswith("nn") or sliceText.endswith("pp") or sliceText.endswith("rr") or sliceText.endswith("tt"):
                                    stemText = sliceText[:-1]
                                elif len(vowel_index) == 1 and len(sliceText) == 2:
                                    if vowel_index[0]+1 != len(sliceText):
                                        if sliceText[vowel_index[0]+1] not in vowel_lst:
                                            stemText = sliceText + "e"
                                elif len(vowel_index) == 1 and len(sliceText) > 2:
                                    check_char =  ["a", "e", "i", "o", "u", "y", "w", "x"]
                                    if vowel_index[0] == len(sliceText)-2:
                                        if sliceText[vowel_index[0]+1] not in check_char:
                                            stemText = sliceText + "e"

                                if stemText.endswith("y"):
                                        if len(stemText) > 2:
                                            if stemText[len(stemText)-2] not in vowel_lst:
                                                stemText = stemText[::-1].replace("y","i",1)[::-1]
                

                        elif stemText.endswith("edly"):
                            sliceText = stemText[:len(stemText)-4]

                            vowel_index = []
                            for vowel in vowel_lst:
                                if sliceText.find(vowel) != -1:
                                    vowel_index.append(sliceText.find(vowel))

                            if len(vowel_index) == 0:
                                if stemText.endswith("y"):
                                    if len(stemText) > 2:
                                        if stemText[len(stemText)-2] not in vowel_lst:
                                            stemText = stemText[::-1].replace("y","i",1)[::-1]
                            else:
                                stemText = sliceText
                                if sliceText.endswith("at") or sliceText.endswith("bl") or sliceText.endswith("iz"):
                                    stemText = sliceText + "e"
                                elif sliceText.endswith("bb") or sliceText.endswith("dd") or sliceText.endswith("ff") or sliceText.endswith("gg") or sliceText.endswith("mm") or sliceText.endswith("nn") or sliceText.endswith("pp") or sliceText.endswith("rr") or sliceText.endswith("tt"):
                                    stemText = sliceText[:-1]
                                elif len(vowel_index) == 1 and len(sliceText) == 2:
                                    if vowel_index[0]+1 != len(sliceText):
                                        if sliceText[vowel_index[0]+1] not in vowel_lst:
                                            stemText = sliceText + "e"
                                elif len(vowel_index) == 1 and len(sliceText) > 2:
                                    check_char =  ["a", "e", "i", "o", "u", "y", "w", "x"]
                                    if vowel_index[0] == len(sliceText)-2:
                                        if sliceText[vowel_index[0]+1] not in check_char:
                                            stemText = sliceText + "e"

                                if stemText.endswith("y"):
                                        if len(stemText) > 2:
                                            if stemText[len(stemText)-2] not in vowel_lst:
                                                stemText = stemText[::-1].replace("y","i",1)[::-1]                  
                            
                        elif stemText.endswith("ing"):
                            sliceText = stemText[:len(stemText)-3]

                            vowel_index = []
                            for vowel in vowel_lst:
                                if sliceText.find(vowel) != -1:
                                    vowel_index.append(sliceText.find(vowel))

                            if len(vowel_index) == 0:
                                if stemText.endswith("y"):
                                    if len(stemText) > 2:
                                        if stemText[len(stemText)-2] not in vowel_lst:
                                            stemText = stemText[::-1].replace("y","i",1)[::-1]
                            else:
                                stemText = sliceText
                                if sliceText.endswith("at") or sliceText.endswith("bl") or sliceText.endswith("iz"):
                                    stemText = sliceText + "e"
                                elif sliceText.endswith("bb") or sliceText.endswith("dd") or sliceText.endswith("ff") or sliceText.endswith("gg") or sliceText.endswith("mm") or sliceText.endswith("nn") or sliceText.endswith("pp") or sliceText.endswith("rr") or sliceText.endswith("tt"):
                                    stemText = sliceText[:-1]
                                elif len(vowel_index) == 1 and len(sliceText) == 2:
                                    if vowel_index[0]+1 != len(sliceText):
                                        if sliceText[vowel_index[0]+1] not in vowel_lst:
                                            stemText = sliceText + "e"
                                elif len(vowel_index) == 1 and len(sliceText) > 2:
                                    check_char =  ["a", "e", "i", "o", "u", "y", "w", "x"]
                                    if vowel_index[0] == len(sliceText)-2:
                                        if sliceText[vowel_index[0]+1] not in check_char:
                                            stemText = sliceText + "e"

                                if stemText.endswith("y"):
                                        if len(stemText) > 2:
                                            if stemText[len(stemText)-2] not in vowel_lst:
                                                stemText = stemText[::-1].replace("y","i",1)[::-1]                  
                                
                        elif stemText.endswith("ingly"):
                            sliceText = stemText[:len(stemText)-5]

                            vowel_index = []
                            for vowel in vowel_lst:
                                if sliceText.find(vowel) != -1:
                                    vowel_index.append(sliceText.find(vowel))

                            if len(vowel_index) == 0:
                                if stemText.endswith("y"):
                                    if len(stemText) > 2:
                                        if stemText[len(stemText)-2] not in vowel_lst:
                                            stemText = stemText[::-1].replace("y","i",1)[::-1]
                            else:
                                stemText = sliceText
                                if sliceText.endswith("at") or sliceText.endswith("bl") or sliceText.endswith("iz"):
                                    stemText = sliceText + "e"
                                elif sliceText.endswith("bb") or sliceText.endswith("dd") or sliceText.endswith("ff") or sliceText.endswith("gg") or sliceText.endswith("mm") or sliceText.endswith("nn") or sliceText.endswith("pp") or sliceText.endswith("rr") or sliceText.endswith("tt"):
                                    stemText = sliceText[:-1]
                                elif len(vowel_index) == 1 and len(sliceText) == 2:
                                    if vowel_index[0]+1 != len(sliceText):
                                        if sliceText[vowel_index[0]+1] not in vowel_lst:
                                            stemText = sliceText + "e"
                                elif len(vowel_index) == 1 and len(sliceText) > 2:
                                    check_char =  ["a", "e", "i", "o", "u", "y", "w", "x"]
                                    if vowel_index[0] == len(sliceText)-2:
                                        if sliceText[vowel_index[0]+1] not in check_char:
                                            stemText = sliceText + "e"

                                if stemText.endswith("y"):
                                        if len(stemText) > 2:
                                            if stemText[len(stemText)-2] not in vowel_lst:
                                                stemText = stemText[::-1].replace("y","i",1)[::-1]   

                    if stemText.endswith("y"):
                            if len(stemText) > 2:
                                if stemText[len(stemText)-2] not in vowel_lst:
                                        stemText = stemText[::-1].replace("y","i",1)[::-1]

             returnList.append(stemText)

    return returnList


if __name__ == '__main__':
    # Read arguments from command line; or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = sys.argv[1] if argv_len >= 2 else "P1-train.gz"
    outputFilePrefix = sys.argv[2] if argv_len >= 3 else "outPrefix"
    tokenize_type = sys.argv[3] if argv_len >= 4 else "spaces"
    stoplist_type = sys.argv[4] if argv_len >= 5 else "yesStop"
    stemming_type = sys.argv[5] if argv_len >= 6 else "porterStem"

    # Below is stopword list
    stopword_lst = stopword_lst = ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
                    "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to",
                    "was", "were", "with"]
    

    with gzip.open(inputFile, "rt") as file:
            nonTokenText = file.read()
            nonTokenText = spaceToken(nonTokenText)

    # file = open(inputFile, "rt")
    # nonTokenText = file.read()
    # nonTokenText = spaceToken(nonTokenText)
    # file.close()
        #     # with open(outputFileName, 'w') as testOutput:
        # testOutput = open(outputFile+".txt", 'w')
        # index = 0
        # for token in tokenText:
        #         testOutput.write(token)
        #         testOutput.write(" ")
        #         testOutput.write(token)
        #         index += 1
        #         testOutput.write("\n")
        #         # if count != len(tokenText):
        #         #     testOutput.write(" ")

        # # file.close()
        # testOutput.close()
    tokenOutput = open(outputFilePrefix+"-tokens.txt", 'w')
    heapOutput = open(outputFilePrefix+"-heaps.txt", 'w')
    statOutput = open(outputFilePrefix+"-stats.txt", 'w')

    numTokens = 0
    numUniqueTokens = 0
    tokenList = []
    uniqueList = []

    plotToken = []
    plotUnique = []

    for nonToken in nonTokenText:
        # print("\n")
        # print(nonToken)
        numTokens += 1
        tokenOutput.write(nonToken)

        # print("nn "+nonToken)
        tokenText = tokenization(nonToken, tokenize_type)
        # print(tokenText)
        stopText = stopping(tokenText, stopword_lst, stoplist_type)
        # print("----"+str(stopText))
        stemText = stemming(stopText, stemming_type)
        # print("======="+str(stemText))

        if stemText != []:
            for text in stemText:
                if text != "":
                    tokenList.append(text)

        uniqueList = set(tokenList)
        uniqueList = list(filter(None, uniqueList))
        
        if len(stemText) != 0:
            for text in stemText:
                tokenOutput.write(" "+text)
        tokenOutput.write("\n")

        if len(tokenList)%10 == 0:
            heapOutput.write(str(len(tokenList))+" "+str(len(uniqueList))+"\n")
            plotToken.append(len(tokenList))
            plotUnique.append(len(uniqueList))

    heapOutput.write(str(len(tokenList))+" "+str(len(uniqueList)))

    statOutput.write(str(len(tokenList))+"\n"+str(len(uniqueList))+"\n")
    plotToken.append(len(tokenList))
    plotUnique.append(len(uniqueList))

    countToken = Counter(tokenList)
    freq_sort_token = sorted(countToken.items(), key=lambda x: (-x[1], x[0]))[:100]
    for token, count in freq_sort_token:
        statOutput.write(str(token)+" "+str(count)+"\n")

    tokenOutput.close()
    heapOutput.close()
    statOutput.close()


    # plt.figure(figsize=(10,4))

    # plt.plot(plotToken, plotUnique, color='blue')
    # plt.grid()

    # plt.show()
