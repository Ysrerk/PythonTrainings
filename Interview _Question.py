###Explanation
# You receive the name of a city as a string, and you need to return a string that shows how many times each letter shows up in the string by using an asterisk (*).
#
# For example:
#
# "Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"
# As you can see, the letter c is shown only once, but wih 2 asterisks.
#
# The return string should include only the letters (not the dashes, spaces, apostrophes, etc). There should be no spaces in the output, and the different letters are separated by a comma (,) as seen in the example above.
#
# Note that the return string must list the letters in order of their first appearence in the original string.
#
# More examples:
#
# "Bangkok"    -->  "b:*,a:*,n:*,g:*,k:**,o:*"
# "Las Vegas"  -->  "l:*,a:**,s:**,v:*,e:*,g:*"
#####

### My Solution





def get_strings(city):

    letters={}
    letters2={}
    let=[]
    star="*"
    for i in city.lower().strip():
        if i in letters.keys():
            letters[i]+=1
        elif i!=" ":
            letters[i]=1
    for key,value in letters.items():
        letters2[key]=value*star
    for key,value in letters2.items():
        let.append((key,value))
    print(let)
    x=""
    for i in let:
        if i!=let[-1]:
            x+=f"{i[0]}:{i[1]},"
        else:
            x += f"{i[0]}:{i[1]}"
    return x




city="Las Vegas"
print(get_strings(city))

