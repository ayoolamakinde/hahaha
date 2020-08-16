"""
Assumption: 
    1. The standard naming convention for file containing potentially offensive text is "input*".
    2. A single high/low risk phrase may occur more than once in a comment.
"""

#python module for finding pathnames
import glob


#read content of a file
def readFile(infile):
    d_file = open(infile, "r")
    
    #convert files containing potentially offensive text to string
    if infile.startswith("input"):
        d_file_convert = d_file.read()
        
        #convert potentially offensive text to lower case
        d_file_convert = d_file_convert.lower()
        
    #convert list of offensive phrases to list
    else:
        d_file_convert = d_file.read().splitlines()
        
        #convert all phrases to lower case
        d_file_convert = [x.lower() for x in d_file_convert]
    
    
    d_file.close()
    return d_file_convert
    
#Append scores to output file   
def outputFile(toAppend):
    with open(output_file_name, 'a') as f:
        f.write(toAppend + "\n")
    
#calculate number of occuerence of risk_phrases
def RiskCalculator(text_input):
    global low_risk_phrases, high_risk_phrases
    
    #convert input text file to String
    current_text= readFile(text_input)
   
    #calculate frequency of low_risk_phrases in a text
    frequency_low = [current_text.count(w) for w in low_risk_phrases]
    
    #calculate frequency of high_risk_phrases in a text
    frequency_high = [current_text.count(w) for w in high_risk_phrases]
    
    # risk score
    riskSum = sum (frequency_low + (2 * frequency_high))
    
    #output format e.g <input-filename-1>:<score-1>
    risk_output = "{} : {}".format(text_input, riskSum)
    
    #append to output file
    outputFile(risk_output)
    

#......................... main ................................

#create output file
output_file_name = "outputfile.txt"
open(output_file_name,'w').close

#List of low_risk_phrases
low_risk_phrases = readFile("low_risk_phrases.txt")

#List of high_risk_phrases
high_risk_phrases = readFile("high_risk_phrases.txt")

#path to input files containing potentially offensive phrases
input_files = glob.glob("input*.txt") 

#calculate risk score for each of the input files
[RiskCalculator(a) for a in  input_files]




