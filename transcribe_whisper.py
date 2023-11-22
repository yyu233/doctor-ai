from concurrent.futures import ThreadPoolExecutor
from utils import recognizer, microphone
from state import state_store
import speech_recognition as sr


def process_audio(recognizer, audio, model, fn):
    #text = recognizer.recognize_whisper_api(audio)
    text = recognizer.recognize_google(audio)
    print("[whisper] transcript: ", text)

    # Cancels the noise words to some extent
    if (len(text) > 8):
        fn(text)
    else:
        print("[whisper] ignored cause noise:", text)


voice_recognition_executor = ThreadPoolExecutor(4)


def get_callback(fn):

    def callback(recognizer, audio):
        voice_recognition_executor.submit(process_audio,
                                           recognizer, audio,
                                            "small.en", fn)
        # received audio data, now we'll recognize it using Google Speech Recognition
        #try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
        #    print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
        #except sr.UnknownValueError:
        #    print("Google Speech Recognition could not understand audio")
        #except sr.RequestError as e:
        #    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return callback


with microphone as source:
    print("[whisper] Calibrating...")
    recognizer.adjust_for_ambient_noise(source)


def transcribe_whisper(fn):
    callback = get_callback(fn)

    print("[whisper] Listening...")
    stop = recognizer.listen_in_background(microphone,
                                          callback,
                                          phrase_time_limit=15)
    return stop
    #import speech_recognition as sr

    #r = sr.Recognizer()

    #with sr.Microphone() as source:
    #    print(source.list_microphone_names())
    #    print("Speak please")
    #    r.adjust_for_ambient_noise(source,duration=1)
    #    audio = r.listen(source, timeout=12)

    #   try:
    #        text = r.recognize_google(audio,  show_all = True )
    #        print(text)
    #    except sr.UnkownValueError:
    #        print("Could not understand audio")