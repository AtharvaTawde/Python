from gtts import gTTS
import os
import PyPDF2  # do pip install PyPDF2


def tts():
    path = input('Enter a valid pathway to the .PDF or'
                 ' .txt file you want to convert to an audio recording: ')
    language = input('Enter the abbreviation of the accent'
                     ' you want the recording to play in (EX: en, es, fr, etc.): ')

    if '.txt' in path:
        f = open(path, 'r')
        lol = f.read()
        f.close()

        recording = gTTS(text=lol, lang=language, slow=False)
        print('Saving...')
        recording.save("recording.mp3")
        print('Recording Saved!')
        print('Loading Recording...')
        os.system("recording.mp3")
        print('Program finished!')

    elif '.pdf' in path:
        # PDF conversion are quite unreliable. TXT files are definitely your best bet. But give the PDF converter a try.
        try:
            pdf = open(path, 'rb')
            reader = PyPDF2.PdfFileReader(pdf)
            print('Number of Pages in PDF: %s' % reader.numPages)
            pagetext = ''
            for i in range(reader.numPages):
                page = reader.getPage(i)
                text = page.extractText()
                print('▯', end="")
                pagetext += text
            print()
            pdf.close()
            recording = gTTS(text=pagetext, lang=language, slow=False)
            print('Saving...')
            recording.save("recording.mp3")
            print('Recording Saved!')
            print('Loading Recording...')
            os.system("recording.mp3")
            print('Program finished!')

        except:
            print("Oof. I guess this PDF just doesn't work! (or gTTS just gave up on you.)")

    else:
        print('File type not supported!')


tts()
