# AudioSpeechProcessingCodes - Brian Stasak (2026)
Quick scripts for processing audio-related files

This directory contains a collection of several python and perl scripts that are useful during audio-speech processing. Brief descriptions regarding each is given below:


# AcousticSpeech_eGeMAPsFeautures_Getter_v0.py
This code extracts 88 supra-segmental low-level descriptive acoustic features (w/header info). These acoustic features were originally designed for speech paralinguistic (emotion) studies. The single version is for one file analysis, whereas batch version reports individual results for a directory of WAVs. It is currently set to run on the batch version. All results can easily be stored for other codes or copy-pasted from the terminal buffer to MS Excel.

For more on eGeMAPS acoustic features, see:
https://sail.usc.edu/publications/files/eyben-preprinttaffc-2015.pdf


# AcousticSpeech_PraatFeatures_Getter_v0.py
This code quickly extracts and prints common acoustic speech features (w/header info). This is same type of acoustic feature output (minus the ASR transcripts) that Automated CalliOpeNLP uses. The single version is for one file analysis, whereas Batch reports all results for a directory of WAVs. It is currently set to run on the batch version. All results can easily be stored for other codes or copy-pasted from the terminal buffer to MS Excel.

For more details on ParselMouth Praat-based features, see:
https://pure.mpg.de/rest/items/item_2627915_2/component/file_2627914/content


# AudioFile_Length_Getter_v0.py
This code quickly extracts and prints audio file lengths, frames, and sampling rates within a given directory. This script can be useful for quality-control purposes, understanding different speakers' level of task compliance, and general file lengths. Results can easily be stored for other codes or copy-pasted from the terminal buffer to MS Excel.


# File_Getter_v0.py + Files_Getter_List.txt
This will look at a list of files called 'Files_Getter_List.txt' and copy only the listed files over to a designated directory. This script is useful when a directory has a very large number of files and you only require a subset of specific ones. 
