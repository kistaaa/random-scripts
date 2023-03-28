from mido import MidiFile
tempo=0
noteons = []
notas = []
mid = MidiFile('D:/music.mid')

for evt in mid:
    if not evt.is_meta:
        tempo += evt.time
        if evt.type == 'note_on':
            noteons.append(evt)
            
        elif evt.type == 'note_off':
            for nota in noteons:
                if nota.note == evt.note:
                    com = tempo - evt.time
                    fim = tempo
                    dur = fim - com
                    notas.append([evt.note, com, fim, dur])
                    noteons.remove(nota)
print(notas)
