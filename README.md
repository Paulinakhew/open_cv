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

## Testing Pytesseract on Example Files
The Pytesseract that we are testing below is the one downloaded using `homebrew`/`sudo apt-get install` and not the one from `pip`.

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
