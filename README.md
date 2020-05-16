# open_cv

## Setup

- Clone (or download) the repository:
```ShellSession
git clone git@github.com:Paulinakhew/open_cv.git
```

- Download all the necessary packages:

* **MacOS Users**
```ShellSession
$ pip3 install -r requirements.txt
$ brew install tesseract
```

* **Ubuntu Users**
```ShellSession
$ pip install -r requirements.txt
$ sudo apt-get install tesseract-ocr
```

## Testing Pytesseract on Clean Example Files
The Pytesseract that we are testing below is the one downloaded using `homebrew`/`sudo apt-get install` and not the one from `pip`. The results will be printed to the terminal.

```ShellSession
$ tesseract tesseract_inputs/example_01.png stdout
```
This should output `Testing Tesseract OCR`

```ShellSession
$ tesseract tesseract_inputs/example_02.png stdout
```
This should output `PyImageSearch`

```ShellSession
$ tesseract tesseract_inputs/example_03.png stdout
```
This should output `650 3428`

## Testing Pytesseract on Noisy Example Files
The results will be printed to the terminal.

```ShellSession
$ tesseract images/example_01.png stdout
$ python3 ocr.py --image images/example_01.png
```

This should output the following:
```text
Noisy image
to test
Tesseract OCR
```

```ShellSession
$ tesseract images/example_02.png stdout
$ python3 ocr.py --image images/example_02.png --preprocess blur
```

This should output the following:
```text
Tesseract Will
Fail With Noisy
Backgrounds
```

```ShellSession
$ tesseract images/example_03.png stdout
$ python3 ocr.py --image images/example_03.png
```

This should output the following:
```text
In order to make the most of this, you will need to have
alittle bit of programming experience. All examples in this
book are in the Python programming language. Familiarity
with Python or other scripting languages is suggested, but
not required.

You'll also need to know some basic mathematics. This
book is hands-on and example driven: lots of examples and
lots of code, so even if your math skills are not up to par,
do not worry! The examples are very detailed and heavily
documented to help you follow along.
```
