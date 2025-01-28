def open_book(path,title):
    with open(path+title) as f:
        return f.read()

def word_counter(book):
    wc=0
    words=book.split()
    return len(words)

def character_counter(book):
    chars=[]
    char_d={}
    book=book.lower()
    for letter in book:
        if letter not in char_d:
            char_d[letter]=1
        else:
            char_d[letter]+=1
    return char_d

def print_report(bd,p,t,wc):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    print(f"--- Begin report of {p}{t} ---")
    print(f'{wc} words found in the document\n')

    bd_sort=sorted(bd.items(), key=lambda item: item[1], reverse=True)
    
    for l in bd_sort:
        if l[0] in alphabet:
            print(f"The '{l[0]}' character was found {l[1]} times")
    
    print('--- End report ---')

def main():
    path='books/'
    title='frankenstein.txt'
    book=open_book(path,title)
    word_count=word_counter(book)
    c_dict=character_counter(book)
    print_report(c_dict,path,title,word_count)

if __name__=="__main__":
    main()