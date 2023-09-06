import speech_recognition as speechRec
from audioplayer import AudioPlayer

listener = speechRec.Recognizer()

try:
    with speechRec.Microphone() as source:
        print("I'm waiting for your instructions")
        AudioPlayer("audio/Hello.wav").play(block=True)


        voice = listener.listen(source)
        userInput = listener.recognize_google(voice)
        print(userInput)

        if 'hello' in userInput:
            print('it worked!')

except:
    pass


