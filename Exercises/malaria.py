''' This code is a part of Running Excersize I

Author: Vaiva Slatkevičiūtė

It's purpose is to merge data from several files into one.
First file is malaria.fna with multiple DNA sequences. To know which protein sequence those DNA sequences relate to, a blastx-run was used and the results were sored in malaria.blastx.tab. Both of the files were given at the start of the excerise.

# Main task: Insert the information about the protein description from the blastx results to the fasta file’s header and save the output into output.txt file.  

If the gene doesn't have a blastx hit, it is NOT included in the output file.

!!! - more structure, shorter, more information about input/output/usage
'''
###############
# The setup
###############

# The setup of calling the script file, input files and the output file
# Goal is 'python malaria.py malaria.fna malaria.blastx.tab output.txt' 

# TODO: uncomment when hardcoded version works | DONE
import sys
ScriptFile = sys.argv[0]    # malaria.py
fnaFile = sys.argv[1]       # malaria.fna
blastxFile = sys.argv[2]    # malaria.blastx.tab
outputFile = sys.argv[3]    # output.txt

print(type(fnaFile))

## QC: checking if setup works | DONE
# print("Script name:", ScriptFile)
print("Input fna file:", fnaFile)
print("Input blastx file:", blastxFile)
print("Output file:", outputFile)
# Checking by running 'python malaria.py malaria.fna malaria.blastx.tab output.txt' in Terminal | DONE

# Are the right files uploaded?

if 'malaria.fna' not in fnaFile:
    proceed_fna = input('fna file name does not match expected file name. Do you want to proceed? (y/n)' ' Code might not work as expected ').lower().strip()
    if proceed_fna not in ('yes', 'y'):
        raise SystemExit("Program interrupted")

if blastxFile != 'malaria.blastx.tab':
    proceed_b = input('blastx.tab file name does not match expected file name. Do you want to proceed? (y/n)' ' Code might not work as expected ').lower().strip()
    if proceed_b not in ('yes', 'y'):
        raise SystemExit("Program interrupted")


# Checking if file exists
# TODO: Hardcoded version first, change to argv variables | DONE
import os
# !!! - import in one place
if os.path.exists(fnaFile):
    None
else:
    print('No', 'malaria.fna', 'found')

if os.path.exists(blastxFile):
    None
else:
    print('No', 'malaria.blastx.tab', 'found')


# Reading the .fna file
# TODO: Hardcoded version first, change to argv variables | DONE
print("processing...")

with open(fnaFile) as f:
    fna = f.readlines()

# Reading the .blastx.tab file
# TODO: Hardcoded version first, change to argv variables | DONE

with open(blastxFile) as r:
    blastx = r.readlines()

'''## QC: uploaded fine? | DONE
print(fna)
print(blastx)'''

##############################
# File coversion into objects
##############################

# Extracting the names and hit descriptions from blastx object
# print(blastx[0]) #queryName queryLength firstQueryPos lastQueryPos hitName hitLength firstHitPos lastHitPos frame hitDescription numberOfHits coverage identity evalue score hspLength relIdentity

names_blastx = []
for line in blastx:
    queryName, queryLength, firstQueryPos, lastQueryPos, hitName, hitLength, firstHitPos, lastHitPos, frame, hitDescription, numberOfHits, coverage, identity, evalue, score, hspLength, relIdentity = (line.split('\t'))
    if hitDescription != 'null': # removing genes that do not have a blastx hit
        names_blastx.append([queryName, hitDescription])

# QC: print(names_blastx[0:5])

# Creating a nested list from fna object ['sequence name', 'sequence']
fna_nested = []
for line in fna:
    line = line.strip() #to avoid whitespaces
    if line.startswith('>'):
        fna_nested.append([line, ""]) # seq name - the first member of the list
    else:
        fna_nested[-1][1] += line # adding the sequence to the last list as the second member

# Preparing the output file
output = []
for nest in fna_nested:
    title, seq = nest 
    fna_name, length, scaffold, strand = title.split('\t')
    fna_nameNoHead = fna_name.replace('>', '')
    for blastx in names_blastx:
        blastx_name, descr = blastx
        if fna_nameNoHead == blastx_name: # mapping matching blastx to fna files
            output.append([title+'\t'+descr, seq])

# QC: print(output[:2])

#####################
# Writing output.txt
#####################
#TODO: Hardcoded version first, change to argv variables | DONE

with open(outputFile, 'w') as w:
    for outNest in output:
        outEntry = '{}\n{}\n'.format(outNest[0],outNest[1])
        w.write(outEntry)

print("Your file", outputFile, "is ready")