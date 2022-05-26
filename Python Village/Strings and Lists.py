#Given: A string s of length at most 200 letters and four integers a, b, c and d.
#Return: The slice of this string from indices aa through b and cc through dd (with space in between), *inclusively*. In other words, we should include elements s[b] and s[d] in our slice.

#input 

s ='86zcstHpPhasianusKcujG4vHMLdFuHJa3BgvkC4QI2IAKTQFLdnbzOUjVkEHgQNRknCWpAeIKmnYfbVcoroneMeVa2JSl6DekBsIHBJTtJAvDQJUMcK2xaBCiqdT0Uxbifh4woGRSbtMqaSOJUJyTgM9qLbT48zBOyIt6wNG55GKfEAPpP0ouFbDDF2cbylsJWwk'
a = 8
b = 16
c = 80
d = 85
e = s[a:b] +s[b] + " " + s[c:d] + s[d]
print(e)

#output > Phasianus corone
