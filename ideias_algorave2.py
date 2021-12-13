Scale.default='majorPentatonic'

print(SynthDefs)

l1 >> loop('floresta-dia', P[16:32])

b1 >> bug(P[:4],oct=3, dur=1, lpf=0, sus=2, scale=Scale.minorPentatonic).every(2, 'shuffle')

p1 >> scatter(P[:8],dur=1/4,blur=2,oct=6, amp=3).spread().shuffle()

p2 >> charm(P[0,3,5]+2)

p3 >> klank(amp=4)

p4 >> feel(P[:8], amp=5).shuffle()

p5 >> glass()

d1 >> play('v{brvnks}', dur=1/2)

l2 >> loop('perc-loop', P[:16]).shuffle().spread()
