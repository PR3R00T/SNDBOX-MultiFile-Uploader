#!/usr/bin/python3

import sys
from sndbox import sndboxapi as SNDBOX
import os
import glob
import time
from filehash import FileHash

#API KEY Goes here
apikey = "key123"

#Populating list of Samples
dionaea_bin_path = "/data/dionaea/binaries/*"
adbhoney_bin_path = "/data/adbhoney/downloads/*"
dionaea_samples = glob.glob(dionaea_bin_path)
adbhoney_samples = glob.glob(adbhoney_bin_path)
sample_list = dionaea_samples + adbhoney_samples

md5hasher = FileHash('md5')
timestr = time.strftime("%Y%m%d")

#Log File paths
output_file = "/data/SNDBOXupload"+timestr+".txt"
patherror =  "/data/SNDBOXuploaderror" + timestr + ".txt"

# iterate each file
for filename in sample_list:
    print("[*] Found file: " + filename)
    #Get hash of file
    hash = md5hasher.hash_file(filename)
    try:
        file_check = SNDBOX.search(apikey=apikey,md5hash=hash)
    except Exception as e:
        f= open(patherror,"a+")
        f.write(file + " Failed to check: " + str(e) + "\n")
        f.close()
        print("Failed to check: "+ hash)
    if file_check.status_code == 200:
        print("[*] Sample already uploaded, ignoring")
    elif file_check.status_code == 404:
        print("[*] New sample found! - " + hash)
        try:
            upload_response = SNDBOX.submit(apikey=apikey,file=filename,email=False)
            if upload_response == False:
                continue

        except Exception as e:
            f= open(patherror,"a+")
            f.write(file + " Failed to upload: " + str(e) + "\n")
            f.close()
            print("Failed to upload: " + hash)
        if upload_response.status_code == 201:
            print("[*] Sample uploaded to SNDBOX! - " + hash)
            f= open(output_file,"a+")
            f.write("Hash Uploaded: - " + hash + "\n")
            f.close()
