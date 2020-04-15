all: MakeReducedNtuple_NANO.x makeTrees.x

MakeReducedNtuple_NANO.x: NanoTreeTemplate.o ./MakeReducedNtuple_NANO.C ./NanoTreeTemplate.h
	g++ -o MakeReducedNtuple.x ./MakeReducedNtuple_NANO.C NanoTreeTemplate.o `root-config --cflags --libs`

NanoTreeTemplate.o: ./NanoTreeTemplate.h ./NanoTreeTemplate.C
	g++ -c ./NanoTreeTemplate.C `root-config --cflags --libs`

makeTrees.x: softLepSignal.o ./makeTrees.C ./softLepSignal.h
	g++ -o makeTrees.x ./makeTrees.C softLepSignal.o `root-config --cflags --libs`

softLepSignal.o: ./softLepSignal.h ./softLepSignal.C
	g++ -c ./softLepSignal.C `root-config --cflags --libs`

clean:
	rm *.o
	rm -f *.x
