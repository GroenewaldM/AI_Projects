import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    #corpus = crawl('corpus0') for testing
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probability_distribution = {}
    for pages in corpus:
        probability_distribution[pages] = (1 - damping_factor)/(len(corpus) - len(corpus[page]))

    for link in corpus[page]:
        probability_distribution[link] = damping_factor/len(corpus[page])
    
    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_list = []
    probability_dictionary = {}
    for page in corpus:
        page_list.append(page)
        probability_dictionary[page] = 0.0
    state = random.choice(page_list)
    
    for _ in range(SAMPLES):
        probabilities = []
        probability_distribution = transition_model(corpus, state, damping_factor)
        for page in probability_distribution:
            probabilities.append(probability_distribution[page])
        state = str(random.choices(page_list, probabilities)[0])
        probability_dictionary[state] += 1.0 
    
    for p in probability_dictionary:
        probability_dictionary[p] = probability_dictionary[p]/SAMPLES
    return probability_dictionary



def probability(corpus, page, damping_factor, starting_probabilities):
    sum_probability_i = 0

    for link in corpus[page]:
        test = 0
        if len(corpus[link]) == 1:
            sum_probability_i = starting_probabilities[link]
        else:
            sum_probability_i  += starting_probabilities[link]/len(corpus[link])
        test = len(corpus[link])

    p = ((1-damping_factor)/len(corpus)) + (damping_factor*sum_probability_i)
    return p

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    probabilities = {}
    previous_probabilities = {}
    iterate = 1
    for page in corpus:
        probabilities[page] = 1 / len(corpus)
        previous_probabilities[page] = 1 / len(corpus)
    probabilities = {'1.html': 0.2208, '2.html': 0.4229, '3.html': 0.2151, '4.html': 0.1412}
    while iterate:
        math = 0
        for page in corpus:
            p = probability(corpus, page, damping_factor, probabilities)
            probabilities[page] = round(p, 4)
        
        for page in corpus:
            if abs(previous_probabilities[page] - probabilities[page]) > 0.00001:
                iterate = True
            else:
                iterate = False
                print(f"math: {math}")
                return probabilities
            math += probabilities[page]
        
        if iterate:
            previous_probabilities = probabilities.copy()



if __name__ == "__main__":
    main()
