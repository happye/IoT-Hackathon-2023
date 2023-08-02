import librosa
from sklearn import svm
import serial

# Reading audio files
audio_file = "C:/UnisysWorkFolder/Tutorials/IoT Hackathon/ioT sound file/bird sing.mp3"
# y signal sr sampling rate Use librosa library to extract various features of audio
# e.g. time-domain features (e.g. duration, maximum, minimum, etc.)
# frequency domain features (e.g. spectrum, mel spectrum, chromaticity diagram, etc.)
# and time-frequency domain features (e.g. short-time Fourier transform, wavelet transform, etc.)
y, sr = librosa.load(audio_file)

# Extract Mel Spectrum Returns a numpy array containing the Mel spectrum of the audio file
mel_spec_1 = librosa.feature.melspectrogram(y=y, sr=sr)
mel_spec_2 = librosa.feature.melspectrogram(y=y, sr=sr)

# Can use various machine learning algorithms (e.g., support vector machines, random forests, etc.) to classify extracted audio features
# Convert the Mel spectrum into a one-dimensional vector
mel_spec_flat_1 = mel_spec_1.flatten()
mel_spec_flat_2 = mel_spec_2.flatten()

# Define a support vector machine classifier and train it
# mel_spec_flat is converting mel spectrum to 1D vector
# clf is a support vector machine classifier, x is a feature vector, y is a category label
clf = svm.SVC()
X = [mel_spec_flat_1, mel_spec_flat_2]
y = ["class1", "class2"]
clf.fit(X, y)
print("Hello, World!")

# Send sorting results to Arduino
# You can use the PySerial library to transfer processing results to the Arduino
# `ser` is the instantiated serial object
# `result` is the sorting result
# The `write()` method sends the sorted results to the Arduino
ser = serial.Serial('COM3', 9600)  # Serial communications
result = clf.predict([mel_spec_flat_1])
ser.write( str(result[0]).encode() )
print("Hello, World!2")
