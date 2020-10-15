#!/usr/bin/env python3

import speech_recognition as sr
import argparse


parser = argparse.ArgumentParser(description=("Performs"
                                              "voice-to-text transcription on"
                                              "audio files using"
                                              "PocketSphinx."))
parser.add_argument('-p', '--path',
                    type=str, required=True, help="Audio file path.")
parser.add_argument('-o', '--output', type=str,
                    required=False, help="Optional output to a file."
                                         "By default, the recognized"
                                         "text is printed out."
                                         "(Choose a file name.)")
args = parser.parse_args()


def main():
    if args.path:
        filepath = args.path
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as infile:
        audio = r.record(infile)
    if args.output:
        output = args.output
        with open(output, 'w') as outfile:
            print(r.recognize_sphinx(audio), file=outfile)
    else:
        print(r.recognize_sphinx(audio))


if __name__ == '__main__':
    main()
