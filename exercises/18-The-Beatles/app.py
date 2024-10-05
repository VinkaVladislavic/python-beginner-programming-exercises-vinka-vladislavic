# ✅↓ Write your code here ↓✅
def sing():
    song=""
    for i in range(0,11):
        if i==0:
            for j in range(1,5):
                song=song+"let it be,\n"
        if i==4:
            song=song+"there will be an answer,\n"
        if i==5:
            for k in range(1,6):
                song=song+"let it be,\n"
        if i==10: 
            song=song+"whisper words of wisdom, let it be"
    return song
print(sing())
