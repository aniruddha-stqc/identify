##########################################################################
# Version 0.1 - 27-Feb-2019
##########################################################################
import datetime
import os
import hashlib
import sys

#Global variables
gv_path_to_code_folder = "/root/Desktop/MoisutureIndicator"
gv_time_start = datetime.datetime.now()

#**************************************************************************
#Writes text (in append mode) to a given file
#**************************************************************************
def write_to_file(p_text_to_write, p_file_to_write):
    #File pointer initialized in append mode
    lv_file_pointer = open(p_file_to_write,"a+")
    #Writes text to the file
    lv_file_pointer.write(p_text_to_write)
    #Closes the file
    lv_file_pointer.close()

#**************************************************************************
#Calculates MD5 of any given file
#**************************************************************************
def calculate_hash(p_file_to_identify, p_file_to_write):
    #File pointer initialized in append mode

    lv_file_pointer = open(p_file_to_identify,"rb")
    try:
        #Calculate MD5
        lv_md5 =  hashlib.md5(lv_file_pointer.read()).hexdigest()
        #Write to file
        write_to_file(lv_md5 + " " + p_file_to_identify + "\n", p_file_to_write)
    except:
        #Hashing Errors are redirected to error log
        write_to_file("Unable to Hash: " + lv_file_pointer + "\n", "log_error.txt")
    #Closes the file
    lv_file_pointer.close()
#**************************************************************************
#Calculates MD5 of source code and APK
#**************************************************************************
def identify_target():
    #Added Time Stamp
    write_to_file("\nTimestamp of Execution", "log_v0.0.txt")
    # Log all MD5 info of Source code files
    write_to_file("\nStart of Listing: \"MD5 and Source Code\"\n", "log_v0.0.txt")
    for root, dirs, files in os.walk(gv_path_to_code_folder):
            for file in files:
                  calculate_hash(os.path.join(root, file), "log_v0.0.txt")
    write_to_file("\nEnd of Listing: \"MD5 and Source Code\"\n", "log_v0.0.txt")


def main():
  #Get all Identification info from source code and APK
  identify_target()
  print("Total time taken: " + str( (datetime.datetime.now() - gv_time_start ).total_seconds() ) + " seconds")

#Call to main function
if __name__== "__main__":
  #Count the number of command line arguments
  count = len( sys.argv[1:] )
  #Process only if there is one argument
  if count == 1:
    #The argument is assumed to be the path to Source code root folder
    gv_path_to_code_folder = sys.argv[1]
    #Execute the main program
    main()
  else:
    #If there are not exactly one argument report error
    print("\nUsage for Windows : identify.exe <space> <path to source code root folder>")
    print("\nUsage for Linux   : identify <space> <path to source code root folder>")
    #Exit
    sys.exit(1)