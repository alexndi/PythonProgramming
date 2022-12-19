import sys

def load_stems(stem_file):
    stems = {}
    with open(stem_file, 'r') as f:
        for line in f:
            word, stem = line.strip().split(':')
            stems[word] = stem
    return stems

def main(stem_file, word):
    stems = load_stems(stem_file)
    if word in stems:
        print(stems[word])
    else:
        print(f"{word} not found in stem dictionary")

if __name__ == '__main__':
    stem_file = sys.argv[1]
    word = sys.argv[2]
    main(stem_file, word)
