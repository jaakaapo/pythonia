import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('IPCC_AR6_SYR_SPM.pdf', 'rb'))
speaker = pyttsx3.init()

for page in pdfreader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n',' ')

speaker.save_to_file(clean_text, 'ipcc_raportti.mp3')
speaker.runAndWait()

speaker.stop()