# AUDIO FILE LENGTH GETTER - Brian Stasak 2022 v0
# This code quickly extracts and prints audio file lengths, frames, and sampling rates within a given directory
# This script can be useful for quality-control purposes, understanding different speakers' level of task compliance
# Results can easily be stored for other codes or copy-pasted to MS Excel

# Required Python toolkit imports
import os
print(os.getcwd())
print(os.curdir)
import pandas as pd
import soundfile as sf

# Option to display maximum rows/columns; just in case large dataset
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# final results stored data structure (if needed later)
results_list = []

# Declare given audio file directory on your computer or USB (where the audio files are)
my_dir = "/YOURDIRECTORYGOESHERE/"

print("************************* Results *************************")
headers = ("AUDIO_FILE_NAME RECORDING_LENGTH_SEC RECORDING_TOTAL_FRAMES RECORDING_SAMPLING_RATE")
print(headers)
results_list.append(headers)

for file in os.listdir(my_dir):
    filename = os.fsdecode(file)
    if filename.endswith(".wav"): # or filename.endswith(".mp3")
        full_link = (os.path.join(my_dir, filename))
        f = sf.SoundFile(full_link)
        print(filename, '{}'.format(f.frames / f.samplerate), '{}'.format(f.frames), '{}'.format(f.samplerate))
        results = (filename, '{}'.format(f.frames / f.samplerate), '{}'.format(f.frames), '{}'.format(f.samplerate))
        results_list.append(results)
    continue
# Check to see how it is stored
#print("\n", results_list)
