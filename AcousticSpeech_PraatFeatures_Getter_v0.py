# -*- coding: utf-8 -*-
# PRAAT ACOUSTIC SPEECH FEATURES GETTER - Brian Stasak 2026 v0
# This code quickly extracts and prints common acoustic speech features (w/header info)
# This is same type of acoustic feature output (minus the ASR transcripts) that Automated CalliOpeNLP uses
# Single version is for one file analysis, whereas Batch reports all results for a directory of WAVs
# Results can easily be stored for other codes or copy-pasted to MS Excel

# Required Python toolkit imports
import parselmouth
from parselmouth.praat import call
import os
import glob

# final results stored data structure (if needed later)
voice_report_data = []

# Declare given audio file directory on your computer or USB (where the audio files are)
directory = '/Users/deckard/Desktop/Temporary/BernieCode/Wavs/'

# Single input feature getter - feed in one file at a time (could take a long time); uncomment if desired
#audio_file = '/YOURDIRECTORYFOLDERWHEREAUDIOFILEIS/YOURSPECIFICSINGLEAUDIOFILENAME.wav'
#sound = parselmouth.Sound(audio_file)
#pitch = sound.to_pitch()
#intensity = sound.get_intensity()
##harmonicity = sound.to_harmonicity()
#acoustic_features = (str(audio_file), "PitchValues: ", str(pitch),"AverageIntensity_dB: ", str(intensity))
#voice_report_data.append(acoustic_features)
#print(voice_report_data)

# Batch searches all WAV files in your directory folder above and line-by-line prints: <filename> and then its <features>
for wave_file in glob.glob(os.path.join(directory, "*.wav")):
    sound = parselmouth.Sound(wave_file)
    pitch = sound.to_pitch()
    intensity = sound.get_intensity()
    acoustic_features = (str(wave_file), "PitchValues: ", str(pitch), "AverageIntensity_dB: ", str(intensity))
    voice_report_data.append(acoustic_features)
    print(acoustic_features)

# Check to see how it is stored
#print(voice_report_data)