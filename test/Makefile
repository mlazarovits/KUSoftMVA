MakeReducedNtuple_NANO.x: NanoTreeTemplate.o ./MakeReducedNtuple_NANO.C ./NanoTreeTemplate.h
	g++ -o MakeReducedNtuple.x ./MakeReducedNtuple_NANO.C NanoTreeTemplate.o `root-config --cflags --libs`

NanoTreeTemplate.o: ./NanoTreeTemplate.h ./NanoTreeTemplate.C
	g++ -c ./NanoTreeTemplate.C `root-config --cflags --libs`

makeTrees.x: makeTrees.o ./makeTrees.C ./softLepSignal.h
	g++ -o makeTrees.x ./makeTrees.C makeTrees.o `root-config --cflags --libs`

makeTrees.o: ./softLepSignal.h ./softLepSignal.C
		g++ -c ./softLepSignal.C `root-config --cflags --libs`

clean:
	rm *.o
	rm -f *.x
