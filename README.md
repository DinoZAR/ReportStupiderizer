# Report Stupiderizer

I wrote this back in high school, and it isn't finished (it can only do the preposition thing).

This was before virtualenv was remotely in my mind, so the setup is a little tricky:

1. Install wxPython. pip doesn't really like this dependency.
2. Install nltk
3. From Python shell, run this to install the data needed by nltk:

```
>>> import nltk
>>> nltk.download()
Downloader> d averaged_perceptron_tagger
Downloader> d punkt
```

4. To run it, run `python main.py`
