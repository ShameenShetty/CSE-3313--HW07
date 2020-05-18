# CSE-3313--HW07
This is the coding assignment for Homework 7 for CSE3313 (Introduction to Signal Processing).  
NOTE: Still incomplete

## Purpose
Learn how to produce a filter bank to detect which of several frequencies are present
in a signal. Also learn to apply bandpass filters

## Processs
Touch tone phones generate dual-tone multifrequency (DTMF) signals. The numbers of a standard keypad can be seen in table 1. When a button on the keypad is pressed, a signal is sent that is the combination of the row frequency and column frequency. For example, when we press ‘8’ a signal composed of 852 Hz and 1336 Hz frequencies is produced.  


<table>
<tbody>
<tr>
<td colspan="4" align="center">&nbsp;DTMF Frequencies</td>
</tr>
<tr align="center">
<td style="width: 89px;">Frequencies</td>
<td style="width: 60.9833px;">1209 Hz</td>
<td style="width: 61.0167px;">1336 Hz</td>
<td style="width: 65px;">1477 Hz</td>
</tr>
<tr align="center">
<td style="width: 89px;">697 Hz</td>
<td style="width: 60.9833px;">&nbsp;1</td>
<td style="width: 61.0167px;">2</td>
<td style="width: 65px;">3</td>
</tr>
<tr align="center">
<td style="width: 89px;">&nbsp;770 Hz</td>
<td style="width: 60.9833px;">4</td>
<td style="width: 61.0167px;">5</td>
<td style="width: 65px;">6</td>
</tr>
<tr align="center">
<td style="width: 89px;">852 Hz </td>
<td style="width: 60.9833px;">7</td>
<td style="width: 61.0167px;">8</td>
<td style="width: 65px;">9</td>
</tr>
<tr align="center">
<td style="width: 89px;">941 Hz </td>
<td style="width: 60.9833px;">*</td>
<td style="width: 61.0167px;">0</td>
<td style="width: 65px;">#</td>
</tr>
</tbody>
</table>

So, in order to determine which button has been pressed, we use a **filter bank**. A filter bank is a set of bandpass filters, with one for each of the frequencies that you wish to detect. The idea is that the filter for frequency f<sub>k</sub> passes the f<sub>k</sub> component relatively unchanged while the other frequencies are attenuated. Checking the output of each filter allows us to determine which of these
frequencies are present in the signal.  

* We read from the csv file *tones.csv* which contains the tones (as a set of numbers in csv format).
* The output will be the phone number that the tones represent
* The sampling rate is f<sub>s</sub> = 8000 Hz. However, each tone is only generated for half a second and therefore represents 4000 samples of the overall signal. The length of the signal will be a multiple of 4000.
* Filter length is L = 64. The filter coefficients are produced using 

<a href="https://www.codecogs.com/eqnedit.php?latex=h[n]&space;=&space;\frac{2}{L}cos(\frac{2\pi&space;f_b&space;n}{f_s}),&space;0&space;\leq&space;n&space;<&space;L" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h[n]&space;=&space;\frac{2}{L}cos(\frac{2\pi&space;f_b&space;n}{f_s}),&space;0&space;\leq&space;n&space;<&space;L" title="h[n] = \frac{2}{L}cos(\frac{2\pi f_b n}{f_s}), 0 \leq n < L" /></a>   

where f<sub>b</sub> is the frequency that the bandpass  is designed to pass and f<sub>s</sub> is the sampling frequency.  
![](https://github.com/ShameenShetty/CSE-3313--HW07/blob/master/Frequency%20Responses%20of%20Bandpass%20Filters.png)

* To determine the frequencies present in a particular tone, determine which of the 7 filters have the highest values for `np.mean(y**2)` where y is the output of the filter. For example, if the first 4000 values have a tone composed of a 697 Hz signal and a 1477 Hz signal, then the bandpass filters for those two frequencies should produce output signals with much higher mean values than the other filters.
