from spellchecker import SpellChecker

corrector = SpellChecker()

texto = input("Ingrese el texto a corregir: ")

if texto in corrector:
    print("Es correcto.")

else:

    corrector_texto = corrector.correction(texto)
    print("El texto correcto es: ", corrector_texto)