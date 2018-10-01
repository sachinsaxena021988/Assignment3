#import functools to use reduce 
from functools import reduce

#define listword
list_words = ["getallY","ysduadhks","dfafafa","affasfwrwetgerhruul","morutujtjtutuning"]

#reduce all with length
reduce((lambda x,y:y if len(y) > len(x) else x), list_words )