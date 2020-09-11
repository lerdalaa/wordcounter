from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>about page<h1> <br /> I like to count words')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items())


    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist), 'sorted_words':sorted_words})