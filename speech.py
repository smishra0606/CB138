import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    
    with sr.Microphone() as source:
        print("Start speaking")
        recognizer.adjust_for_ambient_noise(source)  
        audio_data = recognizer.listen(source)  

    try:
        print("recognising text")
        
        text = recognizer.recognize_google(audio_data, language='en-IN')  
        print("text:", text)

    except sr.UnknownValueError:
        print("unable to understand the audio.")

    except sr.RequestError as e:
        print("Error occurred in audio listening; {0}".format(e))

if __name__ == "__main__":
    speech_to_text()
