from time import sleep
import emoji
print('Contagem para o lançamento de fogos!')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':smiling_face_with_hearts:' * 20))
