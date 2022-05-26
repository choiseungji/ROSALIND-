#방법_1
sample= 'We tried list we tried dicts also we tried Zen'
word= sample.split(' ')
counter = {}
for value in word:
    try: counter[value] += 1
    except: counter[value] =1
for key, value in dict.items(counter):
    print(key,value)

#방법_2
from collections import Counter
sample= 'We tried list we tried dicts also we tried Zen'
array= sample.split(' ')
counter = Counter(array)
for key, value in dict.items(counter):
    print(key, value)
    
#output===================================================
When 1
I 2
find 1
myself 1
in 4
times 1
of 11
trouble 1
Mother 2
Mary 2
comes 2
to 3
me 4
Speaking 3
words 7
wisdom 7
let 30
it 36
be 41
And 3
my 1
hour 1
darkness 1
she 1
is 4
standing 1
right 1
front 1
Let 6
Whisper 4
when 2
the 4
broken 1
hearted 1
people 1
living 1
world 1
agree 1
There 4
will 5
an 4
answer 4
For 1
though 1
they 2
may 1
parted 1
there 2
still 2
a 2
chance 1
that 2
see 1
night 1
cloudy 1
light 1
shines 1
on 1
Shine 1
until 1
tomorrow 1
wake 1
up 1
sound 1
music 1
yeah 2
