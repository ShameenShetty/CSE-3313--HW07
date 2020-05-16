# CSE-3313--HW07
This is the coding assignment for Homework 7 for CSE3313 (Introduction to Signal Processing).

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

