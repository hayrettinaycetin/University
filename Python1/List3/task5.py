import matplotlib.pyplot as plot
import numpy as np


class Sine_wave:
    def __init__(self, frequency, amplitude, acquisition_time,sampling_frequency):
        self.frequency = frequency
        self.sampling_frequency = sampling_frequency
        self.amplitude = amplitude
        self.acquisition_time = acquisition_time
    def generate(self):
        time = np.arange(0, self.acquisition_time, 1 / self.sampling_frequency)
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time)
    def downsample(self,downsample_factor = 3):
        downsampled_frequency = self.sampling_frequency / downsample_factor
        time = np.arange(0, self.acquisition_time, 1 / downsampled_frequency)
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time)
        

        
# My index is 276807 I used only 7 bc of 0
my_sine_wave = Sine_wave(13,2,2,48_000)
my_sine_wave_downsampled = my_sine_wave.downsample()
plot.plot(my_sine_wave.generate(),color = 'r',label = 'Original')
plot.plot(my_sine_wave.downsample(),color = 'b',label = 'Downsampled')
plot.xlabel("Time") 
plot.ylabel("Amplitude") 
plot.title("Sine and Downsampled Sine Waves")
plot.axhline(y=0,color = 'r')
plot.legend()
plot.show()
