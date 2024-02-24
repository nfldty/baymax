import time
import re
import io

import os, sys, contextlib

import pandas as pd
import numpy as np


import speech_recognition as sr
from gtts import gTTS

from pydub import AudioSegment
from scipy.io.wavfile import read, write

import audio2face_pb2
import audio2face_pb2_grpc

import grpc
from audio2face_streaming_utils import push_audio_track

from typing import Union, Type




# Global speech recognition instance



asr = sr.Recognizer()

def speech_to_text(audio: sr.AudioData) -> tuple[bool, Union[str, Type[Exception]]]:
    """
    Convert speech audio to text using Google Web Speech API.
    
    Parameters:
        audio (sr.AudioData): Speech audio data.
        
    Returns:
        Tuple[bool, Union[str, Type[Exception]]]: A tuple containing a boolean indicating if the recognition
                                                 was successful (True) or not (False), and the recognized text
                                                 or the class of the exception if an error occurred.
    """
    global asr
    try:
        # Use Google Web Speech API to recognize speech from audio data
        return True, asr.recognize_google(audio, language="en-US")
    except Exception as e:
        # If an error occurs during speech recognition, return False and the type of the exception
        return False, e.__class__


def get_tts_data(text: str) -> bytes:
    """
    Generate Text-to-Speech (TTS) audio in mp3 format.
    
    Parameters:
        text (str): The text to be converted to speech.
        
    Returns:
        bytes: TTS audio in mp3 format.
    """
    # Create a BytesIO object to hold the TTS audio data in mp3 format
    tts_result = io.BytesIO()
    # Generate TTS audio using gTTS library with the specified text and language (en-US)
    tts = gTTS(text=text, lang='en-US', slow=False)
    # Write the TTS audio data to the BytesIO object
    tts.write_to_fp(tts_result)
    tts_result.seek(0)
    # Read and return the TTS audio data as bytes
    return tts_result.read()

def tts_to_wav(tts_byte: bytes, framerate: int = 22050) -> np.ndarray:
    """
    Convert TTS audio from mp3 format to WAV format and set the desired frame rate and channels.
    
    Parameters:
        tts_byte (bytes): TTS audio in mp3 format.
        framerate (int, optional): Desired frame rate for the WAV audio. Defaults to 22050.
        
    Returns:
        numpy.ndarray: TTS audio in WAV format as a numpy array of float32 values.
    """
    # Convert the TTS audio bytes in mp3 format to a pydub AudioSegment object
    seg = AudioSegment.from_mp3(io.BytesIO(tts_byte))
    # Set the frame rate and number of channels for the audio
    seg = seg.set_frame_rate(framerate)
    seg = seg.set_channels(1)
    # Create a BytesIO object to hold the WAV audio data
    wavIO = io.BytesIO()
    # Export the AudioSegment as WAV audio to the BytesIO object
    seg.export(wavIO, format="wav")
    # Read the WAV audio data from the BytesIO object using scipy.io.wavfile.read()
    rate, wav = read(io.BytesIO(wavIO.getvalue()))
    return wav

def wav_to_numpy_float32(wav_byte: bytes) -> np.ndarray:
    """
    Convert WAV audio from bytes to a numpy array of float32 values.
    
    Parameters:
        wav_byte (bytes): WAV audio data.
        
    Returns:
        numpy.ndarray: WAV audio as a numpy array of float32 values.
    """
    # Convert the WAV audio bytes to a numpy array of float32 values
    return wav_byte.astype(np.float32, order='C') / 32768.0

def get_tts_numpy_audio(text: str) -> np.ndarray:
    """
    Generate Text-to-Speech (TTS) audio in WAV format and convert it to a numpy array of float32 values.
    
    Parameters:
        text (str): The text to be converted to speech.
        
    Returns:
        numpy.ndarray: TTS audio as a numpy array of float32 values.
    """
    # Generate TTS audio in mp3 format from the given text
    mp3_byte = get_tts_data(text)
    # Convert the TTS audio in mp3 format to WAV format and a numpy array of float32 values
    wav_byte = tts_to_wav(mp3_byte)
    return wav_to_numpy_float32(wav_byte)

def make_avatar_speaks(text: str) -> None:
    """
    Make the avatar speak the given text by pushing the audio track to the NVIDIA A2F instance.
    
    Parameters:
        text (str): The text to be spoken by the avatar.
        
    Returns:
        None
    """
    global a2f_url
    global sample_rate
    global a2f_avatar_instance
    # Get the TTS audio in WAV format as a numpy array of float32 values
    tts_audio = get_tts_numpy_audio(text)
    # Push the TTS audio to the NVIDIA A2F instance for the avatar to speak
    push_audio_track(a2f_url, tts_audio, sample_rate, a2f_avatar_instance)
    return






# Define the default audio2face URL and port.
default_url = 'localhost'
default_port = 50051

# Set the audio frame rate for the audio data.
sample_rate = 22050  # Replace '22050' with the desired audio frame rate (samples per second).

# Specify the instance name of the avatar in audio2face service.
a2f_avatar_instance = '/World/audio2face/PlayerStreaming'

# Define a variable for the port (you can change the value as needed).
# For example, if you want to use a different port, modify the value of 'port' accordingly.
port = default_port

# Create the complete audio2face URL by combining the URL and port variables.
a2f_url = f'{default_url}:{port}'

make_avatar_speaks("hello")

         