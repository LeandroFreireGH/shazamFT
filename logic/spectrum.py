import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def plot_spectrogram(audio, Fs, window_length=0.5):
    audio = audio.reshape(-1)
    window_length_samples = (lambda x: x + x % 2)(int(window_length * Fs))
    amount_to_pad = (lambda x: x - audio.size % x)(window_length_samples)
    song_input = np.pad(audio, (0, amount_to_pad))
    frequencies, _, stft = signal.stft(song_input,
                                           Fs, 
                                           nperseg=window_length_samples,  
                                           nfft=window_length_samples, 
                                           return_onesided=True)

    time_index, freq_bins = stft.shape

    # Obtener la matriz de magnitudes (parte real) para el espectrograma
    spectrogram = np.abs(stft)

    # Crear el gráfico del espectrograma
    plt.figure(figsize=(10, 6))
    plt.imshow(spectrogram.T, aspect='auto', origin='lower', extent=[0, time_index, 0, frequencies[-1]])
    plt.colorbar(label='Magnitud')
    plt.xlabel('Tiempo')
    plt.ylabel('Frecuencia (Hz)')
    plt.title('Espectrograma')
    plt.show()


Fs, audio_input = read('logic/recording.wav')
plot_spectrogram(audio_input, Fs)
