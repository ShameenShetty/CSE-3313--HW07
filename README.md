# CSE-3313--HW07
This is the coding assignment for Homework 7 for CSE3313 (Introduction to Signal Processing).

## Purpose
Learn how to produce a filter bank to detect which of several frequencies are present
in a signal. Also learn to apply bandpass filters

## Processs
Touch tone phones generate dual-tone multifrequency (DTMF) signals. The numbers of a standard keypad can be seen in table 1. When a button on the keypad is pressed, a signal is sent that is the combination of the row frequency and column frequency. For example, when we press ‘8’ a signal composed of 852 Hz and 1336 Hz frequencies is produced.  

| ' | ' | ' | ' |
| Frequencies | 1209 Hz | 1336 Hz | 1477 Hz | 
|-------------|---------|---------|---------|
| 697 Hz      | 1       | 2       | 3       |
| 770 Hz      | 4       | 5       | 6       |
| 852 Hz      | 7       | 8       | 9       |
| 941 Hz      | *       | 0       | #       |
