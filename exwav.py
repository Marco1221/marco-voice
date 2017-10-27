# -*- coding: utf-8 -*-
import pygame,sys,pyaudio,wave
from pydub import AudioSegment
import random,string
from aip import AipSpeech

mp3file = AudioSegment.from_mp3("/root/voice/RKY0WIf8.mp3")
mp3file.export("/root/voice/", format="wav")