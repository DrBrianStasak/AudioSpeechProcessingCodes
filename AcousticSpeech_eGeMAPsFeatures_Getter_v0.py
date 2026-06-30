# eGeMAPS Acoustic Speech Feature Getter - Brian Stasak 2022 v0
# This code extracts 88 supra-segmental acoustic features (w/header info)
# These acoustic features were originally designed for speech paralinguistic (emotion) studies
# Single version is for one file analysis, whereas batch reports individual results for a directory of WAVs
# Results can easily be stored for other codes or copy-pasted to MS Excel

# Required Python toolkit imports
import pandas as pd
import re
import os
import opensmile

# final results stored data structure (if needed later)
audio_feat_info = []
all = []

# Declare given audio file directory on your computer or USB (where the audio files are)
# Recordings should be WAV audio format (i.e., mono 16-bit)
directory = '/YOURDIRECTORYFOLDERWHEREAUDIOFILESARE/'
print("Audio Directory: ")
print(directory)
print(" ")

print(os.getcwd())
files = os.listdir(directory)
print("Audio Evaluated: ")
for file in files:
	print(file)
print(" ")

# OpenSmile eGeMAPS feature parameters
# Can choose which features are of interest; (ComParE_2016 = 65; GeMAPSv01a = 62; eGeMAPSv01b = 88; eGeMAPSv02 = 88)
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

# Single extract eGeMAPS from one specific WAV file; uncomment if desire to use
pd.set_option("display.max_rows", None, "display.max_columns", None)
#y = smile.process_file('/YOURDIRECTORYFOLDERWHEREAUDIOFILEIS/YOURSPECIFICSINGLEAUDIOFILENAME.wav')
#print(y)
#audio_feat_info.append(y)
#output = y.transpose()
#print(output)

# Batch extraction of 88-eGeMAPS acoustic functional features for each audio file in a declared folder directory
# Batch searches all WAV files in your directory folder above and line-by-line prints: <filename> and then its <features>
for filename in os.listdir(directory):
	if filename.endswith(".wav"):
	#if filename.endswith(".wav") and filename.startswith("A"): # might want to use instead of above line if wanting subset of files
		print('\n')
		y = smile.process_file(directory + filename)
		all.append(y)
		yy = y.transpose()
		audio_feat_info.append(yy)
		print(yy)
#print(audio_feat_info)
