# oie

Scale.default = 'majorPentatonic'
Root.default='E'

l1 >> loop('floresta-dia', P[16:32], amp=.3).every(2, 'shuffle').spread()

l2 >> loop('perc-loop', P[:16], amp=.3).every(2, 'shuffle').stop()

l3 >> loop('echo-flute', P[:8]).every(2, 'shuffle').stop()

p1 >> klank(amp=.7).stop()

p2 >> scatter(P[:8], dur=1/2, blur=1, oct=(5,6), amp=1.0).every(4, 'shuffle').stop()

p3 >> charm(P[:16], oct=4, pan=PWhite(-1,1), amp=0.6, dur=1/2).every(2, 'shuffle').stop()

p4 >> feel(P[:8], amp=1.5, dur=PDur(5,8)).every(4, 'shuffle')

pi >> piano([(0,2,4,6), (0,2,3,5), (0,3,5,7)], scale=Scale.major, amp=.9, dur=P[2,4,1], sus=4, room=.7, tremolo=2, lpf=sinvar([400,4000],[4,8,2,16])).spread()

d1 >> donk(P[:8], dur=PDur(5,8), amp=.8, pan=sinvar([-1,1],4)).every(4, 'shuffle')

d2 >> play('v{bvks}', dur=2, amp=.5).stop()

b1 >> varsaw(P[:8].shuffle(), oct=3, amp=1.3, dur=1/2, blur=2, coarse=2, lpf=sinvar([500,3000],4))

Group(l1, l2, d1).solo()


# valeu!!!
