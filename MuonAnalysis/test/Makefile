all: MakeReducedNtuple_NANO.x makeTrees1.x makeTrees2.x

MakeReducedNtuple_NANO.x: NanoTreeTemplate.o ./MakeReducedNtuple_NANO.C ./NanoTreeTemplate.h
	g++ -o MakeReducedNtuple.x ./MakeReducedNtuple_NANO.C NanoTreeTemplate.o `root-config --cflags --libs`

NanoTreeTemplate.o: ./NanoTreeTemplate.h ./NanoTreeTemplate.C
	g++ -c ./NanoTreeTemplate.C `root-config --cflags --libs`

makeTrees1.x: softLepSignal.o ./makeTrees1.C ./softLepSignal.h
	g++ -o makeTrees1.x ./makeTrees1.C softLepSignal.o `root-config --cflags --libs`

makeTrees2.x: softLepSignal.o ./makeTrees2.C ./softLepSignal.h
	g++ -o makeTrees2.x ./makeTrees2.C softLepSignal.o `root-config --cflags --libs`

softLepSignal.o: ./softLepSignal.h ./softLepSignal.C
	g++ -c ./softLepSignal.C `root-config --cflags --libs`

clean:
	rm *.o
	rm -f *.x
