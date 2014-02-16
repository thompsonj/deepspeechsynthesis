#/bin/bash

# Convert TIMIT wav files such that they can be read by 
# scipy.io.wavfile and other applications
# Original NIST SPHERE files are kept with their original names. 
# The suffix _convert is added to those which have been converted. 
# N.B. passing the same file name as input and output to sox led to complete loss of data. 

ROOT="data/raw/TIMIT/"

cd $ROOT
LIST=`ls */*/*/*.WAV`

for l in $LIST
do
	echo $l
	filename=${l%.WAV}
	echo $filename
	sox $l -V3 -t sndfile {$filename}_convert.WAV
done


