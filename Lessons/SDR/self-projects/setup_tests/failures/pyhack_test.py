from hackrf import *
from pylab import *     # for plotting

with HackRF() as hrf:
	hrf.sample_rate = 20e6
	hrf.center_freq = 88.5e6

	samples = hrf.read_samples(2e6)

	# use matplotlib to estimate and plot the PSD
	psd(samples, NFFT=1024, Fs=hrf.sample_rate/1e6, Fc=hrf.center_freq/1e6)
	xlabel('Frequency (MHz)')
	ylabel('Relative power (dB)')
	show()