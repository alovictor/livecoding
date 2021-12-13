p1 >> piano(P[:8]*2, dur=1, oct=4, scale=Scale.minorPentatonic, blur=2, tremolo=1, lpf=sinvar([500,4000])).spread()

l1 >> loop('perc-loop', P[:16], slide=PWhite(0,0.2), room=5, pan=PWhite(-1,1)).every(4, 'shuffle').every(4, 'palindrome')

l2 >> loop('floresta-noite', P[4:12].shuffle()).spread()

l3 >> loop('echo-flute', P[:16], amp=1.5, lpf=sinvar([100,4000], 16), tremolo=4).every(8, 'reverse').every(4, 'shuffle')

d1 >> play('v{bvks} b', dur=2)
